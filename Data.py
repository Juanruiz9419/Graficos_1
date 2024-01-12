import matplotlib.pyplot as plt
import numpy as np

rng = np.random.default_rng(42)


matematicas = rng.integers(50, 100, 20)
ciencias = rng.integers(40, 95, 20)
literatura = rng.integers(60, 100, 20)

plt.scatter(matematicas, ciencias, color='red')


plt.title('Relacion entre las calificaciones de Matematicas y ciencias')
plt.xlabel('Calificaciones de matematicas')
plt.ylabel('Calificaciones de ciencias')


plt.show()


materias = ['Matematicas', 'Ciencias', 'Literatura']
promedio = [76 , 68.5 , 80]
errores_altura = [2, 3, 4]

plt.errorbar(materias,promedio, yerr=errores_altura, fmt='o', capsize=5)
plt.title('Gráfico de barras de error')
plt.ylabel('calificaciones promedio y errores')
plt.xlabel('Materias')
plt.show()

# Datos de errores para el gráfico de barras de error
errores_matematicas = rng.uniform(2, 5, 2)
errores_matematicas = [min(errores_matematicas), max(errores_matematicas)]

errores_ciencias = rng.uniform(1, 4, 2)
errores_ciencias = [min(errores_ciencias), max(errores_ciencias)]

errores_literatura = rng.uniform(3, 6, 2)
errores_literatura = [min(errores_literatura), max(errores_literatura)]

rng = np.random.default_rng(42)




matematicas = rng.integers(50, 100, 20)


plt.hist(matematicas, bins=10, color='red', edgecolor='black')


plt.xlabel('Calificacion de Matematicas')
plt.ylabel('Frecuencia')
plt.title('Distribución de Calificaciones de Matemáticas')


plt.show()