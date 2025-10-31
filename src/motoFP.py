from typing import NamedTuple
from datetime import datetime
import csv

Piloto=NamedTuple("Piloto", [("nombre", str),("escuderia", str)])

CarreraFP=NamedTuple("CarreraFP",[
        ("fecha_hora",datetime), 
        ("circuito",str),                    
        ("pais",str), 
        ("seco",bool), # True si el asfalto estuvo seco, False si estuvo mojado
        ("tiempo",float), 
        ("podio", list[Piloto])])


def lee_carreras(ruta: str) -> list[CarreraFP]:
    Carreras = []
    Pilotos = []
    with open(ruta, "r", encoding='utf-8') as f:
        lector = csv.reader(f, delimiter=",")
        next(lector)
        for carrera in lector:
            fecha_hora = datetime.fromisoformat(carrera[0])
            circuito = str(carrera[1])
            pais = str(carrera[2])
            seco = bool(carrera[3])
            tiempo = float(carrera[4])
            podio = []
            for i in range(5, 6):
                nombre = str(carrera[i])
                escuderia = str(carrera[i+1])
                piloto = Piloto(nombre, escuderia)
                podio.append(piloto)
                for i in range(7, 8):
                    nombre = str(carrera[i])
                    escuderia = str(carrera[i+1])
                    piloto = Piloto(nombre, escuderia)
                    podio.append(piloto)
                for i in range(9, 10):
                    nombre = str(carrera[i])
                    escuderia = str(carrera[i+1])
                    piloto = Piloto(nombre, escuderia)
                    podio.append(piloto)
            carrera = CarreraFP(
                fecha_hora,circuito,pais,seco,tiempo,podio
            )
            Carreras.append(carrera)
    return Carreras


def maximo_dias_sin_ganar(carreras: list[CarreraFP], nombre_piloto: str) -> int:
    veces_ganada=[]
    contador = 0
    for carrera in carreras:
        if nombre_piloto == carrera.podio[0].nombre:
            veces_ganada.append(carrera.fecha_hora)
    veces_ganada.sort()
    if len(veces_ganada)<2:
        return None
    else:
        for i in range(len(veces_ganada)-1):
            dias = (veces_ganada[i] - veces_ganada[i-1]).days
            if dias > contador:
                contador = dias
    return contador

def piloto_mas_podios_por_circuito(carreras: list[CarreraFP]) -> dict[str,str]:
    resultado = {}
    for carrera in carreras:
        contador_podio = {}
        for piloto in carrera.podio:
            if piloto.nombre in contador_podio:
                contador_podio[piloto.nombre] += 1
            else:
                contador_podio[piloto.nombre] = 1
        max_podios = max(contador_podio.values())
        for piloto, podios in contador_podio.items():
            if podios == max_podios:
                resultado[carrera.circuito] = piloto
                break
    return resultado


