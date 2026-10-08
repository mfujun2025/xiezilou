"""
Apply enrichment to articles. Reads BATCH data and replaces article content.
Usage: python apply_batch.py <batch_number>
"""
import os
import re
import sys

BLOG_DIR = "D:/louyuzuchang-fix/articles"
os.chdir("D:/louyuzuchang-fix")

# Import batch data
batch_num = sys.argv[1] if len(sys.argv) > 1 else "1"
mod = __import__(f"batch_data_{batch_num}")
BATCH = mod.BATCH

success = 0
fail = 0
for slug, title, tag, color, intro, sections in BATCH:
    filepath = os.path.join(BLOG_DIR, f"{slug}.html")
    if not os.path.exists(filepath):
        print(f"MISS: {slug}")
        fail += 1
        continue
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    # Build new article body
    sec_html = ""
    for h2, body in sections:
        sec_html += f'\n        <h2 class="text-2xl font-bold mt-8 mb-4 text-gray-900">{h2}</h2>\n'
        for para in body.strip().split("\n"):
            para = para.strip()
            if para:
                sec_html += f'        <p class="mb-4 text-gray-700 leading-relaxed">{para}</p>\n'
    # Locate body
    start_marker = '<div class="prose max-w-none">'
    end_marker = '<div class="mt-12 pt-8 border-t">'
    s = content.find(start_marker)
    e = content.find(end_marker)
    if s == -1 or e == -1:
        print(f"MARKER MISS: {slug}")
        fail += 1
        continue
    new_body = (
        f'\n        <div class="bg-{color}-50 border-l-4 border-{color}-500 p-4 mb-8 rounded">\n'
        f'          <p class="text-{color}-900 font-medium">本文导览</p>\n'
        f'          <p class="text-sm text-{color}-800 mt-1">{intro[:80]}...</p>\n'
        f'        </div>\n'
        f'\n        <p class="mb-4 text-gray-700 leading-relaxed">{intro}</p>\n'
        f'{sec_html}\n'
    )
    new_content = content[:s] + f'<div class="prose max-w-none">{new_body}      </div>\n\n      ' + content[e:]
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)
    print(f"OK: {slug} ({len(new_body)} bytes)")
    success += 1
print(f"\nDone: {success} success, {fail} fail")
