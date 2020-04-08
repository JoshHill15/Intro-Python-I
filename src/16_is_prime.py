import sys


x = []
if len(sys.argv) == 1:
    print("no number specified")
else:
    for num in range(2, int(sys.argv[1])):
        prime = True
        for i in range(2, num):
            if num % i == 0:
                prime = False
        if prime:
            x.append(num)
print(x)
