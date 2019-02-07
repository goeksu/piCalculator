
import random
import math

count_inside = 0
print("Deneme sayisi:")
n = input()
for count in range(0, n):
    d = math.hypot(random.random(), random.random())
    if d < 1: count_inside += 1
    count += 1
    pi = 4.0 * count_inside / count
    minus = pi - math.pi
    end = count

    print "{}     {}     {}".format(end, pi, minus)
print "Sayi {} denemede {} olarak hesaplandi.".format(end, pi)
print "Aradaki fark {}".format(minus)

