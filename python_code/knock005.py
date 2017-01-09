def seqToWordNgram(n, seq):
    seq = seq.replace(",", "")
    seq = seq.replace(".", "")
    ls = seq.split()
    ngram_ls = []
    for i in range(len(ls)-n+1):
        ngram_ls.append(" ".join(ls[i:i+n]))
    return ngram_ls

s = "I am an NLPer"
print(seqToWordNgram(2, s))
