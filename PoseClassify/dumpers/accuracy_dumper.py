import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

statistics_accuracy_10=np.load('../statistics_accuracy_10.txt')
plt.ylim((0,100))
plt.plot(xrange(0,len(statistics_accuracy_10)),statistics_accuracy_10, 'r--')
plt.ylabel('accuracy (%)')
plt.xlabel('iteration times')
# plt.title('average accuracy={0}'.format(np.average(statistics_accuracy_10)))

statistics_accuracy_18=np.load('../statistics_accuracy_18.txt')
plt.ylim((0,100))
plt.plot(xrange(0,len(statistics_accuracy_18)),statistics_accuracy_18, 'b--')
plt.ylabel('accuracy (%)')
plt.xlabel('iteration times')
plt.title('Avg red ={0:.2f}%,  Avg blue={1:.2f}%'.format(np.average(statistics_accuracy_10),np.average(statistics_accuracy_18)))
red_patch = mpatches.Patch(color='red', label='10 features')
# plt.legend(handles=[red_patch])

blue_patch = mpatches.Patch(color='blue', label='18 features')
plt.legend(handles=[red_patch,blue_patch])



plt.draw()
plt.show()