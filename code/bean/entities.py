from interfaces.interface_hub import Data
import numpy as np

from util.log_management import LogWrapper
from util.operations import Discard_sentence_on_length, Sort_sentence_on_length, Remove_multiple_space

log=LogWrapper.get_logger()

class Conversation(Data):
    def __init__(self,data,data_extractor,max_len,min_len):
        log.info('initialize Conversation ')
        self.data=data
        self.question_list=[]
        self.answer_list=[]
        self.sentence_max_length=max_len
        self.sentence_min_length=min_len

        data_ext = data_extractor()
        self.question_list, self.answer_list = data_ext.extract_data(self.data)
        self.shape_of_question_dataset = np.array(self.question_list).shape
        self.shape_of_answer_dataset = np.array(self.answer_list).shape

        #text processing start
        self.remove_multiple_space()
        # self.discard_sentences_on_length()
        self.sort_sentences_on_length()



    def get_data(self):
        return self.data

    def get_question_list(self,length=None):
        if length==None:
            return self.question_list
        else:
            return self.question_list[:length]

    def get_answer_list(self,length=None):
        if length==None:
            return self.answer_list
        else:
            return self.answer_list[:length]

    def set_question_answer_list(self, combined_question_andwer_list):

        if len(combined_question_andwer_list)>1:
            self.question_list=combined_question_andwer_list[0]
            self.answer_list=combined_question_andwer_list[1]


    def get_question_answer_list(self,length=None):
        log.info('Length : '+str(length))

        if(length==None):
            log.info('Question shape : '+str(self.shape_of_question_dataset))
            log.info('Answer shape   : '+str(self.shape_of_answer_dataset))
            return self.question_list[:self.shape_of_question_dataset[0]], self.answer_list[:self.shape_of_answer_dataset[0]]
        else:
            return self.question_list[:length], self.answer_list[:length]

    def sort_sentences_on_length(self):
        sorter=Sort_sentence_on_length(self.sentence_max_length)
        input = (self.question_list, self.answer_list)
        self.set_question_answer_list(sorter.operate(input))

    def discard_sentences_on_length(self):
        trim_sentence_on_length=Discard_sentence_on_length(self.sentence_min_length,self.sentence_max_length)
        input=(self.question_list,self.answer_list)
        log.info('Before discarding')
        log.info('Question  : '+str(np.array(self.question_list).shape))
        log.info('Answer  : '+str(np.array(self.answer_list).shape))
        self.set_question_answer_list(trim_sentence_on_length.operate(input))

        log.info('After discarding')
        log.info('Question  : '+str(np.array(self.question_list).shape))
        log.info('Answer  : '+str(np.array(self.answer_list).shape))

    def print_conv(self, conversation, from_which):
        log.info(from_which)
        log.info('---------')
        q_li = conversation.get_question_answer_list()[0]
        a_li = conversation.get_question_answer_list()[1]
        log.info(q_li[:3])
        log.info(a_li[:3])
        log.info('---------')

    def remove_multiple_space(self):
        space_remover= Remove_multiple_space()
        input = self.question_list, self.answer_list
        self.set_question_answer_list(space_remover.operate(input))



class ConversationList(list):

    def __init__(self):
        log.info('Conversation initializing')
        self.conv_list = []