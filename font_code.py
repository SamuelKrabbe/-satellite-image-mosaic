import verify_func


# lendo as primeiras coordenadas
xse, yse, xid, yid = map(float, input().split())

# criando um loop para verificar se há interseção entre coordenadas
ret_ad = []
contador = 1

while True:
    try:
        xse2, yse2, xid2, yid2 = map(float, input().split())

        ponto_se = verify_func.verify_se(xse, yse, xid, yid, xse2, yse2)
        ponto_id = verify_func.verify_id(xse, yse, xid, yid, xid2, yid2)

        if ponto_se == 0:
            ret_ad.append([(xse2, yse2), (xid2, yid2)])
            contador += 1

    except:
        break

ret_ad.append(0, [(xse, yse), (xid, yid)])

print(contador)

for retangulos in ret_ad:
    print(retangulos)
