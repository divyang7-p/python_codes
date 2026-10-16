
a=int(input("Enter Mark Of Mathematics :- "))
b=int(input("Enter Mark Of Physics :- "))
c=int(input("Enter Mark Of Chemistry :- "))
d=int(input("Enter Mark Of English :- "))
e=int(input("Enter Mark Of Computer :- "))

def checkMarks(a,b,c,d,e):
    if(a>100 or a<0):
        return False;
    if(b>100 or b<0):
        return False;
    if(c>100 or c<0):
        return False;
    if(d>100 or d<0):
        return False;
    if(e>100 or e<0):
        return False;
    else:
        return True;
   
def calculate_total(a,b,c,d,e):
    total=a+b+c+d+e;
    return total;

def calculate_avg(total):
    avg=total/5;
    return avg;

def grade(avg):
    if avg>=90:
        print("Grade Is A");
    elif avg>=80:
        print("Grade Is B");
    elif avg>=70:
        print("Grade Is C");
    elif avg>=60:
        print("Grade Is D");
    else:
        print("Grade Is F");

x=checkMarks(a,b,c,d,e);
if (x):
    total=calculate_total(a,b,c,d,e);
    avg=calculate_avg(total);
    grade(avg);
else:
    print("Please Enter Valid Marks between 0 to 100")