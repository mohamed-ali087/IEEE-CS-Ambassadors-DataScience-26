input = int(input("input: "))

for i in range(1, 11):
    if i*input % 4 != 0:
        print(i*input, end=", ")
        
print("\b\b")