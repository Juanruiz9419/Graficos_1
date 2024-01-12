import matplotlib.pyplot as plt
import numpy as np

rng = np.random.default_rng(42)

materias = ['Matematicas', 'Ciencias', 'Literatura']
matematicas = rng.uniform(2, 5, 2)
#errores_matematicas = [min(errores_matematicas), max(errores_matematicas)]

ciencias = rng.uniform(1, 4, 2)
#errores_ciencias = [min(errores_ciencias), max(errores_ciencias)]

literatura = rng.uniform(3, 6, 2)
#errores_literatura = [min(errores_literatura), max(errores_literatura)]

rng = np.random.default_rng(42)

plt.errorbar(materias, matematicas, ciencias, literatura, fmt='o', capsize=5)
plt.title('Gráfico de barras de error')
plt.ylabel('calificaciones promedio y errores')
plt.xlabel('Materias')
plt.show()