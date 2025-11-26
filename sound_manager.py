import pygame
import os

class SoundManager:
    """管理游戏音效的类"""
    
    def __init__(self):
        """初始化音效管理器"""
        self.enabled = True
        try:
            pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=512)
        except:
            print("警告：无法初始化音频系统")
            self.enabled = False
            return
            
        self.sounds = {}
        self.create_sounds()
    
    def create_sounds(self):
        """创建简单的音效"""
        if not self.enabled:
            return
            
        try:
            # 创建射击音效
            self.create_shoot_sound()
            # 创建爆炸音效
            self.create_explosion_sound()
            # 创建游戏结束音效
            self.create_game_over_sound()
            print("音效创建成功")
        except Exception as e:
            print(f"创建音效时出错: {e}")
            self.enabled = False
    
    def create_shoot_sound(self):
        """创建射击音效"""
        # 创建一个简单的射击声
        duration = 0.1  # 持续时间（秒）
        sample_rate = 22050
        samples = int(duration * sample_rate)
        
        # 生成音波数据
        waves = []
        for i in range(samples):
            t = float(i) / sample_rate
            # 使用多个频率创建更丰富的声音
            value = (int(32767.0 * 0.3 * (
                0.6 * pygame.math.Vector2(0, 1).rotate(360 * 200 * t).y +
                0.4 * pygame.math.Vector2(0, 1).rotate(360 * 400 * t).y
            )) * (1 - t/duration))  # 淡出效果
            waves.append([value, value])
        
        # 创建声音对象
        sound = pygame.sndarray.make_sound(waves)
        self.sounds['shoot'] = sound
    
    def create_explosion_sound(self):
        """创建爆炸音效"""
        duration = 0.3
        sample_rate = 22050
        samples = int(duration * sample_rate)
        
        waves = []
        import random
        random.seed(42)
        
        for i in range(samples):
            t = float(i) / sample_rate
            # 创建噪音加上低频
            noise = random.uniform(-1, 1)
            low_freq = pygame.math.Vector2(0, 1).rotate(360 * 60 * t).y
            value = int(32767.0 * 0.4 * (noise * 0.7 + low_freq * 0.3) * (1 - t/duration))
            waves.append([value, value])
        
        sound = pygame.sndarray.make_sound(waves)
        self.sounds['explosion'] = sound
    
    def create_game_over_sound(self):
        """创建游戏结束音效"""
        duration = 0.8
        sample_rate = 22050
        samples = int(duration * sample_rate)
        
        waves = []
        
        for i in range(samples):
            t = float(i) / sample_rate
            # 下降音调
            freq = 400 * (1 - t/duration)
            value = int(32767.0 * 0.3 * pygame.math.Vector2(0, 1).rotate(360 * freq * t).y)
            waves.append([value, value])
        
        sound = pygame.sndarray.make_sound(waves)
        self.sounds['game_over'] = sound
    
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
    
    def stop_all(self):
        """停止所有音效"""
        if self.enabled:
            pygame.mixer.stop()