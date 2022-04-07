import sys

MEM_SIZE = 30000
MEM_ARR = [0 for n in range(MEM_SIZE)]
mem_ptr = 0
ptr = -1

astack = []

program = ""
inp = ""
out = ""

def clear():
    global MEM_ARR, mem_ptr, ptr, astack, program, inp, out

    MEM_ARR = [0 for _ in range(MEM_SIZE)]
    mem_ptr = 0
    ptr = 0
    astack = []
    program = ""

def send_output(val):
    global out
    out += chr(val)

def get_input():
    global inp
    val = 0
    if inp:
        val = ord(inp[0])
        inp = inp[1:]
    return val

def repeat_fun(times, f, *args):
    for i in range(times): f(*args)

def read_file():
    global program
    try:
        with open(sys.argv[1], 'r') as f:
            program += f.read()
    except IndexError:
        raise Exception('Enter valid path to file')

def interpretate():
    global MEM_ARR, mem_ptr, ptr, astack, program, inp, out
    flag = True
    while flag:
        ptr += 1
        try:
            program[ptr]
        except IndexError:
            break
        match (program[ptr]):
            case '>':
                if len(MEM_ARR) == mem_ptr - 1:
                    repeat_fun(5, MEM_ARR.append, 0)
                mem_ptr += 1
                continue
            case '<':
                if not mem_ptr == 0:
                    mem_ptr -= 1
                continue
            case '+':
                MEM_ARR[mem_ptr] += 1
                continue
            case '-':
                if not MEM_ARR[mem_ptr] == 0:
                    MEM_ARR[mem_ptr] -= 1
                continue
            case '.':
                send_output(MEM_ARR[mem_ptr])
                continue
            case ',':
                MEM_ARR[mem_ptr] = get_input()
                continue
            case '[':
                if MEM_ARR[mem_ptr]:
                    astack.append(ptr)
                else:
                    count = 0
                    while True:
                        ptr += 1
                        try:
                            program[ptr]
                        except IndexError:
                            break
                        if program[ptr] == '[':
                            count += 1
                        elif program[ptr] == ']':
                            if count:
                                count -= 1
                            else:
                                break

            case ']':
                ptr = astack.pop(0) - 1
                continue

            case _:
                continue

    print(out)
    return out

if __name__ == '__main__':
    read_file()
    interpretate()
