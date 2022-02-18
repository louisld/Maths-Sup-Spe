import matplotlib.pyplot as plt
import numpy as np

# Constantes
g = 9.81

# Paramètres
v0 = 10
alpha = np.pi/4

def z(x):
    """
    Équation de la trajectoire dans le plan (Oxz)
    """
    return -0.5*g/((v0*np.cos(alpha))**2)*x**2 + np.tan(alpha)*x

def parabole_s(x):
    """
    Équation de la parabole de sûreté dans le plan (Oxz)
    """
    return v0**2/(2*g) - g*x**2/(2*v0**2)

X = np.linspace(0, 10, 1000) # Tableau contenant les abcisses
Z = z(X) # Tableau contenant la hauteur z de la trajectoire pour chaque x
P = parabole_s(X) # Tableau contenant la hauteur z de la parabole de sûreté pour chaque x

plt.plot(X, Z, label="Trajectoire $\\alpha=\\pi/2$")
plt.plot(X, P, label="Parabole de sûreté")
plt.xlabel("Longueur(en m)")
plt.ylabel("Hauteur (en m)")
plt.title("Parabole de sûreté pour un tir de projectile")
plt.legend()
plt.show()