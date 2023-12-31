'''
File input.txt contains numbers separated by comma as shown below,
6,8
7,6
2,8
9,5
9,6
Exercise:1 Write a function countNum(num) so that it returns number of occurrences of a number in that file.e.g, 
countNum(9) should return 2
countNum(100) should return 0
'''

#Solution:
'''

file_content=""" 
6,8
7,6
2,8
9,5
9,6"""


with open ("C:\\Users\\ruhul\\OneDrive\\Documents\\Job preparation 2023\\code basics\\input.txt","w") as f:
    f.write(file_content)
print("successfully done!")
'''


def countNum(num):
    with open ("C:\\Users\\ruhul\\OneDrive\\Documents\\Job preparation 2023\\code basics\\input.txt","r") as f:
        lines=f.readlines()
        count=0
        for line in lines:
            numbers=[int(n) for n in line.strip().split(",")]
            if num in numbers:
                count=count+1
    return count


res_2=countNum(2)
res_5=countNum(5)
res_6=countNum(6)
res_7=countNum(7)
res_8=countNum(8)
res_9=countNum(9)
print(f"Occurance of 2:{res_2}")
print(f"Occurance of 5:{res_5}")
print(f"Occurance of 6:{res_6}")
print(f"Occurance of 7:{res_7}")
print(f"Occurance of 8:{res_8}")
print(f"Occurance of 9:{res_9}")

'''
Exercise:2 Change input.txt so that when program ends it contains sum of all numbers in a line as shown below,
sum:14 | 6,8
sum:13 | 7,6
sum:10 | 2,8
sum:14 | 9,5
sum:15 | 9,6
'''

def updateAndWriteSum():
    with open("input.txt","r") as fr1:
        lines=fr1.readlines()
    with open("input.txt","w") as fw1:
        for line in lines:
            number1=[int(n1) for n1 in line.strip().split(",")]
            sumOfNum=sum(number1)
            fw1.write(f"sum:{sumOfNum} | {line}")


updateAndWriteSum()

