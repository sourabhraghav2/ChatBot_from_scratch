from model.entities import Conversation
from util.data_extractors import ExtracterQuestionAnswer, DataExtractorForCsv
from util.reader_writer import ReadWriteTextFile
from util.reader_writer import ReadWriteTextFileList
import numpy as np

from util.text_cleaner import TextCleaner, GenericCleaner
from util. text_processor import Tokkenizer

class Manager:
    def __init__(self,path_list,type):
        print('manager initialize')

        conversation=None
        #read Data
        if type=='txt':
            #read text file
            reader = ReadWriteTextFileList(path_list)
            group_and_conversation = reader.read(limit=100)
            conversation = Conversation(group_and_conversation, ExtracterQuestionAnswer)

        else:
            if type=='csv':
                # read csv file
                reader = ReadWriteTextFile(path_list[0])
                question_answer_table = reader.read()
                conversation = Conversation(question_answer_table, DataExtractorForCsv)


        cleaner=GenericCleaner()
        conversation=cleaner.clean_data(conversation)

        print('Combined_question_answer : ',conversation.get_question_answer_list())

o=Manager(['../../data/movie_conversations.txt','../../data/movie_lines.txt'],'txt')

