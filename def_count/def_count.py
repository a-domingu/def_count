import os
from pyspark import SparkContext

'''
The function 'get files' will receive a directory as input, and it will look for all the *.py files
withing that directory. The key to do that is to use 'os.walk'

Then, the 'count' function will receive this list of files and it will count all the instances of 'def'
'''

def get_files(path):
    ls = []
    for i in os.walk(path):
        '''
        #'i' is a tuple with 3 elements: i[0] is the path we're in, i[1] is the list of FOLDERS, i[2], FILES
        file_path = os.path.join(i[0], i[2]) #i[2] ES UNA LISTA, NO UN STRING
        ls.append(file_path)'''
        directory, ls_files = i[0], i[2]
        for file in ls_files:
            if file.endswith('.py'):
                path = os.path.join(directory, file)
                ls.append(path)
    return ls

def count(ls_files):
    pass
