import pygame
import os
import numpy as np
from pygame import sndarray
from resource_manager import get_sound_path

class SoundManager:
    """管理游戏音效的类"""
    
    def __init__(self):
        """初始化音效管理器"""
        self.enabled = True
        self.music_enabled = True  # 背景音乐开关
        try:
            pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=512)
        except:
            print("警告：无法初始化音频系统")
            self.enabled = False
            self.music_enabled = False
            return
            
        self.sounds = {}
        self.create_sounds()
    
    def create_sounds(self):
        """创建或加载音效"""
        if not self.enabled:
            print("音频系统未启用，跳过音效加载")
            return
            
        try:
            # 尝试加载外部音效文件
            self.load_sound_files()
            print("🎵 音效加载成功!")
        except Exception as e:
            print(f"❌ 加载音效文件时出错: {e}")
            print("🔧 尝试生成程序化音效...")
            try:
                # 如果加载失败，则创建程序化音效
                self.create_programmed_sounds()
                print("🔧 程序化音效创建成功")
            except Exception as e2:
                print(f"💥 创建音效时出错: {e2}")
                self.enabled = False
    
    def load_sound_files(self):
        """加载外部音效文件"""
        print("开始加载音效文件...")
        
        # 加载射击音效
        try:
            shoot_path = get_sound_path('shoot.wav')
            print(f"尝试加载射击音效: {shoot_path}")
            if os.path.exists(shoot_path):
                self.sounds['shoot'] = pygame.mixer.Sound(shoot_path)
                print(f"✅ 射击音效加载成功")
            else:
                print(f"❌ 射击音效文件不存在: {shoot_path}")
                raise FileNotFoundError(f"射击音效文件未找到: {shoot_path}")
        except Exception as e:
            print(f"❌ 射击音效加载失败: {e}")
            raise
        
        # 加载爆炸音效
        try:
            explosion_path = get_sound_path('explosion.wav')
            print(f"尝试加载爆炸音效: {explosion_path}")
            if os.path.exists(explosion_path):
                self.sounds['explosion'] = pygame.mixer.Sound(explosion_path)
                print(f"✅ 爆炸音效加载成功")
            else:
                print(f"❌ 爆炸音效文件不存在: {explosion_path}")
                raise FileNotFoundError(f"爆炸音效文件未找到: {explosion_path}")
        except Exception as e:
            print(f"❌ 爆炸音效加载失败: {e}")
            raise
        
        # 生成游戏结束音效（因为没有对应的文件）
        try:
            self.create_game_over_sound()
            print(f"✅ 游戏结束音效创建成功")
        except Exception as e:
            print(f"❌ 游戏结束音效创建失败: {e}")
        
        # 加载背景音乐
        try:
            self.load_background_music()
            print(f"✅ 背景音乐加载完成")
        except Exception as e:
            print(f"❌ 背景音乐加载失败: {e}")
        
        print("所有音效加载完成!")

    def create_programmed_sounds(self):
        """创建程序化音效（备用方案）"""
        self.create_shoot_sound()
        self.create_explosion_sound()
        self.create_game_over_sound()

    def create_shoot_sound(self):
        """创建射击音效（备用方案）"""
        # 使用更简单的音效生成方法
        try:
            duration = 0.1  # 持续时间（秒）
            sample_rate = 22050
            samples = int(duration * sample_rate)
            
            # 生成音波数据
            waves = np.zeros((samples, 2), dtype=np.int16)
            for i in range(samples):
                t = float(i) / sample_rate
                # 使用多个频率创建更丰富的声音
                value = int(32767.0 * 0.3 * (
                    0.6 * np.sin(2 * np.pi * 200 * t) +
                    0.4 * np.sin(2 * np.pi * 400 * t)
                ) * (1 - t/duration))  # 淡出效果
                waves[i] = [value, value]
            
            # 创建声音对象
            sound = pygame.sndarray.make_sound(waves)
            self.sounds['shoot'] = sound
        except Exception as e:
            print(f"创建射击音效失败: {e}")
            # 创建一个简单的默认音效
            self.sounds['shoot'] = None
    
    def create_explosion_sound(self):
        """创建爆炸音效（备用方案）"""
        try:
            duration = 0.3
            sample_rate = 22050
            samples = int(duration * sample_rate)
            
            waves = np.zeros((samples, 2), dtype=np.int16)
            np.random.seed(42)
            
            for i in range(samples):
                t = float(i) / sample_rate
                # 创建噪音加上低频
                noise = np.random.uniform(-1, 1)
                low_freq = np.sin(2 * np.pi * 60 * t)
                value = int(32767.0 * 0.4 * (noise * 0.7 + low_freq * 0.3) * (1 - t/duration))
                waves[i] = [value, value]
            
            sound = pygame.sndarray.make_sound(waves)
            self.sounds['explosion'] = sound
        except Exception as e:
            print(f"创建爆炸音效失败: {e}")
            # 创建一个简单的默认音效
            self.sounds['explosion'] = None
    
    def create_game_over_sound(self):
        """创建游戏结束音效（备用方案）"""
        try:
            duration = 0.8
            sample_rate = 22050
            samples = int(duration * sample_rate)
            
            waves = np.zeros((samples, 2), dtype=np.int16)
            
            for i in range(samples):
                t = float(i) / sample_rate
                # 下降音调
                freq = 400 * (1 - t/duration)
                value = int(32767.0 * 0.3 * np.sin(2 * np.pi * freq * t))
                waves[i] = [value, value]
            
            sound = pygame.sndarray.make_sound(waves)
            self.sounds['game_over'] = sound
        except Exception as e:
            print(f"创建游戏结束音效失败: {e}")
            # 创建一个简单的默认音效
            self.sounds['game_over'] = None
    
    def play_shoot(self):
        """播放射击音效"""
        if self.enabled and 'shoot' in self.sounds:
            self.sounds['shoot'].play()
    
    def play_explosion(self):
        """播放爆炸音效"""
        if self.enabled and 'explosion' in self.sounds:
            self.sounds['explosion'].play()
    
    def play_game_over(self):
        """播放游戏结束音效"""
        if self.enabled and 'game_over' in self.sounds:
            self.sounds['game_over'].play()
    
    def load_background_music(self):
        """加载背景音乐"""
        if not self.enabled:
            return
            
        try:
            bgm_path = get_sound_path('BGM.mp3')
            
            if os.path.exists(bgm_path):
                pygame.mixer.music.load(bgm_path)
                print(f"加载背景音乐: {bgm_path}")
            else:
                print(f"背景音乐文件未找到: {bgm_path}")
                self.music_enabled = False
        except Exception as e:
            print(f"加载背景音乐时出错: {e}")
            self.music_enabled = False
    
    def play_background_music(self, loops=-1):
        """播放背景音乐
        
        Args:
            loops: 循环次数，-1表示无限循环
        """
        if self.enabled and self.music_enabled:
            try:
                pygame.mixer.music.play(loops)
                print("背景音乐开始播放")
            except Exception as e:
                print(f"播放背景音乐时出错: {e}")
    
    def stop_background_music(self):
        """停止背景音乐"""
        if self.enabled and self.music_enabled:
            pygame.mixer.music.stop()
            print("背景音乐停止")
    
    def pause_background_music(self):
        """暂停背景音乐"""
        if self.enabled and self.music_enabled:
            pygame.mixer.music.pause()
            print("背景音乐暂停")
    
    def unpause_background_music(self):
        """恢复背景音乐播放"""
        if self.enabled and self.music_enabled:
            pygame.mixer.music.unpause()
            print("背景音乐恢复")
    
    def set_music_volume(self, volume):
        """设置背景音乐音量
        
        Args:
            volume: 音量值 (0.0 到 1.0)
        """
        if self.enabled and self.music_enabled:
            pygame.mixer.music.set_volume(max(0.0, min(1.0, volume)))
    
    def stop_all(self):
        """停止所有音效"""
        if self.enabled:
            pygame.mixer.stop()
            pygame.mixer.music.stop()