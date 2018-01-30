function [C3W,c_pureWater] = sound_speed_saline(T,S,P)
%sound_speed_saline.m determines the speed of sound in water as a function
%of temperature (T), salinity (S), and pressure (P)
%   Salinity is defined in terms of disolved solids (an approximation used
%   here; grams salt/kilograms water).
%   Enter the water TEMPERATURE (Celcius)
%   Enter the water SALINITY (g/kg, default=0)
%   Enter the water PRESSURE (decibar, 10dBar = 1atm = 760mm Hg = 101kPa)
%   The equation used is (3) from J.R. Lovett, J. Acoust. Soc. Am. 63, 1713-1718, 1978.
%   NB: Equations (1) and (2) from that paper are included for comparison
%   and verification.
%   C_pureWater is found in GS Kell, J. Chem. Engng. Data (1975), also in Kaye and Laby (5th) p29
%   NB2: C_pureWater excludes any pressure dependence
%   when T = 2; S = 34.7; P = 6000; expect 1.559462 for (1); 
%   expect 1.559393 for (2); 1.559499 for (3)

c_pureWater =  1.e-3*(1402.736 + 5.03358*T - 0.0579506*T.^2 + ...
        3.31636e-4*T.^3 - 1.45262e-6*T.^4 + 3.0449e-9*T.^5); %in mm/us
    
% C01 = 1402.392;
% C1t = 5.011094*T - 5.509468e-2*T.^2 + 2.21536e-4*T.^3;
% C1s = 1.32952*S + 1.289558e-4*S.^2;
% C1p = 1.59893e-2*P + 2.478901e-7*P.^2 - 8.48572e-12*P.^3;
% C1tsp = - 1.27562e-2*T*S + 6.47715e-4*T*P + 2.760566e-10*T.^2*P.^2 - 1.65695e-8*T*P.^2 + 5.536118e-13*T*P.^3 - 4.466674e-8*T.^3*P - 1.681126e-11*S.^2*P.^2 + 9.684032e-5*T.^2*S + 4.952146e-7*T*S.^2*P - 3.473123e-5*T*S*P;
% % + 2.760566e-8*T^2*P^2 error in exponent (should be e-10?)?
% C1W = (C01 + C1t + C1s + C1p + C1tsp)/10^3;
% 
% C02 = 1402.394;
% C2t = 5.028849*T - 5.723758e-2*T.^2 + 2.858485e-4*T.^3 - 1.404216e-8*T.^5;
% C2s = 1.280746*S + 2.830167e-3*S.^2 - 3.787896e-5*S.^3;
% C2p = 1.594777e-2*P + 2.778778e-7*P.^2 + 7.069489e-21*P.^5;
% C2tsp = - 1.280898e-2*T*S + 1.040187e-4*T.^2*S - 9.301259e-11*T.^3*S.^3 + 9.488555e-5*T*P - 1.23743e-8*T*P.^2 - 7.100174e-6*T.^2*P + 8.592724e-14*T.^2*P.^3 - 9.02519e-8*T.^3*P - 2.70148e-11*T.^3*P^2 - 7.818551e-13*S*P.^3 + 1.303142e-14*S.^2*P.^3 - 6.265617e-13*S.^3*P.^2 - 2.238383e-6*T*S*P + 2.85346e-7*T.^2*S*P; 
% C2W = (C02 + C2t + C2s + C2p + C2tsp)/10^3

C03 = 1402.394;
C3t = 5.0113*T - 5.51303e-2*T.^2 + 2.22100e-4*T.^3;
C3s = 1.33294*S;
C3p = 1.60533e-2*P + 2.1244e-7*P.^2;
C3tsp = - 1.26638e-2*T*S + 9.543664e-5*T.^2*S - 1.052396e-8*T*P.^2 + 2.183988e-13*T*P.^3 - 2.253828e-13*S*P.^3 + 2.062107e-8*T*S.^2*P ;
C3W = (C03 + C3t + C3s + C3p + C3tsp)/10^3;


