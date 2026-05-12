import os
import re

def format_links(table_text):
    lines = table_text.split('\n')
    new_lines = []
    for line in lines:
        if '|' in line and 'https://' in line:
            parts = line.split('|')
            new_parts = []
            for part in parts:
                if 'https://' in part:
                    # Only replace if NOT already in a markdown link [text](URL)
                    if not re.search(r'\[[^\]]+\]\(https://', part):
                        url_match = re.search(r'https://[^\s|]+', part)
                        if url_match:
                            url = url_match.group(0)
                            part = part.replace(url, f"[链接]({url})")
                new_parts.append(part)
            new_lines.append('|'.join(new_parts))
        else:
            new_lines.append(line)
    return '\n'.join(new_lines)

pages = [
    {
        "filename": "14plus.md",
        "id": "mac_14plus",
        "slug": "/mac/k8z4x2p5",
        "title": "Office for Mac (macOS 14 及以上)",
        "desc": "适用于 macOS Tahoe (26), Sequoia (15), Sonoma (14)",
        "suites": """| 软件名称                  | 包含的组件 | 下载链接                                              |
|:-----------------------------|:---|:--------------------------------------------------|
| Office 全家桶 (含 Teams)    | Word, Excel, PowerPoint, Outlook, OneNote, Teams, OneDrive | https://go.microsoft.com/fwlink/p/?linkid=2009112 |
| Office 全家桶 (不含 Teams) | Word, Excel, PowerPoint, Outlook, OneNote, OneDrive | https://go.microsoft.com/fwlink/p/?linkid=525133  |""",
        "standalone": """| 软件名称                  | 包含的组件 | 下载链接                                              |
|:-----------------------------|:---|:--------------------------------------------------|
| Word                         | Word, OneDrive | https://go.microsoft.com/fwlink/p/?linkid=525134  |
| Excel                        | Excel, OneDrive | https://go.microsoft.com/fwlink/p/?linkid=525135  |
| PowerPoint                   | PowerPoint, OneDrive | https://go.microsoft.com/fwlink/p/?linkid=525136  |
| Outlook                      | Outlook, OneDrive | https://go.microsoft.com/fwlink/p/?linkid=525137  |
| OneNote                      | OneNote, OneDrive | https://go.microsoft.com/fwlink/p/?linkid=820886  |"""
    },
    {
        "filename": "13.md",
        "id": "mac_13",
        "slug": "/mac/m7r3w1v9",
        "title": "Office for Mac (macOS 13 Ventura)",
        "desc": "最高支持版本：16.101 (2021 / 2024 版)",
        "suites": """| 软件名称                  | 包含的组件 | 下载链接                                                                                                                                                    |
|:-----------------------------|:---|:--------------------------------------------------------------------------------------------------------------------------------------------------------|
| Office 全家桶 (含 Teams)    | Word, Excel, PowerPoint, Outlook, OneNote, Teams, OneDrive | https://officecdn.microsoft.com/pr/C1297A47-86C4-4C1F-97FA-950631F94777/MacAutoupdate/Microsoft_365_and_Office_16.101.25091314_BusinessPro_Installer.pkg |
| Office 全家桶 (不含 Teams) | Word, Excel, PowerPoint, Outlook, OneNote, OneDrive | https://officecdn.microsoft.com/pr/C1297A47-86C4-4C1F-97FA-950631F94777/MacAutoupdate/Microsoft_365_and_Office_16.101.25091314_Installer.pkg             |""",
        "standalone": """| 软件名称                  | 包含的组件 | 下载链接                                                                                                                                                    |
|:-----------------------------|:---|:--------------------------------------------------------------------------------------------------------------------------------------------------------|
| Word                         | Word, OneDrive | https://officecdn.microsoft.com/pr/C1297A47-86C4-4C1F-97FA-950631F94777/MacAutoupdate/Microsoft_Word_16.101.25091314_Updater.pkg                         |
| Excel                        | Excel, OneDrive | https://officecdn.microsoft.com/pr/C1297A47-86C4-4C1F-97FA-950631F94777/MacAutoupdate/Microsoft_Excel_16.101.25091314_Updater.pkg                        |
| PowerPoint                   | PowerPoint, OneDrive | https://officecdn.microsoft.com/pr/C1297A47-86C4-4C1F-97FA-950631F94777/MacAutoupdate/Microsoft_PowerPoint_16.101.25091314_Updater.pkg                   |
| Outlook                      | Outlook, OneDrive | https://officecdn.microsoft.com/pr/C1297A47-86C4-4C1F-97FA-950631F94777/MacAutoupdate/Microsoft_Outlook_16.101.25091314_Updater.pkg                      |
| OneNote                      | OneNote, OneDrive | https://officecdn.microsoft.com/pr/C1297A47-86C4-4C1F-97FA-950631F94777/MacAutoupdate/Microsoft_OneNote_16.101.25091314_Updater.pkg                      |"""
    },
    {
        "filename": "12.md",
        "id": "mac_12",
        "slug": "/mac/j8f6n9t2",
        "title": "Office for Mac (macOS 12 Monterey)",
        "desc": "最高支持版本：16.88 (2021 版)",
        "suites": """| 软件名称                  | 包含的组件 | 下载链接                                                                                                                                                    |
|:-----------------------------|:---|:--------------------------------------------------------------------------------------------------------------------------------------------------------|
| Office 全家桶 (含 Teams)    | Word, Excel, PowerPoint, Outlook, OneNote, Teams, OneDrive | https://officecdn.microsoft.com/pr/C1297A47-86C4-4C1F-97FA-950631F94777/MacAutoupdate/Microsoft_365_and_Office_16.88.24081116_BusinessPro_Installer.pkg |
| Office 全家桶 (不含 Teams) | Word, Excel, PowerPoint, Outlook, OneNote, OneDrive | https://officecdn.microsoft.com/pr/C1297A47-86C4-4C1F-97FA-950631F94777/MacAutoupdate/Microsoft_365_and_Office_16.88.24081116_Installer.pkg             |""",
        "standalone": """| 软件名称                  | 包含的组件 | 下载链接                                                                                                                                                    |
|:-----------------------------|:---|:--------------------------------------------------------------------------------------------------------------------------------------------------------|
| Word                         | Word, OneDrive | https://officecdn.microsoft.com/pr/C1297A47-86C4-4C1F-97FA-950631F94777/MacAutoupdate/Microsoft_Word_16.88.24081116_Updater.pkg                         |
| Excel                        | Excel, OneDrive | https://officecdn.microsoft.com/pr/C1297A47-86C4-4C1F-97FA-950631F94777/MacAutoupdate/Microsoft_Excel_16.88.24081116_Updater.pkg                        |
| PowerPoint                   | PowerPoint, OneDrive | https://officecdn.microsoft.com/pr/C1297A47-86C4-4C1F-97FA-950631F94777/MacAutoupdate/Microsoft_PowerPoint_16.88.24081116_Updater.pkg                   |
| Outlook                      | Outlook, OneDrive | https://officecdn.microsoft.com/pr/C1297A47-86C4-4C1F-97FA-950631F94777/MacAutoupdate/Microsoft_Outlook_16.88.24081116_Updater.pkg                      |
| OneNote                      | OneNote, OneDrive | https://officecdn.microsoft.com/pr/C1297A47-86C4-4C1F-97FA-950631F94777/MacAutoupdate/Microsoft_OneNote_16.88.24081116_Updater.pkg                      |"""
    },
    {
        "filename": "11.md",
        "id": "mac_11",
        "slug": "/mac/s7h5b3q4",
        "title": "Office for Mac (macOS 11 Big Sur)",
        "desc": "最高支持版本：16.77 (2021/2019 版)",
        "suites": """| 软件名称                  | 包含的组件 | 下载链接                                                                                                                                                       |
|:-----------------------------|:---|:-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Office 全家桶 (含 Teams)    | Word, Excel, PowerPoint, Outlook, OneNote, Teams, OneDrive | https://officecdnmac.microsoft.com/pr/C1297A47-86C4-4C1F-97FA-950631F94777/MacAutoupdate/Microsoft_365_and_Office_16.77.23091003_BusinessPro_Installer.pkg |
| Office 全家桶 (不含 Teams) | Word, Excel, PowerPoint, Outlook, OneNote, OneDrive | https://officecdnmac.microsoft.com/pr/C1297A47-86C4-4C1F-97FA-950631F94777/MacAutoupdate/Microsoft_365_and_Office_16.77.23091003_Installer.pkg             |""",
        "standalone": """| 软件名称                  | 包含的组件 | 下载链接                                                                                                                                                    |
|:-----------------------------|:---|:--------------------------------------------------------------------------------------------------------------------------------------------------------|
| Word                         | Word, OneDrive | https://officecdnmac.microsoft.com/pr/C1297A47-86C4-4C1F-97FA-950631F94777/MacAutoupdate/Microsoft_Word_16.77.23091003_Updater.pkg                         |
| Excel                        | Excel, OneDrive | https://officecdnmac.microsoft.com/pr/C1297A47-86C4-4C1F-97FA-950631F94777/MacAutoupdate/Microsoft_Excel_16.77.23091003_Updater.pkg                        |
| PowerPoint                   | PowerPoint, OneDrive | https://officecdnmac.microsoft.com/pr/C1297A47-86C4-4C1F-97FA-950631F94777/MacAutoupdate/Microsoft_PowerPoint_16.77.23091003_Updater.pkg                   |
| Outlook                      | Outlook, OneDrive | https://officecdnmac.microsoft.com/pr/C1297A47-86C4-4C1F-97FA-950631F94777/MacAutoupdate/Microsoft_Outlook_16.77.23091003_Updater.pkg                      |
| OneNote                      | OneNote, OneDrive | https://officecdnmac.microsoft.com/pr/C1297A47-86C4-4C1F-97FA-950631F94777/MacAutoupdate/Microsoft_OneNote_16.77.23091003_Updater.pkg                      |"""
    },
    {
        "filename": "10.15.md",
        "id": "mac_10_15",
        "slug": "/mac/v2g0d1y8",
        "title": "Office for Mac (macOS 10.15 Catalina)",
        "desc": "最高支持版本：16.66.1 (2021/2019 版)",
        "suites": """| 软件名称                  | 包含的组件 | 下载链接                                                                                                                                               |
|:-----------------------------|:---|:---------------------------------------------------------------------------------------------------------------------------------------------------|
| Office 全家桶 (含 Teams)    | Word, Excel, PowerPoint, Outlook, OneNote, Teams, OneDrive | https://officecdnmac.microsoft.com/pr/C1297A47-86C4-4C1F-97FA-950631F94777/MacAutoupdate/Microsoft_Office_16.66.22101101_BusinessPro_Installer.pkg |
| Office 全家桶 (不含 Teams) | Word, Excel, PowerPoint, Outlook, OneNote, OneDrive | https://officecdnmac.microsoft.com/pr/C1297A47-86C4-4C1F-97FA-950631F94777/MacAutoupdate/Microsoft_Office_16.66.22101101_Installer.pkg             |""",
        "standalone": """| 软件名称                  | 包含的组件 | 下载链接                                                                                                                                               |
|:-----------------------------|:---|:---------------------------------------------------------------------------------------------------------------------------------------------------|
| Word                         | Word, OneDrive | https://officecdnmac.microsoft.com/pr/C1297A47-86C4-4C1F-97FA-950631F94777/MacAutoupdate/Microsoft_Word_16.66.22101101_Updater.pkg                 |
| Excel                        | Excel, OneDrive | https://officecdnmac.microsoft.com/pr/C1297A47-86C4-4C1F-97FA-950631F94777/MacAutoupdate/Microsoft_Excel_16.66.22101101_Updater.pkg                |
| PowerPoint                   | PowerPoint, OneDrive | https://officecdnmac.microsoft.com/pr/C1297A47-86C4-4C1F-97FA-950631F94777/MacAutoupdate/Microsoft_PowerPoint_16.66.22101101_Updater.pkg           |
| Outlook                      | Outlook, OneDrive | https://officecdnmac.microsoft.com/pr/C1297A47-86C4-4C1F-97FA-950631F94777/MacAutoupdate/Microsoft_Outlook_16.66.22101101_Updater.pkg              |
| OneNote                      | OneNote, OneDrive | https://officecdnmac.microsoft.com/pr/C1297A47-86C4-4C1F-97FA-950631F94777/MacAutoupdate/Microsoft_OneNote_16.66.22101101_Updater.pkg              |"""
    },
    {
        "filename": "10.14.md",
        "id": "mac_10_14",
        "slug": "/mac/x3p9k4u6",
        "title": "Office for Mac (macOS 10.14 Mojave)",
        "desc": "最高支持版本：16.54 (2021/2019 版)",
        "suites": """| 软件名称                  | 包含的组件 | 下载链接                                                                                                                                               |
|:-----------------------------|:---|:---------------------------------------------------------------------------------------------------------------------------------------------------|
| Office 全家桶 (含 Teams)    | Word, Excel, PowerPoint, Outlook, OneNote, Teams, OneDrive | https://officecdnmac.microsoft.com/pr/C1297A47-86C4-4C1F-97FA-950631F94777/MacAutoupdate/Microsoft_Office_16.54.21101001_BusinessPro_Installer.pkg |
| Office 全家桶 (不含 Teams) | Word, Excel, PowerPoint, Outlook, OneNote, OneDrive | https://officecdnmac.microsoft.com/pr/C1297A47-86C4-4C1F-97FA-950631F94777/MacAutoupdate/Microsoft_Office_16.54.21101001_Installer.pkg             |""",
        "standalone": """| 软件名称                  | 包含的组件 | 下载链接                                                                                                                                               |
|:-----------------------------|:---|:---------------------------------------------------------------------------------------------------------------------------------------------------|
| Word                         | Word, OneDrive | https://officecdnmac.microsoft.com/pr/C1297A47-86C4-4C1F-97FA-950631F94777/MacAutoupdate/Microsoft_Word_16.54.21101001_Updater.pkg                 |
| Excel                        | Excel, OneDrive | https://officecdnmac.microsoft.com/pr/C1297A47-86C4-4C1F-97FA-950631F94777/MacAutoupdate/Microsoft_Excel_16.54.21101001_Updater.pkg                |
| PowerPoint                   | PowerPoint, OneDrive | https://officecdnmac.microsoft.com/pr/C1297A47-86C4-4C1F-97FA-950631F94777/MacAutoupdate/Microsoft_PowerPoint_16.54.21101001_Updater.pkg           |
| Outlook                      | Outlook, OneDrive | https://officecdnmac.microsoft.com/pr/C1297A47-86C4-4C1F-97FA-950631F94777/MacAutoupdate/Microsoft_Outlook_16.54.21101001_Updater.pkg              |
| OneNote                      | OneNote, OneDrive | https://officecdnmac.microsoft.com/pr/C1297A47-86C4-4C1F-97FA-950631F94777/MacAutoupdate/Microsoft_OneNote_16.54.21101001_Updater.pkg              |"""
    },
    {
        "filename": "10.13.md",
        "id": "mac_10_13",
        "slug": "/mac/f4d3s2a1",
        "title": "Office for Mac (macOS 10.13 High Sierra)",
        "desc": "最高支持版本：16.43.0 (2019 版)",
        "suites": """| 软件名称  | 包含的组件 | 下载链接                                                                                                                                  |
|:-------------|:---|:--------------------------------------------------------------------------------------------------------------------------------------|
| Office 全家桶 | Word, Excel, PowerPoint, Outlook, OneNote, OneDrive | https://officecdn.microsoft.com/pr/C1297A47-86C4-4C1F-97FA-950631F94777/MacAutoupdate/Microsoft_Office_16.43.20110804_Installer.pkg   |""",
        "standalone": """| 软件名称  | 包含的组件 | 下载链接                                                                                                                                  |
|:-------------|:---|:--------------------------------------------------------------------------------------------------------------------------------------|
| Word         | Word, OneDrive | https://officecdn.microsoft.com/pr/C1297A47-86C4-4C1F-97FA-950631F94777/MacAutoupdate/Microsoft_Word_16.43.20110804_Updater.pkg       |
| Excel        | Excel, OneDrive | https://officecdn.microsoft.com/pr/C1297A47-86C4-4C1F-97FA-950631F94777/MacAutoupdate/Microsoft_Excel_16.43.20110804_Updater.pkg      |
| PowerPoint   | PowerPoint, OneDrive | https://officecdn.microsoft.com/pr/C1297A47-86C4-4C1F-97FA-950631F94777/MacAutoupdate/Microsoft_PowerPoint_16.43.20110804_Updater.pkg |
| Outlook      | Outlook, OneDrive | https://officecdn.microsoft.com/pr/C1297A47-86C4-4C1F-97FA-950631F94777/MacAutoupdate/Microsoft_Outlook_16.43.20110804_Updater.pkg    |
| OneNote      | OneNote, OneDrive | https://officecdn.microsoft.com/pr/C1297A47-86C4-4C1F-97FA-950631F94777/MacAutoupdate/Microsoft_OneNote_16.43.20110804_Updater.pkg    |"""
    },
    {
        "filename": "10.12.md",
        "id": "mac_10_12",
        "slug": "/mac/v8c7x6z5",
        "title": "Office for Mac (macOS 10.12 Sierra)",
        "desc": "最高支持版本：16.30 (2019 版)",
        "suites": """| 软件名称  | 包含的组件 | 下载链接                                                                                                                                  |
|:-------------|:---|:--------------------------------------------------------------------------------------------------------------------------------------|
| Office 全家桶 | Word, Excel, PowerPoint, Outlook, OneNote, OneDrive | https://officecdn.microsoft.com/pr/C1297A47-86C4-4C1F-97FA-950631F94777/MacAutoupdate/Microsoft_Office_16.30.19101301_Installer.pkg   |""",
        "standalone": """| 软件名称  | 包含的组件 | 下载链接                                                                                                                                  |
|:-------------|:---|:--------------------------------------------------------------------------------------------------------------------------------------|
| Word         | Word, OneDrive | https://officecdn.microsoft.com/pr/C1297A47-86C4-4C1F-97FA-950631F94777/MacAutoupdate/Microsoft_Word_16.30.19101301_Updater.pkg       |
| Excel        | Excel, OneDrive | https://officecdn.microsoft.com/pr/C1297A47-86C4-4C1F-97FA-950631F94777/MacAutoupdate/Microsoft_Excel_16.30.19101301_Updater.pkg      |
| PowerPoint   | PowerPoint, OneDrive | https://officecdn.microsoft.com/pr/C1297A47-86C4-4C1F-97FA-950631F94777/MacAutoupdate/Microsoft_PowerPoint_16.30.19101301_Updater.pkg |
| Outlook      | Outlook, OneDrive | https://officecdn.microsoft.com/pr/C1297A47-86C4-4C1F-97FA-950631F94777/MacAutoupdate/Microsoft_Outlook_16.30.19101301_Updater.pkg    |
| OneNote      | OneNote, OneDrive | https://officecdn.microsoft.com/pr/C1297A47-86C4-4C1F-97FA-950631F94777/MacAutoupdate/Microsoft_OneNote_16.30.19101301_Updater.pkg    |"""
    },
    {
        "filename": "10.11.md",
        "id": "mac_10_11",
        "slug": "/mac/b2n3m4l5",
        "title": "Office for Mac (macOS 10.11 / 10.10)",
        "desc": "适用于 OS X El Capitan (10.11), Yosemite (10.10). 最高支持版本：16.16.27 (2016 版)",
        "suites": """| 软件名称  | 包含的组件 | 下载链接                                                                                                                                  |
|:-------------|:---|:--------------------------------------------------------------------------------------------------------------------------------------|
| Office 全家桶 | Word, Excel, PowerPoint, Outlook, OneNote, OneDrive | https://officecdn.microsoft.com/pr/C1297A47-86C4-4C1F-97FA-950631F94777/MacAutoupdate/Microsoft_Office_16.16.20101200_Installer.pkg   |""",
        "standalone": """| 软件名称  | 包含的组件 | 下载链接                                                                                                                                  |
|:-------------|:---|:--------------------------------------------------------------------------------------------------------------------------------------|
| Word         | Word, OneDrive | https://officecdn.microsoft.com/pr/C1297A47-86C4-4C1F-97FA-950631F94777/MacAutoupdate/Microsoft_Word_16.16.20101200_Updater.pkg       |
| Excel        | Excel, OneDrive | https://officecdn.microsoft.com/pr/C1297A47-86C4-4C1F-97FA-950631F94777/MacAutoupdate/Microsoft_Excel_16.16.20101200_Updater.pkg      |
| PowerPoint   | PowerPoint, OneDrive | https://officecdn.microsoft.com/pr/C1297A47-86C4-4C1F-97FA-950631F94777/MacAutoupdate/Microsoft_PowerPoint_16.16.20101200_Updater.pkg |
| Outlook      | Outlook, OneDrive | https://officecdn.microsoft.com/pr/C1297A47-86C4-4C1F-97FA-950631F94777/MacAutoupdate/Microsoft_Outlook_16.16.20101200_Updater.pkg    |
| OneNote      | OneNote, OneDrive | https://officecdn.microsoft.com/pr/C1297A47-86C4-4C1F-97FA-950631F94777/MacAutoupdate/Microsoft_OneNote_16.16.20101200_Updater.pkg    |"""
    }
]

for page in pages:
    # Format links to [链接](URL)
    suites_formatted = format_links(page['suites'])
    standalone_formatted = format_links(page['standalone'])
    
    content = f"""---
id: {page['id']}
slug: {page['slug']}
hide_table_of_contents: true
---

# {page['title']}

这里列出的 Office 安装包下载链接均指向微软官方文件。

{page['desc']}

<div className="info-box">
  <strong>💡 注意</strong>

  本网页仅展示软件本体下载链接，下载激活工具<strong><span style={{{{color: "#ff4d4f"}}}}>请查看发货内容中的激活链接</span></strong>。

  - 激活工具（序列化激活程序）提取自官方 ISO 文件。这些激活文件通常仅提供给[付费订阅用户（批量许可）](https://learn.microsoft.com/zh-cn/microsoft-365-apps/mac/volume-license-serializer)，但任何人都可以使用它来激活 Office。
  - 此激活方法与微软官方过程完全一致，不包含任何第三方破解程序。
</div>

#### 🎁 套装版 (全家桶)

{suites_formatted}

#### 📦 单独组件 (Word, Excel, PPT)

{standalone_formatted}
"""
    with open(os.path.join("docs", "mac", page['filename']), "w") as f:
        f.write(content)
