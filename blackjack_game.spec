# -*- mode: python ; coding: utf-8 -*-
import os
from PyInstaller.utils.hooks import collect_data_files, collect_submodules

# Get the current directory
current_dir = os.getcwd()

# Collect all textual data files
textual_datas = collect_data_files('textual')

# Define data files to include
datas = [
    (os.path.join(current_dir, 'tcss'), 'tcss'),
    (os.path.join(current_dir, 'WezTerm'), 'WezTerm'),
    (os.path.join(current_dir, 'blackjackModule.py'), '.'),
    (os.path.join(current_dir, 'blackjack.py'), '.'),
    (os.path.join(current_dir, 'README.md'), '.'),
]

# Add textual data files
datas.extend(textual_datas)

# Hidden imports for all dependencies
hiddenimports = [
    'textual',
    'textual.app',
    'textual.widgets',
    'textual.containers',
    'textual.screen',
    'textual.reactive',
    'textual.binding',
    'textual.css',
    'blackjackModule',
    'rich',
    'rich.console',
    'rich.text',
    'rich.table',
    'rich.panel',
    'rich.align',
    'rich.layout',
    'typing_extensions',
    'importlib_metadata',
]

# Collect all textual submodules
hiddenimports.extend(collect_submodules('textual'))

a = Analysis(
    ['main.py'],
    pathex=[current_dir],
    binaries=[
        (os.path.join(current_dir, 'WezTerm', 'wezterm.exe'), 'WezTerm'),
        (os.path.join(current_dir, 'WezTerm', 'wezterm-gui.exe'), 'WezTerm'),
        (os.path.join(current_dir, 'WezTerm', 'wezterm-mux-server.exe'), 'WezTerm'),
        (os.path.join(current_dir, 'WezTerm', 'conpty.dll'), 'WezTerm'),
        (os.path.join(current_dir, 'WezTerm', 'libEGL.dll'), 'WezTerm'),
        (os.path.join(current_dir, 'WezTerm', 'libGLESv2.dll'), 'WezTerm'),
        (os.path.join(current_dir, 'WezTerm', 'OpenConsole.exe'), 'WezTerm'),
        (os.path.join(current_dir, 'WezTerm', 'strip-ansi-escapes.exe'), 'WezTerm'),
        (os.path.join(current_dir, 'WezTerm', 'wezterm.pdb'), 'WezTerm'),
        (os.path.join(current_dir, 'WezTerm', 'mesa', 'opengl32.dll'), 'WezTerm/mesa'),
    ],
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
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    console=True,
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
