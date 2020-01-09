function membersummary
% Member Class Registration
% Inputs: User Class Selection, Member Class Selection, Cash Member list
% Outputs: Combined Member Class Selection, Class member list

%%
PathName = uigetdir('Select the data folder');

f = waitbar(0,'Please wait...');
pause(.5)

cd(PathName);
mkdir Output
Savepath = [PathName,'\Output'];
%% Read in Member Class file
MCtemp = dir('*MemberClass.xlsx');
MCfilename = MCtemp.name;
[~, ~, MC] = xlsread(MCfilename);

MCmember = size(MC,1)-1;
MCheader = MC(1,1:19);

MCraw = MC(2:MCmember+1,1:19);

%% Read in Member List
MLtemp = dir('*Member.xlsx');
MLfilename = MLtemp.name;
[~, ~, ML] = xlsread(MLfilename);

% MLmember = size(ML,1)-1;
% MLheader = ML(1,:);
%
% MLraw = ML(2:end,:);

%% Ask if Cash Member List exist
[CashM,path] = uigetfile('.xlsx');

waitbar(.2,f,'Loading your data');
pause(0.5)
%%
% try
    %% Read in Cash Member list
    cd(path)
    [~, ~, CashMlist] = xlsread(CashM);
    CMonly = CashMlist(1,:);
    CUonly = CMonly;
    
    % Read in User Class file
    cd(PathName);
    UCtemp = dir('*UserClassSelection.xlsx');
    UCfilename = UCtemp.name;
    [~, ~, UC] = xlsread(UCfilename);
    
    UCmember = size(UC,1)-1;
    UCraw = [cell(UCmember,1),UC(2:UCmember+1,1),UC(2:UCmember+1,7),UC(2:UCmember+1,4:5),UC(2:UCmember+1,2),UC(2:UCmember+1,6),UC(2:UCmember+1,3),UC(2:UCmember+1,8:18)];
    
    %% Match Cash member with UC
    
    cd(Savepath)
    CashM = cell(1,size(UCraw,2));
    for ii = 1:size(CashMlist,1)-1
        ii
        email = CashMlist{ii+1,5}
        index = strcmp(email,UCraw(:,6));
        location = find(index ~= 0);
        if ~isempty(location)
            cashM = UCraw(location,:);
            CashM = [CashM;cashM];
        else % email doesnt match
            logid = CashMlist{ii+1,4};
            index = strcmp(logid,UCraw(:,2));
            location = find(index ~= 0);
            if ~isempty(location)
                cashM = UCraw(location,:);
                CashM = [CashM;cashM];
            else
                CMonly = [CMonly;CashMlist(ii+1,:)];
            end
        end % email match
    end % ii match Cash
    CashM(1,:) = [];
    MClist = [MCheader;MCraw;CashM];
    %%
    if size(CMonly,1) > 1
        xlswrite('Cash Member without class.xlsx',CMonly)
    end % save cash member without class
    
    %% Read in User Waiting Pay file
    cd(PathName);
    UWPtemp = dir('*RegisteredWaitingPayment.xlsx');
    UWPfilename = UWPtemp.name;
    [~, ~, UWP] = xlsread(UWPfilename);
    %%
    UWPmember = size(UWP,1)-1;
    UWPraw = [UWP(2:UWPmember+1,1:2),UWP(2:UWPmember+1,8),UWP(2:UWPmember+1,5:6),UWP(2:UWPmember+1,3),UWP(2:UWPmember+1,7),UWP(2:UWPmember+1,4),cell(UWPmember,7)];
    
    %% Match Cash member with User without paying
    cd(Savepath)
    Cash = cell(1,size(UWPraw,2));
    for ii = 1:size(CashMlist,1)-1
        ii
        email = CashMlist{ii+1,5};
        index = strcmp(email,UWPraw(:,6));
        location = find(index ~= 0);
        if ~isempty(location)
            cash = UWPraw(location,:);
            cash{9} = '2019?????';
            cash{10} = CashMlist{ii+1,8};
            cash{11} = CashMlist{ii+1,6};
            cash{12} = CashMlist{ii+1,7};
            Cash = [Cash;cash];
        else % email doesnt match
            logid = CashMlist{ii+1,4};
            index = strcmp(logid,UWPraw(:,2));
            location = find(index ~= 0);
            if ~isempty(location)
                cash = UWPraw(location,:);
                cash{9} = '2019?????';
                cash{10} = CashMlist{ii+1,8};
                cash{11} = CashMlist{ii+1,6};
                cash{12} = CashMlist{ii+1,7};
                Cash = [Cash;cash];
            else
                cash = cell(1,size(UWPraw,2));
                cash{4} = CashMlist{ii+1,3};
                cash{6} = CashMlist{ii+1,5};
                cash{7} = CashMlist{ii+1,2};
                cash{9} = '2019?????';
                cash{10} = CashMlist{ii+1,8};
                cash{11} = CashMlist{ii+1,6};
                cash{12} = CashMlist{ii+1,7};
                Cash = [Cash;cash];
            end
        end % email match
    end % ii match Cash
    Cash(1,:) = [];
    MLlist = [ML;Cash];
    %%
    if size(CUonly,1) > 1
        xlswrite('Cash User.xlsx',CUonly)
    end % save cash member without class
% catch
%     cd(Savepath)
%     MClist = [MCheader;MCraw];
%     MLlist = ML;
% end % Read Cash member and combine

xlswrite('Combined Member Class Selection.xlsx',MClist)
xlswrite('Combined Member List.xlsx',MLlist)

%% Generate class list
student = MClist(1,1:8);
class = MClist(1,9:end);
Class = cell(size(class,2),2);
for cc = 1:size(class,2)
    Class{cc,1} = [class{cc},'.xlsx'];
    Class{cc,2} = student;
end % fill class name
Selection = cell2mat(MClist(2:end,9:end));

for ss = 1:size(Selection,1)
    sclass = find(Selection(ss,:) == 1);
    for sc = 1:size(sclass,2)
        Class{sclass(sc),2} = [Class{sclass(sc),2};MClist(ss+1,1:8)];
    end % fill each
end % fill student info

%% save files
waitbar(.80,f,'Processing your data');
pause(0.5)

for cc = 1:size(class,2)
    xlswrite(Class{cc,1},Class{cc,2})
end % save files

waitbar(1,f,'Finishing');
pause(1)

close(f)

cd(PathName);
msgbox('Combination Completed');
end


