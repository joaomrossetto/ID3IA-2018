from __future__ import division
import matplotlib.pyplot as plt

erros10 = [0.177719, 0.160146, 0.169098, 0.165782, 0.155836, 0.170756, 0.178050, 0.180371, 0.170093, 0.159814 ]
erros9 = [0.167413, 0.163533, 0.165622, 0.175768, 0.176664, 0.150701, 0.164429, 0.163533, 0.174276 ]
erros8 = [0.183024, 0.165252, 0.162865, 0.169496, 0.177454, 0.164191, 0.172414, 0.164721 ]
erros7 = [0.160631, 0.169684, 0.163649, 0.165506, 0.171309, 0.166667, 0.163417 ]
erros6 = [0.168291, 0.168092, 0.177442, 0.162522, 0.166302, 0.169286]
erros5 = [0.161638, 0.168932, 0.168435, 0.181698, 0.172745]

data = [erros5, erros6, erros7, erros8, erros9,erros10]

fig, ax1 = plt.subplots(figsize=(10, 6))
fig.canvas.set_window_title('K-Fold')

plt.boxplot(data)
plt.xticks([1, 2, 3, 4, 5, 6], [5, 6, 7, 8, 9, 10])
ax1.set_title('Erros do modelo por K em K-Fold')
ax1.set_xlabel('Valor de K')
ax1.set_ylabel('Erro')
plt.show()