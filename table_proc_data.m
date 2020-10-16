t_data_filename_fix = 'T_data_remainder';
for x = 2:10
    file_name = strcat('data_remainder',num2str(x));
    t_data_filename = strcat(t_data_filename_fix, num2str(x));
    B = tabulate(eval(file_name));
    B = cell2table(B, 'VariableNames', {'Value','Count','Percent'});
    B = sortrows(B, 2);
    toDelete = B.Count == 1; 
    B(toDelete,:) = []; 
    eval(['T_data_remainder', num2str(x), ' = B'])                                                 
end
