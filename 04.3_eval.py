with open("data.dat", "r") as file:
    line = file.read()
    scdb = eval(line)

print(line)
print(scdb) # eval 함수를 사용하여 \n이 포함된 문자열을 쉽게 dictionary형태로 변환하였다