from stack import Stack


def Priority(c):
    if c == '-' or c == '+':
        return 1
    elif c == '*' or c == '/':
        return 2
    elif c == '^':
        return 3
    else:
        return 0


def postfix(exp):
    stack = Stack()
    output = ''
    for i in range(len(exp)):
        # check if it is number
        if exp[i].isdigit() or exp[i].isalpha():
            # then put it to output
            output += exp[i]
        # check if it is a '('
        elif exp[i] == '(':
            # then add it to stack
            stack.push(exp[i])
        # check if it is a ')'
        elif exp[i] == ')':
            # if top not equal '(' pop till reaches to '('
            while stack.topValue() != '(':
                output += stack.topValue()
                stack.pop()
            # if it is a '(' then remove it
            stack.pop()
        else:
            while not stack.isEmpty() and Priority(exp[i]) <= Priority(stack.topValue()):
                output += stack.topValue()
                stack.pop()
            # if it is operator then add it to stack
            stack.push(exp[i])
    while not stack.isEmpty():
        output += stack.topValue()
        stack.pop()

    stack.printStack()
    return output


def operation_math(op1, op2, operate):
    if operate == '+':
        return op1 + op2
    elif operate == '-':
        return op1 - op2
    elif operate == '*':
        return op1 * op2
    elif operate == '/':
        return op1 / op2
    else:
        return 0


def postfix_evaluate(exp):
    stack = Stack()
    for i in range(len(exp)):
        if exp[i].isdigit():
            stack.push(exp[i])
        else:
            op2 = stack.topValue()
            stack.pop()

            op1 = stack.topValue()
            stack.pop()

            result = operation_math(int(op1), int(op2), exp[i])
            stack.push(result)
    stack.printStack()
    print(stack.topValue())


postfix('(3+2)+7/2*((7+3)*2)')
postfix_evaluate('382/+5-')
