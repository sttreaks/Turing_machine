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
    def __init__(self, tl=1000):
        self._t = []
        self.tlen = tl

    def cons_input(self):
        s = input("Input your tape: ")
        for i in s:
            self._t.append(int(i))

    def file_read(self, filename):
        with open(filename, 'r') as f:
            for i in f:
                for j in i:
                    self._t.append(int(j))

        while len(self._t) < self.tlen:
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
            if self.point == -1 or self.point == 1000 or i == 10000:
                print("Machine cycled or out of tape range")
                break

    def output(self, filename):
        s = ""
        for i in self.t._t:
            s += str(i)
        with open(filename, 'w') as f:
            print(s, file=f)


if __name__ == '__main__':
    # tA132 = TM("A132/tapeA132.txt", "A132/condA132.txt")
    # tA132.start()
    #
    # print("-------------")
    # print("-------------")
    # print("-------------")
    #
    # tplus = TM("plus/tapeplus.txt", "plus/condplus.txt")
    # tplus.start()
    #
    # print("-------------")
    # print("-------------")
    # print("-------------")

    a = 0
    b = 0
    bo = False

    with open("mul/tapemul.txt", 'r') as f:
        for i in f:
            for j in i:
                if j == '1' and not bo:
                    a += 1
                elif a > 0 and j == '0':
                    bo = True
                elif bo and j == '1':
                    b += 1

    print(f"Multiplication of {a - 1} and {b - 1}")

    tmul = TM("mul/tapemul.txt", "mul/condmul.txt")
    tmul.start()
    tmul.output("mul/resmul.txt")

    c = 0
    with open("mul/resmul.txt", 'r') as f:
        for i in f:
            for j in i:
                if j == '1':
                    c += 1

    print(f"Result is {c - 1}")
    print("You can find result tape by the address ./mul/resmul.txt")
