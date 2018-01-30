% C:\Users\tjhall\Box Sync\QIBA\BC_SWS\CIRS Phantonm SWS v Temperature
tempC = [18.3 21.1 23.8 26.6 29.3];

E2348_1 = [1.85 1.80 1.77 1.76 1.73];
E2348_1std = [0.0822 0.0576 0.0964 0.0614 0.0656];

E2348_2 = [2.46 2.50 2.33 2.26 2.33];
E2348_2std = [0.141 0.196 0.195 0.0787 0.0635];

E2348_3 = [2.84 2.91 2.74 2.80 2.65];
E2348_3std = [0.281 0.222 0.180 0.247 0.215];

E1786_9 = [0.82 0.83 0.83 0.84 0.82];
E1786_9std = [0.0134 0.0145 0.0149 0.0208 0.0148];

figure; errorbar(tempC,E1786_9,E1786_9std,'pg','MarkerFaceColor','g'); hold on

errorbar(tempC,E2348_1,E2348_1std,'sk','MarkerFaceColor','k');
errorbar(tempC,E2348_2,E2348_2std,'db','MarkerFaceColor','b'); 
errorbar(tempC,E2348_3,E2348_3std,'or','MarkerFaceColor','r'); 
 
temp_C = 18:1:30;
[p1,S1] = polyfit(tempC,E2348_1,1); %p1(1) = -0.0102; p1(2) = 2.0246
plot(temp_C,p1(1)*temp_C+p1(2),'k','linewidth',2);
[p2,S2] = polyfit(tempC,E2348_2,1); %p2(1) = -0.0102; p2(2) = 2.0246
plot(temp_C,p2(1)*temp_C+p2(2),'b','linewidth',2);
[p3,S3] = polyfit(tempC,E2348_3,1); %p3(1) = -0.0102; p3(2) = 2.0246
plot(temp_C,p3(1)*temp_C+p3(2),'r','linewidth',2);
[p9,S9] = polyfit(tempC,E1786_9,1); %p9(1) = 0.0004; p9(2) = 0.8191
plot(temp_C,p9(1)*temp_C+p9(2),'g','linewidth',2);


set(gca,'FontSize',16)
xlabel('Temperature (Celsius)','FontSize',16)
ylabel('SWS (m/s)','FontSize',16)

legend('E1786-9','E2348-1','E2348-2','E2348-3','location','northeast')

title('QIBA Phase II Phantoms')












