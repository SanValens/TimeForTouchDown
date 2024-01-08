import matplotlib.pyplot as plt

LAMBDA = 0.81 * 0.007853982 / 2
MASS = 0.6
WEIGHT = MASS * 9.8
valores_variable = []
iteraciones_lista = []
vel = 0
time = 0
net_force = 0
friction_force = 0
distance = 0
altitude_init = 2600
delta_time = 0.0001
density = -(0.00009824 * altitude_init) + 1.2027
counter = 1

while (altitude_init-distance > 2150):
    density = -0.00009824*(altitude_init-distance) + 1.2027
    friction_force = (vel * vel) * LAMBDA * density
    vel += ((WEIGHT - friction_force) / MASS) * delta_time
    distance += vel * delta_time
    time += delta_time  
    valores_variable.append(vel)
    iteraciones_lista.append(counter)
    counter+=1

print()
print(f'Tiempo para tocar el suelo: {time} segundos')
print()
print(f'Distancia recorrida: {distance} metros')
print()
print(f'Velocidad antes de tocar el suelo: {vel} m/s')
print()

plt.plot(iteraciones_lista, valores_variable, marker='o')
plt.title('Grafico de la velocidad respecto al tiempo')
plt.xlabel('Tiempo (s)')
plt.ylabel('Velocidad (m/s)')
plt.grid(True)
plt.show()