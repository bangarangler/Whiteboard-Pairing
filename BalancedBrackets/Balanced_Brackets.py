def balancedBrackets(str):
    line = list(str)
    stack = []
    openers = {
        '(': ')',
        '{': '}',
        '[': ']',
    }

    closers = {
        ")": True,
        "}": True,
        "]": True,
    }

    for c in line:
        if c in openers:
            stack.append(c)
        elif c in closers:
            if (openers[stack.pop()] != c):
                return False
    return len(stack) == 0


print(balancedBrackets('{}[]()'))        # should print True
print(balancedBrackets('{(([]))}'))      # should print True
print(balancedBrackets('{ [ ] ( ) }'))   # should print True
print(balancedBrackets('{ [ ( ] ) }'))   # should print False
print(balancedBrackets('('))             # should print False
print(balancedBrackets('{[}'))           # should print False
