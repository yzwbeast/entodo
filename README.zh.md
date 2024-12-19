
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
3. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```
4. 运行脚本：
   ```bash
   python entodo.py
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
