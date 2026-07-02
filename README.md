# 阿城 · 项目档案（Portfolio）

> 一座托管在 GitHub Pages 上的个人项目作品集站点。每个项目拥有独立的详情页，访客可从首页一键跳转。风格大气、简约、高端、精致，内置白天 / 黑夜模式切换。

- **线上地址**：<https://morecorianders.github.io/portfolio/>
- **源码仓库**：<https://github.com/MORECORIANDERS/portfolio>
- **技术栈**：[Astro 5](https://astro.build/)（静态站点生成）+ 原生 CSS + TypeScript

---

## 目录

1. [快速开始](#快速开始)
2. [核心概念](#核心概念)
3. [目录结构](#目录结构)
4. [日常维护](#日常维护) ← 最高频操作都在这
   - [新增一个项目](#新增一个项目)
   - [编辑 / 删除项目](#编辑--删除项目)
   - [修改个人信息](#修改个人信息)
   - [替换项目封面](#替换项目封面)
5. [项目 Markdown 字段速查](#项目-markdown-字段速查)
6. [设计系统](#设计系统)
7. [昼夜模式机制](#昼夜模式机制)
8. [部署机制](#部署机制)
9. [本地预览（preview.html）](#本地预览previewhtml)
10. [常见问题 FAQ](#常见问题-faq)
11. [文件速查表](#文件速查表)

---

## 快速开始

需要本地已安装 **Node.js 20+**。

```bash
# 1. 安装依赖
npm install

# 2. 启动本地开发服务器（默认 http://localhost:4321/portfolio/）
npm run dev

# 3. 生产构建（输出到 dist/）
npm run build

# 4. 本地预览构建产物
npm run preview
```

> 本地开发地址带 `/portfolio/` 子路径，与线上保持一致（见 [astro.config.mjs](src/astro.config.mjs) 中的 `base`）。

---

## 核心概念

这个站点建立在一个简单想法上：**项目即一份 Markdown 文件**。

1. **Content Collection**：所有项目都是 [src/content/projects/](src/content/projects/) 目录下的 `.md` 文件，由 Astro 的 Content Collection 统一管理并做类型校验（schema 定义在 [src/content.config.ts](src/content.config.ts)）。
2. **动态路由**：每个 `.md` 文件自动生成一个详情页，路由为 `/projects/<文件名>/`，由 [src/pages/projects/[slug].astro](src/pages/projects/%5Bslug%5D.astro) 渲染。
3. **首页聚合**：[src/pages/index.astro](src/pages/index.astro) 读取全部项目，按 `order` 降序 → `pubDate` 降序排序，`featured: true` 的项目置顶且占满整行。
4. **零后端**：构建产物是纯静态 HTML，托管在 GitHub Pages，零运维成本。

**这意味着：新增一个项目，通常只需新建一个 `.md` 文件并推送，无需改动任何代码。**

---

## 目录结构

```
.
├── .github/workflows/deploy.yml   # GitHub Actions 自动部署工作流
├── public/
│   ├── favicon.svg                # 站点图标
│   └── projects/<slug>/cover.svg  # 每个项目的封面图（与项目同名文件夹）
├── src/
│   ├── components/
│   │   ├── Header.astro           # 顶栏（品牌 + 导航 + 主题切换）
│   │   ├── Footer.astro           # 页脚（联系邮箱 + 链接）
│   │   ├── ProjectCard.astro      # 首页项目卡片
│   │   └── ThemeToggle.astro      # 昼夜模式切换按钮 + 逻辑
│   ├── content/
│   │   └── projects/              # ★ 项目内容源（每个 .md 一个项目）
│   │       ├── cbreport-web.md
│   │       ├── eva-presentation.md
│   │       ├── aurora-dashboard.md
│   │       ├── tide-forecast-app.md
│   │       └── inkwell-cms.md
│   ├── content.config.ts          # ★ 项目字段 schema（类型校验）
│   ├── consts.ts                  # ★ 站点全局信息（姓名/邮箱/导航/技能）
│   ├── layouts/BaseLayout.astro   # 页面骨架（<head>、防闪烁脚本、Header/Footer）
│   ├── pages/
│   │   ├── index.astro            # 首页（Hero + 简介 + 作品网格 + 技能条带）
│   │   ├── about.astro            # 关于页
│   │   ├── 404.astro              # 404 页
│   │   └── projects/[slug].astro  # ★ 项目详情页（动态路由）
│   ├── styles/global.css          # ★ 全局样式与设计令牌（配色/字体/主题变量）
│   └── utils/path.ts              # 处理 GitHub Pages 子路径的资源引用
├── astro.config.mjs               # Astro 配置（site / base）
├── package.json
├── preview.html                   # 独立 HTML 样板（不参与构建，离线预览用）
└── README.md                      # 本文档
```

> 标 ★ 的文件是日常维护最常触及的。

---

## 日常维护

### 新增一个项目

**只需 3 步，全程不改代码：**

**第 1 步：新建封面图**

在 [public/projects/](public/projects/) 下新建一个与项目同名的文件夹，放入封面图：

```
public/projects/<你的项目名>/cover.svg   （或 cover.png / cover.jpg）
```

> 若不擅长做图，可复制任意一个现有的 `cover.svg`（如 [eva-presentation/cover.svg](public/projects/eva-presentation/cover.svg)）作为模板修改。SVG 可用任意文本编辑器调整。

**第 2 步：新建项目 Markdown 文件**

在 [src/content/projects/](src/content/projects/) 下新建 `<你的项目名>.md`，**文件名即详情页网址**（`/projects/<文件名>/`）。填入如下结构：

```markdown
---
title: "项目标题"
description: "一句话简介，会出现在卡片和详情页头部。"
pubDate: 2026-07-01
cover: "/projects/<你的项目名>/cover.svg"
coverAlt: "封面图的文字描述（无障碍用）"
role: "独立开发 · 视觉设计"
tags: ["工具", "可视化"]
stack: ["React", "Node.js", "PostgreSQL"]
demoUrl: "https://你的在线演示地址.com"
repoUrl: "https://github.com/你的用户名/仓库名"
featured: false
order: 5
---

## 概述
这个项目是什么、解决什么问题，2-3 句话讲清楚。

## 问题
为什么要做它？痛点是什么？

## 方案
你是怎么做的？列出关键设计决策（用列表更清晰）。

## 成果
做完之后的效果、数据、反馈。
```

**第 3 步：推送**

```bash
git add -A
git commit -m "feat: 新增 <项目名> 项目"
git push
```

推送后 GitHub Actions 会自动构建并部署，约 2-4 分钟后线上即可看到新项目。

> **字段含义与完整说明见下方 [项目 Markdown 字段速查](#项目-markdown-字段速查)。**

---

### 编辑 / 删除项目

- **编辑**：直接修改对应的 `.md` 文件，推送即可。
- **删除**：删掉 `.md` 文件（可选：同时删掉 `public/projects/<同名>/` 封面文件夹），推送即可。详情页会随之消失。

---

### 修改个人信息

几乎所有个人信息都集中在 [src/consts.ts](src/consts.ts)，改这一处全站生效：

```typescript
export const SITE = {
  name: '阿城',                              // 显示名（顶栏、关于页、版权）
  tagline: '项目档案',
  title: '阿城 · 项目档案',                   // 浏览器标签页标题
  description: '阿城的个人项目作品集 —— ...',  // SEO 描述
  author: '阿城',                            // 作者名
  email: 'huocheng.mx@icloud.com',           // ★ 联系邮箱
  github: 'https://github.com/MORECORIANDERS', // GitHub 主页
  location: '中国 · 远程',                    // 所在地（首页简介区）
};

export const NAV = [                          // 顶栏导航
  { label: '作品', href: '/#work' },
  { label: '关于', href: '/about' },
];

export const STACK = [                        // 首页底部技能滚动条带
  'TypeScript', 'React', 'Astro', 'Node.js', 'Python',
  'PostgreSQL', 'Docker', 'Figma', 'Three.js', 'Rust',
];
```

**常见修改：**

| 想改什么 | 改哪里 |
|---------|--------|
| 姓名 / 邮箱 / GitHub 链接 / 所在地 | [src/consts.ts](src/consts.ts) 的 `SITE` |
| 顶栏导航项 | [src/consts.ts](src/consts.ts) 的 `NAV` |
| 首页技能条带内容 | [src/consts.ts](src/consts.ts) 的 `STACK` |
| 首页 Hero 大标题文案 | [src/pages/index.astro](src/pages/index.astro) 的 `.hero-title` |
| 关于页正文 | [src/pages/about.astro](src/pages/about.astro) |
| 页脚文案 | [src/components/Footer.astro](src/components/Footer.astro) |

---

### 替换项目封面

1. 把新图片放进 `public/projects/<项目名>/` 目录。
2. 修改对应 `.md` 文件的 `cover` 字段，指向新文件：

```yaml
cover: "/projects/<项目名>/cover.png"
```

3. 推送即可。建议封面宽高比 **16:10**（普通项目）或 **21:9**（featured 项目更佳）。

---

## 项目 Markdown 字段速查

每个项目 `.md` 文件由两部分组成：**frontmatter**（`---` 之间的元数据）+ **正文**（Markdown 内容）。

### Frontmatter 字段

| 字段 | 类型 | 必填 | 默认值 | 说明 |
|------|------|:----:|--------|------|
| `title` | string | ✅ | — | 项目标题 |
| `description` | string | ✅ | — | 一句话简介（卡片 + 详情页头部 + SEO） |
| `pubDate` | date | ✅ | — | 发布日期，如 `2026-07-01`。影响排序 |
| `updatedDate` | date | ❌ | — | 最后更新日期（详情页展示） |
| `cover` | string | ✅ | — | 封面图路径，如 `/projects/xxx/cover.svg` |
| `coverAlt` | string | ✅ | — | 封面图替代文字（无障碍） |
| `role` | string | ❌ | — | 你的角色，如「全栈开发 · 设计」 |
| `tags` | string[] | ❌ | `[]` | 项目标签（卡片右下角小标签） |
| `stack` | string[] | ❌ | `[]` | 技术栈（详情页展示） |
| `demoUrl` | url | ❌ | — | 在线演示地址（详情页「在线演示」按钮） |
| `repoUrl` | url | ❌ | — | 源码仓库地址（详情页「查看源码」按钮） |
| `featured` | boolean | ❌ | `false` | 是否置顶。`true` 的项目在首页占满整行、封面变 21:9 |
| `order` | number | ❌ | `0` | 排序权重，**越大越靠前**；同 order 时按 `pubDate` 降序 |

> 字段类型与校验规则定义在 [src/content.config.ts](src/content.config.ts)。填错字段会在 `npm run build` 时报错提示。

### 正文结构（约定）

正文用 Markdown 编写，约定使用四段式叙事，每段用二级标题 `##`：

```markdown
## 概述    ← 是什么
## 问题    ← 为什么做
## 方案    ← 怎么做的
## 成果    ← 做出了什么
```

详情页（[src/pages/projects/[slug].astro](src/pages/projects/%5Bslug%5D.astro)）会自动渲染这些标题与段落，并配套元信息卡（日期、角色、技术栈、演示/源码按钮）。

---

## 设计系统

全局设计令牌定义在 [src/styles/global.css](src/styles/global.css) 的 `:root`（白天）与 `[data-theme="dark"]`（黑夜）中。

### 配色

| 令牌 | 白天 | 黑夜 | 用途 |
|------|------|------|------|
| `--bg` | `#f6f3ee` | `#121114` | 页面背景（暖纸 / 暖近黑） |
| `--bg-elev` | `#fbf9f5` | `#1a1a1f` | 抬升表面 |
| `--bg-sunken` | `#efebe3` | `#0d0d10` | 下沉表面 |
| `--ink` | `#1c1b19` | `#ece7de` | 主文字 |
| `--ink-soft` | `#6b655c` | `#8a847a` | 次要文字 |
| `--ink-faint` | `#9a948a` | `#5f5a52` | 弱化文字 |
| `--accent` | `#9a7b4f` | `#b89366` | 强调色（黄铜） |
| `--accent-strong` | `#6e5532` | `#d4ae7a` | 强调色加强 |
| `--line` | `rgba(28,27,25,.12)` | `rgba(236,231,222,.12)` | 分割线 |

### 字体

| 变量 | 字体 | 用途 |
|------|------|------|
| `--font-serif` | Fraunces / Noto Serif SC | 标题、引文（衬线） |
| `--font-sans` | Manrope / Noto Sans SC | 正文（无衬线） |
| `--font-mono` | JetBrains Mono | 标签、元信息、代码 |

字体通过 Google Fonts 在 [BaseLayout.astro](src/layouts/BaseLayout.astro) 的 `<head>` 中加载。

### 其他视觉特征

- **颗粒噪点**：`.grain` 固定层叠加细微噪点，营造质感。
- **滚动入场**：带 `data-reveal` 属性的元素进入视口时淡入上移（由 `IntersectionObserver` 驱动，定义在 [BaseLayout.astro](src/layouts/BaseLayout.astro)）。
- **响应式**：断点 900px / 720px，移动端单列布局。

---

## 昼夜模式机制

主题切换由三部分协作完成，无需后端：

1. **防闪烁脚本**（[BaseLayout.astro](src/layouts/BaseLayout.astro) `<head>` 内 `is:inline` 脚本）：
   在首屏渲染前同步执行，按优先级 `localStorage.theme` → 系统偏好 `prefers-color-scheme` → 默认 `light` 决定主题，写入 `<html data-theme="...">`，避免页面加载瞬间的主题闪烁（FOUC）。

2. **切换按钮**（[ThemeToggle.astro](src/components/ThemeToggle.astro)）：
   点击切换 `data-theme` 并写入 `localStorage`，CSS 变量随之变化。

3. **样式驱动**（[global.css](src/styles/global.css)）：
   所有颜色都用 CSS 变量，`[data-theme="dark"]` 选择器覆盖变量值，整站自动切换。

> 用户偏好会持久化在浏览器 `localStorage`，下次访问自动恢复。

---

## 部署机制

部署完全自动化，由 [.github/workflows/deploy.yml](.github/workflows/deploy.yml) 驱动。

**触发条件**：向 `main` 分支推送，或手动在 GitHub Actions 页面触发。

**流程**：
1. `build` job：Checkout → 安装 Node 20 → `npm ci` → `astro build` → 上传 `dist/` 产物。
2. `deploy` job：调用 `actions/deploy-pages` 将产物部署到 GitHub Pages。

**并发控制**：`concurrency.group: pages` 保证同一时刻只有一份部署，避免并发覆盖（`cancel-in-progress: false` 即排队而非取消）。

**首次部署前提**（已配置好，仅备忘）：
- 仓库 Settings → Pages → Source 设为 **GitHub Actions**。
- 仓库 Settings → Actions → General → Workflow permissions 设为 **Read and write**。

部署通常在推送后 2-4 分钟完成，可在 <https://github.com/MORECORIANDERS/portfolio/actions> 查看进度。

---

## 本地预览（preview.html）

根目录的 [preview.html](preview.html) 是一个**独立、自包含**的 HTML 样板，用于快速预览设计效果，**不参与 Astro 构建**。

- 内联了全部 CSS / JS，CDN 加载字体，**双击即可在浏览器打开**，无需 `npm install`。
- 含完整的昼夜切换、Hero、简介、项目卡片、页脚。
- 封面图直接引用线上已部署的 SVG。
- 顶部有「样板预览」提示条。

**用途**：在不启动开发服务器的情况下，向他人展示设计风格；或作为视觉改稿的快速试验场。改完满意后，再把改动同步回 Astro 组件。

> 该文件不会被部署到线上，仅作本地参考。

---

## 常见问题 FAQ

**Q：新增项目后线上没出现？**
A：① 确认 `.md` 文件在 `src/content/projects/` 下；② 确认 frontmatter 字段齐全且类型正确（`npm run build` 本地试一次）；③ 等待 GitHub Actions 跑完（2-4 分钟）；④ 浏览器强制刷新（Ctrl/Cmd+Shift+R）绕过缓存。

**Q：封面图不显示？**
A：检查 `cover` 路径是否以 `/projects/` 开头、文件是否真的在 `public/projects/<同名>/` 下。注意路径区分大小写。

**Q：本地 `npm run dev` 报错？**
A：先 `npm install` 装依赖；确认 Node 版本 ≥ 20（`node -v`）。

**Q：想换域名 / 改子路径？**
A：修改 [astro.config.mjs](astro.config.mjs) 的 `base`（当前 `/portfolio/`）。若部署到根路径（如自定义域名），把 `base` 改成 `'/'` 或删除该行。

**Q：项目排序怎么控制？**
A：调 frontmatter 的 `order` 字段，越大越靠前；`featured: true` 的项目整体置顶。详见 [字段速查](#项目-markdown-字段速查)。

**Q：怎么换强调色（黄铜色）？**
A：改 [src/styles/global.css](src/styles/global.css) 里 `:root` 和 `[data-theme="dark"]` 的 `--accent` / `--accent-strong` 两对变量。

**Q：push 时提示认证失败？**
A：GitHub 不再支持密码认证。使用 Personal Access Token（需勾选 `repo` 权限）或 SSH key。Token 切勿提交进仓库或泄露。

---

## 文件速查表

| 我想…… | 改这个文件 |
|--------|-----------|
| 新增项目 | 新建 `src/content/projects/<名>.md` + `public/projects/<名>/cover.svg` |
| 改姓名/邮箱/GitHub | [src/consts.ts](src/consts.ts) |
| 改首页技能条带 | [src/consts.ts](src/consts.ts) 的 `STACK` |
| 改首页 Hero 文案 | [src/pages/index.astro](src/pages/index.astro) |
| 改关于页 | [src/pages/about.astro](src/pages/about.astro) |
| 改页脚 | [src/components/Footer.astro](src/components/Footer.astro) |
| 改顶栏导航 | [src/consts.ts](src/consts.ts) 的 `NAV` |
| 改配色/字体 | [src/styles/global.css](src/styles/global.css) |
| 改项目字段规则 | [src/content.config.ts](src/content.config.ts) |
| 改详情页布局 | [src/pages/projects/[slug].astro](src/pages/projects/%5Bslug%5D.astro) |
| 改部署流程 | [.github/workflows/deploy.yml](.github/workflows/deploy.yml) |
| 改站点子路径/域名 | [astro.config.mjs](astro.config.mjs) |

---

*最后更新：2026-07-02*
