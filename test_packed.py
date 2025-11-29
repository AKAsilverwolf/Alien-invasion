#!/usr/bin/env python3
"""
模拟打包环境测试音效
"""

import sys
import os

# 模拟PyInstaller环境
if '_MEIPASS' not in dir(sys):
    sys._MEIPASS = os.path.join(os.getcwd(), 'temp_packed_dir')

print("=== 模拟打包环境测试 ===")
print(f"模拟的临时目录: {sys._MEIPASS}")

# 创建模拟的临时目录结构
temp_dir = sys._MEIPASS
os.makedirs(os.path.join(temp_dir, 'images'), exist_ok=True)
os.makedirs(os.path.join(temp_dir, 'sounds'), exist_ok=True)

# 复制文件到临时目录
import shutil
files_to_copy = [
    ('images/ship.bmp', 'images/ship.bmp'),
    ('images/alien.bmp', 'images/alien.bmp'),
    ('sounds/shoot.wav', 'sounds/shoot.wav'),
    ('sounds/explosion.wav', 'sounds/explosion.wav'),
    ('sounds/BGM.mp3', 'sounds/BGM.mp3')
]

for src, dst in files_to_copy:
    if os.path.exists(src):
        shutil.copy2(src, os.path.join(temp_dir, dst))
        print(f"✅ 复制 {src} -> {dst}")
    else:
        print(f"❌ 缺少 {src}")

print(f"\n临时目录结构:")
for root, dirs, files in os.walk(temp_dir):
    level = root.replace(temp_dir, '').count(os.sep)
    indent = ' ' * 2 * level
    print(f"{indent}{os.path.basename(root)}/")
    subindent = ' ' * 2 * (level + 1)
    for file in files:
        print(f"{subindent}{file}")

# 现在测试resource_manager
from resource_manager import get_sound_path, get_image_path

print(f"\n=== 使用resource_manager测试 ===")
paths_to_test = [
    ('shoot.wav', get_sound_path('shoot.wav')),
    ('explosion.wav', get_sound_path('explosion.wav')),
    ('BGM.mp3', get_sound_path('BGM.mp3')),
    ('ship.bmp', get_image_path('ship.bmp')),
    ('alien.bmp', get_image_path('alien.bmp'))
]

for name, path in paths_to_test:
    exists = os.path.exists(path)
    print(f"{name}: {path} -> {'✅' if exists else '❌'}")

# 测试pygame加载
try:
    import pygame
    pygame.mixer.init()
    
    shoot_path = get_sound_path('shoot.wav')
    if os.path.exists(shoot_path):
        sound = pygame.mixer.Sound(shoot_path)
        sound.play()
        print("✅ 音效加载并播放成功")
    else:
        print("❌ 音效文件不存在")
        
except Exception as e:
    print(f"❌ 音效加载失败: {e}")

# 清理临时目录
import time
time.sleep(2)
shutil.rmtree(temp_dir)
print(f"\n🗑️ 清理临时目录: {temp_dir}")