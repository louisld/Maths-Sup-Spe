import numpy as np
import matplotlib.pyplot as plt

# Constantes
g = 9.81 # m/s^2

# Paramètres généraux
l = 0.5 # m (longueur du pendule)
omega0 = np.sqrt(g/l) # Pulsation propre du pendule
lamb = 0.1 # Coefficient d'amortissement

# Fonctions
def f(theta, t):
    """
    Pendule simple
    d^2theta/dt^2=f(theta, t)
    """
    return -(omega0**2)*np.sin(theta)

def g(theta, v, t):
    """
    Pendule amorti
    d^2theta/dt^2=g(theta, v, t)
    """
    return -2*lamb*v - (omega0**2)*np.sin(theta)

def euler(f, t0, t1, theta0, v0, n):
    # Voir euler_amorti qui est quasiment identique
    t = np.linspace(t0, t1, n)
    h = (t1 - t0)/n
    theta = np.zeros(len(t))
    v = np.zeros(len(t))
    theta[0] = theta0
    v[0] = v0

    for i in range(len(t) - 1):
        v[i + 1] = v[i] + h * f(theta[i], t[i])
        theta[i + 1] = theta[i] + h * v[i]

    return t, theta, v

def euler_amorti(f, t0, t1, theta0, v0, n):
    """
    Méthode d'Euler pour résoudre une équation différentielle
    de la forme d^2theta/dt^2=g(theta, v, t).
    """
    t = np.linspace(t0, t1, n) # Abcisse de temps (suite t)
    h = (t1 - t0)/n # Pas de calcul (en s)
    theta = np.zeros(len(t)) # Angle du pendule (en rad)
    v = np.zeros(len(t)) # Dérivée de l'angle du pendule (en rad/s)
    theta[0] = theta0 # Condition initiale sur l'angle
    v[0] = v0 # Condition initiale sur la dérivée de l'angle

    # Itération des suites theta et v
    for i in range(len(t) - 1):
        v[i + 1] = v[i] + h * g(theta[i], v[i], t[i]) 
        theta[i + 1] = theta[i] + h * v[i]

    return t, theta, v

# Paramètres méthodes d'Euler
t0 = 0
t1 = 30
theta0 = np.pi/6
v0 = 0
n = int(1e6)

# Calcul
(t, theta, v) = euler_amorti(g, t0, t1, theta0, v0, n)

# Affichage des oscillations et du portrait de phase
fig, axs = plt.subplots(2)
axs[0].plot(t, theta)
axs[0].set_xlabel("Temps (en s)")
axs[0].set_ylabel("$\\theta$ (en rad)")
axs[0].set_title("Oscillations du pendule amorti")
axs[1].plot(theta, v)
axs[1].set_xlabel("$\\theta$ (en rad)")
axs[1].set_ylabel("$d\\theta/dt$ (en rad/s)")
axs[1].set_title("Portrait de phase du pendule amorti")
fig.suptitle("Résolution de l'équation différentielle du pendule amorti par la méthode d'Euler")
plt.show()