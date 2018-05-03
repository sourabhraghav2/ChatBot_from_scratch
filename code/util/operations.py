from bs4 import BeautifulSoup
import  re
from nltk import WordNetLemmatizer, SnowballStemmer
from interfaces.interface_hub import UnitOperation
from util.log_management import LogWrapper

log=LogWrapper.get_logger()

class HtmlCleaning(UnitOperation):
    def operate(self, sentence_list):

        cleaned_html = []
        for each_line in sentence_list:
            cleaned_html.append(BeautifulSoup(each_line).getText())
        log.info('Html cleaning done!!')
        return cleaned_html



class Sort_sentence_on_length(UnitOperation):
    def __init__(self,max_len):
        self.max_len=max_len
    def operate(self, question_answer):
        sorted_questions = []
        sorted_answers = []
        input_question_list=question_answer[0]
        input_answer_list=question_answer[1]
        for length in range(1, self.max_len + 1):
            for question,answer in zip(input_question_list,input_answer_list):
                if len(question) == length:
                    sorted_questions.append(question)
                    sorted_answers.append(answer)
        return sorted_questions,sorted_answers



class Remove_multiple_space(UnitOperation):
    def operate(self, question_answer):
        question_list=[]
        answer_list = []
        for question,answer in zip(question_answer[0],question_answer[1]):
            question=re.sub(' +', ' ', question).rstrip().lstrip()
            answer = re.sub(' +', ' ', answer).rstrip().lstrip()
            question_list.append(question)
            answer_list.append(answer)
        return question_list,answer_list

class Discard_sentence_on_length(UnitOperation):
    def __init__(self,min_len,max_len):
        self.min_len=min_len
        self.max_len=max_len
    def operate(self, question_answer):
        question=question_answer[0]
        answer=question_answer[1]
        filtered_question_list = []
        filtered_answer_list = []
        log.info('max: '+str(self.max_len))
        log.info('min: '+ str(self.min_len))
        for q,a in zip(question,answer):
            if(len(a.split(' '))>self.max_len):
                a=''.join(a.split(' ')[:self.max_len])
            if (len(q.split(' ')) > self.max_len):
                q = ''.join(q.split(' ')[:self.max_len])
            if (len(q.split(' '))>self.min_len and len(q.split(' '))<self.max_len)  and len(a.split(' '))>self.min_len and len(a.split(' '))<self.max_len:
                filtered_question_list.append(q)
                filtered_answer_list.append(a)
            # else:
            #     log.info('---------')
            #     log.info("Discard question : "+str(q))
            #     log.info("Discard  len : "+str(len(q.split(' '))))
            #     log.info("Discard answer : "+str(a))
            #     log.info("Discard  len : "+str(len(a.split(' '))))
            #     log.info('---------')

        log.info('Special character removal done!!')
        return filtered_question_list,filtered_answer_list


class SpecialCharacterCleaning(UnitOperation):
    def operate(self, sentence_list):
        cleaned_special_char=[]
        for each_line in sentence_list:
            cleaned_special_char.append( re.sub("[^a-zA-Z]", " ", each_line))
        log.info('Special character removal done!!')
        return cleaned_special_char

class LowerCaseConversion(UnitOperation):
    def operate(self, sentence_list):
        lowered_sentence_list= []
        for each_line in sentence_list:
            lowered_sentence_list.append(each_line.lower())

        log.info('Word lower case conversion done!!')
        return  lowered_sentence_list

class Lamatizer(UnitOperation):
    def operate(self, sentence_list):
        final_sentence_list = []
        lemmatizer = WordNetLemmatizer()
        for each_line in sentence_list:
            line = ''
            for word in each_line.split(' '):
                word = lemmatizer.lemmatize(word, pos="a")
                line = line + ' ' + word
            line = re.sub(' +', ' ', line).rstrip().lstrip()
            final_sentence_list.append(line)
        log.info('Word lamatized done!!')
        return final_sentence_list

class Stemmizer(UnitOperation):
    def operate(self, sentence_list):
        sentence_list = []
        snowball_stemmer = SnowballStemmer('english')
        for each_line in sentence_list:
            line = ''
            each_line=self.custom_word_alternative(each_line)
            for word in each_line.split(' '):
                word = snowball_stemmer.stem(word)
                line = line + ' ' + word
            sentence_list.append(line)
        log.info('Word Stemmization done!!')
        return  sentence_list

    def custom_word_alternative(self,text):
        text = re.sub(r"i'm", "i am", text)
        text = re.sub(r"he's", "he is", text)
        text = re.sub(r"she's", "she is", text)
        text = re.sub(r"it's", "it is", text)
        text = re.sub(r"that's", "that is", text)
        text = re.sub(r"what's", "that is", text)
        text = re.sub(r"where's", "where is", text)
        text = re.sub(r"how's", "how is", text)
        text = re.sub(r"\'ll", " will", text)
        text = re.sub(r"\'ve", " have", text)
        text = re.sub(r"\'re", " are", text)
        text = re.sub(r"\'d", " would", text)
        text = re.sub(r"\'re", " are", text)
        text = re.sub(r"won't", "will not", text)
        text = re.sub(r"can't", "cannot", text)
        text = re.sub(r"n't", " not", text)
        text = re.sub(r"n'", "ng", text)
        text = re.sub(r"'bout", "about", text)
        text = re.sub(r"'til", "until", text)
        text = re.sub(r"[-()\"#/@;:<>{}`+=~|.!?,]", "", text)
        return text


