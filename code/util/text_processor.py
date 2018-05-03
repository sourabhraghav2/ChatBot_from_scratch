import numpy as np


from util.log_management import LogWrapper

log=LogWrapper.get_logger()

class Tokkenizer:

    def __init__(self,conversation,threshold=10,sentence_max_length=20):

        log.info('initializing Tokkenizer ')
        self.conversation=conversation
        self.threshold = threshold
        question_list=conversation.get_question_list()
        answer_list=conversation.get_answer_list()
        self.sntence_list=list(np.concatenate([question_list,answer_list]))
        self.vocab = {each :index for index, each in enumerate(['<PAD>', '<EOS>', '<UNK>', '<GO>'])}
        self.generate_vocab()

        #convert words to digit
        question_list=self.convert_word_to_digit(question_list)
        answer_list= self.convert_word_to_digit(answer_list)

        #padding if required
        answer_list = self.padd_list_with_size_and_digit(answer_list,self.vocab['<PAD>'],sentence_max_length)
        question_list = self.padd_list_with_size_and_digit(question_list,self.vocab['<PAD>'],sentence_max_length)

        conversation.set_question_answer_list((question_list,answer_list))

    def get_vocab(self):
        return self.vocab

    def get_digital_conversation(self):
        return self.conversation

    def padd_list_with_size_and_digit(self,input_list, padding_digit, max_size):
        final_padded_digit_list = []
        for each in input_list:
            if (len(each) < max_size):
                padding_size = max_size - len(each)
                total_padding_values = [padding_digit] * padding_size
                final_padded_digit = each + total_padding_values
            else:
                final_padded_digit = each[:max_size]
            final_padded_digit_list.append(final_padded_digit)

        return final_padded_digit_list

    def generate_vocab(self):

        vocab=self.vocab
        count=self.vocab.__len__()
        log.info("Count starts : "+str(count))
        vocab_with_count={}
        for sentence in self.sntence_list:
            for word in sentence.split(' '):
                if vocab_with_count.get(word) == None:
                    vocab_with_count[word] = 1
                else:
                    vocab_with_count[word] = vocab_with_count[word] + 1;
        #set count zero with less threshold count
        for k, v in vocab_with_count.items():
            if v < self.threshold:
                log.info('del '+str(k)+' : '+str(v))
                vocab_with_count[k] = 0


        for sentence in self.sntence_list:
            for word in sentence.split(' '):
                if word not  in vocab and word !='' and vocab_with_count[word]!=0:
                    count=count+1;
                    vocab[word]=count
        self.vocab=vocab
        return vocab


    def convert_word_to_digit(self,sntence_list):
        digit_sentence_list=[]
        for sentence in sntence_list:
            digit_sentence=[]
            log.info("words sentence  : >"+str(sentence)+"<")
            for word in sentence.split(' '):
                if self.vocab.get(word):
                    digit_sentence.append(self.vocab.get(word))
                else:
                    digit_sentence.append(self.vocab.get('<UNK>'))
            log.info('digital  sentence : '+str(digit_sentence))
            digit_sentence_list.append(digit_sentence)

        return digit_sentence_list




    def print_my_data(self):
        log.info('Vocab :'+str(self.vocab))
        log.info('Sentence: '+str(self.sntence_list[1]))
        log.info('Digit List :'+str(self.digit_sentence_list[1]))

