import random
Data = {
    "capacity": 10,
    "weight": [2, 1, 5, 4],
    "value":  [300, 200, 400, 500],
    "NumberOfItems": 4,
}



def crossoversp(p1,p2,cp):
    child1=p1[:cp]+p2[cp:]
    child2=p2[:cp]+p1[cp:]
    return child1,child2

def mutate(chr,mutationchance):
    global Data
    if random.random()<mutationchance:
        idx=random.randint(0,Data["NumberOfItems"]-1)
        chr[idx]= 1-chr[idx]
    return chr

def rndchromosome():
    global Data
    return [random.randint(0,1) for _ in range (Data["NumberOfItems"])]

def fitness(chr):
    global Data
    fitness=0
    weight=0
    for i in range (Data["NumberOfItems"]):
        if chr[i]==1:
            fitness+=Data["value"][i]
            weight+=Data["weight"][i]
    if weight>Data["capacity"]:
        return -1*fitness
    return fitness

def crossover(survivors):
    child=[]
    global Data
    for i in range(len(survivors)):
        for j in range (i+1,len(survivors),5):
            c1,c2=crossoversp(survivors[i][0],survivors[j][0],Data["NumberOfItems"]//2)
            child.append(c1)
            child.append(c2)
        if len(child)>5:
            break
    return child

def garunner():
    Gen=10
    populationsize=80
    population= [rndchromosome() for _ in range(populationsize)] #[[p1][p2][p3][p4.....ppsize]]
    # print(population)
    scored=[]
    for i in population:
        scored.append([i,fitness(i)])  # [[p1,1000]]
    
    scored.sort(key=lambda x:x[1],reverse=True) #top fitness first 
    # print(scored)
    for gen in range(1,Gen+1):
        survivors=scored[:len(scored)//2]
        # print(survivors)
        if len (survivors)==1:
            break
        elite=survivors[0][0]
        print(elite)
        mutchild=[]
        children=crossover(survivors)
        for i in children:
            mutchild.append(mutate(i,0.10))
        mutchild.append(elite)
        print(mutchild)
        scored=[]

        for i in mutchild:
            scored.append([i,fitness(i)])
        scored.sort(key=lambda x:x[1],reverse=True)
    best=scored[0]

    print (best)
        
    

    
garunner()