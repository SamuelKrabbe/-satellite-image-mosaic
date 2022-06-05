"""
Module Docstring
"""

__author__ = "Samuel Krabbe, Matheus Mota"
__version__ = "Python 3.10.4"

print("Digite as coordenadas das imagens aqui: ", end="")

# Lendo o primeiro input para usar de base para as próximas comparações
x_se, y_se, x_id, y_id = map(int, input().split())

# Criando um loop para ler as próximas coordenadas e definir o retângulo mínimo
while True:
    try:
        x1, y1, x2, y2 = map(int, input().split())
        if x1 < x_se:
            x_se = x1
        if y1 > y_se:
            y_se = y1
        if x2 > x_id:
            x_id = x2
        if y2 < y_id:
            y_id = y2
    except:
        break

# imprimindo "1", pois só vai ter um retângulo no final
print("Quantidade de retângulos mínimos: 1")
# imprimindo as coordenadas do retângulo mínimo
print(
    "Coordenadas do retângulo mínimo: ({}, {}), ({}, {})".format(
        x_se, y_se, x_id, y_id
    ),
    end="",
)
