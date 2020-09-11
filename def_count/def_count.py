import os
from pyspark import SparkContext

'''
The function 'get files' will receive a directory as input, and it will look for all the *.py files
withing that directory. The key to do that is to use 'os.walk'

Then, the 'count' function will receive this list of files and it will count all the instances of 'def'
'''

def _find_def(line):
    ls_words = line.split(' ')
    return 'def' in ls_words



def get_files(path):
    ls = []
    for i in os.walk(path):
        directory, ls_files = i[0], i[2]
        for file in ls_files:
            if file.endswith('.py') and not file.startswith('_'):
                path = os.path.join(directory, file)
                ls.append(path)
    return ls

def count(ls_files):
    sc = SparkContext.getOrCreate()
    num = 0
    for file in ls_files:
        if os.path.exists(file):
            rdd = sc.textFile(file)
            num += rdd.filter(_find_def).count()
    return num

