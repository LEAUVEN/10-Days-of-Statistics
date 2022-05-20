def median(sayilar):
    if len(sayilar)%2 == 0:
        return int(sum(sayilar[len(sayilar)//2-1:len(sayilar)//2+1])/2)
    else:
        return sayilar[len(sayilar)//2]

def quartiles(adet,sayilar):
    Q1 = median(sayilar[:len(sayilar)//2])
    Q2 = median(sayilar)
    if adet%2 == 0:
        Q3 = median(sayilar[len(sayilar)//2:])
    else:
        Q3 = median(sayilar[len(sayilar)//2+1:])
    return Q1,Q2,Q3

adet = int(input())
sayilar = sorted([int(sayilar) for sayilar in input().split()])
Q1,Q2,Q3 = quartiles(adet,sayilar)
print(Q1)
print(Q2)
print(Q3)
