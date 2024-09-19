# Função para calcular a média das notas
def calcular_media(notas):
    return sum(notas) / len(notas)

# Função para verificar se o aluno está aprovado ou reprovado
def verificar_aprovacao(media):
    if media >= 8:
        return "Aprovado"
    else:
        return "Reprovado"

# Lê as notas de 4 alunos
alunos = {}
for i in range(4):
    nome = input(f"Digite o nome do aluno {i+1}: ")
    notas = []
    
    for j in range(4):  # Lê 4 notas de cada aluno
        nota = float(input(f"Digite a nota {j+1} do aluno {nome}: "))
        notas.append(nota)
    
    # Calcula a média e verifica aprovação
    media = calcular_media(notas)
    resultado = verificar_aprovacao(media)
    
    # Armazena o resultado no dicionário
    alunos[nome] = {
        'notas': notas,
        'media': media,
        'resultado': resultado
    }

# Exibe os resultados de todos os alunos
for nome, dados in alunos.items():
    print(f"\nAluno: {nome}")
    print(f"Notas: {dados['notas']}")
    print(f"Média: {dados['media']:.2f}")
    print(f"Resultado: {dados['resultado']}")