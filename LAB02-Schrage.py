# ALGORYTM
# SCHRAGE

#     Dane:
# n – liczba zadań,
# ri – termin dostępności zadania i,
# pi – czas wykonania zadaniai,
# qi – czas dostarczenia zadania i.

#     Szukane:
# π - permutacja wykonania zadań na maszynie,
# Cmax – maksymalny z terminów dostarczenia zadań.

#     Struktury pomocnicze:
# t – chwila czasowa,
# k – pozycja w permutacji π,
# N – zbiór zadań nieuszeregowanych,
# G – zbiór zadań gotowych do realizacji

# r - termin dostępności
# p - czas obslugi
# q - czas dostarczenia zadania


from operator import itemgetter


class PriorityQueue:

    def __init__(self, key, rev, l):
        self._key = key
        self._rev = rev
        if len(l) == 0:
            self._list = []
        else:
            self._list = l.sort(key=key, reverse=rev)

    def delete(self):
        self._list.pop(len(self._list)-1)

    def add(self, val):
        self._list.append(val)
        self._list.sort(key=self._key, reverse=self._rev)
        # print(f"key = {self._key}, list = {self._list}")

    def display(self):
        print(self._list)

    def return_list(self):
        return self._list

    def is_empty(self):
        if len(self._list) == 0:
            return True
        else:
            return False

    def get_element(self):
        return self._list[len(self._list)-1]

    def get_r(self, nb):
        return self._list[len(self._list)-1][0]


def schrage(nb):
    data = open('SCHRAGE'+ str(nb) +'.DAT', 'r')

    n = int(data.readline().strip())
    t = 0
    k = 0
    N = PriorityQueue(itemgetter(0), True, [])
    G = PriorityQueue(itemgetter(2), False, [])

    C_max = 0
    r = []
    p = []
    q = []
    pi = []

    for line in data:
        l = line.split()
        r.append(l[0])
        p.append(l[1])
        q.append(l[2])

    for i in range(0, n):
        N.add([int(r[i]), int(p[i]), int(q[i])])

    while G.is_empty() is False or N.is_empty() is False:  # 2
        while N.is_empty() is False and int(N.get_r(0)) <= t:  # 3
            e = N.get_element()
            G.add(e)
            N.delete()
        if G.is_empty() is True:                                     # 5
            t = int(N.get_r(0))                                    # 6
        else:
            e = G.get_element()
            G.delete()
            k += 1
            pi.append(e)
            t += int(e[1])
            C_max = max(C_max, int(t+int(e[2])))

    print(C_max)
