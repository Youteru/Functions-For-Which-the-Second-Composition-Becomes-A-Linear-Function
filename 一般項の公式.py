import math
L=[]
def combi(b,c) : #長さbのリストのうちc個が1、それ以外0
    if b==c :
        return [[2]*b]
    elif c==0 :
        return [[1]*b]
    else :
        CX=combi(b-1,c)
        CY=combi(b-1,c-1)
        T=[]
        U=[]
        for i in range(len(CX)) :
            T.append([1]+CX[i])
        for i in range(len(CY)) :
            U.append([2]+CY[i])
        return T+U
def f_major(c,n) : #f(f(n))=2n+cという条件におけるf(n)の基本解。c=1,2,3なら
    #それが唯一の解である。
    # O(1)で計算可能である。
    if c==1 :
        A=math.floor(math.log2(n+1))
        B=math.floor(math.log2((n+1)/3))
        ans=(A-B-1)*(2**(A-1)+n)-(A-B-2)*(2*n+1-2**A)
        return ans
    else :
        return f_major(1,n+c-1)-c+1

def f_listup(a,c,n) :
    #ありうるf(k) (k=<n)を列挙する
    #だいたいO(n*P(c-1)) P(c)はパドヴァン数列
    COM=combi(a-1,3+c-2*a)
    k=len(COM)
    ans=[]
    for i in range (k) :
        Table=COM[i]
        G=Table
        while len(Table)<n :
            K=[]
            for j in range (len(G)) :
                if G[j]==1 :
                    K.append(2)
                else :
                    K.append(1)
                    K.append(1)
            Table=Table+K
            G=K
        ANS=[a]
        for i in range (n-1) :
            ANS.append(ANS[i]+Table[i])
        ans.append(ANS)
    return ans
def f_all_listup(c,n) :
    #O(n*P(c-1)) P(c)はパドヴァン数列
    ans=[]
    Afirst=math.ceil((c+4)/3)
    for i in range (-Afirst+math.floor((c+3)/2)+1) :
        ans=ans+f_listup(i+Afirst,c,n)
    return ans
print(f_all_listup(10,20))

def f_fast(a,c,n)
    #f(1)が分かっているとき特定のf(n)のありうる値を高速で計算する
    if n==1 :
        return a
    A=[1,a]
    while A[-1]<n :
        A.append(A[-2]*2+c)
    
    if n==A[-1] :
        return 2*A[-2]+c
    elif len(A)%2==0 : #前半　1がLev個、2がLev個
        t=n-A[-2]
        if t%Level==0 :

        else :
            
    else : #　後半　1が2Level個、2がLevel個
    
        

    
#パドヴァン数列の特定の項をpで割った余りを計算する。
#繰り返し二乗法を用いたpythonのソースコードは存在しなかったので自分で書いた。
