import matplotlib.pyplot as plt

LAMBDA = 0.81 * 0.007853982 / 2 #Valores constantes organizados como un valor unico
MASS = 0.6
WEIGHT = MASS * 9.8

#Arreglos para acumular datos de la gráfica
valores_eje_y = []
iteraciones_lista = []

vel = 0
time = 0
net_force = 0
friction_force = 0
distance = 0
altitude_init = 2600
delta_time = 0.00001 #"Paso" en segundos que va a dar el programa entre una iteración y otra

while (altitude_init-distance > 2150):
    density = -0.00009824*(altitude_init-distance) + 1.2027 #Ecuación que calcula la densidad con respecto a la altura
    friction_force = (vel * vel) * LAMBDA * density #Calcula la fuerza de fricción
    vel += ((WEIGHT - friction_force) / MASS) * delta_time #Calcula la velocidad
    distance += vel * delta_time #Calcula la distancia que ha recorrido desde donde se suelta el satélite
    time += delta_time  
    valores_eje_y.append(vel)
    iteraciones_lista.append(time)

print()
print(f'Tiempo que tarda para tocar el suelo: {time} segundos')
print()
print(f'Distancia recorrida: {distance} metros')
print()
print(f'Velocidad antes de tocar el suelo: {vel} m/s')
print()

plt.plot(iteraciones_lista, valores_eje_y, marker='o')
plt.title('Grafico de la velocidad respecto al tiempo')
plt.xlabel('Tiempo (s)')
plt.ylabel('Velocidad (m/s)')
plt.grid(True)
plt.show()