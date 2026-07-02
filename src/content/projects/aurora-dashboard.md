---
title: "Aurora Dashboard"
description: "面向数据团队的高密度实时指标看板，用克制的视觉承载复杂信息。"
pubDate: 2025-03-12
cover: "/projects/aurora-dashboard/cover.svg"
coverAlt: "Aurora 实时数据看板界面，深色背景上的指标图表"
role: "设计 · 全栈开发"
tags: ["数据可视化", "实时", "SaaS"]
stack: ["React", "TypeScript", "D3", "WebSocket", "Node.js", "PostgreSQL"]
demoUrl: "https://example.com/aurora"
repoUrl: "https://github.com/MORECORIANDERS/aurora"
featured: true
order: 3
---

## 概述

Aurora 是为运营与数据团队打造的实时指标看板。它在一个屏幕里承载数十路并发指标，却始终保持着「能一眼读懂」的克制 —— 这是整个项目最想解决的问题。

## 问题

数据看板最常见的失败，不是信息太少，而是信息太多。团队之前的看板把所有图表塞进一屏，配色花哨、动效喧闹，结果谁也找不到自己要的那一个数字。我们需要的不是更多图表，而是更清晰的层级。

## 方案

- **信息分层**：核心数字最大、次级指标次之、背景趋势最弱，用字号与对比建立秩序而非颜色。
- **实时但不焦躁**：WebSocket 推送数据，但更新动效被刻意压到 300ms 以下的微变化，避免分散注意。
- **暗色优先**：长时间盯屏场景下，深色界面降低疲劳，也让数据高亮更突出。
- **可组合布局**：每个小组件可拖拽、可订阅，团队按自己的关注点拼装专属视图。

## 成果

上线后，团队日常查看看板的平均停留时间反而下降了 —— 这正是目标：更快找到答案，然后离开。被订阅最多的「核心指标」组件，日均触发 1.2 万次实时更新，首屏可交互时间稳定在 800ms 以内。
