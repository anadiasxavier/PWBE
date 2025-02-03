#EXCERCICIO 1

'''class Circulo:
    def __init__(self, raio):
        self.raio = raio
        self.pi = 3.14

    def perimetro(self):
        return 2*self.pi*self.raio
       
    def area(self):
        return self.pi*self.raio**2

raio = float (input("Digite o valor do raio do círculo: "))
circulo = Circulo(raio)

area1 = circulo.area()
perimetro1 = circulo.perimetro()


print(f"A área da circunferência é {area1} e {perimetro1} ")'''

#EXERCICIO 2

'''class ContaBancaria:
    def __init__(self, nome, numeroConta , saldo):
        self.nome = nome
        self.numeroConta = numeroConta
        self.saldo = saldo

    def depositar(self):
        deposito = float (input("Digite o valor a ser depositado: "))
        self.saldo += deposito
        print(f"O seu deposito deu certo! novo saldo: {self.saldo}")
    
    def saque(self):
        saque = float (input("Digite o valor a ser sacado: "))
        self.saldo -= saque
        print(f"O seu saque deu certo! novo saldo: {self.saldo}")
    
    def mostrar_saldo(self):
        print(f"O seu saldo é: {self.saldo}")
    
    def opcao (self):
        
        while True: 
            opcao = int (input(f"1-Depósito 2-Saque 3-Saldo n\ Digite a opção escolhida: "))

            if opcao == 1:
                self.depositar()
            elif opcao == 2:
                self.saque()
            elif opcao == 3:
                self.mostrar_saldo()


def main():
    nome = (input("Digite o seu nome: "))
    numeroConta = int (input("Digite o número da sua conta: "))
    saldo = 100
    conta = ContaBancaria(nome, numeroConta , saldo)
    conta.opcao ()

main()'''

#EXERCICIO 3

'''class retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcularArea(self):
        return self.largura*self.altura
    
    def calcularPerimetro(self):
        return (self.largura+self.altura)*2

retangulo1 = retangulo (30, 15)
area = retangulo1.calcularArea()
perimetro = retangulo1.calcularPerimetro()
print(f"A área do retangulo é {area}, e o seu perimetro é {perimetro}")'''

#EXERCICIO 4

'''class aluno:
    def __init__(self, nome, matricula):
        self.nome = nome 
        self.matricula = matricula
        

    def notas(self):
        nota1 = float (input("Digite sua primeira nota: "))
        nota2 = float (input("Digite sua segunda nota: "))
        nota3 = float(input("Digite sua terceira nota: "))

        media = (nota1 + nota2 + nota3)//3

        if media >= 5:
            print("Você está aprovado.")
        elif media >=2.5 and media < 5:
            print("Você está em recuperação.")
        else:
            print("Você está reprovado.")


nome = str (input("Digite o seu nome: "))
matricula = int (input("Digite o número da sua matricula: "))
medias = aluno(nome, matricula)
medias.notas()'''

#EXERCICIO 5

'''class funcionario:
    def __init__(self, nome, salario, cargo):
        self.nome = nome 
        self.salario = salario
        self.cargo = cargo 

    def descontos(self):
        imposto = self.salario / 15
        beneficio = 300
        salarioliquido = self.salario + beneficio - imposto
        print(f"O seu salário com os descontos são: {salarioliquido:.2f}")

   

nome = str (input("Digite o seu nome: "))
salario = float(input("Digite o seu salario: "))
cargo = str (input("Digite o seu cargo: "))

fun = funcionario(nome, salario, cargo)
fun.descontos()'''

#EXERCICIO 6

'''class Produto:
    def __init__(self, nome, preco, quantidadeEstoque):
        self.nome = nome 
        self.preco = preco
        self.quantidadeEstoque = quantidadeEstoque

    def valor(self):
        valorEstoque = self.quantidadeEstoque * self.preco
        print(f"O valor do produto em estoque é {valorEstoque}")

        if self.quantidadeEstoque >= 0:
            print ("O produto está disponível.")
        else: 
            print("O produto está indisponível.")

nome = str (input("Digite o nome do produto: "))
preco = float (input("Digite o preço do produto: "))
quantidadeEstoque = int (input("Digite a quantidade do produto em estoque: "))

produto = Produto(nome, preco, quantidadeEstoque)
produto.valor()'''

#EXERCICIO 7

'''class triangulo:
    def __init__(self,lado1, lado2, lado3, base, altura):
        self.ladoum = lado1
        self.ladodois = lado2
        self.ladotres = lado3
        self.base = base
        self.altura = altura

    def validar(self):
        if self.ladoum + self.ladodois > self.ladotres and  self.ladoum + self.ladodois +self.ladotres > 0:
            print("O Triângulo é válido")
        else:
            print("O triângulo não é válido.")
    
    def area(self):
        calculoArea = (self.base*self.altura)//2
        print(f"O calculo da area do triângulo é {calculoArea}")



medidasTriangulo = triangulo(15, 15 , 25 , 20 , 30)
medidasTriangulo.validar()
medidasTriangulo.area()'''

#EXERCICIO 8
'''class carro:
    def __init__(self, marca, modelo, velocidade):
        self.marca = marca
        self.modelo = modelo
        self.velocidade = velocidade

    def controle(self):
        while True: 
            opcao = int(input("Digite a opcao que deseja realizar : 1-Frear 2-Acelerar : "))

            if opcao == 1:
                quantidadeVelocidade = int (input("Quanto de velocidade deseja frear?"))
                velocidadeMedia = self.velocidade - quantidadeVelocidade
                print(f"A sua velocidade atual agora é: {velocidadeMedia}")
            
            elif opcao == 2:
                quantidadeVelocidade1 = int (input("Quanto de velocidade deseja acelerar?"))
                velocidadeMedia1 = self.velocidade + quantidadeVelocidade1 
                print(f"A sua velocidade atual agora é: {velocidadeMedia1}")

marca = str (input("Digite a marca do seu veículo: "))
modelo = str (input("Digite o modelo do seu carro: "))
velocidade = int (input("Digite a velocidade atual do carro: "))

Carro = carro(marca, modelo, velocidade)
Carro.controle()
'''
#EXERCICIO 9 
'''class paciente:
    def __init__(self, nome, idade, consulta):
        self.nome = nome
        self.idade = idade
        self.consulta = consulta
    
    def historicoConsulta(self):
    
     while True :
        opcao = int (input("Deseja adicionar uma nova consulta ao seu histórico? 1-Sim 2-Não"))

        if opcao == 1:
            novaConsulta = str (input("Digite a sua nova consulta: "))
            print(f"O seu histório de consultas realizadas é: {consulta}, {novaConsulta}")
        elif opcao ==2:
            break

        print (f"O seu histórico atual de consultas é {consulta}, {novaConsulta}")
    

nome = str (input("Digite o seu nome: "))
idade = int (input("Digite a sua idade: "))
consulta = str (input("Digite o seu historico de consultas: "))
Paciente = paciente(nome, idade, consulta)
Paciente.historicoConsulta()'''

#EXERCICIO 10 
class livro:
        def __init__(self, titulo, autor , numPagina):
            self.titulo = titulo
            self.autor = autor
            self.numPagina = numPagina
            self.estoque = 0

        def emprestarLivro(self):
            opcao = int(input("Deseja emprestar um livro? \n1-Sim \n2-Não "))

            if opcao == 1:
                self.estoque -= 1
                print("Livro emprestado com sucesso!")
            elif opcao == 2:
                print ("Livro não emprestado")
            else:
                print("Essa opção não existe.")
            
        def devolverLivro(self):
            opcao1 = int(input("Deseja delvolver um livro? \n1-Sim \n2-Não "))

            if opcao1 == 1:
                self.estoque += 1
                print("Livro devolvido com sucesso!")
            elif opcao == 2:
                print ("Livro não devolvido")
            else:
                print("Essa opção não existe.")

        def verificar(self):
            nome = str(input("Qual livro deseja verificar? "))

            if nome == self.titulo:
                print("Livro disponível.")
            else:
                print("Livro indisponível.")



titulo = str (input("Digite o titulo do livro: "))
autor = str (input("Digite o autor do livro: "))
numPagina = int (input("Digite o número de páginas do livro: "))

livro = livro(titulo, autor, numPagina)
livro.emprestarLivro()
livro.devolverLivro()
livro.verificar()