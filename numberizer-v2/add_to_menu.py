# https://github.com/seddie95/python_script_in_right_click_menu/blob/master/make_key.py

import os
import sys
import winreg as reg

# Get path of current working directory and python.exe
cwd = os.getcwd()
python_exe = sys.executable

# optional hide python terminal in windows
# hidden_terminal = '\\'.join(python_exe.split('\\')[:-1])+"\\pythonw.exe"

# Set the path of the context menu (right-click menu)
key_path = r'Directory\\Background\\shell\\Numberizer\\'

# Create outer key
key = reg.CreateKey(reg.HKEY_CLASSES_ROOT, key_path)
reg.SetValue(key, '', reg.REG_SZ, '&Numberizer')  # Change 'Organise folder' to the function of your script

# create inner key
key1 = reg.CreateKey(key, r"command")
reg.SetValue(key1, '', reg.REG_SZ, python_exe + f' "{cwd}\\numberizer-v2.py"')
#reg.SetValue(key1, '', reg.REG_SZ, hidden_terminal + f' "{cwd}\\file_organiser.py"')  # use to to hide terminal