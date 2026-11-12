
bakingPoints = 00
meatPoints = 0
SaladPoints = 0
UsageMax = 20
UsagePro = 15
UsageRegular = 10
print("Welcome to culihelp, your personal recipe finder. This will decide a good recipe for you based on answers to a quiz.")
plan = input("What plan do you want to pick? Max is the most, Pro is in the Middle, and then Regular is for basic tasks. Which do you want to pick?")
if plan == "Max":
    print("Sounds great, let's dive in!")
    tries = 20
elif plan == "Pro":
    print("Great! Not a big task this time. Let's dive in!")
    tries = 15
elif plan == "Regular":
    print("Small task this time, this should be quick and easy!")
    tries = 10

for i in range(tries):
    answer1 = input("Are you sure you want to submit this answer? This will be final, and cannot be changed...y/n?")
if answer1 == "y":
    print("Here is your recipe:")
    print ("https://www.mccormick.com/blogs/recipes/vanilla-rich-chocolate-chip-cookies")
else:
    print("https://sallysbakingaddiction.com/key-lime-pie-bars/")

    