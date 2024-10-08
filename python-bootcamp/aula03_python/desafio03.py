# Estruturas de Controle de Fluxo

'''
Integre na solução anterior um fluxo de While que repita o fluxo até que o usuário insira as 
informações corretas
'''

# Variáveis para controle do loop

CONSTANTE_BONUS = 1000
nome_valido = False
salario_valido = False
bonus_valido = False

# Verificação do nome
while not nome_valido:
    nome_usuario = input("Por favor, digite seu nome: ").strip()

    if len(nome_usuario) == 0:
        print("Você não digitou nenhum caractere")

    elif nome_usuario.isspace():
        print("Você digitou apenas espaços")
    
    else:
        nome_valido = True

# Verificação do salário
while not salario_valido:
    try:
        salario_usuario = float(input("Agora, insira o seu salário: ").replace(",", "."))

        if salario_usuario < 0:
            print("Por favor, insira um salário positivo.")
        
        else:
            salario_valido = True

    except ValueError:
        print("Por favor, insira apenas números.")

# Verificação do bonus
while not bonus_valido:
    try:
        bonus_usuario = float(input("Por fim, digite o bonus recebido: ").replace(",", "."))

        if bonus_usuario < 0:
            print("Por favor, insira um salário positivo.")
        
        else:
            bonus_valido = True

    except ValueError:
        print("Por favor, insira apenas números.")

# Cálculo do bonus
bonus_calculado = CONSTANTE_BONUS + (salario_usuario * bonus_usuario)

# Impressão da mensagem para o usuário
print(f"Olá {nome_usuario}, o seu valor bônus foi de {bonus_calculado}")