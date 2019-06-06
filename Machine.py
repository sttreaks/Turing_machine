class Rules:
    def __init__(self):
        self.q = {0: {0: (0, 0, 0), 1: (1, 0, 0)}}
        self.st = 1

    def add_state(self):
        print("Value in cell is 0")
        x0 = int(input("What symbol machine write in that cell? : "))
        q0 = int(input("What state will be next? : "))
        d0 = int(input("Which way you machine will go next? :"))

        print("Value in cell is 1")
        x1 = int(input("What symbol machine write in that cell? : "))
        q1 = int(input("What state will be next? : "))
        d1 = int(input("Which way you machine will go next? :"))

        self.q.update({self.st: {0: (x0, q0, d0), 1: (x1, q1, d1)}})
        self.st += 1

    def file_read(self, filename: str):
        with open(filename, 'r') as f:
            for i in f:
                i = i.split()
                for j in range(len(i)):
                    i[j] = int(i[j])
                self.q.update({self.st: {0: (i[0], i[2], i[1]), 1: (i[3], i[5], i[4])}})
                self.st += 1

    def cons_read(self):
        n = int(input("How many states you wanna enter? : "))
        for i in range(n):
            self.add_state()


class Tape:
    def __init__(self):
        self._t = []

    def cons_input(self):
        s = input("Input your tape: ")
        for i in s:
            self._t.append(int(i))

    def file_read(self, filename):
        with open(filename, 'r') as f:
            for i in f:
                for j in i:
                    self._t.append(int(j))

        while len(self._t) < 1000:
            self._t.append(0)


class TM:
    def __init__(self, f1, f2):
        self.r = Rules()
        self.t = Tape()
        self.point = 0
        self.cs = 1
        self.t.file_read(f1)
        self.r.file_read(f2)

    def start(self):
        i = 0
        while self.cs != 0:
            i += 1
            buff = self.r.q[self.cs][self.t._t[self.point]]
            self.t._t[self.point] = buff[0]
            self.cs = buff[1]
            self.point += buff[2]
            if self.point == -1 or self.point == 1000:
                print("Machine out of tape range")
        print(self.t._t)


if __name__ == '__main__':
    # tA132 = TM("tapeA132.txt", "condA132.txt")
    # tA132.start()
    #
    # print("-------------")
    # print("-------------")
    # print("-------------")

    tplus = TM("tapeplus.txt", "condplus.txt")
    tplus.start()
