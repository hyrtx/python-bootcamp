# Desafio: Refatorar o desafio da aula 03 usando Dicionário, Type Hint e Funcões.

# Variáveis para controle do loop

CONSTANTE_BONUS: float = 1000 # O Bonus sempre parte de R$ 1000

def validacao_nome() -> str:
    '''
    Função para verificar e assegurar que o nome digitado pelo usuário é valido,
    retornando o salário se positivo.
    '''    
    # Loop while para garantir que o preenchimento correto do nome seja feito
    while True:
        nome_usuario: str = input("Por favor, digite seu nome: ").strip()

        # Assegura que a variável nome_usuario não esteja vazia
        if len(nome_usuario) == 0:
            print("Você não digitou nenhum caractere")
        
        # Impede que a variável nome_usuario não seja composta de apenas espaços.
        elif nome_usuario.isspace():
            print("Você digitou apenas espaços")
    
        else:
            break
    
    return nome_usuario

def validacao_salario() -> float:
    '''
    Função para verificar e assegurar que o salário foi digitado corretamente, retornando o 
    salário do usuário.
    '''
    # Loop while para garantir que o salário seja corretamente preenchido
    while True:

        try:
            # Replace para garantir que o preenchimento possa ser feito por vírgula
            salario_usuario: float = float(input("Agora, insira o seu salário: ").replace(",", "."))
            
            # Condicional para verificar se o salário é positivo
            if salario_usuario < 0:
                print("Por favor, insira um salário positivo.")
            
            else:
                break

        except ValueError:
            print("Por favor, insira apenas números.")
    
    return salario_usuario

def validacao_bonus() -> float:
    '''
    Função para verificar e assegurar que o bônus foi digitado corretamente, retornando o 
    valor de bônus do usuário.
    '''    
    # # Loop while para garantir que o bônus seja corretamente preenchido
    while True:

        try:
            # Replace para garantir que o preenchimento possa ser feito por vírgula
            bonus_usuario: float = float(input("Por fim, digite o bonus recebido: ").replace(",", "."))
            
            # Condicional para verificar se o bonus é positivo
            if bonus_usuario < 0:
                print("Por favor, insira um bonus positivo.")
            
            else:
                break

        except ValueError:
            print("Por favor, insira apenas números.")
    
    return bonus_usuario

def registro_usuario() -> dict:
    usuario: dict = {}
    usuario["nome"] = validacao_nome()
    usuario["salario"] = validacao_salario()
    usuario["bonus"] = validacao_bonus()
    return usuario

dados_usuario = registro_usuario()

# Cálculo do bonus
bonus_calculado: float = CONSTANTE_BONUS + (dados_usuario["salario"] * dados_usuario["bonus"])

# Impressão da mensagem para o usuário
print(f"Olá {dados_usuario['nome']}, o seu valor bônus foi de {bonus_calculado}")