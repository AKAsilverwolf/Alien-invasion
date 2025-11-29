#!/usr/bin/env python3
"""
测试音效加载
"""

import pygame
import sys
import os
from resource_manager import get_sound_path

def test_sound_loading():
    """测试音效加载"""
    print("=== 音效加载测试 ===")
    
    # 初始化音频
    try:
        pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=512)
        print("✅ 音频系统初始化成功")
    except Exception as e:
        print(f"❌ 音频系统初始化失败: {e}")
        return
    
    # 测试各个音效文件
    sounds_to_test = [
        ('shoot.wav', '射击音效'),
        ('explosion.wav', '爆炸音效'),
        ('BGM.mp3', '背景音乐')
    ]
    
    for sound_file, description in sounds_to_test:
        path = get_sound_path(sound_file)
        print(f"\n测试 {description}:")
        print(f"  文件路径: {path}")
        print(f"  文件存在: {'✅' if os.path.exists(path) else '❌'}")
        
        if os.path.exists(path):
            try:
                if sound_file.endswith('.mp3'):
                    # 背景音乐
                    pygame.mixer.music.load(path)
                    print(f"  加载结果: ✅ 背景音乐加载成功")
                else:
                    # 普通音效
                    sound = pygame.mixer.Sound(path)
                    print(f"  加载结果: ✅ 音效加载成功")
                    
                    # 测试播放
                    sound.play()
                    print(f"  测试播放: ✅ 播放成功")
                    
            except Exception as e:
                print(f"  加载结果: ❌ 加载失败 - {e}")

if __name__ == '__main__':
    test_sound_loading()
    input("\n按任意键退出...")