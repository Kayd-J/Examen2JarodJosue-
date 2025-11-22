import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import pytest
from Examen2 import MiClase


# ObtieneValencia tests (4)
def test_obtiene_valencia_no_impares():
    obj = MiClase(0, 0, 0, [], [])
    assert obj.ObtieneValencia(2468) == 0


def test_obtiene_valencia_todos_impares():
    obj = MiClase(0, 0, 0, [], [])
    assert obj.ObtieneValencia(13579) == 5


# DivisibleTempo tests (4)
def test_divisible_tempo_normal():
    obj = MiClase(0, 0, 0, [], [])
    assert obj.DivisibleTempo(10) == [1, 2, 5, 10]


def test_divisible_tempo_primo():
    obj = MiClase(0, 0, 0, [], [])
    assert obj.DivisibleTempo(13) == [1, 13]



# ObtieneMasBailable tests (4)
def test_obtiene_mas_bailable_normal():
    obj = MiClase(0, 0, 0, [], [])
    assert obj.ObtieneMasBailable([0.8, 0.9, 0.7]) == 0.9


def test_obtiene_mas_bailable_vacia():
    obj = MiClase(0, 0, 0, [], [])
    assert obj.ObtieneMasBailable([]) is None


# VerificaListaCanciones tests (4)
def test_verifica_lista_canciones_todas_validas():
    obj = MiClase(0, 0, 0, [], [])
    assert obj.VerificaListaCanciones(["Canción 1", "Canción 2"]) is True


def test_verifica_lista_canciones_con_none():
    obj = MiClase(0, 0, 0, [], [])
    assert obj.VerificaListaCanciones(["a", None, "c"]) is False
