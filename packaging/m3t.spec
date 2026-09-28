# -*- mode: python ; coding: utf-8 -*-
# PyInstaller spec for AIOps Cockpit
# Build with:
#   pip install pyinstaller
#   pyinstaller packaging/m3t.spec --clean --noconfirm
# (Run on Windows for .exe output. macOS/Linux can build for testing only.)

from PyInstaller.utils.hooks import collect_submodules

block_cipher = None

a = Analysis(
    ['../aiops_cockpit/__main__.py'],
    pathex=['.'],
    binaries=[],
    datas=[],
    hiddenimports=collect_submodules('aiops_cockpit'),
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='aiops-cockpit',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_redirector=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=None,
)
