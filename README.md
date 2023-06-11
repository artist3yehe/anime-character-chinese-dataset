[**🇨🇳中文**](./README.md) | [**🌐English**](./README_EN.md) | [**🅱️B站**](https://space.bilibili.com/513453119)
<p align="left">
    <img alt="GitHub" src="https://img.shields.io/github/license/ymcui/Chinese-LLaMA-Alpaca.svg?color=blue&style=flat-square">
    <img alt="GitHub top language" src="https://img.shields.io/github/languages/top/ymcui/Chinese-LLaMA-Alpaca">
    <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/ymcui/Chinese-LLaMA-Alpaca">
</p>

<p align="center">
    <br>
    <img src="./img/banner.png" width="700"/>
    <br>
</p>



最近汉语大模型呈现井喷发展，各个体系逐渐完善，语言类应用开始进入全民tuning训练阶段，AI角色个性化这件事作为应用层用户体验的一个关键点也开始受到企业和个人玩家的重视。以促进中文AI角色创作为目标，本项目持续**采集典型二次元动漫角色对话资料（ACCD）**并将其存放在公开仓库中，这些数据可被用于AI角色训练或文学创作学习。

## 用户须知（必读）

- 🍏 数据库数据均来自公开的动漫番剧，这些作品有各自版权限制，本项目数据仅用于AI学习，不可直接用于商用。
- 🍏 数据库数据均来自公开的动漫番剧，其内容不代表项目组思想，且项目组不对内容真实性做担保。

## 采集小组招募！！

本项目希望组织一个开放的动漫数据收集小组，不断为数据库提供新的数据，你可以通过 [**B站私信**](https://space.bilibili.com/513453119) 联系我并加入小组。小组成员可以提前（比如2周）拿到**最新Database**，以及获取**NSFW Database**。

## 数据应用

### 存储形式
本项目数据以json文件存储，借鉴了Alpaca finetuning数据的形式，带有**instruction、input、output**三个键，并扩展**MBTI**人格参数。人格参数在角色数据中也存在，但动漫作品中角色在特定情境下可能呈现不同的人格特征，话语风格也会变化，所以在预料数据库中增加MBTI参数作区别。

### 共性抽象
本项目将数据拆分成**世界知识、自我认知、对话** 3类。其中世界知识和自我认知属于原作设定，不具备共性；对话则可根据需要进行合并使用。例如希望独立训练“元气少女”，那么选几个元气少女型角色的对话部分混合作为训练素材即可获得较好效果。

## 工具应用
### excel2json
项目提供**excel2json**工具，可以将Excel中的对白转成项目标准json格式。
### accd2finetuning
待补充
### accd2ptuning
待补充
