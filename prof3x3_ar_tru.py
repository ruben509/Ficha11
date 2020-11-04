def area_circulo (r1):
    area= 3.14 * (r1*r1)
    return area
def area_coroa(r,r2):
    if r<r2:
        raise ValueError
    else:
        area_coroa = area_circulo(r)-area_circulo(r2)
        return area_coroa

r=float(input("Insere area do criculo extrior:"))
r2=float(input("insere a area do criculo interior:"))
print("Area da suprefice é:",area_coroa(r,r2))