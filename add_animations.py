import re

print("添加数字滚动动画和名字手写体效果...")

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# ========== 1. 给关键数字加span标签 ==========
# 凭证1000余份
html = html.replace("累计处理会计凭证1000余份", '累计处理会计凭证<span class="num-animate" data-target="1000">0</span>余份')
# 超200万元
html = html.replace("累计转介落地存款及理财资金超200万元", '累计转介落地存款及理财资金超<span class="num-animate" data-target="200">0</span>万元')
# 80余人次
html = html.replace("日均接待客户80余人次", '日均接待客户<span class="num-animate" data-target="80">0</span>余人次')
# 20+篇
html = html.replace("累计产出垂直行业原创内容20+篇", '累计产出垂直行业原创内容<span class="num-animate" data-target="20">0</span>+篇')
# 60余位
html = html.replace("累计引流获客60余位", '累计引流获客<span class="num-animate" data-target="60">0</span>余位')
# 20家
html = html.replace("筛选后建群深度沟通20家", '筛选后建群深度沟通<span class="num-animate" data-target="20">0</span>家')
# 落地5家
html = html.replace("最终协助推动业务合作落地5家", '最终协助推动业务合作落地<span class="num-animate" data-target="5">0</span>家')
print("数字标签已添加")

# ========== 2. 添加CSS（手写体+数字动画样式） ==========
css_add = """
<style>
/* 名字手写体悬停效果 */
h1 {
  transition: font-family 0.3s ease;
}
h1:hover {
  font-family: "Ma Shan Zheng", "Zhi Mang Xing", "楷体", "华文行楷", cursive;
  letter-spacing: 0.05em;
}
/* 导航品牌名手写体 */
.brand:hover, .logo:hover {
  font-family: "Ma Shan Zheng", "Zhi Mang Xing", "楷体", "华文行楷", cursive;
}
/* 数字动画样式 */
.num-animate {
  font-weight: 700;
  color: var(--orange, #e75480);
  display: inline-block;
  min-width: 1.5em;
  text-align: center;
}
</style>
"""

# 在第一个</style>后面插入（如果有style标签）
if "</style>" in html:
    html = html.replace("</style>", "</style>\n" + css_add, 1)
else:
    # 在</head>前插入
    html = html.replace("</head>", css_add + "\n</head>")
print("CSS已添加")

# ========== 3. 添加JavaScript（数字滚动动画） ==========
js_add = """
<script>
// 数字滚动动画
(function() {
  function animateNumber(el) {
    var target = parseInt(el.getAttribute('data-target'), 10);
    var duration = 1500;
    var startTime = null;
    function step(timestamp) {
      if (!startTime) startTime = timestamp;
      var progress = Math.min((timestamp - startTime) / duration, 1);
      // easeOutQuart
      var eased = 1 - Math.pow(1 - progress, 4);
      var current = Math.floor(eased * target);
      el.textContent = current;
      if (progress < 1) {
        requestAnimationFrame(step);
      } else {
        el.textContent = target;
      }
    }
    requestAnimationFrame(step);
  }
  var observer = new IntersectionObserver(function(entries) {
    entries.forEach(function(entry) {
      if (entry.isIntersecting) {
        animateNumber(entry.target);
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.5 });
  document.querySelectorAll('.num-animate').forEach(function(el) {
    observer.observe(el);
  });
})();
</script>
"""

# 在</body>前插入
if "</body>" in html:
    html = html.replace("</body>", js_add + "\n</body>")
else:
    html += js_add
print("JavaScript已添加")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
print(f"index.html: {len(html)} bytes")
print("全部完成")
