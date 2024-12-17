#Part 1

# def execute_program(registers, program):
#     # Parse initial registers
#     A, B, C = registers['A'], registers['B'], registers['C']
#     program_len = len(program)
#     output = []

#     # Combo operand mapping
#     def combo_value(operand):
#         if operand <= 3:
#             return operand  # Literal values 0 to 3
#         elif operand == 4:
#             return A  # Register A
#         elif operand == 5:
#             return B  # Register B
#         elif operand == 6:
#             return C  # Register C
#         elif operand == 7:
#             raise ValueError("Invalid combo operand: 7")

#     # Program execution
#     instruction_pointer = 0
#     while instruction_pointer < program_len:
#         opcode = program[instruction_pointer]  # Opcode
#         operand = program[instruction_pointer + 1]  # Operand
        
#         if opcode == 0:  # adv: A = A / 2^operand (integer division)
#             denominator = 2 ** combo_value(operand)
#             A //= denominator

#         elif opcode == 1:  # bxl: B = B XOR operand
#             B ^= operand

#         elif opcode == 2:  # bst: B = operand % 8
#             B = combo_value(operand) % 8

#         elif opcode == 3:  # jnz: if A != 0, jump to operand
#             if A != 0:
#                 instruction_pointer = operand
#                 continue  # Skip incrementing pointer

#         elif opcode == 4:  # bxc: B = B XOR C
#             B ^= C

#         elif opcode == 5:  # out: Output operand % 8
#             output.append(combo_value(operand) % 8)

#         elif opcode == 6:  # bdv: B = A / 2^operand (integer division)
#             denominator = 2 ** combo_value(operand)
#             B = A // denominator

#         elif opcode == 7:  # cdv: C = A / 2^operand (integer division)
#             denominator = 2 ** combo_value(operand)
#             C = A // denominator

#         else:
#             raise ValueError(f"Invalid opcode: {opcode}")

#         instruction_pointer += 2  # Move to the next instruction

#     # Return the joined output as a string
#     return ','.join(map(str, output))

# if __name__ == "__main__":
#     # Input initialization
#     registers = {'A': 63281501, 'B': 0, 'C': 0}
#     program = [2, 4, 1, 5, 7, 5, 4, 5, 0, 3, 1, 6, 5, 5, 3, 0]

#     # Execute program and get output
#     result = execute_program(registers, program)
#     print("Final output:", result)


#Part 2

import re
import os
from rich import print

input_path = os.path.join(os.path.dirname(__file__), 'input.txt')
program = list(map(int, re.findall(r"\d+", open(input_path).read())[3:]))
assert program[-2:] == [3, 0], "program does not end with JNZ 0"

def find(target, ans):
    if target == []: return ans
    for t in range(8):
        a = ans << 3 | t
        b = 0
        c = 0
        output = None
        adv3 = False

        def combo(operand):
            if 0 <= operand <= 3: return operand
            if operand == 4: return a
            if operand == 5: return b
            if operand == 6: return c
            raise AssertionError(f"unrecognized combo operand {operand}")

        for pointer in range(0, len(program) - 2, 2):
            ins = program[pointer]
            operand = program[pointer + 1]
            if ins == 0:
                assert not adv3, "program has multiple ADVs"
                assert operand == 3, "program has ADV with operand other than 3"
                adv3 = True
            elif ins == 1:
                b = b ^ operand
            elif ins == 2:
                b = combo(operand) % 8
            elif ins == 3:
                raise AssertionError("program has JNZ inside expected loop body")
            elif ins == 4:
                b = b ^ c
            elif ins == 5:
                assert output is None, "program has multiple OUT"
                output = combo(operand) % 8
            elif ins == 6:
                b = a >> combo(operand)
            elif ins == 7:
                c = a >> combo(operand)
            if output == target[-1]:
                sub = find(target[:-1], a)
                if sub is None: continue
                return sub

print(find(program, 0))