import sys
sys.setrecursionlimit(10000)

def find(table, n):
    if not table.get(n):
        table[n] = n + 1
        return n
    else:
        table[n] = find(table, table[n])
        return table[n]
    

def solution(k, room_number):
    result = []
    table = dict()
    for room in room_number:
        result.append(find(table, room))

    return result