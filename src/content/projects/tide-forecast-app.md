---
title: "Tide Forecast App"
description: "一款为海边生活者打造的极简潮汐预报应用，只显示真正重要的那一刻。"
pubDate: 2024-09-20
cover: "/projects/tide-forecast-app/cover.svg"
coverAlt: "潮汐预报应用界面，展示涨退潮时间与高度曲线"
role: "产品设计 · 移动端开发"
tags: ["移动端", "极简", "气象"]
stack: ["React Native", "Expo", "FastAPI", "Python"]
demoUrl: "https://example.com/tide"
repoUrl: "https://github.com/MORECORIANDERS/tide"
featured: false
order: 2
---

## 概述

Tide 是一款潮汐预报应用，面向赶海者、冲浪人与海滨居民。它不做花哨的天气大全，只回答一个问题：今天什么时候涨潮、什么时候退潮。

## 问题

市面上的潮汐应用要么信息过载，要么数据陈旧。赶海的人真正关心的只有三件事：潮位最低点、安全返程时间、以及明天是否值得出门。其余都是噪音。

## 方案

- **单屏即答案**：首页只有一条潮位曲线与三个关键时间点，无需滚动。
- **离线优先**：提前缓存 7 天数据，无网络也能查看。
- **温和提醒**：用低饱和色彩与一次轻震动提示潮位变化，不打扰。
- **地点收藏**：常用海滩一键收藏，切换无需搜索。

## 成果

上线半年，周活跃留存稳定在 41%，应用商店评分 4.8。用户反馈里最高频的词是「干净」—— 这正是设计之初的期待。
