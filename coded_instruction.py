def coded_instr(s: str) -> str:
    stack = []
    multiply = 0
    result = ''

    for char in s:
        if char.isdigit():
            multiply = multiply * 10 + int(char)
        elif char == '[':
            stack.append((result, multiply))
            result = ''
            multiply = 0
        elif char == ']':
            prev_result, prev_multiply = stack.pop()
            result = prev_result + result * prev_multiply
        else:
            result += char

    return result


instr = input()
coded_instruction = coded_instr(instr)
print(coded_instruction)
