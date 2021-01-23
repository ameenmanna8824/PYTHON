import time
prices=[10,20,30,40,50,60,70,80,90,100]
result=0
for i in prices:
    result=result+i
    print(result)
    time.sleep(0.01)
print(f"End of result: {result}")
    
