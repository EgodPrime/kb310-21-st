import numpy as np
import matplotlib.pyplot as plt
#读取数据文件
file_sgd = 'sgd_loss.txt'
file_pso = 'pso_loss.txt'
file_ga = 'ga_loss.txt'
#txt变list
sgd_loss = np.loadtxt(file_sgd)
pso_loss = np.loadtxt(file_pso)
ga_loss = np.loadtxt(file_ga)
#plot
plt.plot(range(len(sgd_loss)), sgd_loss, label='sgd')
plt.plot(range(len(sgd_loss)), pso_loss, label='pso')
plt.plot(range(len(ga_loss)), ga_loss, label='ga')
plt.xlabel('epochs')
plt.ylabel('training loss')
plt.legend()
plt.savefig('three_training_loss.png')

plt.show()



