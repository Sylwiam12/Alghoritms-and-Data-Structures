import time
with open("lotr.txt", encoding='utf-8') as f:
        text = f.readlines()
text = ' '.join(text).lower()
##naive_algorithm
def naive_method(pattern,text):
    idx_lst=[]
    W=len(pattern)
    M=len(text)
    m=0
    counter=0
    while m<=M-W:
        w=0
        while w <W:
            counter+=1
            if text[m+w]!=pattern[w]:
                break
            w+=1
        if w==W:
            idx_lst.append(w)
        m+=1
    return len(idx_lst),counter
##test
# s='wyrewolwerowanyrewolwerwyrewolwerowanegorewolwerowca'
# p='rewolwer'    
# print(naive_method(p,s))
p='time.'
result=naive_method(p,text)
print(result[0],';',result[1])

##Rabin_Kharp_algorithm
def hashr(word,d=256,q=101,hw=0):
    for i in range(len(word)):  # N - to długość wzorca
        hw = (hw*d + ord(word[i])) % q  # dla d będącego potęgą 2 można mnożenie zastąpić shiftem uzyskując pewne przyspieszenie obliczeń
    return hw

#pierwsza wersja
def rabin_kharp(pattern,text):
    M = len(text)
    W = len(pattern)
    result_lst=[]
    counter=0
    collision_nr=0
    hW = hashr(pattern)
    for m in range(M-W+1):
        hS = hashr(text[m:m+W])
        counter+=1
        if hS == hW:
            if text[m:m+W] != pattern[0:W]:
                collision_nr+=1 
            else:
                result_lst.append(m)
    return len(result_lst),counter,collision_nr 
#print(rabin_kharp(p,text))

##druga wersja
def rabin_kharpv2(pattern,text,d=256,q=101):
    M = len(text)
    W = len(pattern)
    result_lst=[]
    counter=0
    collision_nr=101
    hW = hashr(pattern)
    h = 1
    for i in range(W-1):
        h = (h*d)%q
    for m in range(M-W+1):
        hS = hashr(text[m:m+W])
        counter+=1
        if hS == hW:
            if text[m:m+W] != pattern[0:W]:
                collision_nr+=1 
            else:
                result_lst.append(m)
        hS =hashr(text[m:m+W],hw=hS - ord(text[i]) * h) 
        if hS<0:
            hS+=q
    return len(result_lst),counter,collision_nr
result=rabin_kharpv2(p,text)
print(result[0],';',result[1],';',result[2])

##KMP_algorithm
def kmp_search(S,W,T):
    m=0
    i=0
    nP=0
    P=[]
    while m<len(S):
            nP+=1
            if W[i] == S[m]:
                m+= 1
                i+=1
                if i == len(W):
                    P.append(m-i)
                    i = T[i]
            else:
                i = T[i]
                if i < 0:
                    m+=1
                    i+=1
    return len(P),nP

def kmp_table(W):
    pos=1
    cnd=0
    T=[0 for k in range(len(W)+1)]
    T[0]=-1
    while pos<len(W):
        if W[pos]==W[cnd]:
            T[pos]=T[cnd]
        else:
            T[pos]=cnd
            while cnd>=0 and W[pos]!=W[cnd]:
                cnd=T[cnd]
        pos+=1
        cnd+=1
    T[pos]=cnd
    return T
T=kmp_table(p)
result=kmp_search(text,p,T)
print(result[0],';',result[1])

# #porównanie czasów
# t_start = time.perf_counter()
# naive_method(p,text)
# t_stop = time.perf_counter()
# print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))

# t_start = time.perf_counter()
# rabin_kharpv2(p,text)
# t_stop = time.perf_counter()
# print("Czas obliczeń (Rabin-Kharp):", "{:.7f}".format(t_stop - t_start))

# t_start = time.perf_counter()
# kmp_search(text,p,T)
# t_stop = time.perf_counter()
# print("Czas obliczeń (KMP):", "{:.7f}".format(t_stop - t_start))