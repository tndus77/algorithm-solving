import sys
from collections import defaultdict
input = sys.stdin.readline

tree = defaultdict(int)
cnt = 0

while True:
    name = input().rstrip()
    if name == "":
        break # 입력이 없으면 break
    tree[name] += 1 #name value에 +1
    cnt += 1
    
tname = list(tree.keys())
tname.sort()

for i in tname:
    print("%s %.4f" % (i, tree[i]*100/cnt))
        