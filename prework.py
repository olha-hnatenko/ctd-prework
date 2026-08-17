# This program checks the weather in your city.

city = input("What city do you live in? ")
temperature = float(input("What is the temperature outside? "))


if temperature > 85:
    print("It's " + str(int(temperature)) + " degrees in " + city + "! It's hot!")
elif temperature >= 70:
    print("The weather is nice in " + city + ". Let's go for a walk!")
else:
    print("Don't forget your jacket! It's cool in " + city +" today.")
    