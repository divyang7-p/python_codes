import random;
secrate = random.randint(1,10);
guess=int(input("Guess A Number Between 1 to 10 (1 and 10 Are Included) :- "));
if secrate==guess :
    print("You Get It Right!!..");
else:
    print("Not Right!!..");
    print("The Number Is ",secrate);
# randint(1,10) convert random number generated between 1 to 10 into an integer..