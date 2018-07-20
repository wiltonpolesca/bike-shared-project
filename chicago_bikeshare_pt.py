# coding: utf-8

# Começando com os imports
import csv
import matplotlib.pyplot as plt

# Vamos ler os dados como uma lista
print("Lendo o documento...")
with open("data/chicago/chicago.csv", "r") as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)
print("Ok!")

# Vamos verificar quantas linhas nós temos
print("Número de linhas:")
print(len(data_list))

# Imprimindo a primeira linha de data_list para verificar se funcionou.
print("Linha 0: ")
print(data_list[0])
# É o cabeçalho dos dados, para que possamos identificar as colunas.
# Estrutura do cabeçalho
#      0              1           2                  3             4               5          6            7  
#['Start Time', 'End Time', 'Trip Duration', 'Start Station', 'End Station', 'User Type', 'Gender', 'Birth Year']

# Imprimindo a segunda linha de data_list, ela deveria conter alguns dados
print("Linha 1: ")
print(data_list[1])

input("Aperte Enter para continuar...")
def wlps_column_to_list(data, index):
    column_list = []
    [column_list.append(item[index]) for item in data]
    # Dica: Você pode usar um for para iterar sobre as amostras, pegar a feature pelo seu índice, e dar append para uma lista
    return column_list

#---------------------------------- TAREFA 1 ----------------------------------
# Imprima as primeiras 20 linhas usando um loop para identificar os dados.
print("\n\nTAREFA 1: Imprimindo as primeiras 20 amostras")
print([line for line in data_list[:20]])

# Vamos mudar o data_list para remover o cabeçalho dele.
data_list = data_list[1:]
input("Aperte Enter para continuar...")


#---------------------------------- TAREFA 2 ----------------------------------
# Imprima o `gênero` das primeiras 20 linhas
print("\nTAREFA 2: Imprimindo o gênero das primeiras 20 amostras")
print ([line[6] for line in data_list[:20]])
input("Aperte Enter para continuar...")


#---------------------------------- TAREFA 3 ----------------------------------
#Crie uma função para adicionar as colunas(features) de uma lista em outra lista, na mesma ordem
def column_to_list(data, index):
    """
    Função responsável por retornar uma nova lista contendo os dados de uma colunda qualquer de outra lista
    Argumentos:
        data: Lista com os dados originais.
        index: Indice da coluna na lista original que se deseja extrair os dados.
    Retorna:
        Um novo array contendo os valores da coluna informada na lista original.
    """
    column_list = []
    [column_list.append(item[index]) for item in data]
    # Dica: Você pode usar um for para iterar sobre as amostras, pegar a feature pelo seu índice, e dar append para uma lista
    return column_list

# Vamos checar com os gêneros se isso está funcionando (apenas para os primeiros 20)
print("\nTAREFA 3: Imprimindo a lista de gêneros das primeiras 20 amostras")
print(column_to_list(data_list, -2)[:20])

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(column_to_list(data_list, -2)) is list, "TAREFA 3: Tipo incorreto retornado. Deveria ser uma lista."
assert len(column_to_list(data_list, -2)) == 1551505, "TAREFA 3: Tamanho incorreto retornado."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[1] == "Male", "TAREFA 3: A lista não coincide."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora sabemos como acessar as features, vamos contar quantos Male (Masculinos) e Female (Femininos) o dataset tem

#---------------------------------- TAREFA 4 ----------------------------------
# Conte cada gênero. Você NÃO deveria usar uma função par fazer isso.
male = 0
female = 0
for item in data_list:
    if item[6].lower() == 'male':
        male += 1 
    elif item[6].lower() == 'female': 
        female += 1

# Verificando o resultado
print("\nTAREFA 4: Imprimindo quantos masculinos e femininos nós encontramos")
print("Masculinos: ", male, "\nFemininos: ", female)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert male == 935854 and female == 298784, "TAREFA 4: A conta não bate."
# -----------------------------------------------------

input("Aperte Enter para continuar...")

#---------------------------------- TAREFA 5 ----------------------------------
# Por que nós não criamos uma função para fazer isso?
# Crie uma função para contar os gêneros. Retorne uma lista.
# Isso deveria retornar uma lista com [count_male, count_female] (exemplo: [10, 15] significa 10 Masculinos, 15 Femininos)
def count_gender(data):
    """
    Função responsável por contar o número de registros por gênero na lista principal
    Argumentos:
        data: Lista com os dados originais.
    Retorna:
        Dois valores sendo o número de registros com o genero 'male' e o número de registro com o genero 'female'
    """
    male = 0
    female = 0

    for item in data:
        if item[6].lower() == 'male':
            male += 1 
        elif item[6].lower() == 'female': 
            female += 1

    return [male, female]


print("\nTAREFA 5: Imprimindo o resultado de count_gender")
print(count_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(count_gender(data_list)) is list, "TAREFA 5: Tipo incorreto retornado. Deveria retornar uma lista."
assert len(count_gender(data_list)) == 2, "TAREFA 5: Tamanho incorreto retornado."
assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[1] == 298784, "TAREFA 5: Resultado incorreto no retorno!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")

#---------------------------------- TAREFA 6 ----------------------------------
# Agora que nós podemos contar os usuários, qual gênero é mais prevalente?
# Crie uma função que pegue o gênero mais popular, e retorne este gênero como uma string.
# Esperamos ver "Masculino", "Feminino", ou "Igual" como resposta.
def most_popular_gender(data):
    """
    Função responsável retornar qual gênero é mais popular na amostragem de dados
    Argumentos:
        data: Lista com os dados originais.
    Retorna:
        String que representa o gênero mais popular
    """
    answer = ""
    count = count_gender(data)
    if count[0] > count[1]:
        answer = "Masculino"
    elif count[0] < count[1]:
        answer = "Feminino"
    else:
        answer = "Igual"
    return answer


print("\nTAREFA 6: Qual é o gênero mais popular na lista?")
print("O gênero mais popular na lista é: ", most_popular_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(most_popular_gender(data_list)) is str, "TAREFA 6: Tipo incorreto no retorno. Deveria retornar uma string."
assert most_popular_gender(data_list) == "Masculino", "TAREFA 6: Resultado de retorno incorreto!"
# -----------------------------------------------------

# Se tudo está rodando como esperado, verifique este gráfico!
gender_list = column_to_list(data_list, -2)
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Gênero')
plt.xticks(y_pos, types)
plt.title('Quantidade por Gênero')
plt.show(block=True)

input("Aperte Enter para continuar...")

#---------------------------------- TAREFA 7 ----------------------------------
# Crie um gráfico similar para user_types. Tenha certeza que a legenda está correta.
print("\nTAREFA 7: Verifique o gráfico!")
gender_list = column_to_list(data_list, -3)
types = ["Assinante", "Cliente"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Tipo de usuário')
plt.xticks(y_pos, types)
plt.title('Quantidade por tipo de usuário')
plt.show(block=True)

input("Aperte Enter para continuar...")

#---------------------------------- TAREFA 8 ----------------------------------
# Responda a seguinte questão
male, female = count_gender(data_list)
print("\nTAREFA 8: Por que a condição a seguir é Falsa?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = "Porque existem registros onde o gênero não está definido."
print("resposta:", answer)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert answer != "Escreva sua resposta aqui.", "TAREFA 8: Escreva sua própria resposta!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")

#---------------------------------- TAREFA 9 ----------------------------------
# Vamos trabalhar com trip_duration (duração da viagem) agora. Não conseguimos tirar alguns valores dele.
# Ache a duração de viagem Mínima, Máxima, Média, e Mediana. Você não deve usar 
# funções prontas para fazer isso, como max() e min().
trip_duration_list = column_to_list(data_list, 2)
ordered_duration_list = []
min_trip = -1.
max_trip = 0.
mean_trip = 0.
median_trip = 0.
sum_trip = 0.
current_trip = 0.
for item in trip_duration_list:
    try:
        current_trip = float(item)
    except:
        current_trip = 0

    # Acumula o valor da duração das viagens
    sum_trip += current_trip

    ordered_duration_list.append(current_trip)

    # Obtem a menor duração
    if min_trip < 0  or min_trip > current_trip:
        min_trip = current_trip

    # Obtem a maior duração
    if max_trip < current_trip:
        max_trip = current_trip

# Calula a média
count = len(data_list)
mean_trip = sum_trip / count

# Ordena a lista para extrair a mediana
ordered_duration_list = sorted(ordered_duration_list)

# Obtem a mediana (para um conjunto com número par de elementos, a mediana é 
# a média dos dois elementos centrais do conjunto ordenado, caso contrário é o 
# valor do elemento central do conjunto ordenado)
if count % 2 == 0:
    median_trip = (ordered_duration_list[(count//2) -1] + ordered_duration_list[count//2]) / 2
else: 
    median_trip = ordered_duration_list[count//2] 

print("\nTAREFA 9: Imprimindo o mínimo, máximo, média, e mediana")
print("Min: ", min_trip, "Max: ", max_trip, "Média: ", mean_trip, "Mediana: ", median_trip)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert round(min_trip) == 60, "TAREFA 9: min_trip com resultado errado!"
assert round(max_trip) == 86338, "TAREFA 9: max_trip com resultado errado!"
assert round(mean_trip) == 940, "TAREFA 9: mean_trip com resultado errado!"
assert round(median_trip) == 670, "TAREFA 9: median_trip com resultado errado!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")

#---------------------------------- TAREFA 10 ---------------------------------
# Gênero é fácil porque nós temos apenas algumas opções. E quanto a start_stations? Quantas opções ele tem?
# Verifique quantos tipos de start_stations nós temos, usando set()
user_types = set(column_to_list(data_list,3))
print("\nTAREFA 10: Imprimindo as start stations:")
print(len(user_types))
print(user_types)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert len(user_types) == 582, "TAREFA 10: Comprimento errado de start stations."
# -----------------------------------------------------

input("Aperte Enter para continuar...")

#---------------------------------- TAREFA 11 ---------------------------------
# Volte e tenha certeza que você documenteou suas funções. Explique os parâmetros de 
# entrada, a saída, e o que a função faz. Exemplo:
print("\nTAREFA 11: Certifique-se que suas funções estão documentadas.")
def new_function(param1: int, param2: str) -> list:
    """
    Função de exemplo com anotações.
    Argumentos:
        param1: O primeiro parâmetro.
        param2: O segundo parâmetro.
    Retorna:
        Uma lista de valores x.

    """

input("Aperte Enter para continuar...")

#---------------------------------- TAREFA 12 ---------------------------------
# Desafio! (Opcional)
# Crie uma função para contar tipos de usuários, sem definir os tipos
# para que nós possamos usar essa função com outra categoria de dados.
print("Você vai encarar o desafio? (yes ou no)")
answer = "yes"

def count_items(column_list):
    item_types = set()
    count_items = []
    for item in column_list:
        item_types.add(item)
        count_items.append(1)
        
    return item_types, count_items


if answer == "yes":
    # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
    column_list = column_to_list(data_list, -2)
    types, counts = count_items(column_list)
    print("\nTAREFA 11: Imprimindo resultados para count_items()")
    print("Tipos:", types, "Counts:", counts)
    assert len(types) == 3, "TAREFA 11: Há 3 tipos de gênero!"
    assert sum(counts) == 1551505, "TAREFA 11: Resultado de retorno incorreto!"
    # -----------------------------------------------------