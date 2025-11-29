#!/usr/bin/env python3
"""
外星人入侵游戏打包脚本
运行此脚本将自动打包游戏为可执行文件
"""

import os
import sys
import subprocess
import shutil

def main():
    print("🚀 开始打包外星人入侵游戏...")
    
    # 检查PyInstaller是否安装
    try:
        import PyInstaller
        print("✅ PyInstaller已安装")
    except ImportError:
        print("❌ PyInstaller未安装，正在安装...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
        print("✅ PyInstaller安装完成")
    
    # 检查必要文件
    required_files = [
        'alien_invasion.py',
        'images',
        'sounds',
        'leaderboard.json',
        'sound_manager.py',
        'game_functions.py',
        'ship.py',
        'alien.py',
        'bullet.py',
        'settings.py',
        'game_stats.py',
        'scoreboard.py',
        'button.py',
        'leaderboard.py',
        'name_input.py',
        'resource_manager.py'  # 新增资源管理器
    ]
    
    missing_files = []
    for file in required_files:
        if not os.path.exists(file):
            missing_files.append(file)
    
    if missing_files:
        print(f"❌ 缺少必要文件: {missing_files}")
        return False
    
    print("✅ 所有必要文件检查通过")
    
    # 检查BGM文件
    bgm_path = os.path.join('sounds', 'BGM.mp3')
    if not os.path.exists(bgm_path):
        print(f"⚠️ 警告: 背景音乐文件未找到: {bgm_path}")
    else:
        print("✅ 背景音乐文件检查通过")
    
    # 清理之前的打包
    if os.path.exists('dist'):
        shutil.rmtree('dist')
        print("🗑️ 清理旧的打包文件")
    
    if os.path.exists('build'):
        shutil.rmtree('build')
        print("🗑️ 清理构建缓存")
    
    # 打包命令
    cmd = [
        'pyinstaller',
        '--onefile',           # 打包为单个exe文件
        '--windowed',          # 无控制台窗口
        '--add-data', 'images;images',  # 包含图像文件
        '--add-data', 'sounds;sounds',  # 包含音效文件
        '--add-data', 'leaderboard.json;.',  # 包含排行榜数据
        '--name', 'AlienInvasion',  # 可执行文件名
        '--clean',             # 清理临时文件
        'alien_invasion.py'
    ]
    
    print(f"📦 执行打包命令: {' '.join(cmd)}")
    
    try:
        subprocess.check_call(cmd)
        print("✅ 打包完成！")
        
        # 检查生成的文件
        exe_path = os.path.join('dist', 'AlienInvasion.exe')
        if os.path.exists(exe_path):
            size_mb = os.path.getsize(exe_path) / (1024 * 1024)
            print(f"📁 生成的可执行文件: {exe_path}")
            print(f"📏 文件大小: {size_mb:.1f} MB")
            print("🎮 你现在可以运行 AlienInvasion.exe 来玩游戏了！")
            return True
        else:
            print("❌ 打包失败，未找到可执行文件")
            return False
            
    except subprocess.CalledProcessError as e:
        print(f"❌ 打包失败: {e}")
        return False
    except Exception as e:
        print(f"❌ 发生错误: {e}")
        return False

if __name__ == '__main__':
    success = main()
    if success:
        print("\n🎉 游戏打包成功！")
        print("💡 提示:")
        print("   - 可执行文件位于 dist/AlienInvasion.exe")
        print("   - 可以将此文件复制到其他Windows电脑运行")
        print("   - 不需要安装Python或Pygame即可运行")
    else:
        print("\n💔 打包失败，请检查错误信息")
        print("💡 解决方案:")
        print("   - 确保所有必要文件都在正确位置")
        print("   - 检查Python和依赖包是否正确安装")
        print("   - 尝试手动运行: pyinstaller --onefile --windowed alien_invasion.py")
    
    input("\n按任意键退出...")