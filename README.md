# 百合音声分享站

这是一个基于 Hugo 和 PaperMod 主题构建的中文静态站点，用于整理和展示百合音声资源。

站点包含资源目录、全文搜索、标签筛选、社团筛选、年龄分级以及单个资源的详细信息页面。

> 本项目仅用于个人资料整理和学习交流。请遵守所在地法律法规、平台规则以及原作者和版权所有者的要求。未经授权，请勿传播受版权保护的内容。

## 功能

- 首页双列资源卡片布局，移动端自动切换为单列
- 按 RJ 号、标题、社团和标签搜索
- 按年龄分级、社团和作品标签筛选
- 资源总目录表格
- 资源详情页展示封面、社团、分级、标签、简介和相关链接
- 使用 Hugo 生成静态页面
- 可部署到 Cloudflare Pages 或其他静态托管服务

## 技术栈

- Hugo 0.128.0
- PaperMod
- HTML / CSS
- Python 3
- CSV

## 目录结构

```text
.
├── assets/css/extended/   # 自定义样式
├── content/
│   ├── posts/             # 资源文章
│   ├── catalog.md         # 资源总目录
│   ├── filter.md          # 分类筛选页
│   └── search.md          # 搜索页
├── layouts/
│   ├── _default/index.json
│   └── shortcodes/        # 资源卡片、目录和筛选组件
├── public/                # 静态资源
├── static/images/         # 封面图片
├── themes/PaperMod/       # PaperMod 主题
├── data.csv               # 资源数据源
├── generate_posts.py      # 根据 CSV 生成文章
├── import_notion.py       # 导入 Notion 导出的 CSV
├── rjnum.py               # 为文章补充数字化 RJ 编号
├── hugo.toml              # Hugo 配置
└── deploy.bat             # Windows 部署脚本
```

## 本地运行

请先安装 Hugo Extended 和 Python 3。

### 预览站点

```bash
hugo server
```

启动后访问 Hugo 输出的本地地址，通常是：

```text
http://localhost:1313/
```

### 构建站点

```bash
hugo --minify
```

生成的静态文件默认位于 `public/` 目录。

## 更新资源

资源数据主要维护在 `data.csv` 中。修改 CSV 后，可以运行：

```bash
python generate_posts.py
```

脚本会根据 CSV 内容生成 `content/posts/` 下的 Markdown 文章。

如果数据来自 Notion 导出文件，可以使用：

```bash
python import_notion.py
```

文章使用 Hugo Front Matter 保存结构化信息，例如：

```yaml
---
title: "资源标题"
rj_id: "RJ00000000"
circle: "社团名称"
rating: "绿"
tags: ["ASMR", "汉化"]
cover:
  image: "/images/cover.jpg"
download_link: "https://example.com"
extract_code: "example"
---
```

修改或新增文章后，建议先运行本地预览，检查标题、封面、链接和筛选分类是否正常。

## 部署

项目配置的站点地址为：

[my-blog-535.pages.dev](https://my-blog-535.pages.dev)

Windows 用户可以使用：

```bat
deploy.bat
```

该脚本会依次执行 Git 提交和推送。提交前请确认：

- 没有把密码、令牌或其他私人信息加入仓库
- 数据中的链接可以公开使用
- 图片和文章内容拥有合适的授权
- 生成的文章和封面显示正常

也可以在 Cloudflare Pages 中连接 GitHub 仓库，使用 Hugo 构建。构建命令可设置为：

```bash
hugo --minify
```

输出目录：

```text
public
```

## 数据与隐私

`data.csv` 可能包含外部链接、访问口令或其他资源信息。发布仓库前请确认这些信息适合公开，并避免提交个人账号凭据、API 密钥和未授权的私人数据。

## 许可

当前仓库未单独声明开源许可证。除仓库作者明确授权的代码外，站点中的文章、图片、音频、封面和第三方资源仍可能受到版权或其他权利保护。

如需公开分发或二次使用，请先取得相应授权。
