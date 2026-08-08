import m
import sys

# Convert command-line arguments properly
num1: int = int(sys.argv[1])
oper: str = sys.argv[2]
num2: int = int(sys.argv[3])
quick: str = sys.argv[4] if len(sys.argv) > 4 else ""

def calc(operation: str, n1: int, n2: int):
    if operation in ('m', 'x', '*'):
        return n1 * n2
    elif operation == '-':
        return n1 - n2
    elif operation == '/':
        return n1 / n2
    elif operation == '+':
        return n1 + n2
    else:
        return 'Error'

ans = calc(oper, num1, num2)

if quick:  # non-empty string means True
    m.echo(f'Answer: {ans}')
else:
    m.echo(f"Answer: {ans}")
    m.chat(ans)
