# # areas = [[xse, yse, xid, yid], [xse2, yse2, xid2, yid2]]
# def rectangleIntersects(rectangle1, rectangle2):
#     print(len(rectangle1), len(rectangle2))
#     hightRectangle1 = abs(rectangle1[1] - rectangle1[3])
#     hightRectangle2 = abs(rectangle2[1] - rectangle2[3])
#     hightSum = abs(rectangle1[1] - rectangle2[3])
#     widthRectangle1 = abs(rectangle1[0] - rectangle1[2])
#     widthRectangle2 = abs(rectangle2[0] - rectangle2[2])
#     widthSum = abs(rectangle1[0] - rectangle2[2])

#     if (
#         hightRectangle1 + hightRectangle2 >= hightSum
#         and widthRectangle1 + widthRectangle2 >= widthSum
#     ):
#         return True

#     return False


# # Pega o valor máximo da coordenada "SE" entre 2 retângulos
# def getMaximumValueSE(rectangle1, rectangle2):
#     xse = rectangle1[0]
#     # para o menor x
#     if rectangle1[0] > rectangle2[0]:
#         xse = rectangle2[0]

#     yse = rectangle2[1]
#     # para o maior y
#     if rectangle1[1] > rectangle2[1]:
#         yse = rectangle1[1]

#     return xse, yse


# # Pega o valor máximo da coordenada "ID" entre 2 retângulos
# def getMaximumValueID(rectangle1, rectangle2):
#     xid = rectangle2[2]
#     # para o maior x
#     if rectangle1[2] > rectangle2[2]:
#         xid = rectangle1[2]

#     yid = rectangle1[3]
#     # para o menor y
#     if rectangle1[3] > rectangle2[3]:
#         yid = rectangle2[3]

#     return xid, yid


# # Define o novo retângulo caso haja sobreposição, para isso ela usa as duas funções acima
# def definingNewRectangle(rectangle1, rectangle2):
#     rectangle3 = [
#         getMaximumValueSE(rectangle1, rectangle2),
#         getMaximumValueID(rectangle1, rectangle2),
#     ]

#     return rectangle3


# def getNewAreas(areas, rectangle):
#     for rectangles in areas:
#         if rectangleIntersects(rectangles, rectangle):
#             newRectangle = definingNewRectangle(rectangles, rectangle)
#             areas.remove(rectangles)
#             return getNewAreas(areas, newRectangle)
#     areas.append(rectangle)
#     return areas
