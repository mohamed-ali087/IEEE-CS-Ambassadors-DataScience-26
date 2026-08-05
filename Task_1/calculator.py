input1 = float(input("input 1: "))
op = input("operator: ")
input2 = float(input("input 2: "))

if op == "/" and int(input2) == 0:
    raise Exception("Zero Division")
    

if op not in "+/*-^":
    raise Exception("Invalid operator")
    
print(eval(f"{input1} {op} {input2}"))