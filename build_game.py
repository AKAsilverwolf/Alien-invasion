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
    """主打包函数"""
    print("🔧 开始打包外星人入侵游戏...")
    print("=" * 50)
    
    # 清理旧文件
    print("📦 清理旧文件...")
    if os.path.exists("dist"):
        shutil.rmtree("dist")
    if os.path.exists("build"):
        shutil.rmtree("build")
    
    # 检查主程序文件
    if not os.path.exists("alien_invasion.py"):
        print("❌ 错误: 未找到主程序文件 alien_invasion.py")
        return False
    
    # 检查资源文件夹
    required_dirs = ["images", "sounds"]
    for dir_name in required_dirs:
        if not os.path.exists(dir_name):
            print(f"❌ 错误: 未找到 {dir_name} 文件夹")
            return False
    
    # 打包命令
    cmd = [
        "pyinstaller",
        "--onefile",
        "--windowed",
        "--add-data", "images;images",
        "--add-data", "sounds;sounds",
        "--add-data", "leaderboard.json;.",
        "--name", "AlienInvasion",
        "alien_invasion.py"
    ]
    
    print("📝 执行打包命令...")
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
        
        if result.returncode == 0:
            print("✅ 打包成功!")
            
            # 检查生成的文件
            exe_path = "dist/AlienInvasion.exe"
            if os.path.exists(exe_path):
                file_size = os.path.getsize(exe_path)
                print(f"📁 文件位置: {exe_path}")
                print(f"📏 文件大小: {file_size:,} 字节 ({file_size/1024/1024:.1f} MB)")
                return True
            else:
                print("❌ 未找到生成的可执行文件")
                return False
        else:
            print("❌ 打包失败!")
            print("错误信息:")
            print(result.stderr)
            return False
            
    except Exception as e:
        print(f"❌ 打包过程中出现异常: {e}")
        return False

if __name__ == "__main__":
    success = main()
    if success:
        print("\n🎉 游戏打包完成!")
        print("💡 运行方法:")
        print("   1. 进入 dist 文件夹")
        print("   2. 双击 AlienInvasion.exe")
        print("\n📤 或者运行 create_portable.bat 创建便携版")
    else:
        print("\n💥 打包失败，请检查错误信息")
    
    input("\n按回车键退出...")