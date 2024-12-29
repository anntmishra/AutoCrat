import PyInstaller.__main__
import os

# Get the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

PyInstaller.__main__.run([
    'autocrat_main.py',
    '--name=AutoCrat',
    '--onefile',
    '--windowed',
    '--icon=app_icon.icns',
    f'--workpath={os.path.join(current_dir, "build")}',
    f'--distpath={os.path.join(current_dir, "dist")}',
    '--add-data=app_icon.icns:.'
])