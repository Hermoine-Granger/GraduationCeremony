
#number of consecutive absents allowed=a

a=int(input("Enter number of consecutive absents allowed: "))
n=int(input("Enter number of days: "))
	
ways=[0 for i in range(a)]
ways.append(1)

hard_coded_size=a+1

for i in range(0,n+1):
    i=i+hard_coded_size
    val=0
    for j in range(1,hard_coded_size+1):
        val+=ways[i-j]
    ways.append(val)

print(ways)
n+=hard_coded_size	
total_ways=ways[n]
if n<=2*hard_coded_size:
	not_attend=ways[n-1]
else:
    val=0
    for j in range(2,hard_coded_size+1):
        val+=ways[n-j]
    not_attend=val

print("(",total_ways,end=',')
print(str(not_attend)+'\\'+str(total_ways)+")")


