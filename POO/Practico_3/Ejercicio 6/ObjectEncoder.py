from ClaseHeladeras import Heladera
from ClaseLavarropas import Lavarropa
from ClaseTelevisores import Televisor
from ClaseLista import Lista
from pathlib import Path
import json
class ObjectEncoder(object):

    def decodificarDiccionario(self,lista : Lista):
        diccionario = self.leerJSONArchivo("Aparatos.json")
        for elem in diccionario:
            if '__class__' not in elem:
                    print("No se encuentra el diccionario")
            else:
                class_name=elem['__class__']
                class_=eval(class_name)
                if class_name == "Heladera":
                    atributos = elem['__atributos__']
                    H = class_(**atributos)
                    lista.agregarAparato(H)
                elif class_name == "Televisor":
                    atributos = elem['__atributos__']
                    T = class_(**atributos)
                    lista.agregarAparato(T)
                elif class_name == "Lavarropa":
                    atributos = elem['__atributos__']
                    L = class_(**atributos)
                    lista.agregarAparato(L)
    def retornarObjeto(self):
        O = None
        marca = input("Ingrese la marca: ")
        model = input("Ingrese el modelo: ")
        col = input("Ingrese el color: ")
        pais = input("Ingrese el pais: ")
        precio = input("Ingrese el precio: ")
        tipo = input("Ingrese el tipo de aparato (Televisor-Heladera-Lavarropa): ")
        if tipo == "Heladera":
            capacidad = input("Ingrese capacidad: ")
            freezer = input("Ingrese si posee freezer (True o False): ")
            cicl = input("Ingrese si posee ciclica (True o False): ")
            O = Heladera(marca, model, col, pais, precio, capacidad, freezer, cicl)
        elif tipo == "Televisor":
            tipo_pant = input("Ingrese tipo de pantalla((crt, vga, svga, plasma, lcd, led, TouchScreen, MultiTouch)): ")
            pulgad = input("Ingrese las pulgadas: ")
            tipo_def = input("Ingrese el tipo de definicion (SD,HD,FULL HD): ")
            conexion = input("Ingrese si posee conexion a internet (True o False): ")
            O = Televisor(marca, model, col, pais, precio, tipo_pant, pulgad, tipo_def, conexion)
        elif tipo == "Lavarropa":
            capacidad = input("Ingrese la capacidad en Kg: ")
            velocidad = input("Ingrese la velocidad de centrifugado: ")
            ct = input("Ingrese la cantidad de programas: ")
            tipo = input("Ingrese el tipo de carga(Frontal o Superior): ")
            O = Lavarropa(marca, model, col, pais, precio, capacidad, velocidad, ct, tipo)
        return O
    def guardarJSONArchivo(self, diccionario, archivo):
        with Path(archivo).open("w", encoding="UTF-8") as destino:
            json.dump(diccionario, destino, indent=4)
            destino.close()
    def leerJSONArchivo(self,archivo):
        with Path(archivo).open(encoding="UTF-8") as fuente:
            diccionario=json.load(fuente)
            fuente.close()
            return diccionario

    def convertirTextoADiccionario(self, texto):
        return json.loads(texto)