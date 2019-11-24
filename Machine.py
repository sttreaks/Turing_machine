import numpy as np


class Rules:
    """
    Class for creating states table for unary turing machine.
    """

    def __init__(self):
        """
        Creating 0 state. Setting the initial state.
        """
        self.q = {0: {0: (0, 0, 0), 1: (1, 0, 0)}}
        self.st = 1

    def add_state(self):
        """
        Adding state from console.

        :return:
        """
        print(f"Input state {len(self.q.keys()) + 1}:")
        print("\nIf u stay in cell with 0")
        x0 = int(input("What symbol machine write in that cell?: "))
        q0 = int(input("What state will be next?: "))
        d0 = int(input("Which way you machine will go next? (-1 if left; 0 if stay; 1 if right):"))

        print("\\nIf u stay in cell with 1")
        x1 = int(input("What symbol machine write in that cell?: "))
        q1 = int(input("What state will be next?: "))
        d1 = int(input("Which way you machine will go next? (-1 if left; 0 if stay; 1 if right):"))

        self.q.update({self.st: {0: (x0, q0, d0), 1: (x1, q1, d1)}})
        self.st += 1

    def file_read(self, filename: str):
        """
        Read states from file.

        :param filename: Path to open and read states data.
        :return:
        """
        with open(filename, 'r') as f:
            for i in f:
                i = i.split()
                for j in range(len(i)):
                    i[j] = int(i[j])
                self.q.update({self.st: {0: (i[0], i[2], i[1]), 1: (i[3], i[5], i[4])}})
                self.st += 1

    def cons_read(self):
        """
        Input how many states u want enter.

        :return:
        """
        n = int(input("How many states you wanna enter? : "))
        for i in range(n):
            self.add_state()


class Tape:
    """
    Class for creating tape. Have only 1 and 0 symbols.
    """

    def __init__(self, tl=100000):
        """
        Initializing tape.

        :param tl: Tape length.
        """

        self._t = np.array([])
        self.tlen = tl

    def cons_input(self):
        """
        Input tape from console.

        :return:
        """
        line = input("Input your tape: ")
        self._t = np.array(list(map(int, line)))

    def file_read(self, filename):
        """
        Reading tape from file.

        :param filename: Path for reading tape.
        :return:
        """
        with open(filename, 'r') as f:
            line = f.readline()
            line += "0" * (self.tlen - len(self._t))
            self._t = np.array(list(map(int, line)))


class TM:
    """
    Connecting tape and states to total structure.
    """

    def __init__(self, f1, f2):
        """
        Initializing tape and states for turing machine.

        :param f1: Path for tape.
        :param f2: Path for states.
        """
        self.r = Rules()
        self.t = Tape()
        self.point = 0  # Position of cell where machine stay now
        self.cs = 1  # Number of current machine state
        self.t.file_read(f1)
        self.r.file_read(f2)
        self.cycled = False

    def start(self):
        """Starting turing machine. All process will be done at this function as well.

        :return:
        """
        while self.cs != 0:
            current_state = self.r.q[self.cs][self.t._t[self.point]]
            self.t._t[self.point] = current_state[0]
            self.cs = current_state[1]
            self.point += current_state[2]
            if self.point == -1 or self.point == self.t.tlen:  # checking if machine out of tape range
                print("Machine cycled or out of tape range")
                break

    def output(self, filename):
        """Function output current tape to file.
        Also it cut useless "0" at the and of tape.

        :param filename: Path to output current tape.
        :return:
        """

        with open(filename, 'w') as f:
            print(str(self), file=f)

    def get_tape(self):
        """Return tape as array.

        :return: Tape as array.
        """
        return self.t._t

    def __str__(self):
        """Reformat tape to string and return it.
        Also it cut useless "0" at the and of tape.

        :return: Tape in string format
        """
        s = "".join(str(i) for i in self.t._t)
        s = s[::-1]
        indx = s.find("1")
        indx = len(s) - indx
        s = s[::-1]
        s = s[:indx + 1]
        if self.cycled:
            return "Machine is cycled"
        return s


if __name__ == '__main__':
    # '''Example from our university'''
    # tA132 = TM("A132/tapeA132.txt", "A132/condA132.txt")
    # tA132.start()
    # tA132.output("A132/resA132.txt")
    #
    # print("-------------")
    # print("-------------")
    # print("-------------")
    #
    # '''Summing a and b'''
    #
    # with open("plus/tapeplus.txt", 'r') as f:
    #     line = f.readline()[1:]  # first 0 symbol (our tape starts from it)
    #     a = line[:line.find("0")].count("1")
    #     b = line[line.find("0"):].count("1")
    #
    # print(f"Summing of {a} and {b}")
    #
    # tplus = TM("plus/tapeplus.txt", "plus/condplus.txt")
    # tplus.start()
    # tplus.output("plus/resplus.txt")
    #
    # with open("plus/resplus.txt", 'r') as f:
    #     c = f.readline().count("1")
    #
    # print(f"Result is {c}")

    print("-------------")
    print("-------------")
    print("-------------")

    '''Analyzing what numbers are at tape for multiplying and show it'''
    bo = False

    with open("mul/tapemul.txt", 'r') as f:
        line = f.readline()[1:]  # first 0 symbol (our tape starts from it)
        a = line[:line.find("0")].count("1")
        b = line[line.find("0"):].count("1")

    print(f"Multiplication of {a - 1} and {b - 1}")

    tmul = TM("mul/tapemul.txt", "mul/condmul.txt")
    tmul.start()
    tmul.output("mul/resmul.txt")

    c = 0

    '''Analyzing result number after multiplying multiplying and show it'''

    with open("mul/resmul.txt", 'r') as f:
        c = f.readline().count("1")

    print(f"Result is {c - 1}")
    print("You can find result tape by the address ./mul/resmul.txt")
