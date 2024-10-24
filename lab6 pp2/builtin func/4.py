import time
import math

def delayed_sqrt(value, delay):
    time.sleep(delay / 1000)  
    return math.sqrt(value)

value = 25100
delay = 2123
result = delayed_sqrt(value, delay)
print(f"Square root of {value} after {delay} milliseconds is {result}")
