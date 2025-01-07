import cupy as cp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random
import time

# Tetraéder csúcsai
A = cp.array([0, 0, 0])
B = cp.array([1, 0, 0])
C = cp.array([0.5, cp.sqrt(3)/2, 0])
D = cp.array([0.5, cp.sqrt(3)/6, cp.sqrt(2/3)])

# Iterációk száma
iterations = 10000

# Kezdőpont véletlenszerűen
current_point = cp.array([0.5, 0.5, 0.5])

# Ábra beállítása
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_title('Sierpiński-tetraéder (GPU)')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_xlim([0, 1])
ax.set_ylim([0, 1])
ax.set_zlim([0, 1])

# Frissítési frekvencia (hány pont kirajzolása után frissítjük a progressziót)
refresh_rate = 100

# Iterációk
start_time = time.time()
for i in range(1, iterations + 1):
    # Véletlenszerűen kiválasztunk egy csúcsot
    random_vertex = random.choice([A, B, C, D])
    
    # Új pont számítása (felezőpont)
    current_point = (current_point + random_vertex) / 2
    
    # Pont kirajzolása
    ax.scatter(current_point[0], current_point[1], current_point[2], color='b', s=1)
    
    # Progresszió és ábra frissítése
    if i % refresh_rate == 0:
        percent_complete = (i / iterations) * 100
        elapsed_time = time.time() - start_time
        print(f"Progress: {percent_complete:.2f}% - Elapsed Time: {elapsed_time:.2f} seconds")
        plt.pause(0.001)  # Valós idejű frissítés

# Végső állapot
print("Progress: 100.00% - Done!")
plt.show()
