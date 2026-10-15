avgmark=float(input("Enter Your Average Maarks :- "));
a="Grade Is :- "
if avgmark>=90:
    age=int(input("What Is Your Age :- "))
    if age<=18:
        print(a+"A+")
    else:
        print(a+"A")
elif avgmark<=89 and avgmark>=80:
    age=int(input("What Is Your Age :- "))
    if age<=18:
            print(a+"B+")
    else:
            print(a+"B")
elif avgmark<=79 and avgmark>=70:
    age=int(input("What Is Your Age :- "))
    if age<=18:
            print(a+"C+")
    else:
            print(a+"C")
elif avgmark<=69 and avgmark>=60:
    age=int(input("What Is Your Age :- "))
    if age<=18:
            print(a+"D+")
    else:
            print(a+"D")
else:
    print(a+"F")