class Bicicleta:

#Construtores = metodos __init__. É executado quando uma nova instancia da classe é criada. 
#Self é uma referencia para o objeto. È similar com o this que usamos em java

    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

#Criação dos métodos (ações ou funções da classe)
 
    def buzinar(self):
        print("Plim plim...")

    def parar(self):
        print("Parando bicicleta...")    
        print("Bicicleta parada!")    

    def correr(self):
        print("Vrummmm")    

    #def __str__(self):
    #    return f"Bicicleta: cor={self.cor}, modelo={self.modelo}, ano={self.ano}, valor={self.valor}" 

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

b1 = Bicicleta ("vermelha", "caloi", 2022, 600)
b1.buzinar()
b1.correr()
b1.parar()

#Para acessar os atributos:

#print(b1.cor, b1.modelo, b1.ano, b1.valor)

b2 = Bicicleta("verde", "monark", 200, 189)
Bicicleta.buzinar(b2)
print(b2.cor)
print(b2)





