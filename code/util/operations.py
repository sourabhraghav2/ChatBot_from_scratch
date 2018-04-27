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


