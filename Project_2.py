answer1 = input("You are going on a trip to Europe! Where do you want to go?")
if answer1 == "Spain":
    print("Vamos!")
elif answer1 == "Germany":
    print("Wichtigste Übersetzungen")
    answer2 = input("Where in Germany do you want to go? Berlin or Munich?")
    if answer2 == "Berlin":
        print ("Good choice, Berlin is Beautiful!")
    elif answer2 == "Munich":
        print ("Also a good choice! Munich is my favorite city.")
    else:
       print ("PLease pick either Berlin or Munich")
elif answer1 == "France":
    print("allons-y!")
    answer3 = input("Do you want to go to Paris or Normandy? ")
    if answer3 == "Paris":
     print("Staying in the city! Nice.")
    elif answer3 == "Normandy":
       print("Some good History up there!")
    else:
       print("Please pick either Paris or Normandy")
elif answer1 == "England":
    print("Let's go mate!")
    answer4 = input("Do you want to go to North London or West London?")
    if answer4 == "North London":
        print("Go Gunners! Lets get another championship!")
    elif answer4 == "West London":
        print("Only going to win that club world cup in the next 10 years. Come over to Arsenal!")
    else:
      print("Please pick either North London or West London")
elif answer1 == "Switzerland":
    print("Wichtigste Übersetzungen")
    answer5 = input("Do you want to go to Geneva or Zurich?")
    if answer5 == "Geneva":
       print("Very  Beautiful there!")
    elif answer5 == "Zurich":
        print("Go skiing, it will be fun!")
elif answer1 == "Italy":
    print("Andiamo!")
else: 
    print("Please pick either Spain, Germany, France,England, Switzerland, or Italy.")
