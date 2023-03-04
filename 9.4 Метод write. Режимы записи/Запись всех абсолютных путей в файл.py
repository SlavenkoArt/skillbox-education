import os

def finde_file(cur_path):

    print('Переходим', cur_path)

    for i_elem in os.listdir(cur_path):
        path = os.path.join(cur_path, i_elem)
        print('   смотрим', path)

        if os.path.isdir(path):
            print('это директория')
            finde_file(path)
        else:
            file_contents = open('scripts1.txt', 'a')

            file_contents.write(path)
            file_contents.write('\n')

            file_contents.close()

            return file_contents

finde_file('/Users/artemslavenko/Desktop/Python_Basic')