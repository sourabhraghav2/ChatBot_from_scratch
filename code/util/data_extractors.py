from interfaces.interface_hub import DataExtractor
from util.log_management import LogWrapper

log=LogWrapper.get_logger()
class DataExtractorForCsv(DataExtractor):
    def __init__(self):
        log.info('initializing DataExtracterForCsv')

    def extract_data(self,data):
        log.info('extracting data from csv')
        # some Extraction code
        # return question_list,answer_list;
        return [], [];

class ExtracterQuestionAnswer(DataExtractor):
    def __init__(self):
        log.info('initializing DataExtracterForText')

    def extract_data(self,data):
        log.info('extracting data from text')

        result=[[],[]]
        if len(data)>1:
            conv_Id_list=data[0]
            actual_lines=data[1]
            log.info('Length Of conv_Id_list :'+str(len(conv_Id_list)))
            log.info('Length Of actual_lines :'+str(len(actual_lines)))

            result=self.get_question_answer_list(conv_Id_list,actual_lines)

        return result;

    def get_question_answer_list(self, conv_Id_list, actual_lines):
        id2line = {}
        for line in actual_lines:
            _line = line.split(' +++$+++ ')
            if len(_line) == 5:
                id2line[_line[0]] = _line[4]
        log.info('.')
        convs = []
        for line in conv_Id_list[:-1]:
            _line = line.split(' +++$+++ ')[-1][1:-1].replace("'", "").replace(" ", "")
            convs.append(_line.split(','))
        log.info('.')
        questions = []
        answers = []

        for conv in convs:
            for i in range(len(conv) - 1):
                if id2line.get(conv[i]) and id2line.get(conv[i + 1]):
                    questions.append(id2line[conv[i]])
                    answers.append(id2line[conv[i + 1]])
        log.info('.')
        log.info("Number of Question :"+str(len(questions)))
        log.info("Number of Answer   :"+str(len(answers)))
        log.info('Questions :'+str(questions[:5]))
        log.info('Questions :'+str(answers[:5]))
        return questions,answers