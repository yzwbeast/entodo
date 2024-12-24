
# 学习进度跟踪器

[English README available here](README.md)

这个项目是一个用 Python 实现的 **学习进度跟踪器**，旨在帮助用户高效规划和跟踪每日学习活动。该工具提供交互功能，用于记录进度、查看记录以及可视化完成率。

## 功能
- **每日任务与主题管理**：预定义学习任务和主题，便于组织学习。
- **进度记录**：交互式记录任务完成情况，并计算每日完成率。
- **可视化**：使用柱状图展示学习进度趋势。
- **用户交互**：友好的提示和反馈，提供直观的用户体验。

## 安装步骤
1. 克隆仓库：
   ```bash
   git clone https://github.com/yzwbeast/entodo.git
   ```
2. 进入项目目录：
   ```bash
   cd entodo
   ```

<details>
<summary>为什么推荐使用虚拟环境</summary>

>当你遇到 “**externally-managed-environment**” 错误时，可能是操作系统 使用 APT 安装的 Python 版本对系统环境进行了严格管理，防止用户通过 pip 修改系统级的 Python 包。<br />
>要解决这个问题，**推荐方法**：<br />使用虚拟环境是最干净、安全的方法。它不会影响系统的 Python 环境，同时方便你自由管理依赖。
</details>

3. 创建虚拟环境<br />在项目目录下运行：
   ```bash
   python3 -m venv entodo
   ```
   - `entodo` 是虚拟环境的名称，可以替换为任意名字。
4. 激活虚拟环境：
   ```bash
   source entodo/bin/activate
   ```
5. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```
6. 运行脚本：
   ```bash
   python entodo.py
   ```
7. 退出虚拟环境：使用完后，可退出环境：
   ```bash
   deactivate 
   ```
8. 删除虚拟环境
直接删除 my_env 文件夹即可：
   ```bash
   rm -rf entodo
   ```

## 使用方法
1. 查看今日的学习任务与主题。
2. 交互式记录任务进度。
3. 查看进度记录。
4. 可视化您的学习进展。

## 文件结构
- `entodo.py`：包含所有功能的主脚本。
- `study_progress.json`：用于存储任务和进度数据的 JSON 文件。

## 配置
更新脚本中的 `font_path`，以匹配您的系统字体目录，确保中文字体支持。

## 许可证
本项目基于 MIT 许可证，详情请参阅 [LICENSE](LICENSE) 文件。

[English README available here](README.md)
