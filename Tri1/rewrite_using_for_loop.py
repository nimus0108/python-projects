#Su Min Kim
#10-20
#Rewrite using a for loop
import math

print ("%-10s%16s%16s" % ("Radius", "Circumference", "Area"))

for i in range(2, 17, 3):
    circum = i * 2 * math.pi
    area = i ** 2 * math.pi

    print ("%-10d%16.1f%16.2f" % (i, circum, area))

