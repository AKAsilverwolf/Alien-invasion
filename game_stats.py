class GameStats():
    """跟踪游戏的统计信息"""
    
    def __init__(self, ai_settings):
        """初始化统计信息"""
        self.ai_settings = ai_settings
        self.reset_stats()
        
        # 游戏刚启动时处于非活动状态
        self.game_active = False
        
        # 在任何情况下都不应重置最高分
        self.high_score = 0
        self.load_high_score()
    
    def load_high_score(self):
        """从文件加载最高分"""
        try:
            import os
            # 尝试从highscore.txt加载
            highscore_path = os.path.join(os.path.dirname(__file__), '..', 'highscore.txt')
            if os.path.exists(highscore_path):
                with open(highscore_path, 'r') as f:
                    self.high_score = int(f.read())
        except:
            self.high_score = 0
        
    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1