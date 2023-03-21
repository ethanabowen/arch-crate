import os

def create_editted_directory(dir):
    if not os.path.exists(dir + '/' + 'Editted'):
        os.mkdir(dir + '/' + 'Editted')

        return True
    return False
