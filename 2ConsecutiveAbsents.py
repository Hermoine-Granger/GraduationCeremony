# 2 consecutive absents allowed

n=int(input())
if n==1:
    print("Possible ways= ",1)
    print("Probability = ",str(0)+'\\'+str(1))
	
ways=[0,0,1,1]


for i in range(1,n+1):
    i=i+3
    ways.append(ways[i-1]+ways[i-2]+ways[i-3])
	
n+=3    
total_ways=ways[n]
not_attend=ways[n-2]+ways[n-3]

print("(",total_ways,end=',')
print(str(not_attend)+'\\'+str(total_ways)+")")
print()
