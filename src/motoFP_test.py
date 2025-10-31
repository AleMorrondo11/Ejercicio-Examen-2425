from motoFP import *

if __name__ == "__main__":
    carreras = lee_carreras("data/mundial_motofp.csv")
    #print(carreras)
    print(maximo_dias_sin_ganar(carreras, "Jorge Martin"))
    print(piloto_mas_podios_por_circuito(carreras))