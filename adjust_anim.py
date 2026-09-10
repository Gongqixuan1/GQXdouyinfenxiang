import re

print("调整动画参数...")

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. 手写体过渡时间从0.3s改成0.8s
html = html.replace("transition: font-family 0.3s ease;", "transition: font-family 0.8s ease;")
print("手写体过渡已调整为0.8秒")

# 2. 数字滚动时间从1500改成2500
html = html.replace("var duration = 1500;", "var duration = 2500;")
print("数字滚动时间已调整为2.5秒")

# 3. 去掉unobserve，让每次进入视口都重新动画
html = html.replace("observer.unobserve(entry.target);", "// 每次进入都重新动画，不取消观察")
print("已改为每次滑到都重新触发")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
print(f"index.html: {len(html)} bytes")
print("完成")
