import json
import os

class Leaderboard:
    """管理游戏排行榜的类"""
    
    def __init__(self, filename="leaderboard.json"):
        """初始化排行榜"""
        # 获取当前脚本所在目录，构建绝对路径
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.filename = os.path.join(current_dir, filename)
        self.leaders = []
        self.load_leaderboard()
    
    def load_leaderboard(self):
        """从文件加载排行榜数据"""
        try:
            if os.path.exists(self.filename):
                with open(self.filename, 'r', encoding='utf-8') as f:
                    self.leaders = json.load(f)
        except Exception as e:
            print(f"加载排行榜数据失败: {e}")
            self.leaders = []
    
    def save_leaderboard(self):
        """保存排行榜数据到文件"""
        try:
            with open(self.filename, 'w', encoding='utf-8') as f:
                json.dump(self.leaders, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"保存排行榜数据失败: {e}")
    
    def add_score(self, name, score, level):
        """添加新的分数记录"""
        import datetime
        entry = {
            'name': name,
            'score': score,
            'level': level,
            'date': datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        }
        self.leaders.append(entry)
        # 按分数降序排序
        self.leaders.sort(key=lambda x: x['score'], reverse=True)
        # 只保留前10名
        self.leaders = self.leaders[:10]
        self.save_leaderboard()
    
    def get_top_scores(self, limit=10):
        """获取前N名分数"""
        return self.leaders[:limit]
    
    def is_high_score(self, score):
        """检查是否是高分（能进入排行榜）"""
        if len(self.leaders) < 10:
            return True
        return score > self.leaders[-1]['score']
    
    def get_rank(self, score):
        """获取分数在排行榜中的排名"""
        for i, leader in enumerate(self.leaders):
            if score > leader['score']:
                return i + 1
        return len(self.leaders) + 1