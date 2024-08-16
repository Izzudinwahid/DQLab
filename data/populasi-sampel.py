import random
import numpy as np

# #3 SIMPLE RANDOM
# #agar nilai random tidak berubah
# random.seed(1234)
# # sampel = []
# # for i in range(12):
# #     sampel.append(random.randint(1,120))

# # print(sampel)
# sampel = [random.randint(1,120)for i in range(12)]
# print(sampel)


# #4 SIMPLE RANDOM USED NUMPY
# np.random.seed(0)
# sampel = np.random.randint(1,121,size = 12)
# print(sampel)