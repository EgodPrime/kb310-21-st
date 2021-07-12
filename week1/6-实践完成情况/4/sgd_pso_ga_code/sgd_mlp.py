import torch
import numpy as np
import sys
sys.path.append("..")
from sklearn.datasets import load_breast_cancer 
import random
import matplotlib.pyplot as plt

def data_iter(batch_size, features, labels):
    num_examples = len(features)
    indices = list(range(num_examples))
    random.shuffle(indices)  # 样本的读取顺序是随机的
    for i in range(0, num_examples, batch_size):
        j = torch.LongTensor(indices[i: min(i + batch_size, num_examples)]) # 最后一次可能不足一个batch
        yield  features.index_select(0, j), labels.index_select(0, j)

def softmax(X):
    X_exp = X.exp()
    partition = X_exp.sum(dim=1, keepdim=True)
    return X_exp / partition  # 这里应用了广播机制

def net(X):
    z1 = torch.mm(X, W1) + b1
    a1 = torch.tanh(z1)
    z2 = torch.mm(a1, W2) + b2
    expf = torch.exp(z2)
    probs = expf / torch.sum(expf, axis=1, keepdims=True)
    return probs

def cross_entropy(y_hat, y):
    
    y = y.long()
    a =  - torch.log(y_hat.gather(1, y.view(-1, 1)))
    return a


def accuracy(y_hat, y):
    return (y_hat.argmax(dim=1) == y).float().mean().item()

# 求acc
def evaluate_accuracy(data_iter, net):
    acc_sum, n = 0.0, 0
    for X, y in data_iter:
        acc_sum += (net(X).argmax(dim=1) == y).float().sum().item()
        n += y.shape[0]
    return acc_sum / n

def sgd(params, lr, batch_size):
    # 这里除以了batch_size，但是应该是不用除的，因为一般用PyTorch计算loss时就默认已经
    # 沿batch维求了平均了。
    for param in params:
        param.data -= lr * param.grad / batch_size # 注意这里更改param时用的param.data





data = load_breast_cancer()
X = torch.from_numpy(data.data)
Y = torch.from_numpy(data.target)

num_samples = X.shape[0]
train_samples = 500
test_samples = 69
X_train = X[0:train_samples,:]
Y_train = Y[0:train_samples]
X_test = X[train_samples:num_samples,:]
Y_test = Y[train_samples:num_samples]

batch_size = 32
num_inputs, num_hiddens, num_outputs= 30, 20, 2





W1 = torch.tensor(np.random.normal(0, 0.01, (num_inputs, num_hiddens)), dtype=torch.double)
b1 = torch.zeros(num_hiddens, dtype=torch.double)
W2 = torch.tensor(np.random.normal(0, 0.01, (num_hiddens, num_outputs)), dtype=torch.double)
b2 = torch.zeros(num_outputs, dtype=torch.double)

params = [W1, b1, W2, b2]
for param in params:
    param.requires_grad_(requires_grad=True)


num_epochs, lr = 1000, 0.0003
loss = cross_entropy
optimizer = None

train_loss = []
train_acc = []
test_acc_list = []


for epoch in range(num_epochs):
    train_l_sum, train_acc_sum, n = 0.0, 0.0, 0
    for X, y in data_iter(batch_size, X_train, Y_train):
        y_hat = net(X)
        l = loss(y_hat, y).sum()

        # 梯度清零
        if optimizer is not None:
            optimizer.zero_grad()
        elif params is not None and params[0].grad is not None:
            for param in params:
                param.grad.data.zero_()

        l.backward()
        if optimizer is None:
            sgd(params, lr, batch_size)
        else:
            optimizer.step()  

        train_l_sum += l.item()
        train_acc_sum += (y_hat.argmax(dim=1) == y).sum().item()
        n += y.shape[0]
    test_iter = data_iter(batch_size, X_test, Y_test)
    test_acc = evaluate_accuracy(test_iter, net)
    # print('epoch %d, loss %.4f, train acc %.3f, test acc %.3f'
    #       % (epoch + 1, train_l_sum / n, train_acc_sum / n, test_acc))
    # print('epoch %d, loss %.4f, train acc %.3f'
    #         % (epoch + 1, train_l_sum / n, train_acc_sum / n))
    a = train_l_sum / n
    train_loss.append(a)
    b = train_acc_sum / n
    train_acc.append(b)
    test_acc_list.append(test_acc)
plt.plot(range(num_epochs), train_loss)
plt.show()

sgd_loss_np = np.array(train_loss)
np.savetxt("sgd_loss.txt", sgd_loss_np)





    
    

    
    




   




