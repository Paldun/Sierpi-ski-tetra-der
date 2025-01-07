import cupy as cp
import matplotlib.pyplot as plt
import random
import time

# Háromszög csúcsai
A = cp.array([0, 0])
B = cp.array([1, 0])
C = cp.array([0.5, cp.sqrt(3) / 2])

# Iterációk száma
iterations = 10000

# Kezdőpont véletlenszerűen
current_point = cp.array([0.5, 0.5])

# Ábra beállítása
plt.figure()
plt.axis('equal')
plt.xlim(-0.1, 1.1)
plt.ylim(-0.1, 1.1)
plt.title('Sierpiński-háromszög (GPU)')
plt.xlabel('X')
plt.ylabel('Y')

# Frissítési frekvencia (hány pont kirajzolása után frissítjük a progressziót)
refresh_rate = 100

# Iterációk
start_time = time.time()
for i in range(1, iterations + 1):
    # Véletlenszerűen kiválasztunk egy csúcsot
    random_vertex = random.choice([A, B, C])
    
    # Új pont számítása (felezőpont)
    current_point = (current_point + random_vertex) / 2
    
    # Pont kirajzolása
    plt.plot(current_point[0], current_point[1], 'b.', markersize=1)
    
    # Progresszió és ábra frissítése
    if i % refresh_rate == 0:
        percent_complete = (i / iterations) * 100
        elapsed_time = time.time() - start_time
        print(f"Progress: {percent_complete:.2f}% - Elapsed Time: {elapsed_time:.2f} seconds")
        plt.pause(0.001)  # Valós idejű frissítés

# Végső állapot
print("Progress: 100.00% - Done!")
plt.show()
