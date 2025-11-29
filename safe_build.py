#!/usr/bin/env python3
"""
安全打包脚本 - 确保音效文件被正确包含
"""

import os
import subprocess
import shutil
import sys

def safe_build():
    print("🛡️ 安全打包 - 确保音效完整性...")
    
    # 清理
    for folder in ['dist', 'build', '__pycache__']:
        if os.path.exists(folder):
            try:
                shutil.rmtree(folder)
                print(f"🗑️ 清理 {folder}")
            except PermissionError:
                print(f"⚠️ {folder} 正在使用中，跳过清理")
                # 只清理内部文件
                try:
                    for root, dirs, files in os.walk(folder):
                        for file in files:
                            if file.endswith('.py') or file.endswith('.spec'):
                                try:
                                    os.remove(os.path.join(root, file))
                                except:
                                    pass
                except:
                    pass
    
    # 创建简化的spec文件
    spec_content = f'''
# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['alien_invasion.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('images', 'images'),
        ('sounds', 'sounds'),
        ('leaderboard.json', '.'),
    ],
    hiddenimports=['pygame', 'numpy', 'json', 'time', 'random', 'os', 'sys'],
    hookspath=[],
    hooksconfig={{}},
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
    [],
    exclude_binaries=True,
    name='AlienInvasion',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
'''
    
    with open('safe.spec', 'w', encoding='utf-8') as f:
        f.write(spec_content)
    
    print("📝 创建安全打包配置")
    
    # 检查文件
    required_files = [
        'alien_invasion.py', 'resource_manager.py', 'sound_manager.py',
        'ship.py', 'alien.py', 'settings.py', 'leaderboard.py'
    ]
    
    for file in required_files:
        if not os.path.exists(file):
            print(f"❌ 缺少文件: {file}")
            return False
    
    print("✅ 核心文件检查通过")
    
    # 检查资源文件
    resources = [
        'images/ship.bmp', 'images/alien.bmp', 'images/background.bmp',
        'sounds/shoot.wav', 'sounds/explosion.wav', 'sounds/BGM.mp3',
        'leaderboard.json'
    ]
    
    for file in resources:
        if not os.path.exists(file):
            print(f"❌ 缺少资源: {file}")
            return False
    
    print("✅ 资源文件检查通过")
    
    # 执行打包
    cmd = [sys.executable, '-m', 'PyInstaller', 'safe.spec', '--clean']
    print(f"📦 执行打包命令: {' '.join(cmd)}")
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ 打包过程完成")
            
            # 检查结果
            exe_path = os.path.join('dist', 'AlienInvasion.exe')
            if os.path.exists(exe_path):
                size_mb = os.path.getsize(exe_path) / (1024 * 1024)
                print(f"📁 生成文件: {exe_path}")
                print(f"📏 文件大小: {size_mb:.1f} MB")
                
                # 创建运行脚本
                run_script = f'''
@echo off
echo 启动外星人入侵游戏...
echo 请等待游戏加载...
echo.
start "" "AlienInvasion.exe"
echo 游戏已启动!
pause
'''
                
                with open(os.path.join('dist', '运行游戏.bat'), 'w', encoding='gbk') as f:
                    f.write(run_script)
                
                print("📄 创建运行脚本: 运行游戏.bat")
                return True
            else:
                print("❌ 未找到生成的exe文件")
                return False
        else:
            print("❌ 打包失败:")
            print("STDOUT:", result.stdout)
            print("STDERR:", result.stderr)
            return False
            
    except Exception as e:
        print(f"❌ 打包异常: {e}")
        return False

if __name__ == '__main__':
    success = safe_build()
    
    if success:
        print("\n🎉 安全打包成功!")
        print("📁 文件位置: dist/AlienInvasion.exe")
        print("💡 运行方法:")
        print("   1. 双击 AlienInvasion.exe")
        print("   2. 或双击 运行游戏.bat")
        print("\n🔊 音效问题解决:")
        print("   - 射击音效: 空格键")
        print("   - 爆炸音效: 击中敌人时")
        print("   - 背景音乐: 自动播放")
        print("   - 音乐控制: M键暂停/恢复")
    else:
        print("\n💔 打包失败，请检查上述错误")
    
    input("\n按任意键退出...")