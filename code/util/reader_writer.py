import pandas as pd
from interfaces.interface_hub import InputOutput
import  numpy as np

class ReadWriteCSVFile(InputOutput):
    def __init__(self,path):
        print('initialize ReadWriteCSVFile ',path)
        self.path=path

    def read(self):
        self.file = pd.read_csv(self.path)
        return self.file

class ReadWriteTextFile(InputOutput):
    def __init__(self,path):
        print('initialize ReadWriteTextFile ',path)
        self.path=path
    def read(self, encoding='utf-8', errors='ignore'):
        return open(self.path, encoding=encoding, errors=errors).read()

class ReadWriteTextFileList(InputOutput):
    def __init__(self,path):
        print('initialize ReadWriteTextFileList ',path)
        self.path=path
    def read(self, encoding='utf-8', errors='ignore',limit=None):
        print('Limit decided :',limit)
        question_list=[]
        answer_list=[]
        if len(self.path[0])>1:
            if limit!=None:
                question_list = open(self.path[0], encoding=encoding, errors=errors).read().split('\n')[:limit]
                answer_list = open(self.path[1], encoding=encoding, errors=errors).read().split('\n')[:limit]
            else:
                question_list = open(self.path[0], encoding=encoding, errors=errors).read().split('\n')
                answer_list = open(self.path[1], encoding=encoding, errors=errors).read().split('\n')

        print('Shape of Question : ',len(question_list))
        print('Shape of Answer   : ', len(answer_list))

        return question_list,answer_list
        # return [], []



