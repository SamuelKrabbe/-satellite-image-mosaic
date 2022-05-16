import verify_func


# lendo as primeiras coordenadas
xse, yse, xid, yid = map(float, input().split())

# criando um loop para verificar se há interseção entre coordenadas
while True:
    try:
        contador = 1
        xse2, yse2, xid2, yid2 = map(float, input().split())

        verify_func.verify_se(xse, yse, xid, yid, xse2, yse2)
        verify_func.verify_id(xse, yse, xid, yid, xid2, yid2)

        contador += 1

    except:
        break

print(contador)
