from math import *
x = "y"
while x == "y":
    print("The Calculation will be nCr and nPr")
    inp1 = input("Enter input (it should be of the format nCr or nPr) : ")
    if "c" in inp1:
        inp = inp1.partition("c")
    if "p" in inp1:
        inp = inp1.partition("p")
    # noinspection PyUnboundLocalVariable
    print(inp)
    n = int(inp[0])
    r = int(inp[2])
    op = inp[1]
    op = op.lower()
    if op == "c":
        nCr = (factorial(n)/(factorial(r)*factorial(n-r)))
        print("nCr is : ", nCr)
    elif op == "p":
        nPr = (factorial(n)/factorial(n-r))
        print("nPr is : ", nPr)
    x = input("Do you want to continue (Y/n) : ")
    x = x.lower()
