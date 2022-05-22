def verify_func(xse, yse, xid, yid, xse2, yse2, xid2, yid2):

    # Verificando interseção
    if xse2 <= xid and yse2 >= yid:

        if xid2 >= xse and yid2 <= yse:

            # Redefinindo o ponto superior esquerdo (se)
            if xse2 >= xse and yse2 >= yse:
                xse = xse
                yse = yse2
            elif xse2 >= xse and yse2 <= yse:
                xse = xse
                yse = yse
            elif xse2 <= xse and yse2 <= yse:
                xse = xse2
                yse = yse
            elif xse2 <= xse and yse2 >= yse:
                xse = xse
                yse = yse2

            # Redefinindo o ponto inferior esquerdo (id)
            if xid2 <= xid and yid2 >= yid:
                xid = xid
                yid = yid
            elif xid2 >= xid and yid2 >= yid:
                xid = xid2
                yid = yid
            elif xid2 >= xid and yid2 <= yid:
                xid = xid2
                yid = yid2
            elif xid2 <= xid and yid2 <= yid:
                xid = xid
                yid = yid2

            return (xse, yse), (xid, yid)

        else:
            return 0

    else:
        return 0
