import time
lock_code = 2580
i = 5

while i>=0:
    guess = int(input('Enter your password'))
    if guess == lock_code:
        print(" Access granted")
        break
    else:
        if(i == 0):
            print(" Chances Over.. Wait for 5 seconds")
            count = 5
            while(count>0):
                print(count)
                time.sleep(1)
                count=count-1
            i=5
        else:
            print(" Wrong Password. You have " +str(i)+" chances reamining")
            i=i-1
        
