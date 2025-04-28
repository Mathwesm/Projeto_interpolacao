
def selecionar_pontos_mais_proximos(pontos, x_interpolar, quantidade):
    pontos_ordenados = sorted(pontos, key=lambda p: abs(p[0] - x_interpolar))
    return pontos_ordenados[:quantidade]