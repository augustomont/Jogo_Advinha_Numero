

nome = input("Qual o seu nome? ")

def boas_vindas(nome = "Fulano"):
    print(f"""  Olá, {nome}! 
    É um prazer te conhecer!
    
    """)

#boas_vindas() - chama a função sem argumento
boas_vindas(nome)

tentativas = []
def advinhe(*args):
  tentativas.append(args)

def numero_secreto(num):
  try:
    if num == 7:
      return print(f"""
      {nome}, você Acertou! 
      Voce tentou {len(tentativas)} vezes. 
      Esses foram o seus palpites: 
      {tentativas} """)
    elif num > 10 or num < 0:
      print("Número inválido!")
    else:
      print("Errou!")
  except ValueError:
    print("Isso nao parece ser um número! Tente novamente.")

print("Bem vindo ao jogo de adivinhação!")
numero = -1
while numero != 7:
    numero = int(input("""Escolha um número entre 0 e 10: """))
    if len(tentativas) > 2:
      print("Você ultrapassou o limite de tentativas!")
      break
    advinhe(numero)
    numero_secreto(numero)
