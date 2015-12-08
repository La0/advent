import sys
import inspect

MAX = 2**15 # 32768

DEBUG = False

class Machine(object):
    def __init__(self):
        self.cursor = 0

        # Setup language bindings
        self.lang = {
            0   : self.halt,
            1   : self.ins_set,
            2   : self.ins_push,
            3   : self.ins_pop,
            4   : self.ins_eq,
            5   : self.ins_gt,
            6   : self.ins_jump,
            7   : self.ins_jt,
            8   : self.ins_jf,
            9   : self.ins_add,
            10  : self.ins_mult,
            11  : self.ins_mod,
            12  : self.ins_and,
            13  : self.ins_or,
            14  : self.ins_not,
            15  : self.ins_rmem,
            16  : self.ins_wmem,
            17  : self.ins_call,
            18  : self.ins_ret,
            19  : self.ins_out,
            20  : self.ins_in,
            21  : self.ins_noop,
        }

        # Setup registers
        # numbers 32768..32775 instead mean registers 0..7
        nb = 8
        self.registers = dict(zip(range(MAX, MAX+nb), [0, ] * nb))

        # Setup stack
        self.stack = []

        # Setup memory
        self.memory = {}

    def run(self, filename):
        # Load all vm instructions
        self.memory = self.read_instructions(filename)

        # Pad memory until MAX
        self.memory += [0, ] * (MAX - len(self.memory))

        # Run those instructions
        while self.cursor >= 0 and self.cursor < len(self.memory):
            ins = self.memory[self.cursor]

            # Not implemented instruction
            method = self.lang.get(ins)
            if not method:
                raise NotImplemented('Missing instruction %d' % ins)

            # Get nb of parameters
            # except self
            nb = len(inspect.getargspec(method).args) - 1
            args = [self.memory[self.cursor + i + 1] for i in range(0, nb)]

            if DEBUG:
                print method.__name__.replace('ins_', ''), args # Debug

            # Run method
            method(*args)

    def convert(self, a):
        """
        Convert value from register
        """
        if a not in self.registers:
            return a
        return self.registers[a]

    def set(self, a, value):
        """
        Helper to set a register value
        """
        if a not in self.registers:
            raise Exception('Invalid register set', a)
        self.registers[a] = value

    def ins_jump(self, a):
        """
        Jump to position a
        """
        self.cursor = self.convert(a)

    def ins_noop(self):
        """
        Do nothing
        """
        self.cursor += 1

    def ins_out(self, a):
        """
        Display character on terminal
        """
        sys.stdout.write(chr(self.convert(a)))
        self.cursor += 2

    def ins_in(self, a):
        """
        read a character from the terminal and write its ascii code to <a>; it can be assumed that once input starts, it will continue until a newline is encountered; this means that you can safely read whole lines from the keyboard and trust that they will be fully read
        """
        print 'READ !!!'
        self.halt()

    def ins_jt(self, a, b):
        """
        if <a> is nonzero, jump to <b>
        """
        if self.convert(a) != 0:
            self.ins_jump(self.convert(b))
        else:
            self.cursor += 3

    def ins_jf(self, a, b):
        """
        if <a> is zero, jump to <b>
        """
        if self.convert(a) == 0:
            self.ins_jump(self.convert(b))
        else:
            self.cursor += 3

    def ins_set(self, a, b):
        """
        set register <a> to the value of <b>
        """
        self.set(a, self.convert(b))
        self.cursor += 3

    def ins_add(self, a, b, c):
        """
        assign into <a> the sum of <b> and <c> (modulo MAX)
        """
        self.set(a, (self.convert(b)+self.convert(c)) % MAX)
        self.cursor += 4

    def ins_eq(self, a, b, c):
        """
        set <a> to 1 if <b> is equal to <c>; set it to 0 otherwise
        """
        if self.convert(b) == self.convert(c):
            self.set(a, 1)
        else:
            self.set(a, 0)
        self.cursor += 4

    def ins_gt(self, a, b, c):
        """
        set <a> to 1 if <b> is greater than <c>; set it to 0 otherwise
        """
        if self.convert(b) > self.convert(c):
            self.set(a, 1)
        else:
            self.set(a, 0)
        self.cursor += 4

    def ins_push(self, a):
        """
        push <a> onto the stack
        """
        self.stack.append(self.convert(a))
        self.cursor += 2

    def ins_pop(self, a):
        """
        remove the top element from the stack and write it into <a>; empty stack = error
        """
        if not self.stack:
            raise Exception('Empty stack')
        self.set(a, self.convert(self.stack.pop()))
        self.cursor += 2

    def ins_ret(self):
        """
        remove the top element from the stack and jump to it; empty stack = halt
        """
        if not self.stack:
            print 'Empty stack !'
            return self.halt()

        self.ins_jump(self.stack.pop())

    def ins_and(self, a, b, c):
        """
        stores into <a> the bitwise and of <b> and <c>
        """
        self.set(a, (self.convert(b) & self.convert(c)) % MAX)
        self.cursor += 4

    def ins_or(self, a, b, c):
        """
        stores into <a> the bitwise or of <b> and <c>
        """
        self.set(a, (self.convert(b) | self.convert(c)) % MAX)
        self.cursor += 4

    def ins_not(self, a, b):
        """
        stores 15-bit bitwise inverse of <b> in <a>
        """
        self.set(a, (~ self.convert(b)) % MAX)
        self.cursor += 3

    def ins_mult(self, a, b, c):
        """
        store into <a> the product of <b> and <c> (modulo MAX)
        """
        self.set(a, (self.convert(b) * self.convert(c)) % MAX)
        self.cursor += 4

    def ins_mod(self, a, b, c):
        """
        store into <a> the remainder of <b> divided by <c>
        """
        self.set(a, (self.convert(b) % self.convert(c)) % MAX)
        self.cursor += 4

    def ins_call(self, a):
        """
        write the address of the next instruction to the stack and jump to <a>
        """
        address = self.cursor + 2
        self.stack.append(address)
        self.cursor = self.convert(a)

    def ins_rmem(self, a, b):
        """
        read memory at address <b> and write it to <a>
        """
        b = self.convert(b)
        if b < MAX:
            self.set(a, self.memory[b])
        else:
            raise Exception('Override memory (rmem)')
        self.cursor += 3

    def ins_wmem(self, a, b):
        """
        write the value from <b> into memory at address <a>
        """
        a = self.convert(a)
        if a < MAX:
            self.memory[a] = self.convert(b)
        else:
            raise Exception('Override memory (wmem)')
        self.cursor += 3

    def halt(self):
        """
        Stop VM
        """
        sys.exit(0)

    def read_instructions(self, filename):
        """
        Read all instructions from file
        """
        out = []
        with open(filename, 'rb') as f:
            while True:
                pair = f.read(2)
                if not pair:
                    break

                # 16-bit little-endian pair (low byte, high byte)
                low,high = ord(pair[0]), ord(pair[1])
                number = (high << 8) + low
                out.append(number)

        return out

if __name__ == '__main__':
    m = Machine()
    m.run('challenge.bin')
