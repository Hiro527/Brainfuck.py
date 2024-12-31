import sys


MEM_SIZE = 30000


args = sys.argv


def load_file(file_name: str) -> str:
    with open(file_name, 'r') as f:
        chars = f.read()
        return chars


def evaluate(program: str) -> None:
    mem = [0] * MEM_SIZE
    ptr = 0
    cnt = 0

    while cnt < len(program):
        char = program[cnt]

        if char == '+':
            mem[ptr] += 1
        elif char == '-':
            mem[ptr] -= 1
        elif char == '[':
            if mem[ptr] == 0:
                nest = 1
                while nest != 0:
                    cnt += 1
                    if cnt == len(program):
                        print('Error: Brackets are not balanced')
                        sys.exit(1)
                    if program[cnt] == '[':
                        nest += 1
                    elif program[cnt] == ']':
                        nest -= 1
        elif char == ']':
            if mem[ptr] != 0:
                nest = 1
                while nest != 0:
                    cnt -= 1
                    if cnt < 0:
                        print('Error: Brackets are not balanced')
                        sys.exit(1)
                    if program[cnt] == ']':
                        nest += 1
                    elif program[cnt] == '[':
                        nest -= 1
        elif char == '.':
            print(chr(mem[ptr]), end='')
        elif char == ',':
            mem[ptr] = ord(input())
        elif char == '>':
            ptr += 1
            if ptr == MEM_SIZE:
                print('Error: Pointer cannot exceed memory size')
                sys.exit(1)
        elif char == '<':
            ptr -= 1
            if ptr == -1:
                print('Error: Pointer cannot be negative')
                sys.exit(1)
        else:
            pass

        cnt += 1


if __name__ == '__main__':
    if len(args) < 2:
        print('Usage: python main.py <file_name>')
        sys.exit(1)

    program = load_file(args[1])
    evaluate(program)
