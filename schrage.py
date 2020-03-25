
# SCHRAGE

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
        # print("r getted")
        return self._list[len(self._list)-1][0]


def schrage(nb):
    data = open('DATA1\SCHRAGE'+ str(nb) +'.DAT', 'r')

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

    return C_max


def schrage_div(nb):
    data = open('DATA2\SCHRAGE'+ str(nb) +'.DAT', 'r')

    n = int(data.readline().strip())
    t = 0                                           # total time
    N = PriorityQueue(itemgetter(0), True, [])      # list of unordered tasks
    G = PriorityQueue(itemgetter(2), False, [])     # list of ready to implementation tasks

    C_max = 0
    r = []                                          # availability time
    p = []                                          # time to complete
    q = []                                          # delivery time
    pi = []

    for line in data:                               # read data from file
        lin = line.split()
        r.append(lin[0])
        p.append(lin[1])
        q.append(lin[2])

    for i in range(0, n):
        N.add([int(r[i]), int(p[i]), int(q[i])])    # add tasks to N list

        onMachine=[0, 0, 999999]                    # current task initialization

    while G.is_empty() is False or N.is_empty() is False:   # check if at least one OR lists isn't empty
        while N.is_empty() is False and int(N.get_r(0)) <= t:  # check if N isn't empty AND availability time is less than total time
            e = N.get_element()                                # ready task
            G.add(e)
            N.delete()
            if e[2] > onMachine[2]:                            # check if time to complete ready task is higher than time on machine
                onMachine[1] = t - e[0]
                t = e[0]
                if onMachine[1] > 0:
                    G.add(onMachine)

        if G.is_empty() is True:                                     # 5
            t = int(N.get_r(0))                                    # 6
        else:
            e = G.get_element()
            G.delete()
            onMachine = e
            pi.append(e)
            t += int(e[1])
            C_max = max(C_max, int(t+int(e[2])))


    return C_max


def test():
    results = [32, 687, 1299, 1399, 3487, 3659, 6918, 6936, 72853]

    for i in range(1,10):
        if schrage(i) == results[i-1]:
            print("OK")
        else:
            print(f"ERROR IN SCHRAGE {i}")


test()

