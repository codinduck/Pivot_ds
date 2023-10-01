
# 1. a 2D matrix of size 5x3 with the column to be aggregated always at the end of the matrix.
# 2. print the aggregated output as key-value pairs

array = [['G','X',1],['G','Y',2],['G','X',3],['H','Y',4],['H','Z',5]]
for row in array:
    print(row)

aggdict={}
valuelist=[]
keylist=[]
combinedkeylist=[]

for i in range(0,5):
    valuelist.append(array[i][2])
    for j in range(0,2):
        keylist.append(array[i][j])


print(valuelist)
print(keylist)

length=len(keylist)
for i in range(0,length,2):
    combinedkeylist.append(keylist[i]+keylist[i+1])

length=len(combinedkeylist)
for x in range(0,length):
    if combinedkeylist[x] in aggdict:
        val=aggdict[combinedkeylist[x]] + valuelist[x]
        key=combinedkeylist[x]
    else:
        key=combinedkeylist[x]
        val=valuelist[x]
    aggdict[key]=val
print(aggdict)
