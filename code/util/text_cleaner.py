from bs4 import BeautifulSoup

from nltk.stem import WordNetLemmatizer
from nltk.stem import SnowballStemmer

from interfaces.interface_hub import Cleaner, UnitOperation
from util.operations import *

log=LogWrapper.get_logger()
class GenericCleaner(Cleaner):
    def __init__(self):
        log.info('initialize Generic Cleaner')

    def clean_data(self,conversation):
        text_cleaner=TextCleaner()
        cleaned_data=text_cleaner.clean_data(conversation.get_question_answer_list())

        conversation.set_question_answer_list(cleaned_data)
        return conversation



class TextCleaner(Cleaner):
    def __init__(self):
        log.info('initialize Text Cleaner')

    def clean_data(self,data):
        self.data = data
        self.question_list = self.data[0]
        self.answer_list = self.data[1]

        pipeline= [HtmlCleaning,SpecialCharacterCleaning,LowerCaseConversion,Lamatizer]
        for each in pipeline:
            try:
                self.question_list= each().operate(self.question_list)
                self.answer_list = each().operate(self.answer_list)
            except:
                import traceback
                log.error('Exception triggered...!! '+str(traceback.format_exc()))
        # log.info("Question : ",self.question_list)
        # log.info("Answer   : ",  self.answer_list)
        return self.question_list,self.answer_list







