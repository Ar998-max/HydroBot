import matplotlib.pyplot as plt

path = 'plot.jpg'
hours =[1,2,3,4,5]
water_intake= [2,5,7,8,9]
plt.plot(hours, water_intake)
plt.title('Your water intake')
plt.xlabel('hours')
plt.ylabel('litres of water consumed')
plt.savefig(path)