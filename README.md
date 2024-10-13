# Password-Converter
## remember simple passwords, enter a complex version of them.

The **Password Converter** is a basic yet very helpful tool for strengthening user passwords by converting them into more complex versions using a custom dictionary (a pattern that you define).

#### use case:

I created it because at times I felt the need for a strong password but remembering one is a tough job, with **password converter** I simply enter a more familiar password that is easy to remember to me, and enter the complex one (converted using the software)

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [How it Works](#how-it-works)
- [Customization](#customization)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Troubleshooting](#troubleshooting)
- [License](#license)

## Overview

Password Converter is a simple graphical user interface (GUI) application built with Python and Tkinter. It converts normal alpha-numeric passwords into complex passwords based on a custom dictionary.

## Features

- Custom dictionary for password conversion.
- Input field for original password.
- Button to convert password.
- Output field for complex password.
- Clear button to reset input and output fields.
- Copy to clipboard button for ease of use.

## How it Works

1. Enter your original password in the input field.
2. Click the "Convert Password" button.
3. The program replaces characters using the custom dictionary.
4. The complex password is displayed in the output field.
5. Use the "Clear" button to reset the input and output fields.
6. Use the "Copy to Clipboard" button to copy the complex password.

## Customization

To modify the conversion logic, you can customize the `password_dict` in the source code. This allows you to add or change the character replacements based on your needs.

## Requirements

- Python 3.12 (or above)
- Tkinter (included with Python)

## Installation

### 1. Clone or download the repository:

```bash
git clone https://github.com/ratneshtripathi07/password-converter.git
cd password-converter
Run password_converter.py
```

### 2. Or make an executable using pyinstaller:

### Step 1: Install PyInstaller

Install PyInstaller using pip:

```bash
pip install pyinstaller
```

### Step 2: Run PyInstaller

Open terminal/command prompt and navigate to the directory containing the Python file. Run:

```bash
pyinstaller --onefile password_converter.py
```

#### Options:

--onefile: Create a single executable file.

--windowed: Hide the console window when running the executable.

--icon=<icon_file>: Custom icon for the executable.

For a full list of options, run:

```bash
pyinstaller --help
```

#### example:

```bash
pyinstaller --onefile --windowed --icon=my_icon.ico password_converter.py
```

### Step 3: Find the Executable

After running PyInstaller, the executable will be located in the **dist directory** within the same directory as password_converter.py file.

## Usage

1. Run the program.
2. Enter your original password in the input field.
3. Click the "Convert Password" button.
4. Use the complex password as needed.
5. Optionally, clear the fields or copy the result using the respective buttons.

## Troubleshooting

<li>Ensure Python and Tkinter are installed.</li>
<li>for the executable, check for the options or command run, or remake the .exe altogether</li>

## License

This software is released under the MIT license. see <a href="https://github.com/Ratneshtripathi07/Password-Converter/blob/main/LICENSE">License</a> for more info.
