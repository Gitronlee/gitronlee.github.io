---
title: JavaScript 数组方法大全
description: 常用数组方法及其使用场景
category: JavaScript
order: 2
---

## 遍历方法

| 方法 | 说明 | 返回值 |
|------|------|--------|
| `forEach` | 遍历每个元素 | `undefined` |
| `map` | 转换每个元素 | 新数组 |
| `filter` | 过滤元素 | 新数组 |
| `reduce` | 累积计算 | 任意值 |

## 查找方法

```javascript
// 查找元素
arr.find(x => x > 10)           // 返回第一个匹配的元素
arr.findIndex(x => x > 10)      // 返回第一个匹配的索引
arr.includes(value)             // 是否包含某个值

// 条件判断
arr.every(x => x > 0)           // 是否所有元素都满足条件
arr.some(x => x > 0)            // 是否有元素满足条件
```

## 操作方法

```javascript
// 添加/删除
arr.push(item)                  // 末尾添加
arr.pop()                       // 末尾删除
arr.unshift(item)               // 开头添加
arr.shift()                     // 开头删除

// 切片
arr.slice(start, end)           // 截取片段
arr.splice(start, count, ...items) // 增删改
```

## 转换方法

```javascript
// 排序
arr.sort((a, b) => a - b)       // 升序
arr.sort((a, b) => b - a)       // 降序

// 其他
arr.reverse()                   // 反转
arr.join('-')                   // 连接为字符串
arr.flat()                      // 扁平化嵌套数组
```
