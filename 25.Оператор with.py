class WordsFinder:
    def __init__(self, *file_name):
        self.file_names = list(file_name)

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            words = []
            with open(file_name, 'r', encoding="utf-8") as file:
                for line in file:
                    line = line.lower()
                    line = line.replace(',', '').replace('.', '').replace('=', '').replace('!', '').replace('?',
                                                                                                            '').replace(
                        ';', '').replace(':', '').replace('-', ' ')
                    words.extend(line.split())
            all_words[file_name] = words
        return all_words

    def find(self, search_word):
        find_word = {}
        for name, words in self.get_all_words().items():
            if search_word.lower() in words:
                find_word[name] = words.index(search_word.lower()) + 1

        return find_word

    def count(self, search_word):
        count_word = {}
        for name, words in self.get_all_words().items():
            count = 0
            for word in words:
                if word.lower() == search_word.lower():
                    count = count + 1
            count_word[name] = count
        return count_word


finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))
