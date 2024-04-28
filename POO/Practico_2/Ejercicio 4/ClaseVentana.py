class Ventana:
    __titulo=""
    __x1=0
    __y1=0
    __x2=0
    __y2=0
    def __init__(self,titulo,xiz=0,yiz=0,xde=500,yde=500):
        self.__titulo=titulo
        self.__x1=xiz
        self.__y1=yiz
        self.__x2=xde
        self.__y2=yde
        if xiz < 0 or yiz < 0 or xde > 500 or yde > 500 or xiz >= xde or yiz >= yde:
            print ("Error: Ingreso de coordenadas incorrectas")
    def getTitulo(self):
        return self.__titulo
    def alto (self):
        return self.__y2 - self.__y1
    def ancho (self):
        return self.__x2 - self.__x1
    def mostrar(self):
        print("Titulo: {} Xsuperior: {} Ysuperior: {} Xinferior: {} Yinferior {}".format(self.getTitulo(),self.__x1,self.__y1,self.__x2,self.__y2))
    def moverDerecha(self,posiciones=1):
        if self.__x1+posiciones>=0:
            self.__x1+=posiciones
        if self.__x2+posiciones<=500:
            self.__x2+=posiciones
    def moverIzquierda(self,posiciones=1):
        if self.__x1-posiciones>=0:
            self.__x1-=posiciones
        if self.__x2-posiciones<=500:
            self.__x2-=posiciones
    def subir (self,posiciones=1):
        if self.__y1 + posiciones >= 0:
            self.__y1 += posiciones
        if self.__y2 + posiciones <= 500:
            self.__y2 += posiciones
    def bajar (self,posiciones=1):
        if self.__y1 - posiciones >= 0:
            self.__y1 -= posiciones
        if self.__y2 - posiciones <= 500:
            self.__y2 -= posiciones

