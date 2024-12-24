[X Posts](https://x.com/yzwbeast/status/1869767947566350820)

# Study Progress Tracker

[中文版本 README available here](README.zh.md)

This project is a **study progress tracker** implemented in Python. It is designed to help users plan and track their daily learning activities effectively. The tool provides interactive features for recording progress, viewing records, and visualizing completion rates.

## Features
- **Daily Task and Theme Management**: Pre-defined study tasks and themes for better organization.
- **Progress Recording**: Interactive task completion tracking and daily completion rate calculation.
- **Visualization**: Bar charts to show progress trends.
- **User Interaction**: Friendly prompts and feedback for an intuitive user experience.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yzwbeast/entodo.git
   ```
2. Navigate to the project directory:
   ```bash
   cd entodo
   ```
<details>
<summary>Why Use Virtual Environments</summary>

> When you encounter the "**externally-managed-environment**" error, it might be because the Python version installed via APT by the operating system enforces strict management of the system environment, preventing users from modifying system-level Python packages with pip.<br />
> **Recommended Solution**:<br />Using a virtual environment is the cleanest and safest method. It does not affect the system Python environment and allows you to freely manage dependencies.
</details>

3. Create a virtual environment<br />Run in the project directory:
   ```bash
   python3 -m venv entodo
   ```
   - `entodo` is the name of the virtual environment and can be replaced with any name.
4. Activate the virtual environment:
   ```bash
   source entodo/bin/activate
   ```
5. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
6. Run the script:
   ```bash
   python entodo.py
   ```
7. Exit the virtual environment: After use, you can exit the environment:
   ```bash
   deactivate
   ```
8. Delete the virtual environment
Just delete the my_env folder:
   ```bash
   rm -rf entodo
   ```

## Usage
1. View today’s study tasks and themes.
2. Record your task progress interactively.
3. Review progress records.
4. Visualize your study progress.

## File Structure
- `entodo.py`: Main script containing all functionalities.
- `study_progress.json`: JSON file for storing tasks and progress data.

## Configuration
Update the `font_path` in the script to match your system’s font directory for Chinese font support.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

[中文版本 README available here](README.zh.md)
