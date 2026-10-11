rows = int (input("Enter Number Of Rows :- "));
for i in range (rows,0,-1):
    for j in range(0,rows-i):
        print(" ",end="");
    for k in range(0,i):
        print("* ",end="");
    print();
