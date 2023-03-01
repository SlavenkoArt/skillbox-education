import os

folder_name = 'access'
file_name = 'admin.bat'

absolut_path = os.path.abspath(file_name)
relative_path = os.path.join('Skillbox', folder_name, file_name)

print(absolut_path)
print(relative_path)