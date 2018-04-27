class Tokkenizer:

    def __init__(self,sentence_list):
        print('initializing Tokkenizer ')
        self.sntence_list=sentence_list
        self.vocab = {each :index for index, each in enumerate(['<PAD>', '<EOS>', '<UNK>', '<GO>'])}
        self.get_vocab()
        self.convert_word_to_digit()


    def get_vocab(self):
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


    def convert_word_to_digit(self):
        digit_sentence_list=[]
        for sentence in self.sntence_list:
            digit_sentence=[]
            for word in sentence.split(' '):
                if self.vocab.get(word):
                    digit_sentence.append(self.vocab.get(word))
                else:
                    digit_sentence.append(self.vocab.get('<UNK>'))

            digit_sentence_list.append(digit_sentence)

        self.digit_sentence_list=digit_sentence_list




    def print_my_data(self):
        print('Vocab :',self.vocab)
        print('Sentence: ', self.sntence_list[1])
        print('Digit List :',self.digit_sentence_list[1])

