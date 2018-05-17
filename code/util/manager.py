from bean.entities import Conversation
from model.lstm import LSTM_with_attention
from util.data_extractors import ExtracterQuestionAnswer, DataExtractorForCsv
from util.log_management import *
from util.reader_writer import ReadWriteTextFile
from util.reader_writer import ReadWriteTextFileList
from property_manager.property_handler import Properties
import numpy as np

from util.text_cleaner import TextCleaner, GenericCleaner
from util. text_processor import Tokkenizer

class Manager:
    def __init__(self,path_list,type):
        self.log=LogWrapper.get_logger()
        self.properties=Properties.get_properties()
        self.log.info('Manager initialization')

        sentence_max_length=int(self.properties['sentence_max_length'])
        sentence_min_length = int(self.properties['sentence_min_length'])


        conversation=None
        #read Data
        if type=='txt':
            #read text file
            reader = ReadWriteTextFileList(path_list)
            group_and_conversation = reader.read(limit=int(self.properties['limit_of_data_to_read']))
            conversation = Conversation(group_and_conversation,
                                        ExtracterQuestionAnswer,
                                        sentence_max_length,
                                        sentence_min_length)

        else:
            if type=='csv':
                # read csv file
                reader = ReadWriteTextFile(path_list[0])
                question_answer_table = reader.read()
                conversation = Conversation(question_answer_table,
                                            DataExtractorForCsv,
                                            sentence_max_length,
                                            sentence_min_length)


        cleaner=GenericCleaner()
        conversation=cleaner.clean_data(conversation)

        tokkenizer=Tokkenizer(conversation,
                              threshold=int(self.properties['vocab_threshold']),
                              sentence_max_length=sentence_max_length)
        conversation=tokkenizer.get_digital_conversation()
        vocab_to_int=tokkenizer.get_vocab_to_int()
        self.log.info('vocab : '+str(vocab_to_int))
        self.log.info('Combined_question_answer : '+str(conversation.get_question_answer_list()))

        model=LSTM_with_attention(self.properties,vocab_to_int)
        model.train_model(conversation,self.properties)







o=Manager(['../../data/movie_conversations.txt','../../data/movie_lines.txt'],'txt')

