# 🖥️ System Resource Analyzer

A Python-based command-line application designed to monitor and analyze essential system resources, including CPU usage, memory utilization, disk space, and system uptime.

The application helps users understand their computer's current resource utilization through a simple terminal interface with color-coded output, status indicators, and health warnings.

## 📌 Project Overview

**System Resource Analyzer** is a system monitoring utility developed using Python. It collects basic system information and presents it in an easy-to-understand format, helping users identify potential resource usage issues.

### Project Details

* **Project Name:** System Resource Analyzer
* **Programming Language:** Python
* **Application Type:** Command-Line Interface (CLI)
* **Project Category:** System Monitoring Utility
* **Developer:** Harsh Sharma
* **Purpose:** Educational and Industrial Training Project

## ✨ Features

### 📊 System Monitoring

* **CPU Usage:** Displays the current CPU utilization percentage.
* **RAM Usage:** Monitors memory consumption and available memory.
* **Disk Usage:** Reports disk space utilization.
* **System Uptime:** Displays how long the system has been running.

### 🚦 System Health Analysis

* Displays system resource utilization.
* Identifies high resource usage.
* Provides warnings when resource usage exceeds configured thresholds.
* Presents system health information using status indicators.

### 🎨 Terminal Interface

* Color-coded output using ANSI escape codes.
* Status icons for improved readability.
* Simple command-line interface.
* Organized presentation of system information.

## 🛠️ Technologies Used

* **Python** — Core programming language.
* **psutil** — System and process monitoring, if used by the implementation.
* **ANSI Escape Codes** — Terminal colors and visual indicators.
* **Command-Line Interface (CLI)** — User interaction.

## 💻 System Requirements

Before running the application, ensure that you have:

* Python 3 installed.
* Git installed.
* A terminal or command prompt.
* pip, the Python package manager.

The application is intended for local execution on a supported operating system.

## 🚀 Installation and Setup

Follow these steps to download and run the project on your computer.

### 1. Clone the Repository

Open a terminal and execute:

```bash
git clone https://github.com/harshsharma45/System-Resource-Analyzer.git
```

Navigate to the project directory:

```bash
cd System-Resource-Analyzer
```

### 2. Create a Virtual Environment (Recommended)

On Windows:

```bash
python -m venv venv
```

Activate the environment using Command Prompt:

```cmd
venv\Scripts\activate
```

Or use PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

Install the required packages:

```bash
python -m pip install -r requirements.txt
```

### 4. Run the Application

Start the program:

```bash
python main.py
```

The application should display system resource information in the terminal.

**Note:** The exact output depends on your operating system, current resource usage, and the application's configuration.

## 📸 Application Preview

Add a screenshot of the application running on your computer to showcase its interface.

For example, if you save a screenshot as `screenshots/healthy.png`, use:

```markdown
![System Resource Analyzer](screenshots/healthy.png)
```

Make sure the screenshot exists at the specified path before adding it to the repository.

## 📂 Project Structure

The project may contain the following files and directories:

```text
System-Resource-Analyzer/
├── screenshots/
├── main.py
├── system_info.py
├── health.py
├── display.py
├── ansi_escape_codes.py
├── requirements.txt
├── .gitignore
└── README.md
```

The exact structure depends on the files present in the repository.

### File Descriptions

| File                   | Purpose                                           |
| ---------------------- | ------------------------------------------------- |
| `main.py`              | Entry point for running the application.          |
| `system_info.py`       | Collects system resource information.             |
| `health.py`            | Evaluates resource usage and health conditions.   |
| `display.py`           | Formats and displays information in the terminal. |
| `ansi_escape_codes.py` | Provides terminal color and formatting codes.     |
| `requirements.txt`     | Lists required Python dependencies.               |
| `screenshots/`         | Stores application screenshots.                   |
| `.gitignore`           | Specifies files Git should ignore.                |

## 🎯 Project Objectives

* Understand system resource monitoring using Python.
* Retrieve CPU, memory, disk, and uptime information.
* Identify high resource utilization through configurable warnings.
* Display system information in a readable terminal format.
* Practice modular programming and Python project organization.
* Develop a practical utility for understanding computer performance.

## 🔮 Future Enhancements

The application can be extended with the following features:

* A graphical dashboard for system monitoring.
* Live CPU, RAM, and disk usage charts.
* Continuous monitoring with automatic refresh.
* Configurable resource warning thresholds.
* Historical resource usage reports.
* Exportable system health reports.
* Improved cross-platform compatibility.

These are proposed enhancements and may not be available in the current version.

## 👨‍💻 Developer

**Harsh Sharma**

* **GitHub:** [@harshsharma45](https://github.com/harshsharma45)
* **Project Repository:** [System Resource Analyzer](https://github.com/harshsharma45/System-Resource-Analyzer)
* **LinkedIn:** [harshsharma45](https://www.linkedin.com/in/harshsharma45/)
* **Email:** [harshsharma2444@gmail.com](mailto:harshsharma2444@gmail.com)

## 🎓 Acknowledgment

This project is intended for educational purposes and practical learning in Python programming and system monitoring.

If the project is based on or adapted from an existing open-source implementation, the original author and repository should be credited in accordance with the applicable license.

## 📄 License

Please refer to the license included in the repository. If no license is present, review the licensing terms of any source code used before redistributing or publishing modified versions.
