# Web Toolbox - Implementation Task List

- [x] 1. 初始化 Astro 项目及配置
  - [x] 1.1 创建 package.json、tsconfig.json、astro.config.mjs
  - [x] 1.2 安装依赖（astro、@astrojs/mdx）
  - [x] 1.3 配置全局样式

- [x] 2. 创建共享布局与组件
  - [x] 2.1 BaseLayout 全局 HTML 布局
  - [x] 2.2 Header 响应式导航栏
  - [x] 2.3 Footer 页脚
  - [x] 2.4 CardGrid 卡片网格组件
  - [x] 2.5 ToolLayout 工具页面布局

- [x] 3. 配置数据注册表
  - [x] 3.1 tools.json 工具注册表（7个工具）
  - [x] 3.2 games.json 游戏注册表（3个游戏占位）
  - [x] 3.3 配置驱动的动态路由

- [x] 4. 实现首页与列表页
  - [x] 4.1 首页 index.astro（Hero + 推荐工具）
  - [x] 4.2 工具列表页 /tools
  - [x] 4.3 游戏列表页 /games
  - [x] 4.4 文档列表页 /docs
  - [x] 4.5 404 页面

- [x] 5. 实现工具组件（7个）
  - [x] 5.1 正则表达式测试器
  - [x] 5.2 时间戳转换工具
  - [x] 5.3 Base64 编解码
  - [x] 5.4 JSON 格式化
  - [x] 5.5 URL 编解码
  - [x] 5.6 哈希计算
  - [x] 5.7 颜色转换器

- [x] 6. 实现动态路由
  - [x] 6.1 /tools/[slug] 工具详情
  - [x] 6.2 /games/[slug] 游戏 Coming Soon 页面
  - [x] 6.3 /docs/[...slug] 文档内容页

- [x] 7. 配置文档模块
  - [x] 7.1 Content Collection 配置
  - [x] 7.2 示例文档（Git 命令、JS 数组方法）

- [x] 8. 构建验证
  - [x] 8.1 执行 npm run build 成功（17 页面）
  - [x] 8.2 所有路由生成正确
