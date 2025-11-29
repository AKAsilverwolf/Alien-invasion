#!/usr/bin/env python3
"""
最终音效修复方案
"""

import os
import sys

def create_fixed_sound_manager():
    """创建修复版的音效管理器"""
    
    # 创建一个新的sound_manager_fixed.py
    fixed_content = '''import pygame
import os
import numpy as np
from pygame import sndarray

class SoundManager:
    """管理游戏音效的类"""
    
    def __init__(self):
        """初始化音效管理器"""
        self.enabled = True
        self.music_enabled = True
        
        try:
            pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=512)
        except:
            print("警告：无法初始化音频系统")
            self.enabled = False
            self.music_enabled = False
            return
            
        self.sounds = {}
        self.create_sounds()
    
    def get_resource_path(self, relative_path):
        """获取资源路径 - 多重保险方案"""
        # 方案1: PyInstaller临时目录
        try:
            base_path = sys._MEIPASS
            full_path = os.path.join(base_path, relative_path)
            if os.path.exists(full_path):
                print(f"使用PyInstaller路径: {full_path}")
                return full_path
        except:
            pass
        
        # 方案2: 相对于exe文件的位置
        try:
            if getattr(sys, 'frozen', False):
                exe_dir = os.path.dirname(sys.executable)
                full_path = os.path.join(exe_dir, relative_path)
                if os.path.exists(full_path):
                    print(f"使用EXE目录路径: {full_path}")
                    return full_path
        except:
            pass
        
        # 方案3: 当前工作目录
        full_path = os.path.abspath(relative_path)
        if os.path.exists(full_path):
            print(f"使用当前目录路径: {full_path}")
            return full_path
        
        # 方案4: 当前文件所在目录
        script_dir = os.path.dirname(os.path.abspath(__file__))
        full_path = os.path.join(script_dir, relative_path)
        print(f"使用脚本目录路径: {full_path}")
        return full_path
    
    def create_sounds(self):
        """创建或加载音效"""
        if not self.enabled:
            return
        
        print("🔊 开始加载音效...")
        
        # 射击音效
        try:
            shoot_path = self.get_resource_path(os.path.join('sounds', 'shoot.wav'))
            if os.path.exists(shoot_path):
                self.sounds['shoot'] = pygame.mixer.Sound(shoot_path)
                print("✅ 射击音效加载成功")
            else:
                print(f"❌ 射击音效文件不存在: {shoot_path}")
        except Exception as e:
            print(f"❌ 射击音效加载失败: {e}")
        
        # 爆炸音效
        try:
            explosion_path = self.get_resource_path(os.path.join('sounds', 'explosion.wav'))
            if os.path.exists(explosion_path):
                self.sounds['explosion'] = pygame.mixer.Sound(explosion_path)
                print("✅ 爆炸音效加载成功")
            else:
                print(f"❌ 爆炸音效文件不存在: {explosion_path}")
        except Exception as e:
            print(f"❌ 爆炸音效加载失败: {e}")
        
        # 游戏结束音效
        try:
            self.create_game_over_sound()
            print("✅ 游戏结束音效创建成功")
        except Exception as e:
            print(f"❌ 游戏结束音效创建失败: {e}")
        
        # 背景音乐
        try:
            self.load_background_music()
            print("✅ 背景音乐加载成功")
        except Exception as e:
            print(f"❌ 背景音乐加载失败: {e}")
        
        print("🎵 音效加载完成!")
    
    def load_background_music(self):
        """加载背景音乐"""
        if not self.enabled:
            return
            
        bgm_path = self.get_resource_path(os.path.join('sounds', 'BGM.mp3'))
        
        if os.path.exists(bgm_path):
            pygame.mixer.music.load(bgm_path)
            print(f"✅ 背景音乐加载: {bgm_path}")
        else:
            print(f"❌ 背景音乐文件不存在: {bgm_path}")
            self.music_enabled = False
    
    def create_game_over_sound(self):
        """创建游戏结束音效"""
        try:
            duration = 0.8
            sample_rate = 22050
            samples = int(duration * sample_rate)
            
            waves = np.zeros((samples, 2), dtype=np.int16)
            
            for i in range(samples):
                t = float(i) / sample_rate
                freq = 400 * (1 - t/duration)
                value = int(32767.0 * 0.3 * np.sin(2 * np.pi * freq * t))
                waves[i] = [value, value]
            
            sound = pygame.sndarray.make_sound(waves)
            self.sounds['game_over'] = sound
        except Exception as e:
            print(f"创建游戏结束音效失败: {e}")
            self.sounds['game_over'] = None
    
    def play_shoot(self):
        """播放射击音效"""
        if self.enabled and 'shoot' in self.sounds and self.sounds['shoot']:
            try:
                self.sounds['shoot'].play()
            except:
                pass
    
    def play_explosion(self):
        """播放爆炸音效"""
        if self.enabled and 'explosion' in self.sounds and self.sounds['explosion']:
            try:
                self.sounds['explosion'].play()
            except:
                pass
    
    def play_game_over(self):
        """播放游戏结束音效"""
        if self.enabled and 'game_over' in self.sounds and self.sounds['game_over']:
            try:
                self.sounds['game_over'].play()
            except:
                pass
    
    def play_background_music(self, loops=-1):
        """播放背景音乐"""
        if self.enabled and self.music_enabled:
            try:
                pygame.mixer.music.play(loops)
            except:
                pass
    
    def stop_background_music(self):
        """停止背景音乐"""
        if self.enabled and self.music_enabled:
            try:
                pygame.mixer.music.stop()
            except:
                pass
    
    def pause_background_music(self):
        """暂停背景音乐"""
        if self.enabled and self.music_enabled:
            try:
                pygame.mixer.music.pause()
            except:
                pass
    
    def unpause_background_music(self):
        """恢复背景音乐播放"""
        if self.enabled and self.music_enabled:
            try:
                pygame.mixer.music.unpause()
            except:
                pass
    
    def stop_all(self):
        """停止所有音效"""
        if self.enabled:
            try:
                pygame.mixer.stop()
                pygame.mixer.music.stop()
            except:
                pass
'''
    
    with open('sound_manager_fixed.py', 'w', encoding='utf-8') as f:
        f.write(fixed_content)
    
    print("🔧 创建修复版音效管理器: sound_manager_fixed.py")

def update_main_file():
    """更新主文件使用修复版音效管理器"""
    
    try:
        with open('alien_invasion.py', 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 替换导入语句
        content = content.replace('from sound_manager import SoundManager', 
                             'from sound_manager_fixed import SoundManager')
        
        with open('alien_invasion_fixed.py', 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("📝 创建修复版主文件: alien_invasion_fixed.py")
        return True
        
    except Exception as e:
        print(f"❌ 更新主文件失败: {e}")
        return False

def create_build_command():
    """创建打包命令"""
    print("📦 准备修复版打包...")
    
    # 创建简化的build命令
    build_script = '''
@echo off
echo 🔧 开始修复版打包...
echo.

rem 清理旧文件
if exist dist rmdir /s /q dist
if exist build rmdir /s /q build

echo 📦 使用修复版主程序打包...
pyinstaller --onefile --windowed --add-data "images;images" --add-data "sounds;sounds" --add-data "leaderboard.json;." --name "AlienInvasion" alien_invasion_fixed.py

echo.
echo 🎉 打包完成!
echo 📁 文件位置: dist\\AlienInvasion.exe
echo.
echo 💡 测试建议:
echo    1. 双击运行 AlienInvasion.exe
echo    2. 测试音效: 空格键(射击), 击中敌人(爆炸)
echo    3. 测试音乐: 应该自动播放, M键控制
echo.
pause
'''
    
    with open('build_fixed.bat', 'w', encoding='gbk') as f:
        f.write(build_script)
    
    print("📄 创建打包脚本: build_fixed.bat")

def main():
    print("🔧 最终音效修复方案")
    print("=" * 50)
    
    # 步骤1: 创建修复版文件
    create_fixed_sound_manager()
    
    # 步骤2: 更新主文件
    if not update_main_file():
        print("❌ 修复失败")
        return False
    
    # 步骤3: 创建打包脚本
    create_build_command()
    
    print("\n🎯 修复方案创建完成!")
    print("📋 接下来的步骤:")
    print("   1. 运行 build_fixed.bat")
    print("   2. 测试 dist/AlienInvasion.exe")
    print("   3. 验证音效功能")
    
    return True

if __name__ == '__main__':
    main()
    input("\n按任意键退出...")