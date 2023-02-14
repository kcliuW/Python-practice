S = 'Python'
P = [S[:i] for i in range(len(S)+1)]
print(*(P+P[::-1]), sep = '\n')