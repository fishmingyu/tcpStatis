clear all;close all;clc;
M=importdata('../data/data.csv');
src = '183.172.173.42';
intcp=0;
outtcp=0;
inudp=0;
outudp=0;

%记录分布曲线
intcpm=zeros(1,1500);
outtcpm=zeros(1,1500);
inudpm=zeros(1,1500);
outudpm=zeros(1,1500);
[hang,lie] = size(M.data);
for i = 1:hang
    if(strcmp(M.textdata(i,13),src))%in
        if(strcmp(M.textdata(i,11),'6'))
            intcp = intcp+1;
            length = str2double(M.textdata(i,7));
            intcpm(length)=intcpm(length)+1;
        elseif(strcmp(M.textdata(i,11),'17'))
            inudp = inudp+1;
            length = str2double(M.textdata(i,7));
            inudpm(length)=inudpm(length)+1;
        end
    elseif(strcmp(M.textdata(i,14),src))%out
        if(strcmp(M.textdata(i,11),'6'))
            outtcp = outtcp+1;
            length = str2double(M.textdata(i,7));
            outtcpm(length)=outtcpm(length)+1;
        elseif(strcmp(M.textdata(i,11),'17'))
            outudp = outudp+1;
            length = str2double(M.textdata(i,7));
            outudpm(length)=outudpm(length)+1;
        end
    end
end
%计算累计曲线
for i = 2:1500
    intcpm(i) = intcpm(i)+intcpm(i-1);
    inudpm(i) = inudpm(i)+inudpm(i-1);
    outtcpm(i) = outtcpm(i)+outtcpm(i-1);
    outudpm(i) = outudpm(i)+outudpm(i-1);
end
intcpm = intcpm/intcpm(1500);
inudpm = inudpm/inudpm(1500);
outtcpm = outtcpm/outtcpm(1500);
outudpm = outudpm/outudpm(1500);
%显示
figure;
subplot(2,2,1);
plot(intcpm);
title('TCP IN');
subplot(2,2,2);
plot(inudpm);
title('UDP IN');

subplot(2,2,3);
plot(outtcpm);
title('TCP OUT');
subplot(2,2,4);
plot(outudpm);
title('UDP OUT');