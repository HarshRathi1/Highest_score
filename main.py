l=[]
highest=[]
scores=set()
for i in range(int(input())):
    name=input()
    score=float(input())
    l.append([name,score])
    scores.add(score)
h=sorted(scores)[-1]
for name,score in l:
    if h==score:
        highest.append(name)
for i in sorted(highest):
    print(i,end="\n")