def seqToWordNgram(n, seq):
    seq = seq.replace(",", "")
    seq = seq.replace(".", "")
    ls = seq.split()
    word_ngram_ls = []
    for i in range(len(ls)-n+1):
        word_ngram_ls.append(" ".join(ls[i:i+n]))
    return word_ngram_ls


def seqToCharNgram(n, seq):
    char_ngram_ls = []
    for i in range(len(seq)-n+1):
        char_ngram_ls.append(seq[i:i+n])
    return char_ngram_ls

if __name__ == '__main__':
    s = "I am an NLPer"
    print(seqToWordNgram(2, s))
    print(seqToCharNgram(2, s))
