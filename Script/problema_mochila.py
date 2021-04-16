import pprint
import random
from deap import creator, base, tools, algorithms

# Definindo peso máximo da mochila
PESO_MAXIMO = int(input("Digite o peso máximo da mochila: "))
print(f"O peso maximo é {PESO_MAXIMO}\n")


# Criando itens
def colocarItens(numItems):
    items = []
    for x in range(numItems):
        items.append({"peso": random.randint(1, 10), "valor": random.uniform(1, 100)})
    return items


# Adicionando os itens criados a uma lista
items = colocarItens(20)
print("items criados e colocados dentro da lista: ")
for item in items:
    print(item)

# Define o tipo fitness: Um objetivo com maximização
creator.create("Fitness", base.Fitness, weights=(1.0,))

# Define o individuo com a fitness criada
creator.create("Individuo", list, fitness=creator.Fitness)

# Toolbox para inicialização dos componentes
toolbox = base.Toolbox()

# Atributo booleano criado de forma aleatório
toolbox.register("attr_bool",
                 random.random)

# Individuo do tipo booleano
toolbox.register("individuo",
                 tools.initRepeat, creator.Individuo, toolbox.attr_bool, n=10)

# Criação da população para o inicio da mutação
toolbox.register("populacao",
                 tools.initRepeat, list, toolbox.individuo)


# Avalia o individuo
def avaliador(individuo):
    value = 0
    weight = 0
    for index in range(len(individuo)):
        if individuo[index] > 0.5:
            value += items[index]['valor']
            weight += items[index]['peso']
    if (weight > PESO_MAXIMO):
        return 100000000, 0
    return weight, value


'''def mutacao(individual):
    if random.random() < 0.5:
        if len(individual) > 0:     # We cannot pop from an empty set
            individual.remove(random.choice(sorted(tuple(individual))))
    else:
        individual.add(random.randrange(20))
    return individual,'''


# Função de pegar itens
def obterItems(individual):
    _items = []
    for index in range(len(individual)):
        if individual[index] > 0.5:
            _items.append((index, items[index]))
    return _items


# registra a função de fitness
toolbox.register("evaluate", avaliador)

# Toobox do crossover
toolbox.register("mate", tools.cxTwoPoint)  # crossover
# Toobox da mutação
toolbox.register("mutate", tools.mutFlipBit, indpb=0.05)  # mutação

# Toobox do método de seleção
toolbox.register("select", tools.selNSGA2)

# tamanho da população
population = toolbox.populacao(n=500)
'''def main():
    NGEN = 50
    MU = 50
    LAMBDA = 100
    CXPB = 0.7
    MUTPB = 0.2

    pop = toolbox.population(n=MU)
    hof = tools.ParetoFront()
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", numpy.mean, axis=0)
    stats.register("std", numpy.std, axis=0)
    stats.register("min", numpy.min, axis=0)
    stats.register("max", numpy.max, axis=0)

    algorithms.eaMuPlusLambda(pop, toolbox, MU, LAMBDA, CXPB, MUTPB, NGEN, stats,
                              halloffame=hof)

    return pop, stats, hof'''

# Processo de evoluão
NGEN = 50
for i in range(NGEN):

    offspring = algorithms.varAnd(population, toolbox, cxpb=0.5, mutpb=0.1)

    # avaliação dos individuos
    fits = toolbox.map(toolbox.evaluate, offspring)

    # liga cada indivíduo ao seu fitness
    for fit, ind in zip(fits, offspring):
        ind.fitness.values = [fit[1]]

    # usa a toobox de seleção para gerar a nova população
    population = toolbox.select(offspring, k=len(population))
    best = tools.selBest(population, k=1)
    print(f"Melhor individuo da geração {i+1}")
    print(best)

# retorna o melhor individuo da seleção
best10 = tools.selBest(population, k=10)

# Imprime o melhor individuo
print()
print("Melhor individuo")
print(best10[0])
print()

print('Peso/valor dos dos itens do melhor individuo')
for item in obterItems(best10[0]):
    print(item)
print()

# Peso e valor total da mochila
print(f"O peso é {sum(list(map(lambda x: x[1]['peso'], obterItems(best10[0]))))}")
print(f"O valor é {sum(list(map(lambda x: x[1]['valor'], obterItems(best10[0]))))}")
