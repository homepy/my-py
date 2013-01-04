class WordCount:
    def __init__(self, word, count):
        self.word = word
        self.count = count

word_str = None
with open('CET.txt', encoding='utf-8') as f:
    word_str = f.read()
word_str = word_str.lower().replace('.', ' ').replace(',', ' ')\
    .replace('\n', ' ').replace('(', ' ').replace(')', ' ').replace('"', ' ')

word_list = word_str.split(' ')
word_list = [word.strip() for word in word_list]

word_set = set(word_list)
word_set.discard('')

result = []
for word in word_set:
    wc_new = WordCount(word, word_list.count(word))
    # order result by count desc
    if len(result) == 0:
        result.append(wc_new)
    else:
        for wc in result:
            if wc_new.count >= wc.count:
                index = result.index(wc)
                result.insert(index, wc_new)
                break

for wc in result:
    print(' {0} : {1} '.format(wc.word, wc.count))
