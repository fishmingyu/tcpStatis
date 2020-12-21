clear all;close all;clc;
M=importdata('data.csv');
ctl = zeros(6,6);
src = '183.172.173.42';
%六行依次表示：进入1，进入0，比例，出去1，出去0，比例；四列以此表示从urg开始的6个控制位
[hang,lie] = size(M.data);
for i = 1:hang
    for j = 1:6
    if(strcmp(M.textdata(i,13),src))%in
        if(M.data(i,j+8)==1)ctl(1,j) = ctl(1,j)+1;
        elseif(M.data(i,j+8)==0)ctl(2,j) = ctl(2,j)+1;
        end
    elseif((strcmp(M.textdata(i,14),src)))%out
        if(M.data(i,j+8)==1)ctl(4,j) = ctl(4,j)+1;
        elseif(M.data(i,j+8)==0)ctl(5,j) = ctl(5,j)+1;
        end
    end
    end
end
for j = 1:6
    ctl(3,j) = ctl(1,j)/(ctl(1,j)+ctl(2,j));
    ctl(6,j) = ctl(4,j)/(ctl(4,j)+ctl(5,j));
end
%结果保存在数组ctl中