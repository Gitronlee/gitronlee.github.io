# Web Toolbox

开发者百宝箱 — Astro 5 静态站点，集成实用工具与小游戏。

[![Built with Astro](https://astro.badg.es/v2/built-with-astro/small.svg)](https://astro.build)

## 功能

- 11 款工具：正则测试、时间戳转换、Base64、JSON 格式化、URL 编解码、哈希计算、颜色转换、番茄时钟、税后工资计算、图片切片、人生 CD 计时
- 单词消消乐：9 年级 × 50 词，支持学习复习
- 响应式深色主题

## 使用

```bash
npm install
npm run dev
```

## 构建部署

```bash
npm run build  # 输出到 dist/
```

自动部署到 GitHub Pages（push to main 触发 CI）。

## 扩展

**新增工具**：`src/data/tools.json` 添加条目 → 创建 `src/components/tools/<Name>.astro` → 在 `src/pages/tools/[slug].astro` 注册

**新增游戏**：`src/data/games.json` 添加条目 → 创建 `src/components/games/<Name>.astro` → 在 `src/pages/games/[slug].astro` 注册
