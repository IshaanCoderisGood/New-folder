def circuit(A, B, C):
    and1 = A and B
    and2 = B and C
    or1 = C or and2
    
    Q = and1 or or1
    
    return Q

inputs = [
    (0, 0, 0),
    (0, 0, 1),
    (0, 1, 0),
    (0, 1, 1),
    (1, 0, 0),
    (1, 0, 1),
    (1, 1, 0),
    (1, 1, 1),
]

print("A B C | Q")
print("------|---")
for A, B, C in inputs:
    Q = circuit(A, B, C)
    print(f"{A} {B} {C} | {Q}")
