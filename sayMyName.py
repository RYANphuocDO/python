'''
#I made an extra that take your inputs and will do the rest
#Feel free to check
#Input your name
print("What's your name?")
name = input()
#Input your SID
print("What's your SID?")
sid = input()
#Print out the first two digits of your SID times
for x in range(int(sid[0:2])+1):
    print(name)
'''

#Name: HUYNH THIEN PHUOC DO
name = "HUYNH THIEN PHUOC DO"
#SID: 510411725
sid = 510411725

for x in range(int(str(sid)[0:2])+1):
    print(name)