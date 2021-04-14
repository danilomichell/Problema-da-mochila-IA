# Problema da mochila
## Desenjvolvedor
* Danilo Michell Lisboa de Freitas
## O que é?
O problema da mochila (em inglês, Knapsack problem) é um problema de optimização combinatória. O nome dá-se devido ao modelo de uma situação em que é necessário preencher uma mochila com objetos de diferentes pesos e valores. O objetivo é que se preencha a mochila com o maior valor possível, não ultrapassando o peso máximo.
## O que foi utilizado?
Foi utilizado a biblioteca ramdom para gerar números eleátorios alem da estrela d vez, a biblioteca deep, que serve como um facilitador da implementação de um algoritmo genético. A biblioteca deep é extremamente simples e robusta, disponibilizando ferramentas já prontas que facilitam a vida do desenvolvedor de um algoritmo genético, a exemplo de algoritmos de mutação, seleção e crossover já implementados e que serão usados caso o programador precise.
## Como o programa funciona?
### Geral
O usuário irá fornecer o valor do peso da machila e com isso o programa gera individuos aléatorios que serão colocados na mochila e com isso se utilizará das ferramentas da biblioteca deep.
### Avaliaçao dos indivíduos
A avaliação será feita da seguinte forma, ele irá pegar o peso do primeiro item e irá somar com o do segundo, o mesmo será feito com o valor e isso será feito com todos os indivíduos, caso o peso ultrapasse o da mochila essa geração não será utilizada como a melhor. Esse processo será feito em toda a geração.
### Mutação e crossover
O prograva utilizará a mutação e o crossover para estarem modificando geração em geração a fim de melhorar cada geração. Todas as gerações serão avaliadas e um função irá retornar as 10 melhores. Porém apenas a melhor será exibida com todos os itens, com seu peso e valor e no fim será exibido o valor total e o peso total da mochila

