#!/usr/bin/env python3
"""
调试资源路径问题
"""

import os
import sys

def debug_paths():
    """调试各种路径情况"""
    print("=== 资源路径调试信息 ===")
    
    # 当前工作目录
    cwd = os.getcwd()
    print(f"当前工作目录: {cwd}")
    
    # 脚本所在目录
    script_dir = os.path.dirname(os.path.abspath(__file__))
    print(f"脚本所在目录: {script_dir}")
    
    # 检查PyInstaller环境
    try:
        base_path = sys._MEIPASS
        print(f"PyInstaller临时目录: {base_path}")
        is_packed = True
    except AttributeError:
        base_path = os.path.abspath(".")
        print("开发环境，使用当前目录")
        is_packed = False
    
    # 检查各种资源文件
    resources_to_check = [
        "images/ship.bmp",
        "images/alien.bmp", 
        "images/background.bmp",
        "sounds/shoot.wav",
        "sounds/explosion.wav",
        "sounds/BGM.mp3",
        "leaderboard.json"
    ]
    
    print("\n=== 资源文件检查 ===")
    for resource in resources_to_check:
        # 开发环境路径
        dev_path = os.path.join(os.path.abspath("."), resource)
        
        # 打包环境路径  
        packed_path = os.path.join(base_path, resource) if is_packed else dev_path
        
        # 检查是否存在
        dev_exists = os.path.exists(dev_path)
        packed_exists = os.path.exists(packed_path)
        
        print(f"\n{resource}:")
        print(f"  开发路径: {dev_path} -> {'✅' if dev_exists else '❌'}")
        if is_packed:
            print(f"  打包路径: {packed_path} -> {'✅' if packed_exists else '❌'}")
        
        # 如果使用resource_manager.py，它会返回什么路径
        try:
            # 模拟resource_manager的逻辑
            test_base = sys._MEIPASS if is_packed else os.path.abspath(".")
            manager_path = os.path.join(test_base, resource)
            manager_exists = os.path.exists(manager_path)
            print(f"  管理器路径: {manager_path} -> {'✅' if manager_exists else '❌'}")
        except:
            pass

if __name__ == '__main__':
    debug_paths()
    input("\n按任意键退出...")