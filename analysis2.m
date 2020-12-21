clear all;close all;clc;
data = csvread('15minuteData.csv',1,2,[1,2,154660,11]);
totalMF = 0;
for i = 1:154660
    ctl = floor(data(i,7)/4096);
    if(ctl==1||ctl==3)
    totalMF = totalMF+1;
    end
end