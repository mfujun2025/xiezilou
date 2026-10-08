# 写字楼出租.cn

上海写字楼出租信息网，专注北上海产业园区资讯。

## 项目结构

```
xiezilou/
├── site/
│   ├── index.html              (首页)
│   ├── sitemap.xml             (站点地图)
│   ├── CNAME                   (自定义域名)
│   └── articles/
│       ├── index.html          (文章列表页)
│       └── *.html              (100篇SEO文章)
├── reports/
│   ├── articles-matrix-full.json  (文章矩阵JSON)
│   └── seo-article-matrix-100.md  (策略文档)
└── drafts/
    └── 北郊产业园-site-plan-v1.md
```

## 部署说明

### GitHub Pages
1. 推送代码到GitHub
2. 仓库设置 → Pages → Source: main branch, /site folder
3. 访问 https://mfujun2025.github.io/xiezilou/

### Cloudflare Pages（推荐）
1. 连接GitHub仓库 `mfujun2025/xiezilou`
2. Build settings: 留空，Output directory: `site`
3. 添加自定义域名 `写字楼出租.cn`

## 联系方式

- 电话：17652523536
- 地址：萧云路501弄55号
- 微信：mfujun（备注「写字楼」）
