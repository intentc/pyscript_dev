
def letter_count(stri):
    d=list()
    s=set()
    for x in stri:
        l=list()
        l.append(x)
        l.append(stri.count(x))
        l=tuple(l)
        d.append(l)
    print(d)

 
stri = input('Please enter one letter:')
letter_count(stri)