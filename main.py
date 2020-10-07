# Lucas Weakland
# Homework 8
# Machine Learning
# Theres a comment at the end of this script that explains the automatic part to this. please read. saving time here lol
import matplotlib.pyplot as plt
from tsmoothie.smoother import *

mu, sigma = 0, 500
x = np.arange(1, 100, 0.1)  # x axis
z = np.random.normal(mu, sigma, len(x))  # noise
y = x ** 2 + z # data

# operate smoothing
smoother = ConvolutionSmoother(window_len=30, window_type='ones')
smoother.smooth(y)

# generate intervals
low, up = smoother.get_intervals('sigma_interval', n_sigma=3)

# plot the smoothed timeseries with intervals
plt.figure(figsize=(11,6))
plt.plot(smoother.data[0], color='orange')
plt.plot(smoother.smooth_data[0], linewidth=3, color='blue')
plt.fill_between(range(len(smoother.data[0])), low[0], up[0], alpha=0.3)


yesNo = input('Hello, would you like to scan for noisy data? Type yes or no.')
if yesNo.lower() == 'yes':
  print("Great! Hereeeee we gooo! " + plt.show())
else:
  print ("Oh...Sorry for asking...")
#plt.show() you could just un comment this , and then get rid of the if else and user input and that way it will be automatic instead of manual.