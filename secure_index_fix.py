import os

def secure_index():
    path = 'docs/index.md'
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    new_lines = []
    # Frontmatter
    new_lines.append('---\n')
    new_lines.append('slug: /\n')
    new_lines.append('---\n\n')
    
    # Imports
    new_lines.append("import Tabs from '@theme/Tabs';\n")
    new_lines.append("import TabItem from '@theme/TabItem';\n\n")
    
    # Visible content
    new_lines.append("# 懿琪数科优选@淘宝 - 内部资源站\n\n")
    new_lines.append("欢迎访问我们的内部资源下载门户。\n\n")
    new_lines.append(":::info 访问提示\n")
    new_lines.append("本站点仅供内部使用或通过特定链接访问。如果您没有获得授权链接，请联系系统管理员或您的服务提供商。\n")
    new_lines.append(":::\n\n")
    
    # Start comment
    new_lines.append("{/* \n")
    new_lines.append("原本的首页内容已在此隐藏，以防止路径泄露。用户无法在浏览器中看到以下内容。\n\n")
    
    # Add original content (skipping the first few lines of frontmatter and title if already added)
    # Actually, I'll just skip lines 1-7 from original
    start_collecting = False
    for i, line in enumerate(lines):
        if i >= 7: # Skip existing frontmatter and imports from the previous bad write
            new_lines.append(line)
    
    # End comment
    new_lines.append("\n*/}\n")
    
    with open(path, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)

if __name__ == '__main__':
    secure_index()
