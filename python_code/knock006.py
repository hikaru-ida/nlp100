import knock005
s1 = "paraparaparadise"
s2 =  "paragraph"

X = set(knock005.seqToCharNgram(2, s1))
Y = set(knock005.seqToCharNgram(2, s2))
print("和集合: ", X | Y)
print("積集合: ", X & Y)
print("差集合(X-Y): ", X - Y)
print("差集合(Y-X): ", Y - X)

if("se" in X):
    print("Xに含まれている")
if("se" in Y):
    print("Yに含まれている")

