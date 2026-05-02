import os
import re

def verify_all_links():
    docs_dir = 'docs'
    errors = []
    
    # Product ID keywords to check for each version
    version_keywords = {
        '365': 'O365',
        '2024': '2024',
        '2021': '2021',
        '2019': '2019',
        '2016': 'Retail', # 2016 usually uses ProPlusRetail without year
        '2013': 'O15'
    }

    print("--- Starting Link Verification ---")

    all_extracted_links = []

    for root, dirs, files in os.walk(docs_dir):
        for file in files:
            if file.endswith('.md'):
                path = os.path.join(root, file)
                if file == 'index.md':
                    continue
                
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                current_version = None
                for v in version_keywords:
                    if v in file:
                        current_version = v
                        break
                
                if not current_version:
                    continue

                sections = re.split(r'<TabItem value="([^"]+)"', content)
                for i in range(1, len(sections), 2):
                    lang_name = sections[i]
                    section_content = sections[i+1]
                    
                    expected_lang = None
                    if '简体' in lang_name: expected_lang = 'zh-cn'
                    elif '繁体' in lang_name: expected_lang = 'zh-tw'
                    elif 'English' in lang_name: expected_lang = 'en-us'

                    # Find product name and link pairs in tables
                    # Format: | **Product Name** | Components | [链接](URL) | [链接](URL) |
                    table_rows = re.findall(r'\| \*\*([^*]+)\*\* \| [^|]+ \| \s*\[[^\]]+\]\((http[^\)]+)\) \s*(?:❤️)? \s*\| \s*(?:\[[^\]]+\]\((http[^\)]+)\)|[^|]+) \|', section_content)
                    
                    for prod_name, online_link, offline_link in table_rows:
                        # Extract Product ID from online link if possible
                        prod_id = "N/A"
                        match = re.search(r'ProductreleaseID=([^&]+)', online_link)
                        if match:
                            prod_id = match.group(1)
                        
                        all_extracted_links.append({
                            'file': file,
                            'lang': lang_name,
                            'product': prod_name.strip(),
                            'prod_id': prod_id,
                            'online': online_link,
                            'offline': offline_link.strip() if 'http' in offline_link else "N/A"
                        })

                        # --- Validation Logic ---
                        link = online_link
                        keyword = version_keywords[current_version]
                        is_valid = (keyword in link or 'O16GA' in link or ('2016' in file and 'Retail' in link))
                        if not is_valid:
                            errors.append(f"[{file}] Version Mismatch: Expected {keyword} in {link}")
                        
                        if offline_link.strip().startswith('http'):
                            link = offline_link.strip()
                            is_valid_off = False
                            if current_version == '2013' and '39168d7e-077b-48e7-872c-b232c3e72675' in link:
                                is_valid_off = True
                            elif current_version in ['2016', '2019', '2021', '2024', '365'] and '492350f6-3a01-4f97-b9c0-c7c6ddf67d60' in link:
                                is_valid_off = True
                            if not is_valid_off:
                                errors.append(f"[{file}] Version Mismatch (Offline): Expected GUID in {link}")

    # Print Summary
    print(f"\n{'PRODUCT':<30} | {'LANG':<10} | {'PRODUCT ID':<25} | {'LINK'}")
    print("-" * 150)
    for item in sorted(all_extracted_links, key=lambda x: (x['file'], x['lang'])):
        print(f"{item['product'][:30]:<30} | {item['lang']:<10} | {item['prod_id']:<25} | {item['online']}")
    
    if not errors:
        print("\n✅ SUCCESS: All links verified and correct!")
    else:
        print(f"\n❌ FAILED: Found {len(errors)} errors:")
        for err in errors:
            print(f"  - {err}")

    if not errors:
        print("\n✅ SUCCESS: All links verified and correct!")
    else:
        print(f"\n❌ FAILED: Found {len(errors)} errors:")
        for err in errors:
            print(f"  - {err}")

if __name__ == '__main__':
    verify_all_links()
