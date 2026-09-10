import re
from PIL import Image

# 1. 压缩teacher.png
print("压缩teacher.png...")
img = Image.open("teacher.png")
if img.mode == "RGBA":
    bg = Image.new("RGB", img.size, (255, 255, 255))
    bg.paste(img, mask=img.split()[3])
    img = bg
img.thumbnail((1200, 1200), Image.LANCZOS)
img.save("teacher.jpg", format="JPEG", quality=82, optimize=True)
print("teacher压缩完成")

# 2. 更新引用
print("更新引用...")
with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()
html = html.replace("teacher.png", "teacher.jpg")
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("引用已更新")
print("全部完成")
