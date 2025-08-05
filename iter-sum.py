from itertools import combinations_with_replacement


numbers = [0, 1, 2, 3, 4, 5, 6, 8]
target_sum = 14

results = []
for combination in combinations_with_replacement(numbers, 4):
    if sum(combination) == target_sum:
        results.append(combination)

print("Combinations that sum to", target_sum, ":", results)
print("Total combinations found:", len(results))        
# Output the results   
for combo in results:
    print(combo)
print("End of combinations.") 