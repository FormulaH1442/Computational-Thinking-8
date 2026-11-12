import random 

hidden_number = random.randint (1, 49)
#Hidden Number!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1
#print(hidden_number)
guess1 = int(input("Pick a number from 1 and 49"))
if guess1 == "hidden_number":
    print("you actually won!")
elif guess1 > "hidden_number":
    print("You went to big try a smaller number!")
elif guess1 < "hidden_number":
    print("You went to small so dream bigger!")
else:
    print("Guess a number")

    for i in range(48):
        #Hidden Number!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1
        #print(hidden_number)
        guess1 = int(input("Pick a number from 1 and 49"))
        if guess1 == "hidden_number":
            print("you actually won!")
        elif guess1 > "hidden_number":
            print("You went to big try a smaller number!")
        elif guess1 < "hidden_number":
            print("You went to small so dream bigger!")
        else:
        
         print("Guess a number")     


