import numpy as np

print('Solving with normal equations...\n');

f = open('data.txt', 'r')
l = [line[:-1].split(', ') for line in f]
 
m = len(l)
X = [[int(l[i][j]) for i in range(m)] for j in range(2)]
y = [int(l[i][-1]) for i in range(m)]

#Add intercept term to X
aux = [int(1) for i in range(len(l))]
X.insert(0, aux)

#Calculate the parameters from the normal equation
X = np.asarray(X)
X = X.transpose()
Xt = X.transpose()

#matlab: theta = pinv(X'*X)*X'*y;
theta = np.dot(np.dot(np.linalg.inv(np.dot(Xt, X)), Xt), y)

print()
grade1 = theta[0]+theta[1]*10+theta[2]*3
print('Estimated number of hours of a student looking fopr grade 10 with difficulty 3 using gradient descent:', grade1)
grade2 = theta[0]+theta[1]*10+theta[2]*1
print('Estimated number of hours of a student looking fopr grade 10 with difficulty 1 using gradient descent:', grade2)