import csv
import math
import numpy as np

##kalmanfilter##
filename='alice_los.csv' ##change to bob_los.csv
RSSI=[]
hasil=[]
with open(filename) as f:
	dataalice = csv.reader(f)
	for row in dataalice:
		RSSI.append(row)
RSSI=np.array(RSSI)
RSSI=[float(i) for i in RSSI]
RSSI=np.array(RSSI)
#####endreshape
# print(rssival_alice)
a=2.13	#a posteri error estimate
h=2.13
R=4.6		#measurement error covariance matrix (noise)
Q=0.0001	#process noise covariance
#=====first estimation=======#
xaposteriori_0=0
paposteriori_0=1
#=========================#
xapriori=[]    # a priori estimate of x
residual=[]
papriori=[]   # a priori error estimate
k=[]           # gain or blending factor
paposteriori=[]
xaposteriori=[]# a posteri estimate of rss_alice
# print(rss_alice)


for m in range(1):
	xapriori.append(a*xaposteriori_0)
	residual.append(RSSI[m]-h*xapriori[m])
	papriori.append(a*a*paposteriori_0+Q)
	k.append(papriori[m]/(papriori[m]+R))
	paposteriori.append(papriori[m]*(1-k[m]))
	xaposteriori.append(xapriori[m]+k[m]*residual[m])
	for n in range (1,len(RSSI)):
		xapriori.append(xaposteriori[n-1])
		residual.append(RSSI[n]-h*xapriori[n])
		papriori.append(a*a*paposteriori[n-1]+Q)
		k.append(papriori[n]/(papriori[n]+R))
		paposteriori.append(papriori[n]*(1-k[n]))
		xaposteriori.append(xapriori[n]+k[n]*residual[n])

np.savetxt("kalmanresult_"+filename,xaposteriori,delimiter=",",fmt='%10.5f')
