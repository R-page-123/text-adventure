# program fibonacci.py
# recursive algorithm to calculate the numbers in the
# Fibonacci sequence 0,1,1,2,3,5,8..
# in which each number after the first two
# is the sum of the previous pair of numbers
#each routine is timed
import time

def fibonacci(n):
    if n <= 1:
        return n
    else:    
        return fibonacci(n-1) + fibonacci(n-2)
    #endif
#endfunction
    
#iterative method
def fibonacci2(n):
    fibNumbers = [0,1]  #list of first two Fibonacci numbers
# now append the sum of the two previous numbers to the list    
    for i in range(2, n+1):
        fibNumbers.append(fibNumbers[i-1] + fibNumbers[i-2])
    return fibNumbers[n]  

#input how many items in series
n = 0
while not (n in range(2,31)):
    n = int(input("input how many numbers (between 3 and 30 in the series to calculate: "))
    if (n < 3) or (n > 30):
        print("Number out of range: please enter a number between 3 and 30")
    #endif
#endwhile
    
#time.clock returns the current processor time in seconds
startTime1 = time.time()
for x in range(n):
    print (x+1,fibonacci(x))
endTime1 = time.time()
time1 = (endTime1 - startTime1)*1000
print("\nexecution time for recursive algorithm: ",  round(time1,4)," milliseconds")


startTime2 = time.time()
for x in range(n):
    print (x+1,fibonacci2(x))
endTime2 = time.time()
time2 = (endTime2 - startTime2)*1000
print("\nexecution time for iterative algorithm: ", round(time2,4)," milliseconds")

input("\nPress Enter to end")
