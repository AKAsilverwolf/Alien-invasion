import pygame
import os
import sys
import numpy as np
from pygame import sndarray

class SoundManager:
    def __init__(self):
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
        try:
            base_path = sys._MEIPASS
            full_path = os.path.join(base_path, relative_path)
            if os.path.exists(full_path):
                print(f"使用PyInstaller路径: {full_path}")
                return full_path
        except:
            pass
        
        try:
            if getattr(sys, 'frozen', False):
                exe_dir = os.path.dirname(sys.executable)
                full_path = os.path.join(exe_dir, relative_path)
                if os.path.exists(full_path):
                    print(f"使用EXE目录路径: {full_path}")
                    return full_path
        except:
            pass
        
        full_path = os.path.abspath(relative_path)
        print(f"使用当前目录路径: {full_path}")
        return full_path
    
    def create_sounds(self):
        if not self.enabled:
            return
        
        print("开始加载音效...")
        
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
        
        # 背景音乐
        try:
            bgm_path = self.get_resource_path(os.path.join('sounds', 'BGM.mp3'))
            if os.path.exists(bgm_path):
                pygame.mixer.music.load(bgm_path)
                print("✅ 背景音乐加载成功")
            else:
                print(f"❌ 背景音乐文件不存在: {bgm_path}")
                self.music_enabled = False
        except Exception as e:
            print(f"❌ 背景音乐加载失败: {e}")
            self.music_enabled = False
        
        # 游戏结束音效
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
            print("✅ 游戏结束音效创建成功")
        except Exception as e:
            print(f"❌ 游戏结束音效创建失败: {e}")
    
    def play_shoot(self):
        if self.enabled and 'shoot' in self.sounds and self.sounds['shoot']:
            try:
                self.sounds['shoot'].play()
            except:
                pass
    
    def play_explosion(self):
        if self.enabled and 'explosion' in self.sounds and self.sounds['explosion']:
            try:
                self.sounds['explosion'].play()
            except:
                pass
    
    def play_game_over(self):
        if self.enabled and 'game_over' in self.sounds and self.sounds['game_over']:
            try:
                self.sounds['game_over'].play()
            except:
                pass
    
    def play_background_music(self, loops=-1):
        if self.enabled and self.music_enabled:
            try:
                pygame.mixer.music.play(loops)
            except:
                pass
    
    def stop_background_music(self):
        if self.enabled and self.music_enabled:
            try:
                pygame.mixer.music.stop()
            except:
                pass
    
    def pause_background_music(self):
        if self.enabled and self.music_enabled:
            try:
                pygame.mixer.music.pause()
            except:
                pass
    
    def unpause_background_music(self):
        if self.enabled and self.music_enabled:
            try:
                pygame.mixer.music.unpause()
            except:
                pass
    
    def stop_all(self):
        if self.enabled:
            try:
                pygame.mixer.stop()
                pygame.mixer.music.stop()
            except:
                pass