# ЗАДАНИЕ ПО ТЕМЕ "Оператор WITH"

class WordsFinder:

    def __init__(self, *file_name):
        self.file_names = [*file_name]

    def get_all_words(self):
        list_files = self.file_names
        all_words = {}
        excluded_char = [',', '.', '=', '!', '?', ';', ':']  # Исключаемые символы
        for i in range(len(list_files)):
            key = list_files[i]
            text_lower = ''
            with open(key, encoding='utf-8') as file:
                # в переменную text_lower перезапишем файл по символам,
                # переводя их в нижний регистр и
                # исключив символы из списка excluded_char
                for line in file:
                    for char in line:
                        if char in excluded_char:
                            continue
                        else:
                            text_lower += char.lower()
                # составим список слов (наборов символов, разделенных пробелом),
                # исключив '-', в которое будет преобразовано тире между словами
                words = [word for word in text_lower.split() if word != '-']
            all_words[key] = words
        return all_words

    def find(self, word):
        all_words = self.get_all_words()
        list_files = list(all_words.keys())
        list_words = list(all_words.values())
        dict_find = {}
        for i in range(len(list_files)):
            key = list_files[i]
            number_word = list_words[i].index(word.lower()) + 1
            dict_find[key] = number_word
        return dict_find

    def count(self, word):
        all_words = self.get_all_words()
        list_files = list(all_words.keys())
        list_words = list(all_words.values())
        dict_count = {}
        for i in range(len(list_files)):
            key = list_files[i]
            word_count = list_words[i].count(word.lower())
            dict_count[key] = word_count
        return dict_count


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего

# finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
#                       'Rudyard Kipling - If.txt',
#                       'Mother Goose - Monday’s Child.txt')
# print(finder1.get_all_words())  # Все слова
# print(finder1.find('the'))
# print(finder1.count('the'))

# finder1 = WordsFinder('Mother Goose - Monday’s Child.txt',)
# print(finder1.get_all_words())
# print(finder1.find('Child'))
# print(finder1.count('Child'))

# finder1 = WordsFinder('Rudyard Kipling - If.txt',)
# print(finder1.get_all_words())
# print(finder1.find('if'))
# print(finder1.count('if'))

# finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')
# print(finder1.get_all_words())
# print(finder1.find('captain'))
# print(finder1.count('captain'))