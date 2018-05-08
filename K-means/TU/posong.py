# -*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt



x = np.random.poisson(lam=15, size=100000)  # lam为λ size为k
pillar = 30
a = plt.hist(x, bins=pillar, normed=True, range=[0, pillar], color='g', alpha=0.5)
plt.plot(a[1][0:pillar], a[0], 'r')
plt.xlabel('k');
plt.ylabel('P(k)');
# plt.show()
plt.grid()
plt.show()