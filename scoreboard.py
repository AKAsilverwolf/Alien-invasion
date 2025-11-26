import pygame.font
from pygame.sprite import Group
from ship import Ship


class Scoreboard():
    """显示得分信息的类"""
    
    def __init__(self, ai_settings, screen, stats):
        """初始化显示得分涉及的属性"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats
        
        # 显示得分信息时使用的字体设置
        self.text_color = (255, 255, 255)
        try:
            import os
            font_paths = [
                "C:/Windows/Fonts/msyh.ttc",
                "C:/Windows/Fonts/simhei.ttf",
                "C:/Windows/Fonts/simsun.ttc",
            ]
            font_loaded = False
            for font_path in font_paths:
                if os.path.exists(font_path):
                    self.font = pygame.font.Font(font_path, 36)
                    self.title_font = pygame.font.Font(font_path, 48)
                    font_loaded = True
                    break
            if not font_loaded:
                self.font = pygame.font.SysFont(None, 36)
                self.title_font = pygame.font.SysFont(None, 48)
        except:
            self.font = pygame.font.SysFont(None, 36)
            self.title_font = pygame.font.SysFont(None, 48)
        
        # 准备包含最高分和当前得分的图像
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()
        
    def prep_score(self):
        """将得分转换为一幅渲染的图像"""
        rounded_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color,
            self.ai_settings.bg_color)
            
        # 将得分放在屏幕右上角
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
        
    def prep_high_score(self):
        """将最高分转换为渲染的图像"""
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True,
            self.text_color, self.ai_settings.bg_color)
            
        # 将最高分放在屏幕顶部中央
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top
        
    def prep_level(self):
        """将等级转换为渲染的图像"""
        self.level_image = self.font.render(str(self.stats.level), True,
            self.text_color, self.ai_settings.bg_color)
            
        # 将等级放在得分下方
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10
        
    def prep_ships(self):
        """显示还余下多少艘飞船"""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_settings, self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)
        
    def show_score(self):
        """在屏幕上显示得分"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        # 绘制飞船
        self.ships.draw(self.screen)
    
    def show_leaderboard(self, screen, leaderboard):
        """显示排行榜"""
        # 创建一个独立于游戏背景的Surface
        leaderboard_surface = pygame.Surface((self.screen_rect.width, self.screen_rect.height))
        leaderboard_surface.fill((10, 10, 30))  # 深蓝色背景
        
        # 标题
        title_text = self.title_font.render("Leaderboard", True, (255, 215, 0))
        title_rect = title_text.get_rect()
        title_rect.centerx = self.screen_rect.centerx
        title_rect.top = 50
        leaderboard_surface.blit(title_text, title_rect)
        
        # 排行榜内容
        leaders = leaderboard.get_top_scores(5)
        y_offset = 120
        
        for i, leader in enumerate(leaders, 1):
            # 排名
            rank_text = self.font.render(f"{i}.", True, (255, 255, 255))
            leaderboard_surface.blit(rank_text, (self.screen_rect.centerx - 200, y_offset))
            
            # 名字
            name_text = self.font.render(leader['name'], True, (255, 255, 255))
            leaderboard_surface.blit(name_text, (self.screen_rect.centerx - 150, y_offset))
            
            # 分数
            score_text = self.font.render(f"{leader['score']:,}", True, (255, 255, 255))
            leaderboard_surface.blit(score_text, (self.screen_rect.centerx + 50, y_offset))
            
            # 等级
            level_text = self.font.render(f"Lv.{leader['level']}", True, (255, 255, 255))
            leaderboard_surface.blit(level_text, (self.screen_rect.centerx + 200, y_offset))
            
            y_offset += 40
        
        # 提示文字
        prompt_text = self.font.render("Press ESC to close", True, (150, 150, 150))
        prompt_rect = prompt_text.get_rect()
        prompt_rect.centerx = self.screen_rect.centerx
        prompt_rect.bottom = self.screen_rect.bottom - 20
        leaderboard_surface.blit(prompt_text, prompt_rect)
        
        # 一次性将整个排行榜界面绘制到屏幕
        screen.blit(leaderboard_surface, (0, 0))
        
        # 标题
        title_text = self.title_font.render("Leaderboard", True, (255, 215, 0))
        title_rect = title_text.get_rect()
        title_rect.centerx = self.screen_rect.centerx
        title_rect.top = 50
        screen.blit(title_text, title_rect)
        
        # 排行榜内容
        leaders = leaderboard.get_top_scores(5)
        y_offset = 120
        
        for i, leader in enumerate(leaders, 1):
            # 排名
            rank_text = self.font.render(f"{i}.", True, self.text_color)
            screen.blit(rank_text, (self.screen_rect.centerx - 200, y_offset))
            
            # 名字
            name_text = self.font.render(leader['name'], True, self.text_color)
            screen.blit(name_text, (self.screen_rect.centerx - 150, y_offset))
            
            # 分数
            score_text = self.font.render(f"{leader['score']:,}", True, self.text_color)
            screen.blit(score_text, (self.screen_rect.centerx + 50, y_offset))
            
            # 等级
            level_text = self.font.render(f"Lv.{leader['level']}", True, self.text_color)
            screen.blit(level_text, (self.screen_rect.centerx + 200, y_offset))
            
            y_offset += 40
        
        # 提示文字
        prompt_text = self.font.render("Press ESC to close", True, (150, 150, 150))
        prompt_rect = prompt_text.get_rect()
        prompt_rect.centerx = self.screen_rect.centerx
        prompt_rect.bottom = self.screen_rect.bottom - 20
        screen.blit(prompt_text, prompt_rect)