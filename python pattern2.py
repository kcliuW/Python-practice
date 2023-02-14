S = 'Python'
P = [S[:i] for i in range(len(S)+1)]
for i in P:
    print(f'{i*(len(i)):^40}')