# -*- mode: python ; coding: utf-8 -*-
import os
import sys
from PyInstaller.utils.hooks import collect_data_files, collect_submodules

# Get the current directory (where the spec file is located)
current_dir = os.path.dirname(os.path.abspath(SPEC))

print(f"Current directory: {current_dir}")

# Collect all textual data files
try:
    textual_datas = collect_data_files('textual')
    print(f"Found {len(textual_datas)} textual data files")
except Exception as e:
    print(f"Error collecting textual data: {e}")
    textual_datas = []

# Define data files to include
datas = []

# Add files with existence checks
data_files = [
    ('tcss', 'tcss'),
    ('WezTerm', 'WezTerm'),
    ('blackjackModule.py', '.'),
    ('blackjack.py', '.'),
    ('requirements.txt', '.'),
    ('LICENSE.md', '.'),
    ('README.md', '.'),
]

for src, dst in data_files:
    src_path = os.path.join(current_dir, src)
    if os.path.exists(src_path):
        datas.append((src_path, dst))
        print(f"Added to bundle: {src_path} -> {dst}")
    else:
        print(f"Warning: File not found: {src_path}")

# Add textual data files
if textual_datas:
    datas.extend(textual_datas)
    print(f"Added {len(textual_datas)} textual data files")

# Comprehensive hidden imports for standalone execution
hiddenimports = [
    # Core textual
    'textual',
    'textual.app',
    'textual.widgets',
    'textual.containers',
    'textual.screen',
    'textual.reactive',
    'textual.binding',
    'textual.css',
    'textual.driver',
    'textual._loop',
    'textual.geometry',
    'textual.color',
    'textual.design',
    'textual.strip',
    'textual.suggestion',
    'textual.filter',
    'textual.dom',
    'textual.css.query',
    'textual.css.parse',
    'textual.css.styles',
    'textual.css.tokenize',
    'textual.css.tokenizer',
    
    # Rich dependencies
    'rich',
    'rich.console',
    'rich.text',
    'rich.table',
    'rich.panel',
    'rich.align',
    'rich.layout',
    'rich.segment',
    'rich.style',
    'rich.color',
    'rich.markup',
    'rich.highlighter',
    'rich.protocol',
    'rich.measure',
    'rich.cells',
    'rich.region',
    'rich.repr',
    'rich._loop',
    'rich._wrap',
    'rich._extension',
    
    # System modules
    'typing_extensions',
    'importlib_metadata',
    'platform',
    'subprocess',
    'os',
    'sys',
    'pathlib',
    'asyncio',
    'threading',
    'time',
    'random',
    'json',
    'functools',
    'itertools',
    
    # Game modules
    'blackjackModule',
]

# Collect all textual and rich submodules
try:
    hiddenimports.extend(collect_submodules('textual'))
    hiddenimports.extend(collect_submodules('rich'))
    print(f"Collected submodules. Total hidden imports: {len(hiddenimports)}")
except Exception as e:
    print(f"Error collecting submodules: {e}")

# Define binaries with existence checks
binaries = []
binary_files = [
    ('WezTerm/wezterm.exe', 'WezTerm'),
    ('WezTerm/wezterm-gui.exe', 'WezTerm'),
    ('WezTerm/wezterm-mux-server.exe', 'WezTerm'),
    ('WezTerm/conpty.dll', 'WezTerm'),
    ('WezTerm/libEGL.dll', 'WezTerm'),
    ('WezTerm/libGLESv2.dll', 'WezTerm'),
    ('WezTerm/OpenConsole.exe', 'WezTerm'),
    ('WezTerm/strip-ansi-escapes.exe', 'WezTerm'),
    ('WezTerm/wezterm.pdb', 'WezTerm'),
    ('WezTerm/mesa/opengl32.dll', 'WezTerm/mesa'),
]

for src, dst in binary_files:
    src_path = os.path.join(current_dir, src)
    if os.path.exists(src_path):
        binaries.append((src_path, dst))
        print(f"Added binary: {src_path} -> {dst}")
    else:
        print(f"Warning: Binary not found: {src_path}")

print(f"\nFinal summary:")
print(f"Data files: {len(datas)}")
print(f"Binaries: {len(binaries)}")
print(f"Hidden imports: {len(hiddenimports)}")

a = Analysis(
    ['main.py'],
    pathex=[current_dir],
    binaries=binaries,
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=None,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=None)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='BlackjackGame',
    debug=True,  # Enable debug mode for better error messages
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    console=True,  # Keep console for debug output
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=False,
    upx_exclude=[],
    name='BlackjackGame',
)
