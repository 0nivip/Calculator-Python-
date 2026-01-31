# Simple console calculator


Plus = "+"
Minus = "-"
Divide = "/"
Multiply = "*"

n = int(input("The first number: "))
op = input("+ to add, - to subtract, / to divide, * to multiply: ")

# Loop allows multiple calculations (up to 100 operations)
for _ in range(100):
    # Validate operation input
    while op != Plus and op != Minus and op != Divide and op != Multiply and op != "=":
        op = input("+ to add, - to subtract, / to divide, * to multiply: ")
    
    # Finish calculation if user inputs "="
    if op == "=":
            break
    
    m = int(input("Next number: "))
    
    # Select operation
    if op == Plus:
        n += m
    elif op == Minus:
        n -= m
    elif op == Divide:
        # Prevent division by zero
        if m == 0:
            print("Error: Division by zero")
            continue
        n /= m
    elif op == Multiply:
        n *= m
    
    op = input("+ to add, - to subtract, / to divide, * to multiply, = to finish: ")
    
    

print("The result is", n)