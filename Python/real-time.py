import matplotlib.pyplot as plt
import random

# A háromszög csúcsai
A = [0, 0]
B = [1, 0]
C = [0.5, (3**0.5)/2]  # Magasság a háromszögnél

# Iterációk száma
iterations = 10000

# Kezdőpont véletlenszerűen a háromszög belsejében
x, y = 0.5, 0.5

# Új ábra létrehozása
plt.figure()
plt.title('Sierpiński-háromszög (valós idejű)')
plt.xlabel('X')
plt.ylabel('Y')
plt.axis('equal')
plt.xlim(-0.1, 1.1)
plt.ylim(-0.1, 1)

# Frissítési frekvencia (hány pont kirajzolása után frissítsük az ábrát és írjuk ki az állapotot)
refresh_rate = 100

# Iterációk
for i in range(iterations):
    # Véletlenszerűen kiválasztunk egy csúcsot
    random_choice = random.choice([A, B, C])
    
    # Új pont számítása
    x = (x + random_choice[0]) / 2
    y = (y + random_choice[1]) / 2
    
    # Pont kirajzolása
    plt.plot(x, y, 'b.', markersize=1)
    
    # Frissítés és állapotjelentés adott számú pont után
    if i % refresh_rate == 0:
        percent_complete = (i / iterations) * 100
        print(f"Progress: {percent_complete:.2f}%")
        plt.pause(0.001)

# Végső állapotjelentés és megjelenítés
print("Progress: 100.00% - Done!")
plt.show()
