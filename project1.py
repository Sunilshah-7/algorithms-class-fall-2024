import time
def algorithm(n, a, b):
    sum = 0
    j = 2
    while j < n:
        k = j
        while k < n:
            sum += a[j] * b[k]
            k = k * k
        j = 2 * j
    return sum

def run_experiment(n_values):
    results = []
    for n in n_values:
        a = list(range(n))
        b = list(range(n))
        
        start_time = time.time()
        algorithm(n, a, b)
        end_time = time.time()
        
        execution_time = end_time - start_time
        results.append((n, execution_time))
    return results

n_values = [10000, 100000, 1000000, 10000000, 100000000]
results = run_experiment(n_values)
print("\nResults:")
for n, time in results:
    print(f"n = {n}: {time} seconds")