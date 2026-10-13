putter = 0
wedge56 = 0
wedge54= 0
ApproachWedge = 0
PitchingWedge = 0
iron9 = 0
iron8 = 0
iron7 = 0
iron6 = 0
iron5 = 0
wood4 = 0
wood5 = 0
driver = 0

answer1 = input("Welcome! This test will decide what your favorite golf club is! First, do you like putting, chipping,irons, or Using your woods? ")
if answer1 == "Putting":
    putter += 1
elif answer1 == "chipping":
    answer2 =   input("Do you prefer aproach shots or short shots?")
    if answer2 == "approach shots":
        ApproachWedge += 1 
elif answer1 == "Irons":
    answer3 = input("Doy you prefer a 9,8,7,6,or 5?")
    if answer3 == "9":
             iron9 += 1
    if answer3 == "8":
                 iron8 += 1
    if answer3 == "7":
                 iron7 += 1  
    if answer3 == "6":
                 iron6 += 1
    if answer3 == "5":
                 iron5 += 1
elif answer1 == "woods":
    answer4 = input("Do your prefer, the driver, 5 wood or hybrid?")
    if answer4 == "5 wood":
            wood5 += 1
    if answer4 == "hybrid":
        wood4 += 1
    if answer4 == "driver":
        driver += 1
print("Nice choices, lets ask some more questions to really narrow this down")
answer4 = input("Some more questions to narrow this down, almost done with this quiz do you like par 3s, par 4s, or par 5s?")
if answer4 == "par 3s "or answer4 == "Par 3s":
    wedge54 += 1
    wedge56 += 1
    ApproachWedge += 1
    PitchingWedge += 1
elif answer4 == "par 4s" or answer4 == "Par 4s":
    driver += 1
    wood4 += 1
    wood5 += 1
    iron6 += 1
    iron5 += 1
elif answer4 == "par 5s" or answer4 == "Par 5s":
    driver += 2
    wood5 += 2
    wood4 += 2
    iron5 += 2
    iron6 += 2
else:
       print("Please pick either par 3,4, or 5")
print("Alright, I think we have all the answer we need.")
if driver > wood5 and driver > wood4 and driver > iron5 and driver > iron6 and driver > iron7 and driver