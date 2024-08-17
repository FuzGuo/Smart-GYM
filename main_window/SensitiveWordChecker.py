class SensitiveWordChecker:
    def __init__(self):
        # 初始化敏感词列表
        self.sensitive_words = {"暴力", "色情", "毒品", "反动", "赌博", "恐怖主义", "走私", "贪污", "腐败", "洗钱"}

    def add_sensitive_word(self, word):
        """添加敏感词到列表"""
        self.sensitive_words.add(word)

    def remove_sensitive_word(self, word):
        """从列表中移除敏感词"""
        self.sensitive_words.discard(word)

    def check_text(self, text):
        """检测文本中是否包含敏感词"""
        found_words = [word for word in self.sensitive_words if word in text]
        return bool(found_words), found_words  # 如果找到敏感词，返回True和敏感词列表

