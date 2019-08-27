# Made by Selva
# For Jai in 27/08/2019
s = [[123,183,1,2],[223,283,1,2],[323,383,1,2],[323,383,1,2]]
result = [ ]
for row in s:
    r1 = [ ]
    r2 = [ ]
    m1 = int(row[0] + (row[1] - row[0])/2) # median? no
    m2 = m1 + 1
    r1.append(row[0])
    r1.append(m1)
    for i in range(2,len(row)):
        r1.append(row[i])
    r2.append(m2)
    r2.append(row[1])
    for i in range(2,len(row)):
        r2.append(row[i])
    result.append(r1)
    result.append(r2)
for row in result:
    print(row)
