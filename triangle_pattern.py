rows=int(input("Enter Number Of Rows :- "));
for i in range(0,rows):
    for j in range(rows-i):
        print(" ",end="");
    for k in range(0,i+1):
        print("* ",end="");
    print()
        # comment: 
    # end for
        # comment: 
    # end for