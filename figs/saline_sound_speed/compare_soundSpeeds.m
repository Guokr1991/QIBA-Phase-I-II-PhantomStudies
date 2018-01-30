format longEng

T = 2:40;
S = 0;
P = 10; 
[C3W,c_pureWater] = sound_speed_saline(T,S,P);
plot(T,C3W); hold on; plot(T,c_pureWater,'r')

S = 9.0;
[C3W,c_pureWater] = sound_speed_saline(T,S,P);
plot(T,C3W,'r--')

S = 45.0;
[C3W,c_pureWater] = sound_speed_saline(T,S,P);
plot(T,C3W,'r.-.')

grid on;
set(gca,'FontSize',16)
xlabel('Temperature (Celcius)','FontSize',16)
ylabel('Sound Speed (mm/\mus)','FontSize',16)
legend('Pure Water','Salinity = 0','Salinity = 9ppt','Salinity = 45ppt','location','southeast')

