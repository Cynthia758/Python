import random # Implies that you're importing the built-in random module into your programe.
# If you are making a game, simulations or anything that requires random behaviour, the random module is super useful.
jackpot = random.randint(1,1000)  # The function random.randint(a,b) returns a random integer between a and b, including both a and b;
guess = int(input('Guess Karo : '))
counter = 1
while guess != jackpot:
    if guess < jackpot:
        print("Go Higher")
    else :
        print("Go Lower")
    guess = int(input('Phirse guess kar : '))
    counter +=1
print("Sahi jawaab")
print("You took", counter ,"no. of trials.")