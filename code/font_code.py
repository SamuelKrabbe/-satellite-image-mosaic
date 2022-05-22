import verify_func


# lendo as primeiras coordenadas
xse, yse, xid, yid = map(int, input().split())

# criando um loop para verificar se há interseção entre coordenadas
ret_ad = []
contador = 1

while True:
    try:
        xse2, yse2, xid2, yid2 = map(int, input().split())

        ponto_se = verify_func.verify_se(xse, yse, xid, yid, xse2, yse2)
        ponto_id = verify_func.verify_id(xse, yse, xid, yid, xid2, yid2)

        if ponto_se == 0:
            ret_ad.append([(xse2, yse2), (xid2, yid2)])
            contador += 1

    except:
        break

ret_ad.insert(0, [ponto_se, ponto_id])

print(contador)

for retangulos in ret_ad:
    print(", ".join(map(str, retangulos)))
