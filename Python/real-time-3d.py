import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random

# A tetraéder négy csúcsa (3D koordináták)
A = [0, 0, 0]
B = [1, 0, 0]
C = [0.5, (3**0.5)/2, 0]  # Háromszög alapmagasság
D = [0.5, (3**0.5)/6, (2/3)**0.5]  # Tetraéder csúcsmagassága

# Iterációk száma
iterations = 10000

# Kezdőpont véletlenszerűen a tetraéder belsejében
x, y, z = 0.5, 0.5, 0.5

# Új ábra létrehozása
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_title('Sierpiński-tetraéder (valós idejű)')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_zlim(0, 1)

# Frissítési frekvencia (hány pont kirajzolása után frissítsük az ábrát és írjuk ki az állapotot)
refresh_rate = 100

# Iterációk
for i in range(iterations):
    # Véletlenszerűen kiválasztunk egy csúcsot
    random_choice = random.choice([A, B, C, D])
    
    # Új pont számítása
    x = (x + random_choice[0]) / 2
    y = (y + random_choice[1]) / 2
    z = (z + random_choice[2]) / 2
    
    # Pont kirajzolása
    ax.scatter(x, y, z, color='blue', s=1)
    
    # Frissítés és állapotjelentés adott számú pont után
    if i % refresh_rate == 0:
        percent_complete = (i / iterations) * 100
        print(f"Progress: {percent_complete:.2f}%")
        plt.pause(0.001)

# Végső állapotjelentés és megjelenítés
print("Progress: 100.00% - Done!")
plt.show()
