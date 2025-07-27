import subprocess
import os

# Thank god stackoverflow and google still exsist

base_dir = os.path.dirname(os.path.abspath(__file__))
wezterm_path = os.path.join(base_dir, "WezTerm", "wezterm-gui.exe")
script_path = os.path.join(base_dir, "blackjack.py")

cmd = [wezterm_path,"start","python", script_path]

subprocess.Popen(cmd, cwd=base_dir)
