def multiply_polynoms(pol1, pol2):
    if pol1==[0] or pol2==[0]:
        return [0]

    new_pol = []
    for i in range(0, len(pol1) + len(pol2) - 1):
        new_pol.append(0)
        for j in range(0, i + 1):
            if j < len(pol1) and (i - j) < len(pol2):
                new_pol[i] += pol1[j] * pol2[i - j]
            else:
                continue

    return new_pol


def print_polynom(pol):
    if pol==[0]:
        print(0)
        return
    string = ""
    for i in reversed(range(1, len(pol))):
        if pol[i] != 0:
            if string != "" and pol[i] > 0:
                string += '+'
            if pol[i] != 1:
                if pol[i] != -1:
                    string += str(pol[i])
                else:
                    string += '-'
            string += "x"
            if i != 1:
                string+='^'
                string += str(i)
            string += ' '
    if pol[0] > 0 and len(pol) > 1:
        string += '+'
    if pol[0] != 0:
        string += str(pol[0])
    print(string)


def is_empty(pol):
    for i in pol:
        if i != 0:
            return False
    return True

def add_polynoms(pol1,pol2):
    if pol1==[0]:
        return pol2.copy()
    if pol2==[0]:
        return pol1.copy()
    new_pol=[]
    for i in range(min(len(pol1),len(pol2))):
        new_pol.append(pol2[i]+pol1[i])
    for i in range(min(len(pol1),len(pol2)),max(len(pol1),len(pol2))):
        if len(pol1)>len(pol2):
            new_pol.append(pol1[i])
        else:
            new_pol.append(pol2[i])
    zero_trail=0

    for i in reversed(range(0,len(new_pol))):
        if new_pol[i] != 0:
            break
        else:
            zero_trail+=1

    if zero_trail== len(new_pol):
        return [0]
    else:
        return new_pol[:len(new_pol)-zero_trail]



def euclid_algorithm(polP,polQ):
    polR=polP.copy()
    polB=[0]
    while polR != [0] and len(polR) >= len(polQ):
        new_coef= polR[-1]/polQ[-1]
        degree= len(polR)-len(polQ)
        new_pol=[0]*degree
        new_pol.append(new_coef)
        polR=add_polynoms(polR, multiply_polynoms([-1],multiply_polynoms(polQ,new_pol)))
        polB= add_polynoms(polB,new_pol)


    return (polB,polR)


def read_polynom():
    pol=[]
    print("Molimo Vas unesite stepen polinoma ")
    degree= int(input())
    if degree<0 :
        print("Uneli ste nevalidnu vrednost")
        exit(1)
    print("Molimo Vas unesite koeficijente polinoma, od najnizeg ka najvecem stepenu (svaki u posebnom redu) ")
    for i in range(degree+1):
        pol.append(int(input()))

    return pol


if __name__ == '__main__':
    print("Molimo Vas unesite polinom P (deljenik) ")
    polP=read_polynom()
    print("Molimo Vas unesite polinom Q (delilac) ")
    polQ=read_polynom()



    mytyple=euclid_algorithm(polP,polQ)
    print("Kolicnik polinoma: ")
    print_polynom(mytyple[0])
    print("Ostatak pri deljenju: ")
    print_polynom(mytyple[1])