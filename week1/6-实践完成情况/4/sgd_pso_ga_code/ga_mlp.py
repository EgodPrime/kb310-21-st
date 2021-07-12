import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer 
import pyswarms as ps
from sko.GA import GA
import time
# 前向传播 params为ga的dimensions
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

def func(x):
    # num_particles = x.shape[0] #x=(num_particles,dimensions)
    # local_value = [forward(X, Y, x[i]) for i in range(num_particles)]
    # local_value = np.array(local_value)
    local_value=forward(X_train,Y_train,x)
    return local_value #返回一个1个loss

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

data = load_breast_cancer()
X = data.data
Y = data.target
num_samples = X.shape[0]
#训练测试参数划分
train_samples = 400
test_samples = 169
X_train = X[0:train_samples,:]
Y_train = Y[0:train_samples]
X_test = X[train_samples:num_samples,:]
Y_test = Y[train_samples:num_samples]
#网络节点分布
inputs = 30
hidden = 20
outputs = 2

#进行GA
dimensions = inputs*hidden+hidden+hidden*outputs+outputs
#dimensions为func的x的长度，size_pop为种群数目,prob_mut为变异概率，max_iter为迭代次数,lb ub为自变量最小值和最大值 precision为求值精度
#GA是求最小值的方法,也就是对func返回的loss进行优化
start = time.time()
ga = GA(func=func, n_dim=dimensions, size_pop=100, max_iter=1000, prob_mut=0.0005, lb=-5, ub=5, precision=0.001)
best_x, best_loss,history_loss = ga.run()
end = time.time()
acc = test_acc(X_test,Y_test,best_x)
print("best_x:",best_x,'\n',"best_loss:",best_loss,'\n',"acc:",acc,'\n',"time:",(end-start))

#画历史loss曲线图
plt.plot(history_loss,'r')
plt.ylabel("loss")
plt.xlabel("iters")
plt.show()

#保存loss数据
hs = np.array(history_loss)
np.savetxt("ga_loss.txt",hs)