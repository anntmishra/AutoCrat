#!/bin/bash

# Function to check if a command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Function to locate Python and set up a virtual environment
setup_python_env() {
    echo "Checking Python installation..."
    if command_exists python3; then
        PYTHON_EXEC=$(command -v python3)
    elif command_exists python; then
        PYTHON_EXEC=$(command -v python)
    else
        echo "Python not found. Attempting to install Python..."
        if [[ "$OS_TYPE" == "Mac" ]]; then
            install_homebrew_if_needed
            echo "Installing Python via Homebrew..."
            brew install python3 || { echo "Failed to install Python. Please install it manually."; exit 1; }
            PYTHON_EXEC=$(command -v python3)
        else
            echo "Please install Python from https://www.python.org/ and re-run this script."
            exit 1
        fi
    fi
    echo "Python found at: $PYTHON_EXEC"

    echo "Creating virtual environment..."
    $PYTHON_EXEC -m venv "$HOME/Desktop/autotyper/venv" || { echo "Failed to create virtual environment."; exit 1; }
    source "$HOME/Desktop/autotyper/venv/bin/activate"
}

# Function to install Homebrew if it is not present (macOS only)
install_homebrew_if_needed() {
    echo "Checking for Homebrew..."
    if ! command_exists brew; then
        echo "Homebrew not found. Installing Homebrew..."
        /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)" || { echo "Failed to install Homebrew. Please install it manually."; exit 1; }
    else
        echo "Homebrew is already installed."
    fi
}

# Function to verify Git installation
verify_git_installation() {
    echo "Checking for Git installation..."
    if ! command_exists git; then
        echo "Git is not installed."
        if [[ "$OS_TYPE" == "Mac" ]]; then
            install_homebrew_if_needed
            echo "Installing Git via Homebrew..."
            brew install git || { echo "Failed to install Git. Please install it manually."; exit 1; }
        else
            echo "Please install Git from https://git-scm.com/ and re-run this script."
            exit 1
        fi
    else
        echo "Git is already installed."
    fi
}

# Function to clone or update the repository
clone_or_update_repo() {
    REPO_PATH="$HOME/Desktop/autotyper/The-Typer"
    if [ -d "$REPO_PATH" ]; then
        echo "Repository already exists. Updating repository..."
        cd "$REPO_PATH" && git pull || { echo "Failed to update repository. Check your internet connection."; exit 1; }
    else
        echo "Cloning repository..."
        mkdir -p "$HOME/Desktop/autotyper"
        git clone https://github.com/anntmishra/AutoCrat.git "$REPO_PATH" || { echo "Failed to clone repository. Check your internet connection."; exit 1; }
    fi
}

# Function to install Python dependencies
install_python_dependencies() {
    echo "Installing required Python dependencies..."
    PIP_EXEC="$HOME/Desktop/autotyper/venv/bin/pip"
    source "$HOME/Desktop/autotyper/venv/bin/activate"
    if ! $PIP_EXEC show pyautogui > /dev/null 2>&1 || ! $PIP_EXEC show pyqt5 > /dev/null 2>&1; then
        echo "Installing dependencies..."
        $PIP_EXEC install pyautogui pyqt5 || { echo "Failed to install dependencies. Ensure pip is installed."; exit 1; }
    else
        echo "Dependencies are already installed."
    fi
}

# Function to create a macOS shortcut
create_mac_shortcut() {
    echo "Creating macOS application shortcut..."
    APP_FOLDER="$HOME/Desktop/AutoCrat.app"
    mkdir -p "$APP_FOLDER/Contents/MacOS"
    echo '#!/bin/bash' > "$APP_FOLDER/Contents/MacOS/AutoCrat"
    echo "$HOME/Desktop/autotyper/venv/bin/python $HOME/Desktop/autotyper/The-Typer/autocrat_main.py" >> "$APP_FOLDER/Contents/MacOS/AutoCrat"
    chmod +x "$APP_FOLDER/Contents/MacOS/AutoCrat"
    echo "Shortcut created on your Desktop as AutoCrat.app."
}

# Function to create a Windows shortcut
create_windows_shortcut() {
    echo "Creating Windows shortcut..."
    powershell -Command "
        \$WshShell = New-Object -ComObject WScript.Shell;
        \$Shortcut = \$WshShell.CreateShortcut([System.IO.Path]::Combine([System.Environment]::GetFolderPath('Desktop'), 'AutoCrat.lnk'));
        \$Shortcut.TargetPath = '$HOME\\Desktop\\AUTOCRAT\\venv\\Scripts\\python.exe';
        \$Shortcut.Arguments = '\"$HOME\\Desktop\\AUTOCRAT\\AUTOCRAT\\autocrat_main.py\"';
        \$Shortcut.WorkingDirectory = '\"$HOME\\Desktop\\AUTOCRAT\\The-Typer\"';
        \$Shortcut.Save();
    " || { echo "Failed to create Windows shortcut. Please create it manually."; exit 1; }
    echo "Shortcut created on your Desktop as AutoCrat.lnk."
}

# Function to execute the Python script
run_autocrat_script() {
    SCRIPT_PATH="$HOME/Desktop/autotyper/The-Typer/autocrat_main.py"
    if [ -f "$SCRIPT_PATH" ]; then
        echo "Executing autocrat_main.py..."
        $HOME/Desktop/autotyper/venv/bin/python "$SCRIPT_PATH" || { echo "Failed to execute autocrat_main.py. Ensure Python is correctly set up."; exit 1; }
    else
        echo "File autocrat_main.py not found at $SCRIPT_PATH. Please check the file path."
        exit 1
    fi
}

# Determine the operating system
if [[ "$OSTYPE" == "darwin"* ]]; then
    OS_TYPE="Mac"
elif [[ "$OSTYPE" == "cygwin" || "$OSTYPE" == "msys" ]]; then
    OS_TYPE="Windows"
else
    echo "This script is only supported on macOS and Windows."
    exit 1
fi
echo "Operating system detected: $OS_TYPE"

# Main script execution
setup_python_env
verify_git_installation
clone_or_update_repo
install_python_dependencies

# Create a shortcut based on the operating system
if [[ "$OS_TYPE" == "Mac" ]]; then
    create_mac_shortcut
elif [[ "$OS_TYPE" == "Windows" ]]; then
    create_windows_shortcut
fi

# Run the main Python script
run_autocrat_script

echo "Setup completed successfully!"