import random

# ── Problem data ──────────────────────────────────────────────────────────────
Data = {
    "capacity":      10,
    "weight":        [2, 1, 5, 3],
    "value":         [300, 200, 400, 500],
    "NumberOfItems": 4,
}

# ── Helper functions ──────────────────────────────────────────────────────────

def rnd_chromosome():
    """Random binary chromosome, one gene per item."""
    return [random.randint(0, 1) for _ in range(Data["NumberOfItems"])]

def fitness(chrom):
    """
    Sum values of selected items.
    Returns NEGATIVE if total weight exceeds capacity
    so overweight solutions always rank last.
    """
    total_value  = 0
    total_weight = 0
    for i in range(Data["NumberOfItems"]):
        if chrom[i] == 1:
            total_value  += Data["value"][i]
            total_weight += Data["weight"][i]
    if total_weight > Data["capacity"]:
        return -total_value
    return total_value

def crossover_sp(p1, p2):
    """
    Single-point crossover.
    Split point = middle of the chromosome (not the population!).
    
    TIP: crossover point must be based on chromosome length,
         not population size — those are completely different things.
    """
    cp = len(p1) // 2          # e.g. 4 items → split at index 2
    child1 = p1[:cp] + p2[cp:]
    child2 = p2[:cp] + p1[cp:]
    return child1, child2

def mutate(chrom, mutation_rate=0.1):
    """
    Flip one random gene with probability mutation_rate.
    
    TIP: pass a fixed rate (e.g. 0.1) instead of random.random() —
         using random.random() as the rate means the chance of mutating
         is itself random every call, which is unpredictable.
    """
    if random.random() < mutation_rate:
        idx = random.randint(0, Data["NumberOfItems"] - 1)
        chrom[idx] = 1 - chrom[idx]   # flip: 0→1 or 1→0
    return chrom

def score_and_sort(population):
    """
    Pair each chromosome with its fitness score, sort best first.
    Returns: [ [chromosome, fitness], ... ]
    
    TIP: sort ONCE after all items are added —
         sorting inside the append loop is wasteful.
    """
    scored = [[chrom, fitness(chrom)] for chrom in population]
    scored.sort(key=lambda x: x[1], reverse=True)  # highest fitness first
    return scored

def crossover_population(survivors, max_children=50):
    """
    Breed children from survivor pairs, capped at max_children.

    TIP: Without a cap the population doubles+ every generation
         (50 → 140 → 1022 → 52000 ...) and runs out of memory fast.
         Always cap the output size to keep generations stable.
    """
    children = []
    for i in range(len(survivors)):
        for j in range(i + 1, len(survivors), 5):
            c1, c2 = crossover_sp(survivors[i][0], survivors[j][0])
            children.append(c1)
            children.append(c2)
            if len(children) >= max_children:   # stop once cap is hit
                return children
    return children

# ── Main GA loop ──────────────────────────────────────────────────────────────

def ga_runner():
    GENERATIONS   = 10
    POPULATION    = 50
    MUTATION_RATE = 0.10   # fixed 10% — not random each call

    # Step 0 — create and score initial population
    population = [rnd_chromosome() for _ in range(POPULATION)]
    scored     = score_and_sort(population)

    print(f"{'Gen':>4}  {'Best Fitness':>13}  Chromosome")
    print("-" * 45)
    print(f"{'init':>4}  {scored[0][1]:>13}  {scored[0][0]}")

    for gen in range(1, GENERATIONS + 1):

        # Step 1 — selection: keep top 50%
        survivors = scored[:len(scored) // 2]

        # Step 2 — elitism: carry the best chromosome forward unchanged
        # TIP: this guarantees the best solution is never lost to crossover/mutation
        elite = survivors[0][0]

        # Step 3 — crossover: breed new children from survivor pairs
        children = crossover_population(survivors, max_children=POPULATION)

        # Step 4 — mutation: randomly flip genes for diversity
        children = [mutate(c, MUTATION_RATE) for c in children]

        # Step 5 — re-insert elite, then score and sort
        # TIP: sort ONCE here, outside any loop
        children.append(elite)
        scored = score_and_sort(children)

        print(f"{gen:>4}  {scored[0][1]:>13}  {scored[0][0]}")

    # ── Final result ──────────────────────────────────────────────────────────
    best_chrom, best_fit = scored[0]

    print("\n" + "=" * 45)
    print("  BEST SOLUTION")
    print("=" * 45)
    total_w = total_v = 0
    for i, gene in enumerate(best_chrom):
        if gene == 1:
            w, v = Data["weight"][i], Data["value"][i]
            total_w += w
            total_v += v
            print(f"  Item {i}  weight={w}  value={v}")
    print(f"  Total weight : {total_w} / {Data['capacity']}")
    print(f"  Total value  : {total_v}")
    print(f"  Fitness      : {best_fit}")
    print("=" * 45)


if __name__ == "__main__":
    random.seed(42)
    ga_runner()