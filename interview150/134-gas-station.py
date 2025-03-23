def canCompleteCircuit(gas, cost):
    # cost is cost to travel from station ith to station (i + 1)th
    # gas is amount of gas can be filled at station ith

    # idea: if sum(gas) >= sum(cost) -> exist an index that we can complete an circular route. -1 otherwise
    # we also notice that if gas[i] < cost[i], we cannot start there -> remove possibilities
    # we tend to start at an index where the difference of gas[i] and cost[i] is the maximum in the difference array
    # create a difference array, and return the result of an index for the maximum difference
    # this approach don't work based on example 3. Need to find another way.

    # idea is to start at the zero index and check if the tank which is a difference between gas and cost is
    # smaller than 0. If that is the case, we reset the tank and increment start index. We keep adding the
    # tank until the last index.
    # Time: O(n)
    # Space: O(1)
    n = len(gas)
    if sum(gas) < sum(cost):
        return -1
    start_index = 0
    tank = 0
    for i in range(n):
        tank += gas[i] - cost[i]
        # if tank is negative, reset start index
        if tank < 0:
            start_index = i + 1
            tank = 0
    return start_index


gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]
# print(canCompleteCircuit(gas, cost))  # 3

gas = [2, 3, 4]
cost = [3, 4, 3]
# print(canCompleteCircuit(gas, cost))  # -1

gas = [5, 8, 2, 8]
cost = [6, 5, 6, 6]
print(canCompleteCircuit(gas, cost))  # 3
