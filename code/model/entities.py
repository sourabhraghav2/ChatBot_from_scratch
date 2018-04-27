from interfaces.interface_hub import Data
import numpy as np
class Conversation(Data):
    def __init__(self,data,data_extractor):
        print('initialize Conversation ')
        self.data=data
        self.question_list=[]
        self.answer_list=[]
        data_ext = data_extractor()
        self.question_list, self.answer_list = data_ext.extract_data(self.data)
        self.shape_of_question_dataset=np.array(self.question_list).shape
        self.shape_of_answer_dataset = np.array(self.answer_list).shape

    def get_data(self):
        return self.data

    def get_question_list(self,length):
        return self.question_list[:length]
    def get_answer_list(self,length):
        return self.answer_list[:length]

    def set_question_answer_list(self, combined_question_andwer_list):
        if len(combined_question_andwer_list)>1:
            self.question_list=combined_question_andwer_list[0]
            self.answer_list=combined_question_andwer_list[1]

    def get_question_answer_list(self,length=None):
        print('Length : ',length)

        if(length==None):
            print('Question shape : ',self.shape_of_question_dataset)
            print('Answer shape   : ', self.shape_of_answer_dataset)
            return self.question_list[:self.shape_of_question_dataset[0]], self.answer_list[:self.shape_of_answer_dataset[0]]
        else:
            return self.question_list[:length], self.answer_list[:length]



class ConversationList(list):

    def __init__(self):
        print('Conversation initializing')
        self.conv_list = []