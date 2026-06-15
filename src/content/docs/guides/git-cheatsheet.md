---
title: 常用 Git 命令速查
description: 日常开发中最常用的 Git 命令和用法
category: Git
order: 1
---

## 基础操作

```bash
# 初始化仓库
git init

# 克隆远程仓库
git clone <url>

# 查看状态
git status

# 添加文件到暂存区
git add <file>
git add .

# 提交更改
git commit -m "描述"
```

## 分支管理

```bash
# 创建分支
git branch <name>

# 切换分支
git checkout <name>

# 创建并切换
git checkout -b <name>

# 合并分支
git merge <name>

# 删除分支
git branch -d <name>
```

## 远程操作

```bash
# 添加远程
git remote add origin <url>

# 推送到远程
git push origin <branch>

# 拉取更新
git pull origin <branch>
```

## 实用技巧

- 使用 `git log --oneline` 查看简洁提交历史
- 使用 `git diff` 查看未暂存的更改
- 使用 `git stash` 临时保存工作进度
