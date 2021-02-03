# 2 consecutive absents allowed

n=int(input())
if n==1:
    print("Possible ways= ",1)
    print("Probability = ",str(0)+'\\'+str(1))
	
ways=[0,2,4,7]

for i in range(4,n+1):
	ways.append(ways[i-1]+ways[i-2]+ways[i-3])
	
total_ways=ways[n]
if n<4:
	not_attend=ways[n-1]
else:
    not_attend=ways[n-2]+ways[n-3]
print("(",total_ways,end=',')
print(str(not_attend)+'\\'+str(total_ways)+")")
print()
