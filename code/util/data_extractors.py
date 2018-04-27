from interfaces.interface_hub import DataExtractor


class DataExtractorForCsv(DataExtractor):
    def __init__(self):
        print('initializing DataExtracterForCsv')

    def extract_data(self,data):
        print('extracting data from csv')
        # some Extraction code
        # return question_list,answer_list;
        return [], [];

class ExtracterQuestionAnswer(DataExtractor):
    def __init__(self):
        print('initializing DataExtracterForText')

    def extract_data(self,data):
        print('extracting data from text')

        result=[[],[]]
        if len(data)>1:
            conv_Id_list=data[0]
            actual_lines=data[1]
            print('Length Of conv_Id_list :', len(conv_Id_list))
            print('Length Of actual_lines :', len(actual_lines))

            result=self.get_question_answer_list(conv_Id_list,actual_lines)

        return result;

    def get_question_answer_list(self, conv_Id_list, actual_lines):
        id2line = {}
        for line in actual_lines:
            _line = line.split(' +++$+++ ')
            if len(_line) == 5:
                id2line[_line[0]] = _line[4]
        print('.')
        convs = []
        for line in conv_Id_list[:-1]:
            _line = line.split(' +++$+++ ')[-1][1:-1].replace("'", "").replace(" ", "")
            convs.append(_line.split(','))
        print('.')
        questions = []
        answers = []

        for conv in convs:
            for i in range(len(conv) - 1):
                if id2line.get(conv[i]) and id2line.get(conv[i + 1]):
                    questions.append(id2line[conv[i]])
                    answers.append(id2line[conv[i + 1]])
        print('.')
        print("Number of Question :",len(questions))
        print("Number of Answer   :", len(answers))
        print('Questions :',questions[:5])
        print('Questions :', answers[:5])
        return questions,answers