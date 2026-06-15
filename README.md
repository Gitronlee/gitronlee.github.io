# Web Toolbox

基于 Astro 框架构建的开发者百宝箱，集成实用工具、小游戏和学习文档。

[![Built with Astro](https://astro.badg.es/v2/built-with-astro/small.svg)](https://astro.build)

## 特性

- 7 款实用工具：正则表达式、时间戳转换、Base64、JSON 格式化、URL 编解码、哈希计算、颜色转换器
- 游戏模块占位（支持后续扩展）
- Markdown 文档渲染系统
- 配置驱动的动态路由
- 响应式深色主题 UI

## 快速开始

```bash
npm install
npm run dev
```

## 构建

```bash
npm run build
```

构建产物输出到 `dist/` 目录，可直接部署到 GitHub Pages、Vercel、Netlify 等平台。

## 扩展指南

### 新增工具

1. 在 `src/data/tools.json` 中添加工具信息
2. 在 `src/components/tools/` 创建 Astro 组件
3. 在 `src/pages/tools/[slug].astro` 中注册组件

### 新增文档

在 `src/content/docs/` 下新建 Markdown 文件，添加 frontmatter：

```yaml
title: 标题
description: 描述
category: 分类
order: 排序
```

## 部署 GitHub Pages

1. 修改 `astro.config.mjs` 中的 `site` 和 `base` 为你的仓库信息
2. 运行 `npm run build`
3. 推送 `dist/` 部署到 `gh-pages` 分支
