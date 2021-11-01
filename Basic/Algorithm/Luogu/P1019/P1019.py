class SpliceWord:
    def __init__(self):
        self.word_dict = {}  # 利用字典存储词和使用的次数
        word_num = int(input())
        for i in range(word_num):
            word = input()
            if len(word) > 1:
                self.word_dict[word] = 0  # 定义单词使用次数为0
        self.first_letter = input()  # 接收第一个开头的字符
        # print(self.word_dict)   # 测试
        self.max_length = 0  # 定义全局最大长度

    def start(self):
        first_word = self.first_letter  # 获取开头输入的头字符
        self.depth_first_search(' ' + first_word, self.max_length)  # 增加字符避免匹配失败
        return self.max_length

    def depth_first_search(self, first_word, new_length):
        self.max_length = max(new_length, self.max_length)
        for second_word in self.word_dict:
            used_time = self.word_dict[second_word]
            if used_time >= 2:
                continue  # 如果一个词的使用次超过2，循环到下一个数
            cut_check_success_letter = self.check_letter(first_word, second_word)  # 进入匹配函数
            if cut_check_success_letter:
                self.word_dict[second_word] += 1  # 被匹配的单词使用次数加1
                new_first_word = first_word + second_word[cut_check_success_letter:]
                new_length = len(new_first_word.strip())
                #   strip方法去除一开始为避免匹配使用增加的字符
                self.depth_first_search(new_first_word, new_length)
                self.word_dict[second_word] -= 1

    def check_letter(self, first_word, second_word) -> int:
        cut_letter_length = min(len(first_word), len(second_word))
        for cut_letter in range(1, cut_letter_length):
            if first_word[-cut_letter:] == second_word[:cut_letter]:
                return cut_letter
            else:
                continue  # 找不到当前切片长度时继续循环第二个切片长度
        return False  # 找不到所有切片长度的匹配项时返回False


max_length = SpliceWord().start()
print(max_length)
