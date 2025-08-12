try:
 with open("sample.txt",'r')as f:
    lines=f.readlines()
    for line in lines:
        print(line.strip())
except FileNotFoundError:
    print("file {'sample.txt'}is not present")



