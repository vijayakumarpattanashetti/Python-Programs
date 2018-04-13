import matplotlib.pyplot as plt
 
# x axis values
x = [1,2,3,4,5,6]
# corresponding y axis values
y = [2,4,1,5,2,6]
 
# plotting the points 
plt.plot(x, y, color='green', linestyle='dashed', linewidth = 4,
         marker='o', markerfacecolor='black', markersize=15)
 
# setting x and y axis range
plt.ylim(1,10)
plt.xlim(1,10)
 
# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')
 
# giving a title to my graph
plt.title('Some cool customizations!')
 
# function to show the plot
plt.show()
