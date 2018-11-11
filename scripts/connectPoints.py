import copy


def distance(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** (1 / 2)


def connectPoints(lst):
    lst = copy.deepcopy(lst)
    result = []
    start = lst[0]
    while len(lst) > 0:
        min = None
        closest = None
        for elem in lst:
            if (min == None or distance(elem, start) < min) and distance(elem,
                                                                         start) != 0:
                min = distance(elem, start)
                closest = elem
        result.append(closest)
        lst.remove(start)
        start = closest
    result[-1]=result[0]
    result.pop(10)
    return result


def printlst(lst):
    for elem in lst:
        print(elem)

