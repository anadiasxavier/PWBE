class Cachorro:
    def __init__(self, nome, raca, cor, idade)
        self.nome = nome 
        self.raca_cachorro = raca
        self.cor = cor
        self.idade = idade
        self.orelhas = 2

    def latir(self, kms):
        print(f"{self.nome} diz: au au")
    
    def correr(self):
        print(f"{self.nome} correu {kms} km.")

# cachorro_da_Luana= Cachorro("Pituco", "Vira-Lata", "Caramelo" )

# cachorro_da_Luana.correr(35)

class Livro:
    def __init__(self, categoria, titulo, autor, personagens, indicacao)
        self.genero = categoria
        self.titulozinho
        self.escritor = autor
        self.indicacao = idicacao
        self.personagens = personagens
    
    def abrir(self, pagina):
        print(f"O livro {self.titulozinho} foi aberto ma pagina {pagina}")
    def__str__(self):
    return f"{self.titulozinho} do genero {self.genero} escrita por {self.escritor}"

    def __eq__(self, value):
        if (isinstance(value, Livro)):
             titulo_igual = self.titulozinho == value.titulo
             autores_iguais = self.escritor == value.escritor
             return titulo_igual and autores_iguais
        else:
            return False

       



livro_da_kamila = Livro("Romance", "Crepusculo", "JK. ROWLIG", ["Bela", "Ewdard"], 14)
livro_da_kamila.abrir(10)

print(livro_da_kamila)

