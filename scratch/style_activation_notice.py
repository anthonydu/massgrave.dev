import os

files = [
    "docs/11/2013.md",
    "docs/11/2016.md",
    "docs/11/2019.md",
    "docs/11/2021.md",
    "docs/11/2024.md",
    "docs/11/365.md",
    "docs/8/2013.md",
    "docs/8/2016.md"
]

target_text = "这里提供的都是微软官方原版的 Office 安装包。它们都是零售版 (Retail)，并且自带最新的更新。"
# The old notice text I added in the previous turn
old_notice_text = "此网页仅展示软件安装链接，<strong>激活工具不在本网页上，请前往商品说明书（教程）</strong>的激活部分内容查看具体激活方式及步骤。
<div className="info-box">
由于 Win 系统对文件形式的激活工具有严格限制，我们会使用 PowerShell 用复制粘贴一串代码的形式直接下载并打开激活工具，不会也无需下载任何独立文件。
</div>

现在请先下载您需要的安装包，<strong>激活步骤仅可在安装完成后进行</strong>，不可在安装完成前提前进行。"

# The new styled notice
new_styled_notice = """
<div className="info-box">
  <strong>💡 激活提示</strong>




  此网页仅展示软件安装链接，<strong>激活工具不在本网页上，请前往商品说明书（教程）</strong>的激活部分内容查看具体激活方式及步骤。
<div className="info-box">
由于 Win 系统对文件形式的激活工具有严格限制，我们会使用 PowerShell 用复制粘贴一串代码的形式直接下载并打开激活工具，不会也无需下载任何独立文件。
</div>

现在请先下载您需要的安装包，<strong>激活步骤仅可在安装完成后进行</strong>，不可在安装完成前提前进行。
</div>
"""

for rel_path in files:
    abs_path = os.path.join("/Users/dpu0122/code/massgrave.dev", rel_path)
    if not os.path.exists(abs_path):
        print(f"File not found: {abs_path}")
        continue
    
    with open(abs_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace the old notice if it exists, or insert if it doesn't (though it should exist now)
    if old_notice_text in content:
        # Avoid double wrapping if already styled
        if '<div className="info-box">' in content and '💡 激活提示' in content:
             print(f"Styled notice already exists in {rel_path}")
             continue
        
        # We need to be careful with the replacement to not leave extra newlines
        # The previous turn added it as f"{target_text}\n\n{old_notice_text}"
        new_content = content.replace(f"{target_text}\n\n{old_notice_text}", f"{target_text}\n{new_styled_notice}")
        with open(abs_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {rel_path} with styled box")
    elif target_text in content:
        # Fallback if the previous turn didn't run or failed for some reason
        new_content = content.replace(target_text, f"{target_text}\n{new_styled_notice}")
        with open(abs_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Inserted styled box in {rel_path}")
    else:
        print(f"Target text not found in {rel_path}")
