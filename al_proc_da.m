path_fix = 'C:\Users\spsim\Desktop\crc_data\data_remainder';
filename_fix = 'data_remainder';
h=waitbar(0,'please wait');
for i = 0:2046
    str=['ÔËÐÐÖÐ...',num2str(i/2046*100),'%'];
    waitbar(i/2046,h,str)
    k_num = string(i);
    path = strcat(path_fix, k_num);
    %file_name = strcat(filename_fix, k_num);
    %file_name = importfile(path, 1, 2000);
    eval(['data_remainder',num2str(i),'=','importfile(path, 1, 2000)']);
end
delete(h);
