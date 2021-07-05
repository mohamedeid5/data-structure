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
    for i in range(len(exp)):
        # if finds any open bracktes add it to stack
        if exp[i] == '(' or exp[i] == '{' or exp[i] == '[':
            stack.push(exp[i])
        elif exp[i] == ')' or exp[i] == '}' or exp[i] == ']':
            # if stack is empty then there's no open brackets then it is not balanced
            if stack.isEmpty():
                return False
            # if open bracktes is not balanced return false
            elif not pair(stack.top_value(), exp[i]):
                return False
            stack.pop() # if exists then remove last one
        else: 
            return False
            
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
