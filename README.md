# AutoCrat - Automatic Code Typer

AutoCrat is a cross-platform application that allows you to automatically type text from your clipboard.

## Prerequisites

- Python 3.x installed on your system
  - Windows: Download from [Python.org](https://www.python.org/downloads/)
  - Mac: Use Homebrew (`brew install python@3.11`)

## Installation Instructions

### For Windows Users:

1. Clone or download this repository
2. Open Command Prompt in the project directory
3. Create a virtual environment:

```bash
python -m venv venv
venv\Scripts\activate
```

4. Install required packages:

```bash
pip install -r requirements.txt
pip install pyinstaller
```

5. Build the executable:

```bash
python windows_setup.py
```

6. Find the executable in the `dist` folder

### For Mac Users:

1. Clone or download this repository
2. Open Terminal in the project directory
3. Create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

4. Install required packages:

```bash
pip3 install pyautogui
pip3 install pyperclip
pip3 install pynput
pip3 install pyinstaller
```

5. Build the executable:

```bash
python3 mac_setup.py
```

6. Find the executable in the `dist` folder

### First-time Setup

#### Windows:

- Double-click the executable in the `dist` folder
- Allow any security permissions if prompted

#### Mac:

1. Go to System Preferences > Security & Privacy > Privacy
2. Enable permissions for:
   - Accessibility
   - Input Monitoring
3. Double-click the executable in the `dist` folder

## Usage

1. Copy the text you want to auto-type
2. Open AutoCrat
3. Click "Start Typing"
4. Within 5 seconds, click where you want the text to be typed
5. To stop, click the "Stop Typing" button

## Troubleshooting

### Mac Users:

- If you get permission errors, try running the install commands with `sudo`
- Make sure to grant all necessary permissions in System Preferences

### Windows Users:

- Run Command Prompt as Administrator if you encounter permission issues
- Make sure Python is added to your system's PATH

## Support

If you encounter any issues:

1. Check if all permissions are granted
2. Verify Python installation
3. Try recreating the virtual environment
4. Create an issue in the repository

## Contributing

Feel free to fork the repository and submit pull requests for any improvements!
