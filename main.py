import subprocess
import os
import platform
import sys
import traceback

# Thank god stackOverflow and google still exist

def wait_for_user_input():
    """Wait for user to press Enter or Esc to close"""
    print("\nPress Enter or Esc to close...")
    try:
        import msvcrt
        while True:
            key = msvcrt.getch()
            if key in [b'\r', b'\x1b']:  # Enter or Esc
                break
    except ImportError:
        # Non-Windows fallback
        input()

def debug_print(message):
    """Print debug information"""
    print(f"[DEBUG] {message}")

try:
    # Check if we're running from a PyInstaller bundle
    is_built = getattr(sys, 'frozen', False)
    
    if is_built:
        # Running from PyInstaller bundle - files are in _internal
        debug_print("Detected PyInstaller bundle")
        base_dir = sys._MEIPASS
        script_path = os.path.join(base_dir, "blackjack.py")
        python_exe = sys.executable
        debug_print(f"Bundle base directory: {base_dir}")
        debug_print(f"Using bundled Python executable: {python_exe}")
    else:
        # Running in development mode
        debug_print("Running in development mode")
        base_dir = os.path.dirname(os.path.abspath(__file__))
        script_path = os.path.join(base_dir, "blackjack.py")
        python_exe = "python"
        debug_print(f"Development base directory: {base_dir}")
    
    debug_print(f"Script path: {script_path}")
    
    # Check if blackjack.py exists
    if not os.path.exists(script_path):
        raise FileNotFoundError(f"blackjack.py not found at: {script_path}")
    
    if platform.system() == "Windows":
        wezterm_path = os.path.join(base_dir, "WezTerm", "wezterm-gui.exe")
        debug_print(f"WezTerm path: {wezterm_path}")
        
        # Check if WezTerm exists
        if not os.path.exists(wezterm_path):
            raise FileNotFoundError(f"wezterm-gui.exe not found at: {wezterm_path}")
        
        if is_built:
            # In built mode, run blackjack.py directly with python from PATH
            # Use just the script name since we set the working directory
            cmd = [wezterm_path, "start", "--cwd", base_dir, "python", "blackjack.py"]
        else:
            # In development mode, use regular python
            cmd = [wezterm_path, "start", "python", script_path]
    else:
        if is_built:
            # On Linux/macOS, run blackjack.py directly
            cmd = ["python", script_path]
        else:
            cmd = ["python", script_path]
    
    debug_print(f"Command to execute: {' '.join(cmd)}")
    debug_print(f"Working directory: {base_dir}")
    
    # Launch the game
    debug_print("Launching game...")
    process = subprocess.Popen(cmd, cwd=base_dir)
    debug_print(f"Game launched successfully! Process ID: {process.pid}")
    
    if is_built:
        # In built mode, we can exit immediately
        debug_print("Built mode - exiting launcher")
    else:
        # In development mode, provide some feedback
        debug_print("Development mode - launcher will exit, game running separately")

except Exception as e:
    print(f"\n❌ ERROR: Failed to launch the game!")
    print(f"Error details: {str(e)}")
    print(f"\n🔍 Debug Information:")
    print(f"  - Python executable: {sys.executable}")
    print(f"  - Current working directory: {os.getcwd()}")
    print(f"  - Script location: {__file__ if '__file__' in globals() else 'Unknown (built)'}")
    print(f"  - Is built with PyInstaller: {getattr(sys, 'frozen', False)}")
    
    if getattr(sys, 'frozen', False):
        print(f"  - Bundle directory (_MEIPASS): {getattr(sys, '_MEIPASS', 'Not available')}")
    
    print(f"\n📋 Full traceback:")
    traceback.print_exc()
    
    wait_for_user_input()
