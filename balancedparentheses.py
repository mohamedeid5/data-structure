from stack import Stack


def pair(open, close):
    if open == '(' and close == ')':
        return True
    elif open == '{' and close == '}':
        return True
    elif open == '[' and close == ']':
        return True
    else:
        return False


def balanced(exp):
    stack = Stack()
    # get expression
    for i in range(len(exp)):
        # chek if the expression has a open bracket
        if exp[i] == '(' or exp[i] == '{' or exp[i] == '[':
            # then put the expression
            stack.push(exp[i])
            # check if it has a close bracket
        elif exp[i] == ')' or exp[i] == '}' or exp[i] == ']':
            # if stack is empty, it means no open brackets so return false
            if stack.isEmpty():
                return False
            # check if the top value equals
            elif not pair(stack.topValue(), exp[i]):
                return False
            stack.pop()  # if exists then remove last one
    if stack.isEmpty():
        return True
    else:
        return False


while True:
    exp = input('enter your expression:\n')

    if exp == 'q':
        break
    if balanced(exp):
        print('expression is balanced')
    else:
        print('expression is not balanced')
