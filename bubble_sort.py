import random 

def bubble(numbers): 
    length = len(numbers) - 1 
    sorted = False
    
    while sorted != True: 
        sorted = True
        for n in range(0,length):
            if numbers[n] > numbers[n+1]:
                sorted = False
                numbers[n],numbers[n+1]  = numbers[n+1], numbers[n]
    return numbers
    
numbers = []
for i in range(10):
    numbers.append(random.randint(0,100))

print (f"Random Numbers: {numbers}" )
print()
print (f"Sorted List: {bubble(numbers)}")
