#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
为 写字楼出租.cn 新增 4 篇长尾 SEO 文章（不覆盖既有 100 篇矩阵）：
  - xiezilou-bangongshi-qubie  写字楼出租和办公室出租的区别
  - jiaji-xiezilou             甲级写字楼出租怎么选（甲乙丙分级）
  - xiezilou-zhongjie-zhijie   写字楼出租中介 vs 直租（渠道怎么选）
  - lianhe-gongzuoshi         联合办公/共享办公出租（vs 传统写字楼）
采用与全站一致的页面外壳（head + OG/Twitter + Article JSON-LD + sticky header +
breadcrumb + 本文导览 + H2 正文 + 常见问题 + 相关文章 + CTA + footer）。
同时把新文章写入 sitemap.xml，并在 articles/index.html 与首页 最新资讯 网格插入卡片。
"""
import os

ROOT = r"D:/.workbuddy/2026-10-12-14-59-49/xiezilou"
BLOG = os.path.join(ROOT, "articles")
SITEMAP = os.path.join(ROOT, "sitemap.xml")
ART_INDEX = os.path.join(BLOG, "index.html")
HOME = os.path.join(ROOT, "index.html")
DATE = "2026-10-13"
DOMAIN = "https://xn--g7q0iw0x3volkt.cn"

# ---------------------------------------------------------------- 数据
# 每篇: slug, title, desc, keywords, tag, color, intro, sections[(h2, body)], faq[(q,a)], related[(href,label)]
ARTICLES = [
 {
  "slug": "xiezilou-bangongshi-qubie",
  "title": "写字楼出租和办公室出租的区别（怎么选不踩坑）",
  "desc": "写字楼出租和办公室出租到底有没有区别？本文从词义、搜索意图、适用企业、预算区域四个维度讲清二者的关系，并给出按企业类型与预算快速选房的方法，附北郊未来产业园等高性价比案例。",
  "keywords": "写字楼出租,办公室出租,写字楼和办公室区别,办公室租赁,办公选址,小面积办公室,写字楼怎么选",
  "tag": "概念辨析", "color": "blue",
  "intro": "很多人在搜「写字楼出租」和「办公室出租」时，以为是两个不同的东西。其实两者本质指向同一件事——办公空间的租赁。本文把这两个词的关系、使用场景和选型方法一次讲清，帮你少走弯路、快速锁定合适的办公空间。",
  "sections": [
    ("一、两个词到底有没有区别",
     "严格说，「写字楼出租」和「办公室出租」没有物理上的区别，都指把办公用房租给企业使用。差异主要在语感与习惯：「写字楼」更书面、更正式，常用来描述整栋标准办公楼或甲级写字楼的租赁；「办公室」更口语化，侧重「具体的办公空间」，小到一间工作室、大到一层总部都适用。\n\n在搜索引擎里，百度、搜狗、360 都把二者视为高度相关的近义词。你搜「写字楼出租」和「办公室出租」，返回的结果高度重叠。所以对企业来说，二者不是二选一，而是同一需求的两面。"),
    ("二、为什么找房时要同时看这两个词",
     "虽然意思接近，但用户的搜索习惯不同：决策层、行政负责人更习惯搜「写字楼出租」；初创者、个体户更常搜「办公室出租」「小办公室出租」。如果只盯一个词，会漏掉另一批长尾结果（如「30平米办公室出租」「可注册办公室」）。\n\n本站的建议是：以「写字楼出租 + 城市/区域」为主词锁定板块，再用「办公室出租 + 面积/预算」细化户型。两个词组合使用，覆盖的房源和信息更全。"),
    ("三、按企业类型选：你该重点看哪个词",
     "初创团队 / 办事处：优先搜「办公室出租 + 面积」，如 30㎡、50㎡ 小面积办公室，关注精装修、拎包入驻、押一付一的灵活性。\n\n成长型企业：搜「写字楼出租 + 区域」，关注整层、得房率、会议室配置与扩租空间。\n\n总部 / 研发型：搜「产业园办公室出租」「写字楼出租 独栋」，关注冠名权、环评、平台资源。像宝山罗泾的北郊未来产业园，就是典型的「产业园办公室」供给，支持研发、中试与总部办公。\n\n纯贸易 / 轻资产：核心商圈小面积写字楼即可，重点看客户来访便利性。"),
    ("四、按预算选区域（2026 参考）",
     "核心商圈（陆家嘴、静安寺、淮海路）：甲级写字楼约 4.5–6 元/㎡/天，适合金融、专业服务、外资总部，看重客户信任感。\n\n副中心（市北高新、漕河泾、张江、前滩）：约 2.5–4 元/㎡/天，得房率高、配套成熟，是成长型企业主力区间。\n\n产业园区 / 远郊（宝山罗泾、松江 G60、嘉定）：约 1.5–2.5 元/㎡/天，空间大、停车免费、可环评，适合研发、制造服务、内部协作型团队。北郊未来产业园日租金约 2.0 元/㎡/天，比市区便宜一半以上。"),
    ("五、避坑：别被「低价办公室」误导",
     "低价「办公室出租」常藏在几个陷阱里：一是商住楼 / 住宅底商，消防不达标、营业执照办不下来；二是「虚拟注册」地址，客户来访不够正式、影响信任；三是报价低但物业费、空调延时费、公摊极高，实际全成本高。\n\n判断标准：看产权用途是否为商业办公（C 类），确认能否实地注册与消防验收，把租金 + 物业费 + 空调 + 停车一起算总账。"),
    ("六、怎么快速锁定合适房源",
     "三步走：先定预算（月租控制在营收的 8–15% 以内），再定区域（按客户来访频率与员工通勤），最后实地看 3–5 个并谈免租期。\n\n如果你要的是「总部形象 + 研发闭环 + 高性价比」，建议直接看北郊未来产业园这类国资科创总部园：28 栋独栋、41–7554㎡ 自由分割、可注册可环评、免费班车接驳地铁 7 号线，预约看房还能拿到可谈免租期的报价。"),
  ],
  "faq": [
    ("Q: 写字楼出租和办公室出租有区别吗？", "A: 本质没有区别，都是办公空间的租赁。「写字楼」更书面正式，「办公室」更口语化，搜索引擎视为近义词，找房时两个词都要看。"),
    ("Q: 小团队应该搜哪个词？", "A: 建议搜「办公室出租 + 面积」，如 30㎡、50㎡ 小面积办公室，重点看精装修、灵活性和付款方式。"),
    ("Q: 北郊未来产业园属于哪一类？", "A: 属于产业园办公室 / 写字楼出租，日租金约 2.0 元/㎡/天，支持研发中试、实地注册与环评，适合总部与科创企业。"),
    ("Q: 怎么避免低价办公室的坑？", "A: 确认产权用途为商业办公、可实地注册与消防验收，把租金、物业费、空调、停车一并核算，不要只看单价。"),
  ],
  "related": [
    ("/articles/baoshan-luojing-xiezilou-chuzu.html", "宝山罗泾写字楼出租"),
    ("/articles/shanghai-office-rent-guide.html", "上海写字楼出租全解析"),
    ("/articles/baoshan-office-rent-guide.html", "宝山写字楼租金一览"),
    ("/articles/xiaomianji-bangongshi.html", "小面积办公室出租"),
    ("/articles/sme-office-rent-guide.html", "中小企业选址避坑"),
    ("/articles/startup-office-rent.html", "初创企业办公室出租"),
  ],
 },
 {
  "slug": "jiaji-xiezilou",
  "title": "甲级写字楼出租怎么选（甲级/乙级/丙级分级指南）",
  "desc": "甲级、乙级、丙级写字楼到底差在哪？本文讲清分级标准、租金区间、各等级适合的企业，以及选甲级的隐性成本与高性价比替代方案，帮你在写字楼出租时把钱花在刀刃上。",
  "keywords": "甲级写字楼出租,乙级写字楼,丙级写字楼,写字楼等级,写字楼分级,陆家嘴写字楼,写字楼租金",
  "tag": "等级指南", "color": "indigo",
  "intro": "搜「写字楼出租」时，你一定见过「甲级」「乙级」「丙级」这些标签。它们不是营销话术，而是对楼宇硬件、区位、物业与智能化的分级。本文把分级标准、租金差异和选型逻辑一次讲清，帮你判断到底要不要为「甲级」买单。",
  "sections": [
    ("一、什么是甲级写字楼",
     "甲级写字楼通常指区位核心、硬件顶配、物业专业的办公楼宇。典型标准包括：地处核心商务区（如陆家嘴、南京西路）、挑高大堂与高品质公区、电梯配比充足（等待时间短）、层高与采光优秀、配备智能楼宇系统与专业物业管理。\n\n上海代表项目有陆家嘴的国金中心、上海中心，南京西路的嘉里中心等。甲级楼的优势是地标效应与客户信任感，劣势是租金与隐性成本都高。"),
    ("二、乙级、丙级怎么区分",
     "乙级写字楼硬件与区位次于甲级，但仍属正规办公楼宇，常见于副中心（市北高新、漕河泾、张江）和部分核心区老牌项目，性价比更高。丙级多为老旧办公楼或改造物业，装修与设备一般，适合预算敏感、对形象要求不高的团队。\n\n简单判断：看租金、看大堂与电梯、看物业品牌。甲级靠「牌子」，乙级靠「实用」，丙级靠「便宜」。"),
    ("三、各等级租金区间（2026 参考）",
     "核心区甲级：约 4.5–6 元/㎡/天（陆家嘴、静安寺、淮海路）。\n\n副中心甲级 / 优质乙级：约 2.5–4 元/㎡/天（市北、漕河泾、张江、前滩）。\n\n普通乙级：约 2–3 元/㎡/天。\n\n丙级 / 产业园区：约 1.5–2.5 元/㎡/天（嘉定、松江、宝山罗泾等）。\n\n注意：租金只是显性成本，下面的隐性成本往往更关键。"),
    ("四、不同等级适合什么企业",
     "金融、律所、咨询、外资总部：客户来访频繁、重品牌形象，优先甲级。\n\n成长型科技 / 贸易公司：重性价比与配套，副中心乙级 / 甲级最合适。\n\n研发、智能制造、生物医药总部：需要环评、荷载与冠名权，产业园办公室（如北郊未来产业园）比传统甲级更适配。\n\n项目制 / 临时团队：乙级小面积或联合办公即可。"),
    ("五、选甲级的隐性成本",
     "甲级的坑不在租金单价，而在附加项：物业费通常 20–40 元/㎡/月；空调延时费（晚 8 点后加收，约 5–10 元/㎡/小时）；车位 1500–2000 元/月/位；大堂 LOGO 展示费约 1–3 万/年。\n\n1000㎡ 甲级月租可能 40–60 万，加上隐性成本，年支出轻松破千万。签合同时务必把这些写入费用明细。"),
    ("六、性价比之选：副中心与产业园",
     "多数企业不需要为「甲级」的光环多花一倍租金。副中心的优质乙级 / 甲级，得房率更高（70–75% vs 甲级 60–65%），配套也不差。\n\n如果团队更看重空间、停车、环评与政策，产业园是更优解。北郊未来产业园日租金约 2.0 元/㎡/天，28 栋花园式独栋、可注册可环评、免费班车接驳地铁 7 号线，是「甲级体验、产业园价格」的代表。"),
  ],
  "faq": [
    ("Q: 甲级和乙级写字楼主要差在哪？", "A: 差在区位、硬件（大堂/电梯/层高）、物业与智能化。甲级重品牌与体验，乙级重实用与性价比。"),
    ("Q: 甲级写字楼的隐性成本有哪些？", "A: 物业费、空调延时费、车位费、大堂 LOGO 费是高发项，签合同前要全部写入费用明细。"),
    ("Q: 什么样的企业适合产业园而不是甲级？", "A: 研发、智能制造、生物医药等需要环评、荷载、冠名权与低成本空间的企业，产业园比甲级更适配。"),
    ("Q: 上海各等级租金大概多少？", "A: 核心甲级 4.5–6 元/㎡/天，副中心 2.5–4，乙级 2–3，产业园 1.5–2.5 元/㎡/天（2026 参考）。"),
  ],
  "related": [
    ("/articles/baoshan-luojing-xiezilou-chuzu.html", "北郊产业园写字楼出租"),
    ("/articles/jingan-office-rent-guide.html", "静安写字楼选址攻略"),
    ("/articles/pudong-office-rent-guide.html", "浦东写字楼租金行情"),
    ("/articles/huangpu-office-rent-guide.html", "黄浦写字楼租赁攻略"),
    ("/articles/baoshan-office-rent-guide.html", "宝山写字楼租金一览"),
    ("/articles/north-shanghai-office-rent.html", "北上海写字楼性价比"),
  ],
 },
 {
  "slug": "xiezilou-zhongjie-zhijie",
  "title": "写字楼出租中介 vs 直租（找房渠道怎么选不踩坑）",
  "desc": "找写字楼出租有哪些渠道？本文对比中介、园区直租、线上平台和招商中心的利弊，讲清佣金、信息真实性与议价空间，并给出防坑清单与高性价比直租入口。",
  "keywords": "写字楼出租中介,写字楼直租,写字楼出租平台,写字楼招商,写字楼出租渠道,园区直租,找办公室",
  "tag": "渠道指南", "color": "orange",
  "intro": "搜到心仪的「写字楼出租」房源后，下一步是找渠道。中介、园区直租、安居客 / 58 / 优楼网这类平台、政府招商中心，各有优劣。本文帮你理清每种渠道的佣金、信息真实性与议价空间，避免被虚假房源和隐藏费用坑了。",
  "sections": [
    ("一、主流找房渠道盘点",
     "中介 / 经纪：掌握大量房源，能带看、谈价、办手续，但成交通常收佣金（1 个月左右租金，双方分担）。\n\n开发商 / 园区直租：园区招商中心直接放租，无佣金，还能给免租期与政策。\n\n线上平台：安居客、58 同城、优楼网等，信息量大但鱼龙混杂，低价多为引流。\n\n政府 / 产业招商：各区招商部门、园区官网，适合拿政策与补贴的企业。"),
    ("二、中介 vs 直租 利弊对比",
     "中介优势：房源多、省时间、能横向比价、谈判专业。劣势：佣金成本、部分房源重复挂、存在「赚差价」风险。\n\n直租优势：零佣金、价格透明、免租期与装修期可谈、能直接对接园区政策。劣势：房源分散、需要自己跑、信息不对称。\n\n结论：大面积 / 总部选址建议「中介 + 直租」并行；中小面积优先直租或园区招商，省下的佣金就是利润。"),
    ("三、线上平台怎么用不踩坑",
     "平台上的「超低价办公室」八成是引流：要么是过期房源，要么是「先低价约你看，再看贵的」。识别方法：要求发实景视频与门牌、核实产权用途、确认是否含物业费与空调。\n\n建议把平台当「线索库」，落地一定以园区官网、招商电话或实地为准。像北郊未来产业园这类园区，直接在招商中心拿报价最稳妥。"),
    ("四、园区招商中心直租的优势",
     "以国资背景的北郊未来产业园为例，直租有三大好处：一是零佣金，价格直接对接招商中心；二是可谈免租期、装修期与车位优惠；三是能同步申请大张江、宝山「北转型」等政策线索。\n\n园区还为 C65 科研用地，支持工商注册与实地注册、可环评，对研发与科创企业尤其友好。"),
    ("五、谈判与防坑清单",
     "1. 核实产权：确认业主是否为产权人，房产有无抵押 / 查封。\n\n2. 费用明细：要求书面列清租金、物业费、空调、停车、网络，拒绝「包干含含糊糊」。\n\n3. 免租期：弱市窗口期常可谈 1–3 个月，用于装修搬迁。\n\n4. 递增与续租：明确年递增比例与续租租金机制。\n\n5. 合同审核：由法务 / 财务把关违约责任与退出条款。"),
    ("六、推荐：高性价比直租入口",
     "如果你要的是低成本、高配套、可注册的办公空间，直接走园区招商中心最划算。北郊未来产业园提供 41–7554㎡ 自由分割、日租金约 2.0 元/㎡/天、免费班车接驳地铁 7 号线，预约看房即可拿到最新可租楼栋清单与可谈免租期方案。"),
  ],
  "faq": [
    ("Q: 写字楼出租中介一般收多少佣金？", "A: 通常约 1 个月租金，由甲乙双方分担；大面积可谈。园区直租多为零佣金。"),
    ("Q: 线上平台的低价房源可信吗？", "A: 多数低价是引流，需核实实景、产权用途与费用明细，落地以园区官方为准。"),
    ("Q: 园区直租有什么好处？", "A: 零佣金、价格透明、免租期与政策可谈，还能直接对接园区招商与补贴。"),
    ("Q: 签约前必须核查哪些？", "A: 产权真实性、费用明细、免租期、租金递增与续租机制、合同违约与退出条款。"),
  ],
  "related": [
    ("/articles/baoshan-luojing-xiezilou-chuzu.html", "北郊产业园直租指南"),
    ("/articles/shanghai-office-rent-guide.html", "上海写字楼出租全解析"),
    ("/articles/baoshan-office-rent-guide.html", "宝山写字楼租金一览"),
    ("/articles/rental-contract-guide.html", "写字楼租赁合同模板"),
    ("/articles/sme-office-rent-guide.html", "中小企业选址避坑"),
    ("/articles/kezhuce-xiezilou.html", "上海可注册写字楼"),
  ],
 },
 {
  "slug": "lianhe-gongzuoshi",
  "title": "联合办公 / 共享办公出租（vs 传统写字楼怎么选）",
  "desc": "联合办公、共享办公出租适合谁？本文对比联合办公与传统写字楼的灵活性、成本、隐私与配套，讲清计价方式、适用人群与「何时该转传统写字楼」，并给出上海分布参考。",
  "keywords": "联合办公出租,共享办公,写字楼出租,共享办公室,WeWork,初创办公室,灵活办公,写字楼vs联合办公",
  "tag": "办公形态", "color": "teal",
  "intro": "「联合办公出租」「共享办公」是近几年最火的办公形态之一，也是「办公室出租」搜索里高频出现的词。它和传统写字楼到底差在哪？适合谁、不适合谁、怎么计价？本文一次讲清，并告诉你什么阶段该转回传统写字楼。",
  "sections": [
    ("一、什么是联合办公",
     "联合办公（共享办公）把一大片空间拆成开放工位、独立办公室和共享会议室，按需租用。代表品牌有 WeWork、雷格斯、办伴等，也有大量本土孵化器与创意园区。\n\n它的核心卖点是「灵活」：按月签、随时扩缩、含前台 / 网络 / 会议室 / 咖啡，适合早期团队与项目制工作。"),
    ("二、联合办公 vs 传统写字楼 全面对比",
     "灵活性：联合办公按月、按工位，扩缩自由；传统写字楼通常 1 年起、整间租。\n\n成本：联合办公表面单价高但零装修零押金压力；传统写字楼前期投入大但长期单价低。\n\n品牌与隐私：传统写字楼独立、正式、可挂铭牌；联合办公社群强但客户来访不够正式、易串岗。\n\n配套：联合办公含会议、打印、活动；传统写字楼需自建或共用物业配套。"),
    ("三、怎么计价",
     "开放工位：约 1500–3000 元/工位/月，含水电、网络、公共会议室额度。\n\n独立办公室：按间计，1–10 人间的月租约 5000–30000 元不等，看区位与装修。\n\n隐性项：部分按使用时长收会议室超时费、打印费、门禁卡费。签前问清「全包」边界。"),
    ("四、适合谁 / 不适合谁",
     "适合：1–15 人初创、项目制团队、自由职业者、外地办事处、需要社群的活动型公司。\n\n不适合：需要保密（财务、法务、研发样品）、需要强品牌形象与独立冠名、团队超过 15–20 人且稳定、需要环评或实地注册的企业。\n\n判断一句话：客户是企业（B2B）且要正式感 → 选传统写字楼；客户在线或纯内部 → 联合办公即可。"),
    ("五、上海联合办公分布",
     "静安、黄浦老法租界创意氛围浓；长宁、徐汇生活气息重；杨浦五角场年轻创意人聚集；浦东张江、前滩面向科技与外资。\n\n租金随区位浮动，核心区工位可达 2500–3500 元/月，副中心 1500–2200 元/月。"),
    ("六、什么阶段该转传统写字楼",
     "当团队稳定超过 15–20 人、需要独立空间与品牌门脸、或需要实地注册地址与环评时，就该转传统写字楼 / 产业园了。\n\n这类企业常选副中心或产业园以控成本。北郊未来产业园日租金约 2.0 元/㎡/天，41–7554㎡ 自由分割、可注册可环评、免费班车接驳地铁 7 号线，是从联合办公「毕业」到独立总部的热门落点。"),
  ],
  "faq": [
    ("Q: 联合办公和传统写字楼主要差在哪？", "A: 差在灵活性、成本结构与品牌形象。联合办公按月按工位、含配套但不够正式；传统写字楼稳定、独立、可挂铭牌但投入大。"),
    ("Q: 联合办公一般怎么计价？", "A: 开放工位约 1500–3000 元/工位/月，独立办公室按间 5000–30000 元/月，签前问清是否全包。"),
    ("Q: 什么企业不适合联合办公？", "A: 需要保密、强品牌形象、实地注册与环评，或团队稳定超过 15–20 人的企业。"),
    ("Q: 团队壮大后转哪里合适？", "A: 转向副中心或产业园控成本，如北郊未来产业园，可注册可环评、性价比高。"),
  ],
  "related": [
    ("/articles/baoshan-luojing-xiezilou-chuzu.html", "北郊产业园办公室出租"),
    ("/articles/startup-office-rent.html", "初创企业办公室出租"),
    ("/articles/freelancer-office-rent.html", "自由职业者办公室出租"),
    ("/articles/small-business-office-rent.html", "小微企业办公室出租"),
    ("/articles/xiaomianji-bangongshi.html", "小面积办公室出租"),
    ("/articles/shanghai-office-rent-guide.html", "上海写字楼出租全解析"),
  ],
 },
]

# ---------------------------------------------------------------- 模板
HEAD_TMPL = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>__TITLE__</title>
  <meta name="description" content="__DESC__">
  <meta name="keywords" content="__KW__">
  <link rel="canonical" href="__URL__">
  
  <!-- Open Graph -->
  <meta property="og:title" content="__TITLE__">
  <meta property="og:description" content="__DESC__">
  <meta property="og:type" content="article">
  <meta property="og:url" content="__URL__">
  <meta property="og:site_name" content="xn--g7q0iw0x3volkt.cn">
  <meta property="og:locale" content="zh_CN">
  
  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="__TITLE__">
  <meta name="twitter:description" content="__DESC__">
  
  <!-- JSON-LD Schema -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "__TITLE__",
    "description": "__DESC__",
    "keywords": "__KW__",
    "url": "__URL__",
    "datePublished": "__DATE__",
    "dateModified": "__DATE__",
    "author": {
      "@type": "Organization",
      "name": "写字楼出租.cn 招商研究组",
      "url": "https://xn--g7q0iw0x3volkt.cn"
    },
    "publisher": {
      "@type": "Organization",
      "name": "写字楼出租.cn",
      "logo": {
        "@type": "ImageObject",
        "url": "https://xn--g7q0iw0x3volkt.cn/logo.png"
      }
    }
  }
  </script>
  
  <script src="https://cdn.tailwindcss.com"></script>
  <style>
    html { scroll-behavior: smooth; }
    a { color: #1e3a5f; }
    a:hover { color: #e8742a; }
  </style>
<meta property="og:image" content="https://xn--g7q0iw0x3volkt.cn/assets/og-cover.png" />
<meta property="og:image:width" content="1200" />
<meta property="og:image:height" content="630" />
<meta property="og:image:type" content="image/png" />
<meta name="twitter:image" content="https://xn--g7q0iw0x3volkt.cn/assets/og-cover.png" />
</head>
<body class="bg-gray-50 text-gray-800 font-sans">

  <header class="bg-white shadow-sm sticky top-0 z-50">
    <div class="max-w-6xl mx-auto px-4 py-3 flex items-center justify-between">
      <a href="/" class="text-xl font-bold text-blue-900">写字楼出租<span class="text-orange-500">.cn</span></a>
      <nav class="hidden md:flex gap-6 text-sm">
        <a href="/" class="hover:text-orange-500">首页</a>
        <a href="/articles/" class="text-orange-500 font-medium">行业资讯</a>
        <a href="/#about" class="hover:text-orange-500">关于我们</a>
        <a href="/#contact" class="hover:text-orange-500">联系我们</a>
      </nav>
      <a href="tel:17652523536" class="bg-orange-500 text-white px-4 py-2 rounded-lg text-sm font-medium hover:bg-orange-600">📞 电话咨询</a>
    </div>
  </header>

  <div class="bg-white border-b">
    <div class="max-w-4xl mx-auto px-4 py-3 text-sm text-gray-500">
      <a href="/" class="hover:text-orange-500">首页</a> >
      <a href="/articles/" class="hover:text-orange-500">行业资讯</a> >
      <span class="text-gray-700">__BREAD__</span>
    </div>
  </div>

  <article class="max-w-4xl mx-auto px-4 py-8">
    <header class="mb-8">
      <div class="flex items-center gap-3 text-sm text-gray-400 mb-4">
        <span class="bg-__COLOR__-100 text-__COLOR__-700 px-3 py-1 rounded-full text-xs font-medium">__TAG__</span>
        <span>__DATE__</span>
        <span>·</span>
        <span>8 分钟阅读</span>
      </div>
      <h1 class="text-3xl md:text-4xl font-bold text-gray-900 leading-tight mb-4">__TITLE__</h1>
      <p class="text-gray-500 text-lg">__DESC__</p>
    </header>

    <div class="prose max-w-none">
        <div class="bg-__COLOR__-50 border-l-4 border-__COLOR__-500 p-4 mb-8 rounded">
          <p class="text-__COLOR__-900 font-medium">本文导览</p>
          <p class="text-sm text-__COLOR__-800 mt-1">__INTRO__</p>
        </div>

        <p class="mb-4 text-gray-700 leading-relaxed">__INTRO__</p>
__BODY__
        <h2 class="text-2xl font-bold mt-8 mb-4 text-gray-900">常见问题</h2>
        <div class="space-y-4 mb-8">
__FAQ__
        </div>
    <div class="mt-12 pt-8 border-t">
      <h2 class="text-xl font-bold mb-4">相关文章</h2>
__RELATED__
        <div class="mt-12 bg-blue-900 text-white rounded-xl p-8 text-center">
      <h2 class="text-2xl font-bold mb-3">需要帮助选址？</h2>
      <p class="text-blue-200 mb-6">专业顾问1对1服务，为您匹配最适合的办公空间</p>
      <div class="flex flex-col sm:flex-row gap-4 justify-center">
        <a href="tel:17652523536" class="bg-orange-500 text-white px-6 py-3 rounded-lg font-medium hover:bg-orange-600">📞 电话咨询</a>
        <a href="https://wa.me/8617652523536" target="_blank" class="bg-green-500 text-white px-6 py-3 rounded-lg font-medium hover:bg-green-600">💬 微信咨询</a>
      </div>
      <p class="text-blue-300 text-sm mt-4">微信号：mfujun（备注「写字楼」）</p>
    </div>

  </article>

  <footer class="bg-blue-950 text-blue-400 text-sm py-8 mt-12">
    <div class="max-w-6xl mx-auto px-4 text-center">
      <p>© 2026 xn--g7q0iw0x3volkt.cn · 上海写字楼信息网</p>
      <p class="mt-2 text-blue-500">
        <a href="/" class="hover:text-white">首页</a> ·
        <a href="/articles/" class="hover:text-white">行业资讯</a> ·
        <a href="/#contact" class="hover:text-white">联系我们</a>
      </p>
    </div>
  </footer>

</body>
</html>"""

def build_body(sections):
    html = ""
    for title, content in sections:
        html += f'<h2 class="text-2xl font-bold mt-8 mb-4 text-gray-900">{title}</h2>\n'
        for para in content.strip().split("\n"):
            para = para.strip()
            if para:
                html += f'<p class="mb-4 text-gray-700 leading-relaxed">{para}</p>\n'
    return html

def build_faq(faq):
    html = ""
    for q, a in faq:
        html += f'          <div class="bg-gray-50 rounded-lg p-4">\n            <h3 class="font-semibold text-gray-900 mb-2">{q}</h3>\n            <p class="text-gray-700 text-sm">A: {a}</p>\n          </div>\n'
    return html

def build_related(related):
    html = ""
    # 3 行，每行 2 个
    for i in range(0, len(related), 2):
        pair = related[i:i+2]
        html += '        <div class="grid md:grid-cols-2 gap-4">\n'
        for href, label in pair:
            html += f'          <a href="{href}" class="bg-white rounded-lg p-4 shadow-sm hover:shadow-md transition block">\n            <span class="text-xs text-blue-600 font-medium">相关资讯</span>\n            <h3 class="font-semibold mt-1">{label}</h3>\n          </a>\n'
        html += '        </div>\n'
    return html

def build_html(a):
    bread = a["title"].split("（")[0].split("|")[0].strip()
    body = build_body(a["sections"])
    faq = build_faq(a["faq"])
    related = build_related(a["related"])
    url = f"{DOMAIN}/articles/{a['slug']}.html"
    h = (HEAD_TMPL
         .replace("__TITLE__", a["title"])
         .replace("__DESC__", a["desc"])
         .replace("__KW__", a["keywords"])
         .replace("__URL__", url)
         .replace("__DATE__", DATE)
         .replace("__TAG__", a["tag"])
         .replace("__COLOR__", a["color"])
         .replace("__BREAD__", bread)
         .replace("__INTRO__", a["intro"])
         .replace("__BODY__", body)
         .replace("__FAQ__", faq)
         .replace("__RELATED__", related))
    return h

# ---------------------------------------------------------------- 生成文章
for a in ARTICLES:
    html = build_html(a)
    out = os.path.join(BLOG, f"{a['slug']}.html")
    with open(out, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"WROTE article: {a['slug']}.html ({len(html)} bytes)")

# ---------------------------------------------------------------- sitemap
with open(SITEMAP, "r", encoding="utf-8") as f:
    sm = f.read()
new_urls = ""
for a in ARTICLES:
    url = f"{DOMAIN}/articles/{a['slug']}.html"
    new_urls += (
        f"    <url>\n"
        f"      <loc>{url}</loc>\n"
        f"      <lastmod>{DATE}</lastmod>\n"
        f"      <changefreq>weekly</changefreq>\n"
        f"      <priority>0.7</priority>\n"
        f"    </url>\n"
    )
if "</urlset>" in sm:
    sm = sm.replace("</urlset>", new_urls + "  </urlset>")
    with open(SITEMAP, "w", encoding="utf-8") as f:
        f.write(sm)
    print(f"UPDATED sitemap.xml (+{len(ARTICLES)} urls)")
else:
    print("WARN: </urlset> not found in sitemap.xml")

# ---------------------------------------------------------------- 文章索引
def home_card(a):
    return (
        f'        <a href="/articles/{a["slug"]}.html" class="card bg-white rounded-lg overflow-hidden shadow-sm">\n'
        f'          <div class="p-6">\n'
        f'            <span class="text-xs text-{a["color"]}-600 font-medium">{a["tag"]}</span>\n'
        f'            <h3 class="font-bold text-lg mt-2 mb-3">{a["title"].split("（")[0].split("|")[0].strip()}</h3>\n'
        f'            <p class="text-gray-500 text-sm mb-4">{a["desc"][:40]}...</p>\n'
        f'            <div class="text-xs text-gray-400">2026-10-13 · 8分钟阅读</div>\n'
        f'          </div>\n'
        f'        </a>\n'
    )

# articles/index.html: 插在「宝山写字楼租金对比」卡片前
with open(ART_INDEX, "r", encoding="utf-8") as f:
    ai = f.read()
marker_ai = '      <!-- 文章：宝山写字楼租金对比 -->'
if marker_ai in ai:
    cards = "".join(home_card(a) for a in ARTICLES)
    ai = ai.replace(marker_ai, cards + marker_ai, 1)
    with open(ART_INDEX, "w", encoding="utf-8") as f:
        f.write(ai)
    print(f"UPDATED articles/index.html (+{len(ARTICLES)} cards)")
else:
    print("WARN: articles/index.html marker not found")

# 首页 最新资讯 网格: 插在「查看全部文章」按钮前
with open(HOME, "r", encoding="utf-8") as f:
    hm = f.read()
marker_home = '      <div class="text-center mt-8">\n        <a href="/articles/"'
if marker_home in hm:
    cards = "".join(home_card(a) for a in ARTICLES)
    hm = hm.replace(marker_home, cards + '      <div class="text-center mt-8">\n        <a href="/articles/"', 1)
    with open(HOME, "w", encoding="utf-8") as f:
        f.write(hm)
    print(f"UPDATED index.html homepage (+{len(ARTICLES)} cards)")
else:
    print("WARN: homepage marker not found")

print("\nAll done.")
