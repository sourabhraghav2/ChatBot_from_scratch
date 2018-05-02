from bean.entities import Conversation
from util.data_extractors import ExtracterQuestionAnswer, DataExtractorForCsv
from util.reader_writer import ReadWriteTextFile
from util.reader_writer import ReadWriteTextFileList
import numpy as np

from util.text_cleaner import TextCleaner, GenericCleaner
from util. text_processor import Tokkenizer

class Manager:
    def __init__(self,path_list,type):
        print('manager initialize')
        sentence_max_length=20
        sentence_min_length = 2

        conversation=None
        #read Data
        if type=='txt':
            #read text file
            reader = ReadWriteTextFileList(path_list)
            group_and_conversation = reader.read(limit=500)
            conversation = Conversation(group_and_conversation,
                                        ExtracterQuestionAnswer,
                                        sentence_max_length,
                                        sentence_min_length
                                        )

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


        tokken=Tokkenizer(conversation)
        conversation=tokken.get_digital_conversation()
        
        print('Combined_question_answer : ',conversation.get_question_answer_list())





o=Manager(['../../data/movie_conversations.txt','../../data/movie_lines.txt'],'txt')

