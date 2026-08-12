import os
import re
import glob

content_dir = "content/posts/"  # 你的文章目录

for filepath in glob.glob(os.path.join(content_dir, "*.md")):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 查找现有 rj_id
    m = re.search(r'^rj_id:\s*"RJ(\d+)"', content, re.MULTILINE)
    if not m:
        continue
    rj_num = int(m.group(1))  # 转为整数（自动去除前导零）
    
    # 检查是否已有 rj_num，避免重复添加
    if re.search(r'^rj_num:', content, re.MULTILINE):
        continue
    
    # 在 rj_id 行后插入 rj_num
    new_content = re.sub(
        r'(^rj_id:\s*"[^"]+")\n',
        r'\1\nrj_num: ' + str(rj_num) + '\n',
        content,
        flags=re.MULTILINE
    )
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated: {filepath}")