import pandas as pd
from interfaces.interface_hub import InputOutput
import  numpy as np

from util.log_management import LogWrapper

log=LogWrapper.get_logger()


class ReadWriteCSVFile(InputOutput):
    def __init__(self,path):
        log.info('initialize ReadWriteCSVFile '+str(path))
        self.path=path

    def read(self):
        self.file = pd.read_csv(self.path)
        return self.file

class ReadWriteTextFile(InputOutput):
    def __init__(self,path):
        log.info('initialize ReadWriteTextFile '+str(path))
        self.path=path
    def read(self, encoding='utf-8', errors='ignore'):
        return open(self.path, encoding=encoding, errors=errors).read()

class ReadWriteTextFileList(InputOutput):
    def __init__(self,path):
        log.info('initialize ReadWriteTextFileList '+str(path))
        self.path=path
    def read(self, encoding='utf-8', errors='ignore',limit=None):
        log.info('Limit decided :'+str(limit))
        question_list=[]
        answer_list=[]
        if len(self.path[0])>1:
            if limit!=None:
                question_list = open(self.path[0], encoding=encoding, errors=errors).read().split('\n')[:limit]
                answer_list = open(self.path[1], encoding=encoding, errors=errors).read().split('\n')[:limit]
            else:
                question_list = open(self.path[0], encoding=encoding, errors=errors).read().split('\n')
                answer_list = open(self.path[1], encoding=encoding, errors=errors).read().split('\n')

        log.info('Shape of Question : '+str(len(question_list)))
        log.info('Shape of Answer   : '+ str(len(answer_list)))

        return question_list,answer_list
        # return [], []



