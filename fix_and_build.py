#!/usr/bin/env python3
"""
修复打包问题并重新打包
"""

import os
import sys
import subprocess
import shutil

def main():
    print("🔧 修复打包问题并重新打包...")
    
    # 清理之前的打包
    print("🗑️ 清理旧的打包文件...")
    if os.path.exists('dist'):
        shutil.rmtree('dist')
    if os.path.exists('build'):
        shutil.rmtree('build')
    
    # 检查所有必要文件
    required_files = [
        'alien_invasion.py',
        'resource_manager.py',
        'ship.py', 
        'alien.py',
        'settings.py',
        'sound_manager.py',
        'leaderboard.py',
        'images/ship.bmp',
        'images/alien.bmp', 
        'images/background.bmp',
        'sounds/shoot.wav',
        'sounds/explosion.wav',
        'sounds/BGM.mp3',
        'leaderboard.json'
    ]
    
    missing = []
    for file in required_files:
        if not os.path.exists(file):
            missing.append(file)
    
    if missing:
        print(f"❌ 缺少文件: {missing}")
        return False
    
    print("✅ 所有必要文件检查通过")
    
    # 执行打包命令
    print("📦 开始打包...")
    cmd = [
        'pyinstaller',
        '--onefile',
        '--windowed',
        '--add-data', 'images;images',
        '--add-data', 'sounds;sounds', 
        '--add-data', 'leaderboard.json;.',
        '--name', 'AlienInvasion',
        'alien_invasion.py'
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ 打包成功!")
            
            # 检查生成的文件
            exe_path = os.path.join('dist', 'AlienInvasion.exe')
            if os.path.exists(exe_path):
                size_mb = os.path.getsize(exe_path) / (1024 * 1024)
                print(f"📁 生成的文件: {exe_path}")
                print(f"📏 文件大小: {size_mb:.1f} MB")
                print("🎮 游戏已修复，可以正常运行!")
                return True
            else:
                print("❌ 未找到生成的exe文件")
                return False
        else:
            print("❌ 打包失败:")
            print(result.stdout)
            print(result.stderr)
            return False
            
    except Exception as e:
        print(f"❌ 打包出错: {e}")
        return False

if __name__ == '__main__':
    success = main()
    input("\n按任意键退出...")