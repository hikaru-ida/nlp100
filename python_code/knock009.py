import random


def Typoglycemia(s):
    words_ls = s.split(" ")
    shuffled_ls = []
    for word in words_ls:
        if(len(word) >= 4):
            rand_ls = list(word[1:-1])
            random.shuffle(rand_ls)
            shuffled_word = word[0]+"".join(rand_ls) + word[-1]
            shuffled_ls.append(shuffled_word)
        else:
            shuffled_ls.append(word)

    return " ".join(shuffled_ls)

if __name__ == '__main__':
    s = "I couldn't believe that I could actually understand " \
        "what I was reading : the phenomenal power of the human mind ."
    print(Typoglycemia(s))
