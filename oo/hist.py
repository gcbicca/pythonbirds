import matplotlib.pyplot as plt
import numpy as np

# Gerando uma amostra de dados
mu, sigma = 0, 0.1 # mean and standard deviation
s = np.random.normal(mu, sigma, 1000)

# Criando o histograma
n, bins, patches = plt.hist(s, bins=50, density=True, histtype='bar', color='g', alpha=.7)

# calculando a função de probabilidade da distribuição normal
y = ((1 / (np.sqrt(2 * np.pi) * sigma)) * np.exp(-0.5 * (1 / sigma * (bins - mu))**2))

# Desenhando a linha da distribuição normal
plt.plot(bins, y, '-', color='r')

plt.xlabel('X-axis')
plt.ylabel('Frequency')
plt.title('Normal Distribution')
plt.show()
