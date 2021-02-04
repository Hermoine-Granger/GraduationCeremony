# 2 consecutive absents allowed

n=int(input())
	
ways=[0,0,1,1]
hard_coded_last_idx=3

for i in range(1,n+1):
    i=i+hard_coded_last_idx
    ways.append(ways[i-1]+ways[i-2]+ways[i-3])
	
n+=hard_coded_last_idx    
total_ways=ways[n]
if n<=2*hard_coded_last_idx:
	not_attend=ways[n-1]
else:
	not_attend=ways[n-2]+ways[n-3]

print("(",total_ways,end=',')
print(str(not_attend)+'\\'+str(total_ways)+")")
