import random

import numpy

from deap import algorithms
from deap import base
from deap import creator
from deap import tools

IND_INIT_SIZE = 5
MAX_ITEM = 50
MAX_WEIGHT = 50
NBR_ITEMS = 20

#Cria uma seed para o programa
random.seed(64)

#Inicia o dicionário {chave,valor}
items = {}
# Adiciona os valores ao dicionario.
for i in range(NBR_ITEMS):
    items[i] = (random.randint(1, 10), random.uniform(0, 100))

#Cria as fitness do programa
creator.create("Fitness", base.Fitness, weights=(-1.0, 1.0))
creator.create("Individual", set, fitness=creator.Fitness)

toolbox = base.Toolbox()

# Cria a caixa de ferramentas do gerador
toolbox.register("attr_item", random.randrange, NBR_ITEMS)

