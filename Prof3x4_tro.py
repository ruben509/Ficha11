x=int(input("Insere o valor:"))
l=x//50
K=0
for i in range(l):
    if x>=50:
        K=K+1
        x=x-50
    elif x>=20:
        u=u+1
        x=x-20
        print(u)
    elif x>=10:
        a=a+1
        x=x-10
        print(a)
    elif x>=5:
        z=z+1
        x=x-5
        print(z)

print("SAo",K,"DE cinequenta euros")   