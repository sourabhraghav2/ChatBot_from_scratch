import numpy as np
class Tokkenizer:

    def __init__(self,conversation):
        print('initializing Tokkenizer ')
        self.conversation=conversation
        question_list=conversation.get_question_list()
        answer_list=conversation.get_answer_list()
        self.sntence_list=list(np.concatenate([question_list,answer_list]))
        self.vocab = {each :index for index, each in enumerate(['<PAD>', '<EOS>', '<UNK>', '<GO>'])}
        self.generate_vocab()

        #convert words to digit
        question_list=self.convert_word_to_digit(question_list)
        answer_list= self.convert_word_to_digit(answer_list)

        conversation.set_question_answer_list((question_list,answer_list))

    def get_vocab(self):
        return self.vocab

    def get_digital_conversation(self):
        return self.conversation

    def generate_vocab(self):
        vocab=self.vocab
        count=self.vocab.__len__()
        print("Count starts : ",count)
        for sentence in self.sntence_list:
            # print(sentence,' : ',end='')
            for word in sentence.split(' '):
                # print(' ',word,end='')
                if word not  in vocab and word !='':
                    count=count+1;
                    vocab[word]=count
        self.vocab=vocab
        return vocab


    def convert_word_to_digit(self,sntence_list):
        digit_sentence_list=[]
        for sentence in sntence_list:
            digit_sentence=[]
            print("words sentence  : >",sentence,"<")
            for word in sentence.split(' '):
                if self.vocab.get(word):
                    digit_sentence.append(self.vocab.get(word))
                else:
                    digit_sentence.append(self.vocab.get('<UNK>'))
            print('digital  sentence : ',digit_sentence)
            digit_sentence_list.append(digit_sentence)

        return digit_sentence_list




    def print_my_data(self):
        print('Vocab :',self.vocab)
        print('Sentence: ', self.sntence_list[1])
        print('Digit List :',self.digit_sentence_list[1])

