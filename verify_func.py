# verificação ponto superior esquerdo
def verify_se(xse, yse, xid, yid, xse2, yse2):
    if xse <= xse2 and xse2 <= xid:
        if yse >= yse2 and yse2 <= yid:
            xse = xse
            yse = yse
        elif yse2 > yse:
            xse = xse
            yse = yse2

        return (xse, yse)

    elif xse2 < xse:
        if yse >= yse2 and yse2 <= yid:
            xse = xse2
            yse = yse
        elif yse2 > yse:
            xse = xse2
            yse = yse2

        return (xse, yse)

    else:
        return 0


# --------------------------------------------------------------------------------------

# verificação ponto inferior direito
def verify_id(xse, yse, xid, yid, xid2, yid2):
    if xse <= xid2 and xid2 <= xid:
        if yse >= yid2 and yid2 <= yid:
            xid = xid
            yid = yid

        elif yid2 < yid:
            xid = xid
            yid = yid2

        return (xid, yid)

    elif xid2 > xid:
        if yse >= yid2 and yid2 <= yid:
            xid = xid2
            yid = yid

        elif yid2 < yid:
            xid = xid2
            yid = yid2

        return (xid, yid)

    else:
        return 0
