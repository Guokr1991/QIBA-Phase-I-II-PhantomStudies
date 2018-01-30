"""
This code is directed to the csv for the MGH data.  It then looks through all the data
and isolates the cases with "good" displacement and velocity ransacs.  From there it 
plots a scatter plot of the Vdisp v Vvel and does a paired t-test.
author: Cody Morris
"""
import scipy.io as sio
from scipy.stats import iqr
import csv
import numpy
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt

speeddoc = 'LiverLatsumsUpsampled2.csv'
data = numpy.genfromtxt(speeddoc, delimiter = ',', dtype = str)
print('Shape of data is {}x{}'.format(data.shape[0], data.shape[1]))

goodDisps = []
goodVels = []
goodDispsF0 = []
goodVelsF0 = []
goodDispsF1 = []
goodVelsF1 = []
goodDispsF2 = []
goodVelsF2 = []
goodDispsF3 = []
goodVelsF3 = []
goodDispsF4 = []
goodVelsF4 = []
goodPatients = []
totalPatients = []


dispPerPatient = []
velPerPatient = []
fibPerPatient = []
for i in range(1,data.shape[0]):
    if data[i][0] not in totalPatients:
        totalPatients.append(data[i][0])
    if float(data[i][3]) < 5.8 and float(data[i][4]) < 5.8 and data[i][5] != 'NaN':
        if (float(data[i][4])-float(data[i][3])) >=0: 
            if data[i][0] not in goodPatients:
                goodPatients.append(data[i][0])
                dispPerPatient.append([])
                velPerPatient.append([])
                fibPerPatient.append(data[i][5])
            patInd = goodPatients.index(data[i][0])
            dispPerPatient[patInd].append(float(data[i][3]))
            velPerPatient[patInd].append(float(data[i][4]))
            goodDisps.append(float(data[i][2]))
            goodVels.append(float(data[i][2]))


meanPatientDisp = []
meanPatientVel = []
stdPatientDisp = []
stdPatientVel = []
nanCount = 0
for i in range(0, len(goodPatients)):
    meanPatientDisp.append(numpy.mean(dispPerPatient[i]))
    meanPatientVel.append(numpy.mean(velPerPatient[i]))
    stdPatientDisp.append(numpy.std(dispPerPatient[i]))
    stdPatientVel.append(numpy.std(velPerPatient[i]))
    if fibPerPatient[i] == '1':
        goodDispsF1.append(numpy.mean(dispPerPatient[i]))
        goodVelsF1.append(numpy.mean(velPerPatient[i]))
    if fibPerPatient[i] == '2':
        goodDispsF2.append(numpy.mean(dispPerPatient[i]))
        goodVelsF2.append(numpy.mean(velPerPatient[i]))
    if fibPerPatient[i] == '3':
        goodDispsF3.append(numpy.mean(dispPerPatient[i]))
        goodVelsF3.append(numpy.mean(velPerPatient[i]))
    if fibPerPatient[i] == '4':
        goodDispsF4.append(numpy.mean(dispPerPatient[i]))
        goodVelsF4.append(numpy.mean(velPerPatient[i]))
    if fibPerPatient[i] == '0':
        goodDispsF0.append(numpy.mean(dispPerPatient[i]))
        goodVelsF0.append(numpy.mean(velPerPatient[i]))
    if fibPerPatient[i] == 'NaN':
        nanCount += 1
print('Number of good acquisitions: {}'.format(len(goodDisps)))
print('Number of total acquisitions: {}'.format(data.shape[0]-1))
print('Number of good patients: {}'.format(len(goodPatients)))
print('Number of total patients: {}'.format(len(totalPatients)))
print('Fibrosis Stage 1: {}'.format(len(goodDispsF1)))
print('Fibrosis Stage 2: {}'.format(len(goodDispsF2)))
print('Fibrosis Stage 3: {}'.format(len(goodDispsF3)))
print('Fibrosis Stage 4: {}'.format(len(goodDispsF4)))
print('Fibrosis Stage 0: {}'.format(len(goodDispsF0)))
print('NaN Count: {}'.format(nanCount))

with open('dispPerPatient.csv', 'wt') as csvfile:
    SWSWriter = csv.writer(csvfile, dialect = 'excel')
    for i in range(0, len(goodPatients)):
        SWSWriter.writerow(dispPerPatient[i])

with open('velPerPatient.csv', 'wt') as csvfile:
    SWSWriter = csv.writer(csvfile, dialect = 'excel')
    for i in range(0, len(goodPatients)):
        SWSWriter.writerow(velPerPatient[i])

#Get the iqrs back from matlab:
#matcontents = sio.loadmat('iqrsPerPatient.mat', struct_as_record=False, squeeze_me=True)
#iqrPatientDisp = matcontents['dispiqr']
#iqrPatientVel = matcontents['veliqr']

#Lists to hold iqr/mean
iqrmeanDisp = []
iqrmeanVel = []
#for i in range(0, len(iqrPatientDisp)):
#    if iqrPatientDisp[i] == 0:
#        iqrmeanDisp.append(1)
#    else:
#        iqrmeanDisp.append(iqrPatientDisp[i]/numpy.mean(dispPerPatient[i]))
#    if iqrPatientVel[i] == 0:
#        iqrmeanVel.append(1)
#    else:
#        iqrmeanVel.append(iqrPatientVel[i]/numpy.mean(velPerPatient[i]))
for i in range(0, len(goodPatients)):
    for j in range(0, len(dispPerPatient[i])):
        if dispPerPatient[i][j] == 0:
            dispPerPatient[i][j] = numpy.nan;
    iqrmeanDisp.append(iqr(dispPerPatient[i])/numpy.mean(dispPerPatient[i]));
    for j in range(0, len(velPerPatient[i])):
        if velPerPatient[i][j] == 0:
            velPerPatient[i][j] = numpy.nan;
    iqrmeanVel.append(iqr(velPerPatient[i])/numpy.mean(velPerPatient[i]));


patientsw3ormore = []
patientswgoodiqrdisp = []
patientswgoodiqrvel = []
patientswbothiqrs = []
patientswiqrsand3ormore = []
plotablepatients = []
for i in range(0, len(goodPatients)):
    if len(dispPerPatient[i]) >= 3:
        patientsw3ormore.append(goodPatients[i])
    if iqrmeanDisp[i] <= .3:
        patientswgoodiqrdisp.append(goodPatients[i])
    if iqrmeanVel[i] <= .3:
        patientswgoodiqrvel.append(goodPatients[i])
    if iqrmeanDisp[i] <= .3 and iqrmeanVel[i] <= .3:
        patientswbothiqrs.append(goodPatients[i])
    if len(dispPerPatient[i]) >= 3 and iqrmeanDisp[i] <= .3 and iqrmeanVel[i] <= .3:
        patientswiqrsand3ormore.append(goodPatients[i])
        plotablepatients.append(i)
print('Patients with 3 or more good acquisitions: {}'.format(len(patientsw3ormore)))
print('List of indices: {}'.format(patientsw3ormore))
print('Patients with good displacement iqr/mean: {}'.format(len(patientswgoodiqrvel)))
print('List of indices: {}'.format(patientswgoodiqrdisp))
print('Patients with good velocity iqr/mean: {}'.format(len(patientswgoodiqrvel)))
print('List of indices: {}'.format(patientswgoodiqrvel))
print('Patients with good iqr/means for both: {}'.format(len(patientswbothiqrs)))
print('List of indices: {}'.format(patientswbothiqrs))
print('Patients with 3 or more and good iqrs for both: {}'.format(len(patientswiqrsand3ormore)))
print('List of indices: {}'.format(patientswiqrsand3ormore))
print(plotablepatients)
print(len(plotablepatients))
goodDispsF0 = []
goodVelsF0 = []
stdDispsF0 = []
stdVelsF0 = []
goodDispsF1 = []
goodVelsF1 = []
stdDispsF1 = []
stdVelsF1 = []
goodDispsF2 = []
goodVelsF2 = []
stdDispsF2 = []
stdVelsF2 = []
goodDispsF3 = []
goodVelsF3 = []
stdDispsF3 = []
stdVelsF3 = []
goodDispsF4 = []
goodVelsF4 = []
stdDispsF4 = []
stdVelsF4 = []
meanVF0 = []
diffVF0 = []
meanVF1 = []
diffVF1 = []
meanVF2 = []
diffVF2 = []
meanVF3 = []
diffVF3 = []
meanVF4 = []
diffVF4 = []
nanCount = 0
#go through 
for ind in plotablepatients:
    if fibPerPatient[ind] == '1':
        goodDispsF1.append(numpy.mean(dispPerPatient[ind]))
        goodVelsF1.append(numpy.mean(velPerPatient[ind]))
        stdDispsF1.append(numpy.std(dispPerPatient[ind]))
        stdVelsF1.append(numpy.std(velPerPatient[ind]))
        diffVF1.append(numpy.subtract(velPerPatient[ind], dispPerPatient[ind]))
        meanVF1.append(numpy.divide(numpy.add(velPerPatient[ind], dispPerPatient[ind]), 2))
        #diffVF1.append(numpy.mean(velPerPatient[ind])-numpy.mean(dispPerPatient[ind]))
        #stddiffVF1.append(numpy.std(numpy.subtract(velPerPatient[ind], dispPerPatient[ind])))
        #meanVF1.append((numpy.mean(velPerPatient[ind])+numpy.mean(dispPerPatient[ind]))/2)
        #stdmeanVF1.append(numpy.std(numpy.divide(numpy.add(velPerPatient[ind], dispPerPatient[ind]),2)))
    if fibPerPatient[ind] == '2':
        goodDispsF2.append(numpy.mean(dispPerPatient[ind]))
        goodVelsF2.append(numpy.mean(velPerPatient[ind]))
        stdDispsF2.append(numpy.std(dispPerPatient[ind]))
        stdVelsF2.append(numpy.std(velPerPatient[ind]))
        diffVF2.append(numpy.subtract(velPerPatient[ind], dispPerPatient[ind]))
        meanVF2.append(numpy.divide(numpy.add(velPerPatient[ind], dispPerPatient[ind]),2))
        #diffVF2.append(numpy.mean(velPerPatient[ind])-numpy.mean(dispPerPatient[ind]))
        #stddiffVF2.append(numpy.std(numpy.subtract(velPerPatient[ind], dispPerPatient[ind])))
        #meanVF2.append((numpy.mean(velPerPatient[ind])+numpy.mean(dispPerPatient[ind]))/2)
        #stdmeanVF2.append(numpy.std(numpy.divide(numpy.add(velPerPatient[ind], dispPerPatient[ind]),2)))
    if fibPerPatient[ind] == '3':
        goodDispsF3.append(numpy.mean(dispPerPatient[ind]))
        goodVelsF3.append(numpy.mean(velPerPatient[ind]))
        stdDispsF3.append(numpy.std(dispPerPatient[ind]))
        stdVelsF3.append(numpy.std(velPerPatient[ind]))
        diffVF3.append(numpy.subtract(velPerPatient[ind], dispPerPatient[ind]))
        meanVF3.append(numpy.divide(numpy.add(velPerPatient[ind], dispPerPatient[ind]),2))
        #diffVF3.append(numpy.mean(velPerPatient[ind])-numpy.mean(dispPerPatient[ind]))
        #stddiffVF3.append(numpy.std(numpy.subtract(velPerPatient[ind], dispPerPatient[ind])))
        #meanVF3.append((numpy.mean(velPerPatient[ind])+numpy.mean(dispPerPatient[ind]))/2)
        #stdmeanVF3.append(numpy.std(numpy.divide(numpy.add(velPerPatient[ind], dispPerPatient[ind]),2)))
    if fibPerPatient[ind] == '4':
        goodDispsF4.append(numpy.mean(dispPerPatient[ind]))
        goodVelsF4.append(numpy.mean(velPerPatient[ind]))
        stdDispsF4.append(numpy.std(dispPerPatient[ind]))
        stdVelsF4.append(numpy.std(velPerPatient[ind]))
        diffVF4.append(numpy.subtract(velPerPatient[ind], dispPerPatient[ind]))
        meanVF4.append(numpy.divide(numpy.add(velPerPatient[ind], dispPerPatient[ind]),2))
        #diffVF4.append(numpy.mean(velPerPatient[ind])-numpy.mean(dispPerPatient[ind]))
        #stddiffVF4.append(numpy.std(numpy.subtract(velPerPatient[ind], dispPerPatient[ind])))
        #meanVF4.append((numpy.mean(velPerPatient[ind])+numpy.mean(dispPerPatient[ind]))/2)
        #stdmeanVF4.append(numpy.std(numpy.divide(numpy.add(velPerPatient[ind], dispPerPatient[ind]),2)))
    if fibPerPatient[ind] == '0':
        goodDispsF0.append(numpy.mean(dispPerPatient[ind]))
        goodVelsF0.append(numpy.mean(velPerPatient[ind]))
        stdDispsF0.append(numpy.std(dispPerPatient[ind]))
        stdVelsF0.append(numpy.std(velPerPatient[ind]))
        diffVF0.append(numpy.subtract(velPerPatient[ind], dispPerPatient[ind]))
        meanVF0.append(numpy.divide(numpy.add(velPerPatient[ind], dispPerPatient[ind]),2))
        #diffVF0.append(numpy.mean(velPerPatient[ind])-numpy.mean(dispPerPatient[ind]))
        #stddiffVF0.append(numpy.std(numpy.subtract(velPerPatient[ind], dispPerPatient[ind])))
        #meanVF0.append((numpy.mean(velPerPatient[ind])+numpy.mean(dispPerPatient[ind]))/2)
        #stdmeanVF0.append(numpy.std(numpy.divide(numpy.add(velPerPatient[ind], dispPerPatient[ind]),2)))
    if fibPerPatient[ind] == 'NaN':
        nanCount += 1
print('Fibrosis Stage 1: {}'.format(len(goodDispsF1)))
print('Fibrosis Stage 2: {}'.format(len(goodDispsF2)))
print('Fibrosis Stage 3: {}'.format(len(goodDispsF3)))
print('Fibrosis Stage 4: {}'.format(len(goodDispsF4)))
print('Fibrosis Stage 0: {}'.format(len(goodDispsF0)))
print('NaN Count: {}'.format(nanCount))
print('DispsF0: {}'.format(goodDispsF0))
print('DispsF1: {}'.format(goodDispsF1))
print('DispsF2: {}'.format(goodDispsF2))
print('DispsF3: {}'.format(goodDispsF3))
print('DispsF4: {}'.format(goodDispsF4))
print('VelF0: {}'.format(goodVelsF0))
print('VelF1: {}'.format(goodVelsF1))
print('VelF2: {}'.format(goodVelsF2))
print('VelF3: {}'.format(goodVelsF3))
print('VelF4: {}'.format(goodVelsF4))
#Plot the scatterplot
plt.ioff()
fig = plt.figure()
fig.set_size_inches(9, 9)
ax=fig.add_subplot(111)
#ax.spines['bottom'].set_color('white')
#ax.spines['top'].set_color('white') 
#ax.spines['right'].set_color('white')
#ax.spines['left'].set_color('white')
ax.spines['bottom'].set_linewidth(4.0)
ax.spines['top'].set_linewidth(4.0)
ax.spines['right'].set_linewidth(4.0)
ax.spines['left'].set_linewidth(4.0)
ax.tick_params(axis='x', labelsize=16)
ax.tick_params(axis='y', labelsize=16)
#plt.errorbar(goodDispsF0, goodVelsF0, xerr=stdDispsF0, yerr=stdVelsF0, color = 'pink', label='Fibrosis Score 0', fmt = 'o')
#plt.errorbar(goodDispsF1, goodVelsF1, xerr=stdDispsF1, yerr=stdVelsF1, color = 'red', label='Fibrosis Score 1', fmt = 'o')
#plt.errorbar(goodDispsF2, goodVelsF2, xerr=stdDispsF2, yerr=stdVelsF2, color = 'orange', label='Fibrosis Score 2', fmt = 'o')
#plt.errorbar(goodDispsF3, goodVelsF3, xerr=stdDispsF3, yerr=stdVelsF3, color = 'green', label='Fibrosis Score 3', fmt = 'o')
#plt.errorbar(goodDispsF4, goodVelsF4, xerr=stdDispsF4, yerr=stdVelsF4, color = 'blue', label='Fibrosis Score 4', fmt = 'o')
plt.scatter(goodDispsF0, goodVelsF0, color = 'pink', label='Fibrosis Score 0')
plt.scatter(goodDispsF1, goodVelsF1, color = 'red', label='Fibrosis Score 1')
plt.scatter(goodDispsF2, goodVelsF2, color = 'orange', label='Fibrosis Score 2')
plt.scatter(goodDispsF3, goodVelsF3, color = 'green', label='Fibrosis Score 3')
plt.scatter(goodDispsF4, goodVelsF4, color = 'blue', label='Fibrosis Score 4')
plt.errorbar(0.8094, 0.8471, yerr=0.0057, xerr=0.0064, elinewidth=3, marker='o', ms=8, color='cyan', label='E1786-1')
plt.errorbar(1.9714, 2.0150, yerr=0.0202, xerr=0.0180, elinewidth=3, marker='o', ms=8, color='magenta', label='E1787-1')
plt.errorbar(1.7685, 2.0835, yerr=0.1132, xerr=0.1005, elinewidth=3, marker='o', ms=8, color='red', label='E2297-A1')
plt.errorbar(2.2539, 2.6633, yerr=0.1495, xerr=0.0905, elinewidth=3, marker='o', ms=8, color='green', label='E2297-B3')
plt.errorbar(2.5937, 3.3036, yerr=0.1711, xerr=0.1134, elinewidth=3, marker='o', ms=8, color='blue', label='E2297-C1')
leg = ax.legend(scatterpoints = 1, numpoints=1, loc = 4, fontsize=20, framealpha=0.0)
for text in leg.get_texts():
#    text.set_color("white")
    text.set_weight('bold')
plt.plot([0,5.5],[0,5.5], color='k', linewidth=4.0)
plt.xlim([0, 5.5])
plt.ylim([0, 5.5])
plt.axes().set_aspect('equal')
plt.ylabel('gSWSv (m/s)', fontsize = 32, color='k')
plt.xlabel('gSWSd (m/s)', fontsize = 32, color='k')
plt.savefig('gSWSMark.png', dpi=400)
#plt.show()

