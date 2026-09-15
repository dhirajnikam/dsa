def can_complete_circuit(gas, cost):
    # O(n) time, O(1) space
    # Total surplus >= 0 guarantees a solution; whenever the running tank goes negative,
    # every start up to here is ruled out, so restart from the next station.
    if sum(gas) < sum(cost):
        return -1
    start = tank = 0
    for i in range(len(gas)):
        tank += gas[i] - cost[i]
        if tank < 0:
            start, tank = i + 1, 0
    return start
