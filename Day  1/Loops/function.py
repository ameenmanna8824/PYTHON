def weatherForecast(weather):
    if(weather=="Sunny"):
        print("It is hot day")
    elif(weather=="Rainy"):
        print("Its Raining")
    else:
        print("Normal Day")

while True:
	n=input()
	weatherForecast(n)
