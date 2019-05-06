function varargout = Member7seas(varargin)
% MEMBER7SEAS MATLAB code for Member7seas.fig
%      MEMBER7SEAS, by itself, creates a new MEMBER7SEAS or raises the existing
%      singleton*.
%
%      H = MEMBER7SEAS returns the handle to a new MEMBER7SEAS or the handle to
%      the existing singleton*.
%
%      MEMBER7SEAS('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in MEMBER7SEAS.M with the given input arguments.
%
%      MEMBER7SEAS('Property','Value',...) creates a new MEMBER7SEAS or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before Member7seas_OpeningFcn gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to Member7seas_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Edit the above text to modify the response to help Member7seas

% Last Modified by GUIDE v2.5 04-May-2019 01:25:15

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
                   'gui_Singleton',  gui_Singleton, ...
                   'gui_OpeningFcn', @Member7seas_OpeningFcn, ...
                   'gui_OutputFcn',  @Member7seas_OutputFcn, ...
                   'gui_LayoutFcn',  [] , ...
                   'gui_Callback',   []);
if nargin && ischar(varargin{1})
    gui_State.gui_Callback = str2func(varargin{1});
end

if nargout
    [varargout{1:nargout}] = gui_mainfcn(gui_State, varargin{:});
else
    gui_mainfcn(gui_State, varargin{:});
end
% End initialization code - DO NOT EDIT


% --- Executes just before Member7seas is made visible.
function Member7seas_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to Member7seas (see VARARGIN)

% Choose default command line output for Member7seas
handles.output = hObject;

% Update handles structure
guidata(hObject, handles);

% UIWAIT makes Member7seas wait for user response (see UIRESUME)
% uiwait(handles.figure1);


% --- Outputs from this function are returned to the command line.
function varargout = Member7seas_OutputFcn(hObject, eventdata, handles) 
% varargout  cell array for returning output args (see VARARGOUT);
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Get default command line output from handles structure
varargout{1} = handles.output;


% --- Executes on button press in pushbutton1.
function pushbutton1_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
membersummary
