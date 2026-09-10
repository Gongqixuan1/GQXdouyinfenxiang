import re
import urllib.request

# 1. 下载头像
print("下载头像...")
urllib.request.urlretrieve(
    "https://raw.githubusercontent.com/Gongqixuan1/rongrong-portfolio/backup-before-interactive-features/avatar.jpg",
    "avatar.jpg"
)
print("头像下载完成")

# 2. 修复作品集位置
print("修复作品集位置...")
with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

works_match = re.search(
    r'(<section class="section soft"><div class="wrap"><div class="works">.*?</div></div></section>)',
    html, re.DOTALL
)
if works_match:
    works = works_match.group(1)
    html = html.replace(works, "")
    exp_end = html.find('</section>', html.find('id="experience"'))
    if exp_end > 0:
        html = html[:exp_end+10] + works + html[exp_end+10:]
        print("作品集位置已修复")
    else:
        print("未找到实习经历结束位置")
else:
    print("未找到作品集section")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
print(f"index.html: {len(html)} bytes")

# 3. 笔记页插入图片
print("处理笔记页...")
with open("note-01.html", "r", encoding="utf-8") as f:
    note = f.read()

img_tag = '<div style="text-align:center;margin:20px 0 30px;"><img src="note1.png" alt="笔记配图" style="max-width:100%;height:auto;border-radius:12px;"></div>'

if 'note1.png' not in note:
    # 在note-body前面插入
    if '<div class="note-body">' in note:
        note = note.replace('<div class="note-body">', img_tag + '\n<div class="note-body">')
        print("笔记图片已插入")
    else:
        print("未找到note-body")
else:
    print("笔记图片已存在")

with open("note-01.html", "w", encoding="utf-8") as f:
    f.write(note)
print(f"note-01.html: {len(note)} bytes")
print("全部完成")
