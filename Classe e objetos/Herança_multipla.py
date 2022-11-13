class Animal:
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
    

class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        self.cor_pelo = cor_pelo
        super().__init__(**kw)

class Ave(Animal):
     def __init__(self, cor_bico, **kw):
        self.cor_bico = cor_bico
        super().__init__(**kw)

class Cachorro(Mamifero):
    pass

class Gato(Mamifero):
    pass

class Leao(Mamifero):
    pass

class Ornitorrico(Mamifero, Ave):
    pass

gato = Gato(nro_patas = 4, cor_pelo="Branco")
print(gato)

ornitorrinco = Ornitorrico(nro_patas = 2, cor_pelo = "Verde", cor_bico = "Azul")
print(ornitorrinco)