import sys

input = sys.stdin.readline

n, k = map(int, input().split())
tables = list(input())

for i in range(n):
    if tables[i] == 'P':
        for j in range(i-k, i+k+1):
            if j < 0 or j >= n:
                continue
            if tables[j] == 'H':
                tables[j] = 'E'
                break
        
print(tables.count('E'))