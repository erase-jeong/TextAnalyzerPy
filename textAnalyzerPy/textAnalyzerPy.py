import re
from collections import Counter

class TextAnalyzer:
    def __init__(self, text):
        self.text = text
        self.words = self._words()

    def _words(self):
        # 텍스트에서 단어만 추출
        words = re.findall(r'\b\w+\b', self.text.lower())
        return words

    def most_common_words(self, num=10):
        # 가장 많이 나타나는 단어를 찾기
        count = Counter(self.words)
        return count.most_common(num)

    def text_complexity(self):
        # 텍스트의 복잡성을 평가
        num_words = len(self.words)
        unique_words = len(set(self.words))
        lex_diversity = unique_words / num_words
        return {
            "total_words": num_words,
            "unique_words": unique_words,
            "lexical_diversity": lex_diversity
        }
