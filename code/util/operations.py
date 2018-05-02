from bs4 import BeautifulSoup
import  re
from nltk import WordNetLemmatizer, SnowballStemmer
from interfaces.interface_hub import UnitOperation



class HtmlCleaning(UnitOperation):
    def operate(self, sentence_list):

        cleaned_html = []
        for each_line in sentence_list:
            cleaned_html.append(BeautifulSoup(each_line).getText())
        print('Html cleaning done!!')
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
        print('max: ',self.max_len)
        print('min: ', self.min_len)
        for q,a in zip(question,answer):
            if(len(a.split(' '))>self.max_len):
                a=''.join(a.split(' ')[:self.max_len])
            if (len(q.split(' ')) > self.max_len):
                q = ''.join(q.split(' ')[:self.max_len])
            if (len(q.split(' '))>self.min_len and len(q.split(' '))<self.max_len)  and len(a.split(' '))>self.min_len and len(a.split(' '))<self.max_len:
                filtered_question_list.append(q)
                filtered_answer_list.append(a)
            # else:
            #     print('---------')
            #     print("Discard question : ",q)
            #     print("Discard  len : ", len(q.split(' ')))
            #     print("Discard answer : ", a)
            #     print("Discard  len : ", len(a.split(' ')))
            #     print('---------')

        print('Special character removal done!!')
        return filtered_question_list,filtered_answer_list


class SpecialCharacterCleaning(UnitOperation):
    def operate(self, sentence_list):
        cleaned_special_char=[]
        for each_line in sentence_list:
            cleaned_special_char.append( re.sub("[^a-zA-Z]", " ", each_line))
        print('Special character removal done!!')
        return cleaned_special_char

class LowerCaseConversion(UnitOperation):
    def operate(self, sentence_list):
        lowered_sentence_list= []
        for each_line in sentence_list:
            lowered_sentence_list.append(each_line.lower())

        print('Word lower case conversion done!!')
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
        print('Word lamatized done!!')
        return final_sentence_list

class Stemmizer(UnitOperation):
    def operate(self, sentence_list):
        sentence_list = []
        snowball_stemmer = SnowballStemmer('english')
        for each_line in sentence_list:
            line = ''
            for word in each_line.split(' '):
                word = snowball_stemmer.stem(word)
                line = line + ' ' + word
            sentence_list.append(line)
        print('Word Stemmization done!!')
        return  sentence_list


