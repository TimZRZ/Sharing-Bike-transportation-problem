import csv
import numpy as np
import matplotlib.pyplot as plt

csv_file = open("change_of_num_29result.csv", "r")
reader = csv.reader(csv_file)
latitude_list = []
longtitude_list = []
change_value = []

for row in reader:
    if row[3] == "latitude":
        latitude_list.append(0)
        longtitude_list.append(0)
        change_value.append(' ')
    elif row[3] != "latitude":
        latitude = (float(row[3])-37.750506)/(37.80477-37.750506)
        longtitude = (float(row[4])+122.4442926)/(-122.3904285+122.4442926)
        latitude_list.append(latitude)
        longtitude_list.append(longtitude)
        change_value.append(str(row[2]))

def drawArrow1(A, B):
    ax = plt.subplot(122)
    ax.annotate("", xy=(B[0], B[1]), xytext=(A[0], A[1]),arrowprops=dict(arrowstyle="->"))
    ax.grid()
    ax.set_aspect('equal') #x轴y轴等比例
drawArrow1(np.array([longtitude_list[11],latitude_list[11]]),np.array([longtitude_list[13],latitude_list[13]]))
drawArrow1(np.array([longtitude_list[13],latitude_list[13]]),np.array([longtitude_list[19],latitude_list[19]]))
drawArrow1(np.array([longtitude_list[19],latitude_list[19]]),np.array([longtitude_list[22],latitude_list[22]]))
drawArrow1(np.array([longtitude_list[22],latitude_list[22]]),np.array([longtitude_list[24],latitude_list[24]]))
drawArrow1(np.array([longtitude_list[24],latitude_list[24]]),np.array([longtitude_list[29],latitude_list[29]]))
drawArrow1(np.array([longtitude_list[29],latitude_list[29]]),np.array([longtitude_list[11],latitude_list[11]]))
plt.scatter(longtitude_list[1:], latitude_list[1:], s=10,color="r")
for i in range (1,len(longtitude_list)):
    ax = plt.subplot(122)
    ax.grid()
    ax.scatter(longtitude_list[i],latitude_list[i], c='r', s=10)
    #ax.annotate("%s" %change_value[i],xy=(longtitude_list[i],latitude_list[i]),xycoords='data',xytext=(3, 3),textcoords = 'offset points',fontsize=9,color = 'blue')
plt.show()
