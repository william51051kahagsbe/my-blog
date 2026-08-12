import csv
import os
import re

# 1. 配置文件路径
csv_filename = "data.csv"
output_dir = "content/posts"  # 生成的文件保存路径

# 如果输出目录不存在则创建
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 2. 读取 CSV 并生成 Markdown
with open(csv_filename, mode="r", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)

    count = 0
    for row in reader:
        # 获取 CSV 各列数据（请根据你 CSV 的实际表头名称微调 key）
        title = row.get("标题", "").strip().replace('"', '\\"')
        rj_id = row.get("RJ号", "").strip()
        cover = row.get("封面", "").strip()
        rating = row.get("分级/年龄向", "").strip()
        circle = row.get("社团", "").strip()
        tags_raw = row.get("标签", "").strip()
        link = row.get("网盘链接", "").strip()
        code = row.get("解压码", "").strip()

        # 跳过空行或无 RJ号 的行
        if not rj_id:
            continue

        # 处理标签列表（按空格或逗号分割）
        tags_list = [
            t.strip() for t in re.split(r"[,，\s]+", tags_raw) if t.strip()
        ]
        if circle:
            tags_list.append(circle)  # 可以顺便把社团也加入标签中
        tags_json = (
            str(tags_list).replace("'", '"') if tags_list else '["同人音声"]'
        )

        # 格式化文件名（例如：RJ01672667.md）
        filename = f"{rj_id}.md"
        filepath = os.path.join(output_dir, filename)

        # 组装 Hugo Front Matter 格式
        md_content = f"""---
title: "{title}"
date: 2026-08-13T00:00:00+08:00
draft: false
rj_id: "{rj_id}"
cover: "{cover}"
rating: "{rating}"
tags: {tags_json}
download_link: "{link}"
extract_code: "{code}"
---

{{{{< voice_card >}}}}

### 剧情简介
（暂无详细简介）
"""

        # 写入文件
        with open(filepath, "w", encoding="utf-8") as out_f:
            out_f.write(md_content)

        count += 1

print(f"成功批量生成 {count} 篇音声文章到 {output_dir}/ 目录！")