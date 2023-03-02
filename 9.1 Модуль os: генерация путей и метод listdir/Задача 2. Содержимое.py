import os

def print_dirs(project):
    print('\n Содержимое директории', project)
    for i_elem in os.listdir(project):
        path = os.path.join(project, i_elem)
        print('  ', path)

project_list = ['skillbox-education', 'Skillbox']

for i_project in project_list:
    path_to_project = os.path.abspath(os.path.join('..', '..', i_project))
    print_dirs(path_to_project)