class Email:
    __idCuenta= ""
    __dominio  = ""
    __tip_dom = ""
    __contraseña = ""
    def __init__(self,id,dom,tipdom,contra):
        self.__idCuenta=id
        self.__dominio=dom
        self.__tip_dom=tipdom
        self.__contraseña=contra
    def retornarEmail(self):
        return(self.__idCuenta+"@"+self.__dominio+"."+self.__tip_dom)
    def getDominio(self):
        return (self.__dominio)
    def crearCuenta(self,correo):
        adr=correo.split("@")
        tip=adr[1].split(".")
        self.idCuenta=adr[0]
        self.dominio=tip[0]
        self.tip_dom=tip[1]
    def modifica_contra(self,oldpass):
        if self.__contraseña == oldpass:
            self.__contraseña= input("Ingrese nueva contraseña:")
            print("Su contraseña se modifico a: "+self.__contraseña)
        else:
            print("Contraseña incorrecta")