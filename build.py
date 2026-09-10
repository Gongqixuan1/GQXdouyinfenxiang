#!/usr/bin/env python3
import re, urllib.request

# 1. 下载基础模板
url = "https://raw.githubusercontent.com/Gongqixuan1/rongrong-portfolio/backup-before-interactive-features/index.html"
html = urllib.request.urlopen(url).read().decode('utf-8')
print(f"Downloaded: {len(html)} bytes")

# 2. 导航栏删除 TIME MAP / PROJECTS / CONTACT
html = html.replace('<a href="#about">TIME MAP</a>', '')
html = html.replace('<a href="#projects">PROJECTS</a>', '')
html = html.replace('<a href="#contact">CONTACT</a>', '')

# 3. hero 删除 GRAD 卡片（含重庆科技大学）
html = re.sub(r'<div class="fact"><label>GRAD</label><strong>2027</strong><small>重庆科技大学</small></div>', '', html)

# 4. 删除整个 MY TIME MAP 板块
html = re.sub(r'<section id="about"[^>]*>.*?</section>', '', html, flags=re.DOTALL)

# 5. 实习经历公司名脱敏
html = html.replace('重庆中瑞诚会计师事务所', '事务所')
html = html.replace('招商银行重庆巴南支行', '银行')
html = html.replace('深圳亿龙达信息技术有限公司', '跨境物流公司')
html = html.replace('精准推荐重庆巴南支行', '精准推荐该银行')
html = html.replace('重庆科技大学大学生创业助学基地', '某高校大学生创业助学基地')

# 6. 删除整个项目经历板块（含封面作品集）
html = re.sub(r'<section id="projects"[^>]*>.*?</section>', '', html, flags=re.DOTALL)

# 7. 删除整个联系方式板块
html = re.sub(r'<section id="contact"[^>]*>.*?</section>', '', html, flags=re.DOTALL)

# 8. 重新编号
html = html.replace('02 — INTERNSHIPS', '01 — INTERNSHIPS')
html = html.replace('04 — COMPETITIONS', '02 — COMPETITIONS')
html = html.replace('05 — SIDE ROLES', '03 — SIDE ROLES')
html = html.replace('06 — SKILLS', '04 — SKILLS')

# 9. 新增头脑风暴板块
bs = '<section id="brainstorm" class="section soft"><div class="wrap"><div class="top"><div><div class="kicker">05 — BRAINSTORM</div><h2 class="title">宫启宣的头脑风暴</h2></div></div><p style="color:var(--muted);font-size:15px;margin-bottom:36px;">记录一些对生活中遇到的疑问！</p><div class="brainstorm-list"><a href="note-01.html" class="brainstorm-item"><div class="brainstorm-no">疑问 01</div><h3>抖音的小程序游戏是怎么盈利的</h3><span class="brainstorm-arrow">→ 查看笔记</span></a></div></div></section>'
html = html.replace('</main>', bs + '</main>')

# 10. 头脑风暴 CSS
css = '''
.brainstorm-list{display:flex;flex-direction:column;gap:14px}
.brainstorm-item{display:block;background:#fff;border:1px solid var(--line);padding:24px 28px;transition:.25s;text-decoration:none;color:inherit}
.brainstorm-item:hover{transform:translateY(-3px);box-shadow:0 12px 30px #0b1f3a12;border-color:var(--orange)}
.brainstorm-no{font-size:9px;color:var(--orange);font-weight:700;letter-spacing:.12em;margin-bottom:8px}
.brainstorm-item h3{font-size:22px;margin:0 0 6px;font-weight:700}
.brainstorm-arrow{font-size:12px;color:var(--orange);font-weight:600}
@media(max-width:560px){.brainstorm-item{padding:18px 20px}.brainstorm-item h3{font-size:18px}}
'''
html = html.replace('</style>', css + '</style>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print(f"index.html: {len(html)} bytes")
print(f"  about={html.count('id=\"about\"')} projects={html.count('id=\"projects\"')} contact={html.count('id=\"contact\"')}")
print(f"  brainstorm={html.count('id=\"brainstorm\"')} 大学={html.count('重庆科技大学')}")

# 11. 生成笔记页 note-01.html
note = '''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>抖音小程序游戏怎么盈利 · 宫启宣的头脑风暴</title><style>
@import url("https://fonts.googleapis.com/css2?family=Zhi+Mang+Xing&display=swap");
:root{--ink:#0b1f3a;--orange:#e75480;--blue:#4c6fff;--pink:#f5a9c5;--yellow:#ffd86b;--cream:#fff9f1;--paper:#f7f8fa;--muted:#66758a;--line:#e3e7ed}
*{box-sizing:border-box}body{margin:0;color:var(--ink);font-family:Inter,-apple-system,BlinkMacSystemFont,'PingFang SC','Microsoft YaHei',sans-serif;line-height:1.9;background:var(--cream)}
.nav{position:sticky;top:0;z-index:100;background:#ffffffee;backdrop-filter:blur(10px);border-bottom:1px solid var(--line)}.navin{max-width:820px;margin:auto;padding:14px 24px;display:flex;align-items:center;justify-content:space-between}.brand{font-weight:700;font-size:15px}.back-btn{font-size:12px;color:var(--orange);text-decoration:none;font-weight:600;padding:6px 14px;border:1px solid var(--orange);border-radius:20px;transition:.2s}.back-btn:hover{background:var(--orange);color:#fff}
.note-wrap{max-width:820px;margin:auto;padding:48px 24px 80px}
.note-eyebrow{font-size:10px;letter-spacing:.15em;color:var(--orange);font-weight:700;margin-bottom:12px}
.note-title{font-family:'Zhi Mang Xing','STKaiti','KaiTi',cursive;font-size:clamp(36px,6vw,56px);line-height:1.2;margin:0 0 8px}
.note-meta{font-size:12px;color:var(--muted);margin-bottom:40px;padding-bottom:24px;border-bottom:1px solid var(--line)}
.note-body h2{font-size:22px;margin:40px 0 14px;padding-left:14px;border-left:4px solid var(--orange);line-height:1.4}
.note-body h3{font-size:17px;margin:28px 0 10px;color:var(--ink)}
.note-body p{font-size:14.5px;color:#334155;margin:0 0 14px;line-height:1.9}
.note-body ul{margin:0 0 14px;padding-left:22px}.note-body li{font-size:14px;color:#334155;margin-bottom:8px;line-height:1.8}
.note-body strong{color:var(--ink)}
.highlight-box{background:#fff;border:1px solid var(--line);border-radius:12px;padding:20px 24px;margin:20px 0}
.summary-box{background:linear-gradient(135deg,#fff5f8,#fff0f5);border:1px solid #f5c9d8;border-radius:12px;padding:24px;margin-top:40px}
.summary-box h2{border-left-color:var(--orange);margin-top:0}
.win-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin-top:16px}
.win-card{background:#fff;border-radius:10px;padding:16px;border:1px solid #f5c9d8}
.win-card h4{margin:0 0 8px;font-size:14px;color:var(--orange)}
.win-card p{font-size:12.5px;color:#555;margin:0;line-height:1.7}
@media(max-width:640px){.win-grid{grid-template-columns:1fr}.note-wrap{padding:32px 18px 60px}}
</style></head><body>
<nav class="nav"><div class="navin"><div class="brand">宫启宣 ✦ 头脑风暴</div><a href="index.html" class="back-btn">← 返回主页</a></div></nav>
<div class="note-wrap">
<div class="note-eyebrow">疑问 01 · BRAINSTORM NOTE</div>
<h1 class="note-title">抖音的小程序游戏是怎么盈利的</h1>
<div class="note-meta">记录一些对生活中遇到的疑问！ · 宫启宣</div>
<div class="note-body">
<h2>💰 模式一：广告变现 (IAA, In-App Advertising)</h2>
<p>这是目前很多小游戏，尤其是轻度休闲游戏的主要收入来源。游戏本身免费，通过向玩家展示广告来获利。</p>
<h3>运作方式</h3>
<p>玩家在游戏过程中，为了获得额外生命、道具、游戏币或通关等，需要观看一段视频广告（通常是15-30秒的激励视频）。</p>
<h3>收入分成</h3>
<p>开发者的收入主要来自广告展示。根据抖音官方规则，广告收入的分成比例如下：</p>
<ul>
<li><strong>投广场景</strong>（指游戏开发者在抖音进行广告投放来推广自己的游戏）：开发者可获得广告收入的 <strong>90%</strong>。</li>
<li><strong>非投广场景</strong>：开发者可获得广告收入的 <strong>60%</strong>。</li>
</ul>
<h3>成功案例</h3>
<p>游戏《赵云与阿斗》就是"纯广告变现"模式的典型代表。它没有任何充值入口，玩家通过观看激励视频来获取游戏资源。凭借海量用户和高频广告展示，它成功登顶了抖音小游戏热门榜与畅销榜双榜首位。</p>
<h2>💎 模式二：内购变现 (IAP, In-App Purchase)</h2>
<p>这种模式常见于中重度游戏，玩家在游戏内直接付费购买虚拟道具、皮肤、特权、钻石等。</p>
<h3>收入分成</h3>
<p>内购收入的分成相对复杂，分为"一般"和"减免版"两种政策。</p>
<ul>
<li><strong>一般内购收益政策</strong>：所有场景下，开发者可获得内购消费总额的 <strong>60%</strong>。</li>
<li><strong>减免版内购收益政策</strong>：满足平台特定条件（如接入特定功能、达到一定用户渗透率等）的游戏，可获得更高分成。
<ul>
<li>投广场景：安卓端内购收入的 <strong>90%</strong>，iOS端内购收入的 <strong>99%</strong>。</li>
<li>非投广场景：安卓与iOS双端内购收入的 <strong>80%</strong>。</li>
</ul></li>
</ul>
<h2>🧩 模式三：混合变现</h2>
<p>这是目前很多小游戏采用的策略，结合了"广告+内购"两种模式。轻度玩家可以通过看广告免费游玩，而重度玩家则可以选择直接付费，从而最大化游戏的总体收入。</p>
<h2>🎁 平台的"额外激励"</h2>
<p>除了上述直接收入，抖音平台还提供了多种激励政策，帮助开发者增加收益。</p>
<ul>
<li><strong>投放金与任务金</strong>：在特定场景下，开发者除了获得现金收益，还能获得额外的"投放金"或"任务金"，可用于在抖音平台进行广告投放。例如，在投广场景下，开发者可获得广告收入 5% 的投放金。</li>
<li><strong>内容激励</strong>：通过"巨量星图"平台的"游戏发行人计划"，开发者或内容创作者可以通过制作游戏相关视频获取收益。</li>
<li><strong>新游扶持</strong>：平台会为新上线游戏提供高额激励。例如，曾有政策对"同发新游"给予高达 25% 的返点，最高激励可达数百万元。</li>
</ul>
<div class="highlight-box">
<h3>🎯 问题一：为什么我们"不看"，广告商还要买单？</h3>
<p>关键在于，广告商买的不是你的"认真观看"，而是你的<strong>"有效行为"</strong>。</p>
<p>这种广告模式叫激励视频广告（Rewarded Video Ad）。它的核心是注意力交易：你用15-30秒的时间和一次主动点击，换取游戏里的道具、复活机会等奖励。</p>
<p>广告商看重的正是这种"主动"带来的高价值：</p>
<ul>
<li><strong>高完成率</strong>：因为是主动换取奖励，这类广告的完播率高达95%。</li>
<li><strong>高转化率</strong>：愿意为奖励看广告的用户，本身就带有需求，后续产生下载、注册等行为的可能性更高。</li>
<li><strong>精准触达</strong>：广告平台（如穿山甲）能根据你的游戏喜好、设备等画像，推送你可能感兴趣的广告，让投放更精准。</li>
</ul>
<p>简单来说，广告商不是在为你的"注视"付费，而是在为一次高概率的潜在转化机会付费。</p>
</div>
<div class="highlight-box">
<h3>💰 问题二：广告商是怎么付费的？</h3>
<p>广告商的付费方式很灵活，主要有以下几种计费模式：</p>
<ul>
<li><strong>CPM (千次展示成本)</strong>：这是激励视频广告最主要的计费方式。广告主为每1000次广告展示付费。激励视频的eCPM（有效千次展示收益）远高于普通横幅广告，能达到50-120元，是后者的5-6倍。</li>
<li><strong>CPC (单次点击成本)</strong>：用户点击了广告，广告主才付费。</li>
<li><strong>CPA (单次行动成本)</strong>：用户观看后，进一步完成了下载、安装、注册等特定行为，广告主才为此付费。</li>
</ul>
</div>
<div class="highlight-box">
<h3>🎮 问题三：游戏开发者如何从中分成？</h3>
<p>抖音作为一个平台，连接了广告商和游戏开发者。广告商的钱先给到平台，平台再按规则分给开发者。</p>
<p>根据抖音的公开政策，游戏开发者的分成比例相当可观：</p>
<ul>
<li><strong>投广场景</strong>：指开发者自己也在抖音投放广告来推广游戏。这种情况下，开发者能获得广告收入的<strong>90%</strong>现金收益。</li>
<li><strong>非投广场景</strong>：开发者没有进行广告投放。这种情况下，开发者能获得广告收入的<strong>60%</strong>现金收益。</li>
</ul>
<p>所以，你每看完一个15秒的激励视频广告，广告商支付的费用就会按 <strong>"广告商 → 抖音平台 → 游戏开发者"</strong> 的路径进行分配。</p>
</div>
</div>
<div class="summary-box">
<h2>💎 总结</h2>
<p>这个模式其实是一个三方共赢的系统：</p>
<div class="win-grid">
<div class="win-card"><h4>对于你（玩家）</h4><p>不用花钱，花点时间就能获得游戏道具和更好的体验。</p></div>
<div class="win-card"><h4>对于广告商</h4><p>用相对低廉的成本，换取了一次高价值的精准营销和潜在转化。</p></div>
<div class="win-card"><h4>对于开发者</h4><p>通过免费游戏吸引海量用户，再将用户的注意力转化为收入。</p></div>
</div>
</div>
</div>
</body></html>'''

with open('note-01.html', 'w', encoding='utf-8') as f:
    f.write(note)
print(f"note-01.html: {len(note)} bytes")
print("Build complete!")
