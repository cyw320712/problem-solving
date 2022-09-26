a = input()
b = input()

anum = a.count('1')
bnum = b.count('1')

if (anum%2==0 and anum < bnum) or (anum%2==1 and anum + 1 < bnum):
    print("DEFEAT")
else:
    print("VICTORY")