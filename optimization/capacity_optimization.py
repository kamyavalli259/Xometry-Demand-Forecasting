from pulp import LpMinimize, LpProblem, LpVariable, lpSum

def optimize_capacity(demand, capacities, costs):
    model = LpProblem("CapacityOptimization", LpMinimize)

    allocation = {
        m: LpVariable(f"alloc_{m}", lowBound=0)
        for m in capacities
    }

    model += lpSum(allocation[m] * costs[m] for m in capacities)

    model += lpSum(allocation[m] for m in capacities) >= demand

    for m in capacities:
        model += allocation[m] <= capacities[m]

    model.solve()

    return {m: allocation[m].value() for m in capacities}
