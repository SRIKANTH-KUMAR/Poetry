import os

def folder_creation(folder_name):
        if not os.path.exists(folder_name):
                os.mkdir(folder_name)

if __name__ == '__main__':
        folder_name = 'test_folder'
        folder_creation(folder_name)