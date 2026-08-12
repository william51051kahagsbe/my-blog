import csv
import json
import os

csv_filename = "data.csv"
output_dir = "content/posts"

os.makedirs(output_dir, exist_ok=True)

with open(csv_filename, mode="r", encoding="utf-8") as f:
    reader = csv.reader(f)

    count = 0
    for row in reader:
        if not row or len(row) < 9:
            continue

        title = row[0].strip()
        rj_id = row[1].strip()
        cover_raw = row[2].strip()
        rating = row[3].strip()
        has_translation = row[4].strip()
        circle = row[5].strip()
        tags_raw = row[6].strip()
        link = row[7].strip()
        code = row[8].strip()

        if not rj_id.upper().startswith("RJ"):
            continue

        cover = ""
        if cover_raw.startswith("attachment:"):
            filename = cover_raw.split(":")[-1]
            cover = f"/images/{filename}"
        else:
            cover = cover_raw

        # 处理标签
        tags = [t.strip() for t in tags_raw.split(",") if t.strip()]
        if has_translation == "有" and "汉化" not in tags:
            tags.append("汉化")

        safe_title = json.dumps(title, ensure_ascii=False)
        tags_json = json.dumps(tags, ensure_ascii=False)
        circles_json = json.dumps([circle] if circle else [], ensure_ascii=False)
        ratings_json = json.dumps([rating] if rating else [], ensure_ascii=False)

        md_content = f"""---
title: {safe_title}
date: 2026-08-13T00:00:00+08:00
draft: false
rj_id: "{rj_id}"
circles: {circles_json}
ratings: {ratings_json}
rating: "{rating}"
circle: "{circle}"
cover:
  image: "{cover}"
tags: {tags_json}
download_link: "{link}"
extract_code: "{code}"
---

{{{{< voice_card >}}}}

### 剧情简介
（暂无详细简介，欢迎补充）
"""

        filepath = os.path.join(output_dir, f"{rj_id}.md")
        with open(filepath, "w", encoding="utf-8") as out_file:
            out_file.write(md_content)

        count += 1

print(f"✅ 成功更新 {count} 篇文章分类数据！")