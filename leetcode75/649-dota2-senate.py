"""
Dota2 Senate

2 rights:
ban right
announce victory

input:
senate -> R / D

output:
Radiant / Dire
"""

import queue


def predictPartyVictory(senate):
    res = ""
    n = len(senate)
    # using two queues: 1 for R and 1 for D
    rq = queue.Queue()
    dq = queue.Queue()
    for i in range(n):
        if senate[i] == "R":
            rq.put(i)
        else:
            dq.put(i)

    while not rq.empty() and not dq.empty():
        if rq.queue[0] < dq.queue[0]:
            rq.put(rq.queue[0] + n)
        else:
            dq.put(dq.queue[0] + n)
        rq.get()
        dq.get()
    if rq.qsize() == 0:
        res = "Dire"
    else:
        res = "Radiant"
    return res


import queue


def predictPartVictory(senate):
    n = len(senate)
    rq, dq = queue.deque(), queue.deque()
    for i in range(n):
        if senate[i] == "R":
            rq.append(i)
        else:
            dq.append(i)
    while rq and dq:
        if rq[0] < dq[0]:
            rq.append(rq[0] + n)
        else:
            dq.append(dq[0] + n)
        rq.popleft()
        dq.popleft()
    return "Radiant" if rq else "Dire"


senate = "RD"
print(predictPartyVictory(senate))  # Radiant
senate = "RDD"
print(predictPartyVictory(senate))  # Dire
senate = "RRDRD"
print(predictPartyVictory(senate))  # Radiant
senate = "RRDDD"
print(predictPartyVictory(senate))  # Radiant
