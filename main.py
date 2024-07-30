# Função que calcula f(n) = 3n^2 + 2n + 1 :)
def f(n):
    return 3 * n**2 + 2 * n + 1

c = 6

n_start = 1
n_end = 10 

for n in range(n_start, n_end + 1):
    left_side = f(n)  # 3n^2 + 2n + 1
    right_side = c * n**2  # 6n^2
    
    if left_side <= right_side:
        print(f"Para n = {n}: {left_side} <= {right_side} (verdadeiro)")
    else:
        print(f"Para n = {n}: {left_side} > {right_side} (falso)")

print("\nConclusão: f(n) = 3n^2 + 2n + 1 é O(n^2) para n >= 1.")

# coments
# 3n^2+ 2n + 1 ≤ 6n^2
# 3n^2 + 2n + 1 ≤ 3n^2 + 2n^2 + n^2 = 6n^2
# 𝑓(𝑛) = 3n^2 + 2n + 1 é O(n^2)