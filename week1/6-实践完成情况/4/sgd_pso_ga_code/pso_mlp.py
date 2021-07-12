# 用pso分类breast cancer数据集
# data : {ndarray, dataframe} of shape (569, 30)
# target: {ndarray, Series} of shape (569,)

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer 
import pyswarms as ps
from pyswarms.utils.plotters import plot_cost_history, plot_contour, plot_surface
import matplotlib.pyplot as plt

# 前向传播 params为pso的dimensions
def forward(X, Y, params):
    #参数切分
    w1 = params[0:inputs*hidden].reshape((inputs, hidden))
    b1 = params[inputs*hidden:inputs*hidden+hidden].reshape((hidden,))
    w2 = params[inputs*hidden+hidden:inputs*hidden+hidden+hidden*outputs].reshape((hidden,outputs))
    b2 = params[inputs*hidden+hidden+hidden*outputs:inputs*hidden+hidden+hidden*outputs+outputs].reshape((outputs,))
    #运算
    z1 = np.dot(X, w1) + b1
    a1 = np.tanh(z1)
    z2 = np.dot(a1, w2) + b2
    #softmax
    expf = np.exp(z2)
    probs = expf / np.sum(expf, axis=1, keepdims=True)
    #计算loss
    logprobs = -np.log(probs[range(train_samples), Y])
    loss = np.sum(logprobs) / train_samples
    return loss
#定义pso的参数f
def func(x):
    num_particles = x.shape[0]
    local_value = [forward(X_train, Y_train, x[i]) for i in range(num_particles)]
    local_value = np.array(local_value)
    return local_value
#预测函数
def test_acc(X, Y, params):
    #参数切分
    w1 = params[0:inputs*hidden].reshape((inputs, hidden))
    b1 = params[inputs*hidden:inputs*hidden+hidden].reshape((hidden,))
    w2 = params[inputs*hidden+hidden:inputs*hidden+hidden+hidden*outputs].reshape((hidden,outputs))
    b2 = params[inputs*hidden+hidden+hidden*outputs:inputs*hidden+hidden+hidden*outputs+outputs].reshape((outputs,))
    #运算
    z1 = np.dot(X, w1) + b1
    a1 = np.tanh(z1)
    z2 = np.dot(a1, w2) + b2
    y = np.argmax(z2, axis=1)
    acc = (y==Y).mean()
    return acc



# load dataset
data = load_breast_cancer()
X = data.data
Y = data.target
num_samples = X.shape[0]
train_samples = 500
test_samples = 69
X_train = X[0:train_samples,:]
Y_train = Y[0:train_samples]
X_test = X[train_samples:num_samples,:]
Y_test = Y[train_samples:num_samples]

#网络节点分布
inputs = 30
hidden = 20
outputs = 2
#参数设置
options = {'c1': 0.5, 'c2': 0.3, 'w':0.9}
dimensions = inputs*hidden+hidden+hidden*outputs+outputs

#pso
optimizer = ps.single.GlobalBestPSO(n_particles=100, dimensions=dimensions, options=options)
loss, weight = optimizer.optimize(func, iters=1000)

      
print("test acc:", test_acc(X_test, Y_test, weight))

# Plot the loss
loss_history = optimizer.cost_history
plot_cost_history(optimizer.cost_history)
plt.savefig("loss_pso.png")
plt.show()

pso_loss_np = np.array(loss_history)
np.savetxt("pso_loss.txt", pso_loss_np)





















