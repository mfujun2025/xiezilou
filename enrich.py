import os, re

base = r"D:/louyuzuchang-fix/articles"

def build_article(tag, tag_color, title, intro, sections):
    """构建一篇充实的文章HTML"""
    # 生成正文内容
    sec_html = ""
    for sec_title, sec_content in sections:
        sec_html += f'<h2 class="text-2xl font-bold mt-8 mb-4">{sec_title}</h2>\n'
        # 按行分割内容，每段包裹在<p>中
        for line in sec_content.strip().split('\n'):
            line = line.strip()
            if line:
                sec_html += f'<p class="mb-4 text-gray-700 leading-relaxed">{line}</p>\n'
    
    # FAQ部分
    faq_html = """
      <h2 class="text-2xl font-bold mt-8 mb-4">常见问题解答</h2>
      <div class="space-y-4">
        <div class="bg-white rounded-lg p-4 shadow-sm">
          <h3 class="font-semibold text-gray-900 mb-2">上海写字楼租金一般多少？</h3>
          <p class="text-gray-600 text-sm">租金因区域、档次、配套等因素差异较大。北郊片区（宝山、嘉定、杨浦）日均2.5-4.5元/㎡，市中心区域在8-15元/㎡。</p>
        </div>
        <div class="bg-white rounded-lg p-4 shadow-sm">
          <h3 class="font-semibold text-gray-900 mb-2">如何选择合适的办公空间？</h3>
          <p class="text-gray-600 text-sm">建议从交通便利性、租金成本、产业配套、企业形象等多个维度综合评估，优先选择有扩展空间的园区。</p>
        </div>
        <div class="bg-white rounded-lg p-4 shadow-sm">
          <h3 class="font-semibold text-gray-900 mb-2">有哪些隐性成本需要注意？</h3>
          <p class="text-gray-600 text-sm">物业管理费、空调费、停车费、水电费、网络费等都可能另计，签约前务必确认全包价格。</p>
        </div>
      </div>
"""
    
    # 相关文章部分
    related_html = """
    <div class="mt-12 pt-8 border-t">
      <h2 class="text-xl font-bold mb-4">相关文章</h2>
      <div class="grid md:grid-cols-2 gap-4">
        <a href="/articles/baoshan-office-rent-guide.html" class="bg-white rounded-lg p-4 shadow-sm hover:shadow-md transition block">
          <span class="text-xs text-blue-600 font-medium">相关资讯</span>
          <h3 class="font-semibold mt-1">宝山写字楼出租价格一览</h3>
        </a>
        <a href="/articles/jiading-office-rent-guide.html" class="bg-white rounded-lg p-4 shadow-sm hover:shadow-md transition block">
          <span class="text-xs text-blue-600 font-medium">相关资讯</span>
          <h3 class="font-semibold mt-1">嘉定区写字楼入驻流程</h3>
        </a>
        <a href="/articles/pudong-office-rent-guide.html" class="bg-white rounded-lg p-4 shadow-sm hover:shadow-md transition block">
          <span class="text-xs text-blue-600 font-medium">相关资讯</span>
          <h3 class="font-semibold mt-1">浦东新区写字楼选址攻略</h3>
        </a>
        <a href="/articles/minhang-office-rent-guide.html" class="bg-white rounded-lg p-4 shadow-sm hover:shadow-md transition block">
          <span class="text-xs text-blue-600 font-medium">相关资讯</span>
          <h3 class="font-semibold mt-1">闵行区写字楼租金行情</h3>
        </a>
        <a href="/articles/yangpu-office-rent-guide.html" class="bg-white rounded-lg p-4 shadow-sm hover:shadow-md transition block">
          <span class="text-xs text-blue-600 font-medium">相关资讯</span>
          <h3 class="font-semibold mt-1">杨浦滨江办公区行情</h3>
        </a>
        <a href="/articles/address-registration-guide.html" class="bg-white rounded-lg p-4 shadow-sm hover:shadow-md transition block">
          <span class="text-xs text-blue-600 font-medium">相关资讯</span>
          <h3 class="font-semibold mt-1">企业注册地址如何选择</h3>
        </a>
      </div>
"""
    
    # CTA部分
    cta_html = """
    <div class="mt-12 bg-blue-900 text-white rounded-xl p-8 text-center">
      <h2 class="text-2xl font-bold mb-3">需要帮助选址？</h2>
      <p class="text-blue-200 mb-6">专业顾问1对1服务，为您匹配最适合的办公空间</p>
      <div class="flex flex-col sm:flex-row gap-4 justify-center">
        <a href="tel:17652523536" class="bg-orange-500 text-white px-6 py-3 rounded-lg font-medium hover:bg-orange-600">📞 电话咨询</a>
        <a href="https://wa.me/8617652523536" target="_blank" class="bg-green-500 text-white px-6 py-3 rounded-lg font-medium hover:bg-green-600">💬 微信咨询</a>
      </div>
      <p class="text-blue-300 text-sm mt-4">微信号：mfujun（备注「写字楼」）</p>
    </div>
"""
    
    full_content = f"""
    <div class="prose max-w-none">
      <h2 class="text-2xl font-bold mt-8 mb-4">市场概况</h2>
      <p class="mb-4 text-gray-700 leading-relaxed">{intro}</p>
      {sec_html}
      {faq_html}
    </div>
    {related_html}
    {cta_html}
"""
    return full_content

# 文章数据定义
ARTICLES = {
    "shanghai-office-rent-guide.html": {
        "tag": "租金行情",
        "tag_color": "blue",
        "title": "上海写字楼出租信息网 - 全市租金行情与园区分布全景分析",
        "subtitle": "2026年上海写字楼租金全景解析：各区价格、隐性成本与省钱攻略",
        "intro": "在上海创业或扩张团队，办公楼选址是绕不开的一道题。很多人盯着表面租金看，最后算上物业、停车、转让费才发现总支出远远超出预算。这篇文章帮你把上海写字楼市场的底细摸清楚，按区域、按面积、按类型都给你盘明白了，附带真实案例和省钱技巧。",
        "sections": [
            ("一、上海写字楼租金整体格局", "上海写字楼市场呈现明显的圈层结构，内环以内以甲级写字楼为主，平均租金在每天8-15元/㎡；内中环之间是性价比最高的选择，大量新兴园区和更新改造的老楼混杂其中，价格区间每天3-8元/㎡；北郊片区（宝山、嘉定、杨浦）是整个上海租金洼地，平均每天2.5-4.5元/㎡，同等条件下比市中心便宜40%-60%。\n\n从空间分布来看，北郊片区承接了大量从市中心外溢的企业需求。宝山区有宝山软件园、智慧谷等成熟园区；嘉定区以汽车城周边产业园为代表，产业聚集效应明显；杨浦区则依托复旦、交大等高校资源，数字创意类企业扎堆。这些区域共同构成了上海北郊产业园区的核心带。"),
            ("二、各区域租金对比（2026年最新）", "不同区域租金差异显著，以下数据为市场参考价，实际价格随楼层、装修、配套等因素波动较大：\n\n黄浦区：甲级写字楼日均租金约10-16元/㎡，老牌商圈，配套最完善，但空置率偏低，适合对形象要求高的企业。\n静安区：日均租金8-14元/㎡，融合老上海风情与现代商务，适合品牌展示型企业和金融机构。\n长宁区：日均租金7-12元/㎡，生活气息浓厚，外资企业较多，交通便捷，适合服务业和外企办事处。\n徐汇区：日均租金8-13元/㎡，科技与文创产业聚集，漕河泾开发区是重要载体，政策扶持力度大。\n浦东新区：日均租金5-12元/㎡，张江高科、陆家嘴两大核心板块，税收优惠政策多，适合科技和金融行业。\n普陀区：日均租金4-7元/㎡，苏州河畔改造空间大，性价比突出，适合成长型中小企业。\n杨浦区：日均租金3-6元/㎡，凭借复旦交大等高校资源，创新创业氛围浓厚，适合科技和文创企业。\n虹口区：日均租金4-7元/㎡，北外滩开发带来新机会，传统商业底蕴深厚。\n宝山区：日均租金2.5-4.5元/㎡，上海北郊产业园带的核心区域，政策扶持力度大，是初创企业和成长型企业的优选。\n嘉定区：日均租金2.5-4.5元/㎡，汽车产业和先进制造业集群，园区配套成熟。\n闵行区：日均租金3-5.5元/㎡，虹桥商务区辐射效应强，交通枢纽优势明显。\n松江区：日均租金2.5-4元/㎡，松江新城和G60科创走廊带动发展。\n青浦区：日均租金2.5-4元/㎡，虹桥国际开放枢纽核心区，毗邻长三角。\n奉贤区：日均租金2-3.5元/㎡，南向拓展重点区域，土地资源丰富。\n金山区：日均租金1.8-3元/㎡，临港新片区联动发展，适合大型制造企业。\n崇明区：日均租金1.5-2.5元/㎡，生态岛定位，适合绿色产业和文旅项目。\n\n总结规律：越靠近市中心，租金越高；北郊片区（宝山、嘉定、杨浦）是3-5元/㎡区间的主力，性价比最优。"),
            ("三、租金之外的隐性成本清单", "很多老板只算了月租金，结果发现每季度账单远超预期。以下是容易被忽视的隐性成本，签约前务必确认：\n\n物业管理费：通常另计，日均0.8-3元/㎡，部分园区已包含在报价中，签约前务必确认是否"全包价"。\n空调费：办公时间空调通常含在物业费里，但部分写字楼分体空调单独计费，夏天高峰期每月可能多出数千元。\n停车位：地下车位月租300-800元不等，部分园区首月免费，后续按次收费，建议提前确认车位数量和价格。\n水电费：商业用电约1.2元/度，商业用水约8元/吨，远超民用标准，每月电费几千元很常见。\n网络费：部分写字楼指定运营商，月费500-2000元不等，也可自带宽带但需物业配合穿线。\n装修押金：退租时验收合格退还，一般1-2个月租金作为押金，部分园区还收取垃圾清运费。\n转让费：热门地段老楼转让，中介可能收取半月至一月租金作为服务费，避免通过中介可省这笔钱。\n\n建议把以上成本全部纳入总预算，用"总拥有成本"概念评估房源，避免签约后才发现超出承受能力。"),
            ("四、省钱实战策略", "基于服务上千家的经验，总结出以下几种切实可行的省钱方式，帮你的每一分钱都花在刀刃上：\n\n第一，选择免租期较长的房源。旺季时招商方愿意给出1-3个月免租期，相当于直接减免数月租金，这笔钱可以用来支付装修和搬家费用。签约时要把免租期明确写进合同。\n\n第二，选择毛坯或简装房自己装。房东提供精装房的租金单价通常高出20%-30%，如果团队有自己的装修需求，选毛坯房自己来更划算，也能按团队习惯设计工位布局。\n\n第三，关注园区政府补贴政策。宝山、嘉定等北郊园区对符合条件的企业给予租金补贴，最高可达实际租金的30%，持续2-3年，签约前务必向园区管委会咨询。\n\n第四，短租过渡。初创期团队不稳定，可以选择共享办公或短租公寓式办公室，等团队稳定后再搬入长期租赁的独立办公室，避免一次性投入过大。\n\n第五，错峰签约。年底是写字楼出租淡季，很多房东愿意在价格上做出让步，春节前后签约往往能拿到更好的条件，避开年初抢楼的涨价潮。"),
            ("五、如何判断一个写字楼是否值得租", "除了租金价格，以下五个维度也是关键考察点，建议实地走访时逐项打分：\n\n交通便利性：距离地铁站步行不超过800米，周边公交线路不少于3条，方便员工通勤。最好在不同时段实地考察，看早高峰拥堵情况。\n\n产业聚集度：周边是否有同类或上下游企业，产业氛围好的园区更容易获得政策支持和业务合作机会，形成良性循环。\n\n园区配套：食堂、便利店、快递柜、会议室等基础配套设施是否完善，能否满足日常办公需求，减少员工通勤外的奔波。\n\n企业形象：大堂气派程度、外墙整洁度、周边绿化环境，都会影响客户来访的第一印象，对B2B业务尤为关键。\n\n扩展空间：园区内是否有可扩租的空间，或者同园区其他楼栋可供调剂，避免未来搬迁的麻烦，节省搬家成本和客户信任成本。")
        ]
    }
}

print("Script ready. Now enriching articles...")
