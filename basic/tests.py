import operator

def count_flag(filename):
    content = open(filename, 'r').read()
    for char in ['?','!','-','.',',','\'','`','(',')','_','-','\"',':','\n']:
        content = content.replace(char, ' ')
    print(content)
    content = open(filename, 'rt')
    dict_word = dict()
    for line in content:
        words = line.split(' ')
        for word in words:
            word = word.lower()
            if word in dict_word:
                dict_word[word] += 1
            else:
                dict_word[word] = 1
    return dict_word

def print_words(filename):
    dict_word = count_flag(filename)
    words = sorted(dict_word.keys())
    for word in words:
        print(word, dict_word[word])


def print_top(filename):
    x = count_flag(filename)
    sorted_x = sorted(x.items(), key=operator.itemgetter(1),reverse=True)
    print((sorted_x)[:20])

print(count_flag('alice.txt'))
#print(print_words('alice.txt'))
#rint(print_top('alice.txt'))

def punctuation_remove(filename):
    with open(filename, 'r') as infile, open(filename, 'w') as outfile:
        data = infile.read()
        for char in ['?', '!', '-', '.', ',', '\'', '`', '(', ')', '_', '-', '\"', ':', '\n']:
            data = data.replace(char,'')
            outfile.write(data)


#print(punctuation_remove('alice.txt'))


