with open("text.txt", "rt") as file:
    line1 = file.readline()
    line2 = file.readline()
    line3 = file.readline()
    line4 = file.readline()
    print(line1) # "1번 줄\n"
    print(line2) # "2번 줄\n"
    print(line3) # "3번 줄"
    print(line4) # ""

with open("text.txt", "rt") as file:
    lines = file.readlines()
    print(lines) # ["1번 줄\n", "2번 줄\n", "3번 줄"]
    
with open("text.txt", "rt") as file:
    allLines = file.read()
    print(allLines) # "1번 줄\n 2번줄\n 3번줄\n"