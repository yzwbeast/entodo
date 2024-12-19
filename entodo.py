import json
import datetime
import os
from replit import clear
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm

# 配置中文字体
# 如果是 Windows 系统，通常使用 SimHei 或 Microsoft YaHei
# 如果是 Mac，可以使用 STHeiti 或 PingFang
font_path = "/System/Library/Fonts/STHeiti Light.ttc"  # macOS 示例
# font_path = "C:/Windows/Fonts/simhei.ttf"  # Windows 示例
zh_font = fm.FontProperties(fname=font_path)

# 文件路径
DATA_FILE = "study_progress.json"

# 任务安排（任务内容）参考 https://youtu.be/5-T6Xqlh6BU?si=QTHCA2zQytbsdwPj
TASKS = {
    "Monday": ["阅读您的书籍", "阅读新闻", "阅读简单维基上的文章", "同时记下一些新词及其定义", "(rest)从书中大声朗读", "(rest)抄写书中的一些段落", "(rest)听书的音频版", "(rest)使用多邻国或其他学习应用"],
    "Tuesday": ["在笔记本上写下昨天今天和明天的活动", "在油管视频下留言", "写一些关于您喜欢或不喜欢的歌曲书籍和电视剧的句子", "总结前一天阅读的书籍内容", "在词典中添加新词", "(rest)阅读您所写的内容", "(rest)将您所写的内容粘贴到谷歌翻译中让它读给您听", "(rest)大声朗读您所写的内容", "(rest)使用多邻国或其他学习应用"],
    "Wednesday": ["观看您的电视剧", "听您的歌曲", "如果有聆听书的音频版", "观看油管视频", "在词典中添加新词", "(rest)阅读关于您的电视剧的信息", "(rest)写下您的歌曲给您的感受", "(rest)模仿或影随电视剧中的人物", "(rest)跟唱歌曲"],
    "Thursday": ["大声讲话", "叙述您的生活", "录下自己并回放", "在词典中添加新词", "(rest)大声朗读", "(rest)大声唱歌", "(rest)影随或模仿电视剧中的演员"],
    "Friday": ["复习词典中的所有词汇", "写出它们", "大声说出它们", "将它们用在句子中", "创建一个Quizlet的集合", "制作闪卡", "直到全部记住为止"],
    "Saturday": ["寻找一首新的歌曲", "寻找一本新的书籍", "寻找一部新的电视剧"],
    "Sunday": ["休息一下"]
}

# 每周的学习主题
LEARNING_THEMES = {
    "Monday": "Spend 30-40 minutes Reading",
    "Tuesday": "Spend 30-40 minutes Writing",
    "Wednesday": "Spend 30-40 minutes Listening",
    "Thursday": "Spend 30-40 minutes Speaking",
    "Friday": "Spend the Entire hour on Vocabulary"
}

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# 加载数据（如果文件不存在，初始化数据）
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    else:
        # 如果文件不存在，初始化任务结构和进度
        return {
            "tasks": TASKS,
            "progress": {}
        }

# 保存数据
def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

# 显示今天的学习任务和主题
def record_progress(today_tasks):
    data = load_data()
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")  # 获取今天的日期
    current_weekday = datetime.datetime.now().strftime("%A")  # 获取星期几

    if "progress" not in data:
        data["progress"] = {}

    if current_date not in data["progress"]:
        data["progress"][current_date] = {
            "星期": current_weekday,
            "任务": {}
        }

    # 定义颜色：模仿苹果官网风格
    WHITE = '\033[38;5;15m'       # 白色（主要文本色）
    LIGHT_GRAY = '\033[38;5;245m' # 浅灰色（次要信息）
    GREEN = '\033[38;5;34m'       # 柔和绿色（已完成）
    ORANGE = '\033[38;5;214m'     # 柔和橙色（未完成）
    BLUE = '\033[38;5;75m'        # 蓝色（用户输入提示）
    RESET = '\033[0m'             # 重置颜色

    # 打印头部信息
    print(f"{LIGHT_GRAY}今日日期：{WHITE}{current_date}  星期：{WHITE}{current_weekday}{RESET}")
    print(f"{LIGHT_GRAY}今日任务清单：{RESET}")

    completed_count = 0
    total_tasks = len(today_tasks)

    for task in today_tasks:
        status = input(f"{BLUE}完成了 {task} 吗? (y/n): {RESET}").strip().lower()
        if status == "y":
            data["progress"][current_date]["任务"][task] = "✅"
            completed_count += 1
            print(f"{GREEN}✔ 已完成: {task}{RESET}")  # 柔和绿色
        elif status == "n":
            data["progress"][current_date]["任务"][task] = "⬜️"
            print(f"{ORANGE}✘ 未完成: {task}{RESET}")  # 柔和橙色
        else:
            print(f"{ORANGE}无效输入，默认为未完成。{RESET}")
            data["progress"][current_date]["任务"][task] = "⬜️"
            print(f"{ORANGE}✘ 未完成: {task}{RESET}")

    # 计算完成率
    completion_rate = (completed_count / total_tasks) * 100
    data["progress"][current_date]["完成百分比"] = round(completion_rate, 2)

    # 打印总结
    print(f"\n{LIGHT_GRAY}总结：{RESET}")
    print(f"{WHITE}总任务数：{completed_count}/{total_tasks}  "
          f"完成率：{GREEN}{completion_rate:.2f}%{RESET}")

    save_data(data)

# 查看当天学习记录
def view_progress():
    data = load_data()
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    print(f"\n📅 今天是 {current_date}，学习记录如下：")

    if "progress" in data and current_date in data["progress"]:
        daily_data = data["progress"][current_date]
        print(f"星期: {daily_data['星期']}")
        print("任务完成情况：")

        # 按任务内容判断，将包含 "(rest)" 的任务放在第二列
        tasks = daily_data["任务"]
        first_column = [task for task in tasks if "(rest)" not in task]  # 不包含 "(rest)"
        second_column = [task for task in tasks if "(rest)" in task]  # 包含 "(rest)"

        # 计算最大任务数量
        max_len = max(len(first_column), len(second_column))

        # 打印每行的任务完成情况，确保列对齐
        for i in range(max_len):
            # 获取任务和状态
            task1 = first_column[i] if i < len(first_column) else ""  # 第一列任务
            status1 = tasks[task1] if task1 else ""  # 第一列状态

            task2 = second_column[i] if i < len(second_column) else ""  # 第二列任务
            status2 = tasks[task2] if task2 else ""  # 第二列状态
            column_width = 30-len(task1)
            # 输出每行的任务和状态
            print(f"{status1} {task1:<{column_width}}  {status2} {task2:<30}")

        # 打印完成百分比
        print(f"\n完成百分比: {daily_data['完成百分比']}%")
    else:
        print("今天还没有学习记录！")

# 绘制学习进度图表
def plot_progress():
    data = load_data()
    if "progress" not in data or not data["progress"]:
        print("没有足够的数据绘制图表！")
        return

    dates = []
    completion_rates = []
    for date, info in data["progress"].items():
        dates.append(date)
        completion_rates.append(info["完成百分比"])

    # 绘制柱状图
    plt.figure(figsize=(10, 6))
    plt.bar(dates, completion_rates, color='skyblue')

    # 设置标题、X轴和Y轴标签（使用中文字体）
    plt.title("每日学习任务完成率", fontproperties=zh_font, fontsize=16)
    plt.xlabel("日期", fontproperties=zh_font, fontsize=12)
    plt.ylabel("完成率 (%)", fontproperties=zh_font, fontsize=12)

    # 设置Y轴范围
    plt.ylim(0, 100)

    # 旋转X轴日期标签，避免重叠
    plt.xticks(rotation=45, fontproperties=zh_font)
    # 优化图表标签
    # plt.xticks(range(0, len(dates), max(1, len(dates) // 10)), rotation=45, fontproperties=zh_font)

    # 显示图表
    plt.tight_layout()  # 防止标签被遮挡
    plt.show()

# 获取当天任务列表
def get_today_tasks():
    today_weekday = datetime.datetime.now().strftime("%A")
    return TASKS.get(today_weekday, [])

# 显示今天的学习任务和主题
def show_today_task():
    # 加载保存的进度数据
    data = load_data()  # 假设这是从 JSON 文件加载的数据

    # 获取今天的日期和星期几
    today = datetime.date.today()
    weekday = today.strftime("%A")  # 获取今天星期几（英文格式）
    today_date = today.strftime("%Y-%m-%d")

    # 根据英文星期获取中文星期
    chinese_weekday = {
        "Monday": "星期一",
        "Tuesday": "星期二",
        "Wednesday": "星期三",
        "Thursday": "星期四",
        "Friday": "星期五",
        "Saturday": "星期六",
        "Sunday": "星期日"
    }

    # 获取当天的任务和主题
    tasks = TASKS.get(weekday, [])
    theme = LEARNING_THEMES.get(weekday, "")

    # 加载当天任务状态，如果没有记录，使用默认未完成状态
    task_status = data.get("progress", {}).get(today_date, {}).get("任务", {})
    task_status = {task: task_status.get(task, "⬜️") for task in tasks}

    # 按照任务内容判断，将包含 "(rest)" 的任务放在第二列
    first_column = [task for task in tasks if "(rest)" not in task]  # 不包含 "(rest)"
    second_column = [task for task in tasks if "(rest)" in task]  # 包含 "(rest)"

    # 打印今天的日期、星期和任务主题
    print(f"今天是：{today_date}（{chinese_weekday[weekday]}）")
    print(f"学习主题：{theme}")
    print("今天的学习任务：")

    # 计算最大任务数量
    max_len = max(len(first_column), len(second_column))

    # 打印每行的任务及状态
    for i in range(max_len):
        task1 = first_column[i] if i < len(first_column) else ""  # 如果第一列没有任务，则为空
        task2 = second_column[i] if i < len(second_column) else ""  # 如果第二列没有任务，则为空

        # 从状态字典中获取任务状态
        status1 = task_status.get(task1, "") if task1 else ""
        status2 = task_status.get(task2, "") if task2 else ""

        column_width = 30 - len(task1)
        # 打印任务及其状态
        if task1:
            print(f"{status1} {task1:<{column_width}}", end="  ")
        else:
            print(" " * (column_width + 2), end="  ")

        if task2:
            print(f"{status2} {task2}")
        else:
            print()  # 如果第二列任务为空，则换行

# 主程序
def main():
    # 显示今天的任务和主题
    show_today_task()
    # print(f"\n今天是：{datetime.datetime.now().strftime('%Y-%m-%d')}（星期{datetime.datetime.now().strftime('%A')}）")
    # print("今天的学习任务：")
    # for task in today_tasks:
    #     print(f"- {task}")

    while True:
        # 获取今天的任务
        today_tasks = get_today_tasks()

        # 提供选项
        print("\n请选择操作：")
        print("1. 记录学习进度")
        print("2. 查看学习记录")
        print("3. 绘制学习进度图表")
        print("4. 退出程序")

        choice = input("请输入选择 (1/2/3/4): ").strip()

        if choice == "1":
            clear()  # 清除屏幕
            # 分隔符
            print("-" * (2 * 40))
            record_progress(today_tasks)
        elif choice == "2":
            clear()  # 清除屏幕
            # 分隔符
            print("-" * (2 * 40))
            view_progress()
        elif choice == "3":
            clear()  # 清除屏幕
            # 分隔符
            print("-" * (2 * 40))
            plot_progress()
        elif choice == "4":
            clear()  # 清除屏幕
            print("退出程序...")
            break
        else:
            clear()  # 清除屏幕
            # 分隔符
            print("-" * (2 * 40))
            print("无效选择，请重新输入。")

if __name__ == "__main__":
    clear()  # 清除屏幕
    # 分隔符
    print("-" * (2 * 40))
    main()
