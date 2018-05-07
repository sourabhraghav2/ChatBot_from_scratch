from interfaces.interface_hub import NN
from util.log_management import LogWrapper
import tensorflow as tf


class BasicModel(NN):
    def __init__(self):
        super(BasicModel, self).__init__()
        self.log = LogWrapper.get_logger()
        self.log.info('BasicModel initialization')

    def train_model(self,  conversation):
        #training model
        self.log.info('Training model')

    def load_and_predict(self, X_test, batch_size):
        self.log.info('Loading data and predicting')
