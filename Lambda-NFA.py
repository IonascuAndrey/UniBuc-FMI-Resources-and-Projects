#Helper functions
def auElemComune(list1, list2):
    return any(check in list1 for check in list2)

def lambda_inchidere(x):
    initial = set()
    initial.update(x)
    l_inchidere_x = set()
    l_inchidere_x.update(x)
    while True:
        x.update(l_inchidere_x)
        for i in x:
            try:
                l_inchidere_x.update(tranzitii[(i, ".")])
            except:
                pass
        if(l_inchidere_x == initial): break;
        initial.update(l_inchidere_x)
    return l_inchidere_x

#Main function
def LNFA(q, w): #multime de stari(multime), cuvant
    l_inchidere_q = lambda_inchidere(q)
    if len(w) == 1:
            ret= set()
            for i in l_inchidere_q:
                try:
                    ret.update(tranzitii[(i, w)])
                except:
                    pass
            ret = lambda_inchidere(ret)
            return ret
    else:
            ret = set()
            for i in l_inchidere_q:
                try:
                    ret.update(tranzitii[(i, w[0])])
                except:
                    pass
            ret = lambda_inchidere(ret)
            return LNFA(ret, w[1:])

#Data Reading
fin = open("input.txt", "r")
nr_stari = int(fin.readline())
stari = {int(x) for x in fin.readline().split()}
nr_litere = int(fin.readline())
litere = {x for x in fin.readline().split()}
stare_init = {int(fin.readline())}
nr_stari_finale = int(fin.readline())
stari_finale= {int(x) for x in fin.readline().split()}
nr_tranzitii = int(fin.readline())
tranzitii= {}
for i in range(nr_tranzitii):
    [a, b, c] = [x for x in fin.readline().split()]
    a = int(a)
    c = int(c)
    if (a, b) not in tranzitii:
        tranzitii.update({(a, b): {c}})
    else:
        tranzitii[(a, b)].update({c})
nr_cuvinte=int(fin.readline())
cuvinte = [x.rstrip('\n') for x in fin.readlines()]

#Checking the words
for x in cuvinte:
    if auElemComune(LNFA(stare_init, x), stari_finale):
        print("DA")
    else:
        print("NU")