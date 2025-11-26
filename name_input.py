import pygame
import pygame.font
import os

class NameInput:
    """玩家名字输入界面"""
    
    def __init__(self, ai_settings, screen):
        """初始化名字输入界面"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        
        # 字体设置
        try:
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
        
        # 输入框设置
        self.input_box_rect = pygame.Rect(0, 0, 400, 50)
        self.input_box_rect.center = self.screen_rect.center
        
        # 文本颜色
        self.text_color = (255, 255, 255)
        self.box_color = (100, 100, 100)
        self.active_color = (0, 150, 255)
        
        # 输入状态
        self.active = False
        self.text = ''
        self.max_length = 15
        
        # 按钮
        self.ok_button = pygame.Rect(0, 0, 120, 40)
        self.ok_button.centerx = self.screen_rect.centerx - 70
        self.ok_button.top = self.input_box_rect.bottom + 30
        
        self.cancel_button = pygame.Rect(0, 0, 120, 40)
        self.cancel_button.centerx = self.screen_rect.centerx + 70
        self.cancel_button.top = self.input_box_rect.bottom + 30
        
    def handle_event(self, event):
        """处理输入事件"""
        if event.type == pygame.MOUSEBUTTONDOWN:
            # 检查是否点击输入框
            if self.input_box_rect.collidepoint(event.pos):
                self.active = True
            else:
                self.active = False
                
            # 检查是否点击按钮
            if self.ok_button.collidepoint(event.pos) and self.text:
                return 'ok'
            elif self.cancel_button.collidepoint(event.pos):
                return 'cancel'
                
        elif event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN and self.text:
                    return 'ok'
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                elif len(self.text) < self.max_length:
                    self.text += event.unicode
        
        return None
    
    def draw(self, screen, score, level):
        """绘制输入界面"""
        # 半透明背景
        overlay = pygame.Surface((self.screen_rect.width, self.screen_rect.height))
        overlay.set_alpha(128)
        overlay.fill((0, 0, 0))
        screen.blit(overlay, (0, 0))
        
        # 标题
        title_text = self.title_font.render("New High Score!", True, (255, 215, 0))
        title_rect = title_text.get_rect()
        title_rect.centerx = self.screen_rect.centerx
        title_rect.top = self.screen_rect.centery - 180  # 向上移动更多
        screen.blit(title_text, title_rect)
        
        # 分数显示
        score_text = self.font.render(f"Score: {score}  Level: {level}", True, self.text_color)
        score_rect = score_text.get_rect()
        score_rect.centerx = self.screen_rect.centerx
        score_rect.top = title_rect.bottom + 30  # 增加与标题的间距
        screen.blit(score_text, score_rect)
        
        # 提示文字
        name_prompt_text = self.font.render("Enter your name:", True, self.text_color)
        name_prompt_rect = name_prompt_text.get_rect()
        name_prompt_rect.centerx = self.screen_rect.centerx
        name_prompt_rect.bottom = self.input_box_rect.top - 30  # 增加与输入框的间距
        screen.blit(name_prompt_text, name_prompt_rect)
        
        # 输入框
        color = self.active_color if self.active else self.box_color
        pygame.draw.rect(screen, color, self.input_box_rect, 2)
        
        # 输入的文字
        text_surface = self.font.render(self.text, True, self.text_color)
        screen.blit(text_surface, (self.input_box_rect.x + 5, self.input_box_rect.y + 10))
        
        # OK按钮
        pygame.draw.rect(screen, (0, 200, 0), self.ok_button)
        ok_text = self.font.render("OK", True, self.text_color)
        ok_text_rect = ok_text.get_rect(center=self.ok_button.center)
        screen.blit(ok_text, ok_text_rect)
        
        # Cancel按钮
        pygame.draw.rect(screen, (200, 0, 0), self.cancel_button)
        cancel_text = self.font.render("Cancel", True, self.text_color)
        cancel_text_rect = cancel_text.get_rect(center=self.cancel_button.center)
        screen.blit(cancel_text, cancel_text_rect)