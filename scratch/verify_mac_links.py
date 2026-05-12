import os
import re
import urllib.request
import urllib.error
import ssl
from concurrent.futures import ThreadPoolExecutor

def extract_links(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    # Find all markdown links [text](URL)
    return re.findall(r'\[[^\]]+\]\((http[s]?://[^\)]+)\)', content)

def check_link(url):
    # Disable SSL verification for this check
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        req = urllib.request.Request(url, headers=headers, method='HEAD')
        with urllib.request.urlopen(req, timeout=10, context=ctx) as response:
            return url, True, response.status
    except urllib.error.HTTPError as e:
        if e.code in [403, 404, 405]:
            try:
                req = urllib.request.Request(url, headers=headers, method='GET')
                with urllib.request.urlopen(req, timeout=10, context=ctx) as response:
                    return url, True, response.status
            except urllib.error.HTTPError as e2:
                return url, False, e2.code
            except Exception as e2:
                return url, False, str(e2)
        return url, False, e.code
    except Exception as e:
        return url, False, str(e)

def main():
    mac_docs_dir = 'docs/mac'
    all_links = set()
    
    print(f"Scanning {mac_docs_dir} for links...")
    if not os.path.exists(mac_docs_dir):
        print(f"Directory {mac_docs_dir} not found!")
        return

    for root, dirs, files in os.walk(mac_docs_dir):
        for file in files:
            if file.endswith('.md'):
                links = extract_links(os.path.join(root, file))
                for link in links:
                    all_links.add(link)
    
    if not all_links:
        print("No links found!")
        return

    print(f"Found {len(all_links)} unique links. Verifying (SSL verification disabled)...")
    
    results = []
    # Use fewer workers to avoid being throttled
    with ThreadPoolExecutor(max_workers=3) as executor:
        results = list(executor.map(check_link, sorted(list(all_links))))
    
    errors = []
    successes = 0
    for url, status, code in results:
        if status:
            successes += 1
            print(f"✅ OK [{code}]: {url}")
        else:
            errors.append(f"❌ FAIL [{code}]: {url}")
            print(f"❌ FAIL [{code}]: {url}")
    
    print("\n--- Summary ---")
    print(f"Total Unique Links: {len(all_links)}")
    print(f"Successful: {successes}")
    print(f"Failed: {len(errors)}")
    
    if errors:
        print("\nDetails of Failures:")
        for err in errors:
            print(err)
    else:
        print("\nAll links are valid!")

if __name__ == "__main__":
    main()
