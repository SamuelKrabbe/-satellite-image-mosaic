import verify

# lendo as primeiras coordenadas
xse, yse, xid, yid = map(int, input().split())

# criando um loop para verificar se há interseção entre coordenadas
ret_ad = []
contador = 1

while True:
    try:
        xse2, yse2, xid2, yid2 = map(int, input().split())

        retang = verify.verify_func(xse, yse, xid, yid, xse2, yse2)

        if retang == 0:
            ret_ad.append([(xse2, yse2), (xid2, yid2)])
            contador += 1

    except:
        break

ret_ad.insert(0, [retang])

print(contador)

for retangs in ret_ad:
    print(", ".join(map(str, retangs)))