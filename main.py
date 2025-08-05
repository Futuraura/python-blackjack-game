import subprocess
import os
import platform

# Thank god stackOverflow and google still exist

base_dir = os.path.dirname(os.path.abspath(__file__))
script_path = os.path.join(base_dir, "blackjack.py")

if platform.system() == "Windows":
    wezterm_path = os.path.join(base_dir, "WezTerm", "wezterm-gui.exe")
    cmd = [wezterm_path, "start", "python", script_path]
else:
    cmd = ["python", script_path]

subprocess.Popen(cmd, cwd=base_dir)
