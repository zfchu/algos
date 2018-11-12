# coding=utf-8
import string
import random
import editdistance
from array import array
import matplotlib.pyplot as plt

gene_library = string.printable # 基因库，每个字符是一个基因

target = "Hello, world!" # 目标字符串
n = 400 # 初始种群数量
mutation_rate = 0.0005 # 突变率，会影响收敛速度
reproduction_rate = 2 # 繁殖速度
max_generation = 5000 # 最大进化次数
threshold = 0.2 # 当 target 在种群中的比例超过 threshold 时结束

def random_string(n):
    '''生成一个长度为 n 的字符串，即一个个体的基因'''
    return ''.join(random.choice(gene_library) for _ in range(n))

def similarity(p1, p2):
    '''计算两个个体的相似度，通常p2=target，相似度计算方法对收敛速度影响很大。相似度要介于[0, 1]之间'''
    from difflib import SequenceMatcher
#     sim = SequenceMatcher(None, p1, p2).ratio() # 基于相同字符数
    sim =  1.0/(editdistance.eval(p1, p2)+1) # 基于编辑距离
    return sim

def mating(str1, str2):
    '''交配， 产生一个后代'''
    assert(len(str1) == len(str2))
    idx = range(len(str1))
    random.shuffle(idx)
    chars = array('c', ' '* len(str1))
    pos = len(idx)/2
    for i in idx[:pos]:
        chars[i] = str1[i]
    for i in idx[pos:]:
        chars[i] = str2[i]
    return chars.tostring()

def mutation(gene):
    '''基因突变，以一定的概率随机改变每一个基因'''
    chars = array('c', gene)
    for i in xrange(len(gene)):
        prob = random.random()
        if prob < mutation_rate:
            chars[i] = random.choice(gene_library)
    return chars.tostring()

def random_element(elements):
    '''从 elements 随机选择一个，用于随机交配'''
    assert isinstance(elements, list)
    return elements[random.randint(0, len(elements)-1)]

def reach_threshold(population):
    '''population 的类型是 list<tuple<candidate, similarity>>'''
    return len([tup for tup in population if tup[1] == 1.0]) * 1.0 / len(population) >= threshold

def main(population):
    '''进化 generation 次，每次进化都淘汰最不相似的样本，保留最相似样本'''
    best_similarity = []
    avg_similarity = []
    worst_similarity = []

    population = [(candidate, similarity(candidate, target)) for candidate in population]
    population.sort(key=lambda tup:tup[1], reverse=True)
    generation = 0

    best_similarity.append(population[0][1])
    avg_similarity.append(sum([tup[1] for tup in population]) * 1.0 / len(population))
    worst_similarity.append(population[-1][1])

    while True:
        if reach_threshold(population):
            print "reach threshold in %d generation." % generation
            break
        if generation > max_generation:
            print 'max_generation reached.'
            break

        new_population = []
        for j in xrange(int(reproduction_rate * n)):
            child = mutation(mating(random_element(population)[0], random_element(population)[0]))
            new_population.append((child, similarity(child, target)))
        new_population.sort(key=lambda tup:tup[1], reverse=True)
        population = new_population[:n]
        generation += 1

        best_similarity.append(population[0][1])
        avg_similarity.append(sum([tup[1] for tup in population]) * 1.0 / len(population))
        worst_similarity.append(population[-1][1])

    population = [tup[0] for tup in population]
    return population, generation, (best_similarity, avg_similarity, worst_similarity)

population = [random_string(len(target)) for i in xrange(n)] # 初始种群
result, generation, statistics = main(population)

X = range(generation+1)
plt.plot(X, statistics[0], color="blue", label='best similarity')
plt.plot(X, statistics[1], color="green", label='avg similarity')
plt.plot(X, statistics[2], color="red", label='worst similarity')
plt.legend(loc='upper left', frameon=False)
plt.xlabel('generation')
plt.ylabel('similarity')
plt.show()
print result[0]
print result[-1]
