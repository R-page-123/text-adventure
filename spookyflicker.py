import random
import time

light = "HIGH"
while light != "":
    ran = random.randint(10, 1001)
    ran = ran / 1000
    light = "HIGH"
    print(light)
    time.sleep(ran)
    light = "LOW"
    print(light)