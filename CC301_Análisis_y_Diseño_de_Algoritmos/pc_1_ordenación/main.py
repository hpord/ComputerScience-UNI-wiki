import time
import os

start1 = time.time()
os.system('python sort_bubble.py')
done1 = time.time()

start2 = time.time()
os.system('python sort_insection.py')
done2 = time.time()

start3 = time.time()
os.system('python sort_selection.py')
done3 = time.time()

start4 = time.time()
os.system('python sort_cocktail.py')
done4 = time.time()

print("\nLos tiempos son: \n")
print(done1 - start1)
print(done2 - start2)
print(done3 - start3)
print(done4 - start4)
