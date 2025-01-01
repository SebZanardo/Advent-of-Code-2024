import sys


print("This brute force solution is so slow it is not even worth running")
print("I was unable to produce an answer using this solution")


def simulate(A: int, B: int, C: int, program: list[int]) -> list[int]:
    output = []
    instruction_ptr = 0
    while instruction_ptr < len(program):
        instruction = program[instruction_ptr]
        operand = program[instruction_ptr + 1]
        combo_operand = operand

        match operand:
            case 4:
                combo_operand = A
            case 5:
                combo_operand = B
            case 6:
                combo_operand = C
            case 7:
                # Should not appear in valid programs
                break

        match instruction:
            # adv
            case 0:
                A = int(A/(2 ** operand))
            # bxl
            case 1:
                B = B ^ operand
            # bst
            case 2:
                B = combo_operand % 8
            # jnz
            case 3:
                if A != 0:
                    instruction_ptr = operand
                    # Do not increment instruction_ptr by 2
                    continue
            # bxc
            case 4:
                B = B ^ C
            # out
            case 5:
                output.append(combo_operand % 8)
            # bdv
            case 6:
                B = int(A/(2 ** combo_operand))
            # cdv
            case 7:
                C = int(A/(2 ** combo_operand))

        instruction_ptr += 2

    return output


# Try to read a path to an input file from command line arguments
path = sys.argv[1] if len(sys.argv) > 1 else "input.in"

A = 0
B = 0
C = 0
program = []
with open(path, "r") as f:
    A = int(f.readline().split(':')[1])
    B = int(f.readline().split(':')[1])
    C = int(f.readline().split(':')[1])
    f.readline()
    program = list(map(int, f.readline().split(':')[1].split(',')))

i = 0
while True:
    if i % 1000000 == 0:
        print(i)
    if simulate(i, B, C, program) == program:
        break
    i += 1

print(f"Solution:\n{i}")
