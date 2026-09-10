import re

# ========== 1. 删除技能板块 ==========
print("删除技能板块...")
with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 删除id="skills"的整个section
html = re.sub(r'\s*<section id="skills"[^>]*>.*?</section>', '', html, flags=re.DOTALL)

# 重新编号：brainstorm从05改成04
html = html.replace("05 — BRAINSTORM", "04 — BRAINSTORM")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
print(f"index.html: {len(html)} bytes")

# ========== 2. 缩减笔记内容 ==========
print("缩减笔记内容...")

new_body = '''
<div class="note-body">
<h3>💰 模式一：广告变现（IAA）</h3>
<p>游戏免费，玩家通过观看15-30秒激励视频广告获取道具、复活等奖励。</p>
<p><strong>分成：</strong>投广场景开发者获90%，非投广场景获60%。</p>
<p><strong>案例：</strong>《赵云与阿斗》纯广告变现，登顶热门榜与畅销榜双榜首。</p>

<h3>💎 模式二：内购变现（IAP）</h3>
<p>玩家付费购买虚拟道具、皮肤、特权等。</p>
<p><strong>分成：</strong>一般政策开发者获60%；满足条件的减免版，投广场景安卓90%/iOS99%，非投广场景双端80%。</p>

<h3>🧩 模式三：混合变现</h3>
<p>广告+内购结合，轻度玩家看广告免费玩，重度玩家直接付费，最大化收入。</p>

<h3>🎁 平台额外激励</h3>
<p>投放金/任务金（投广场景额外5%）、内容激励（巨量星图发行人计划）、新游扶持（最高25%返点）。</p>

<h3>🎯 三个核心问题</h3>

<h4>问题一：为什么我们"不看"，广告商还要买单？</h4>
<p>广告商买的不是"认真观看"，而是"有效行为"。激励视频的核心是注意力交易：你用时间和主动点击换取游戏奖励。</p>
<p>价值在于：完播率高达95%、用户有需求转化率高、平台能精准触达。简单说，广告商为高概率的潜在转化机会付费。</p>

<h4>问题二：广告商怎么付费？</h4>
<ul>
<li><strong>CPM（千次展示）：</strong>最主要方式，激励视频eCPM达50-120元，是普通横幅的5-6倍</li>
<li><strong>CPC（单次点击）：</strong>点击才付费</li>
<li><strong>CPA（单次行动）：</strong>完成下载/安装/注册才付费</li>
</ul>

<h4>问题三：开发者怎么分成？</h4>
<p>广告费按"广告商→抖音平台→开发者"路径分配。投广场景开发者获90%，非投广场景获60%。</p>

<h3>💎 总结：三方共赢</h3>
<ul>
<li><strong>玩家：</strong>不花钱，花时间获得更好体验</li>
<li><strong>广告商：</strong>低成本换取高价值精准营销</li>
<li><strong>开发者：</strong>免费游戏吸引海量用户，将注意力转化为收入</li>
</ul>
</div>
'''

with open("note-01.html", "r", encoding="utf-8") as f:
    note = f.read()

# 替换note-body
note = re.sub(r'<div class="note-body">.*?</div>\s*</div>', new_body.strip() + '\n</div>', note, flags=re.DOTALL)

with open("note-01.html", "w", encoding="utf-8") as f:
    f.write(note)
print(f"note-01.html: {len(note)} bytes")
print("全部完成")
