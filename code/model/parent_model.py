from interfaces.interface_hub import NN
from util.log_management import LogWrapper
import tensorflow as tf
import numpy as np
import tensorflow as tf
import time

class BasicModel(NN):
    def __init__(self):
        super().__init__()
        self.log = LogWrapper.get_logger()
        self.log.info('BasicModel initialization')

    def train_model(self,  conversation,properties):
        #training model
        self.log.info('Training model')
        # Validate the training with 10% of the data

        question_list,answer_list=conversation.get_question_answer_list()
        train_valid_split = int(len(question_list) * 0.15)

        # Split the questions and answers into training and validating data
        train_questions = question_list[train_valid_split:]
        train_answers = answer_list[train_valid_split:]

        valid_questions = question_list[:train_valid_split]
        valid_answers = answer_list[:train_valid_split]

        print(len(train_questions))
        print(len(valid_questions))

        display_step = 100  # Check training loss after every 100 batches
        stop_early = 0
        stop = 5  # If the validation loss does decrease in 5 consecutive checks, stop training
        validation_check = ((len(train_questions)) // int(properties['batch_size']) // 2) - 1  # Modulus for checking validation loss
        total_train_loss = 0  # Record the training loss for each display step
        summary_valid_loss = []  # Record the validation loss for saving improvements in the model
        learning_rate=float(properties['learning_rate'])
        min_learning_rate=float(properties['min_learning_rate'])
        learning_rate_decay= float(properties['learning_rate_decay'])
        batch_size=int(properties['batch_size'])
        epochs=int(properties['epochs'])
        keep_probability=float(properties['keep_probability'])

        sess = tf.InteractiveSession()
        sess.run(tf.global_variables_initializer())

        for epoch_i in range(1, epochs + 1):
            for batch_i, (questions_batch, answers_batch) in enumerate(self.batch_data(train_questions, train_answers, batch_size)):
                start_time = time.time()
                _, loss = sess.run([self.train_op, self.cost],
                                   {self.input_data: questions_batch,
                                    self.targets: answers_batch,
                                    self.lr: learning_rate,
                                    self.sequence_length: answers_batch.shape[1],
                                    self.keep_prob: keep_probability})

                total_train_loss += loss
                end_time = time.time()
                batch_time = end_time - start_time

                if batch_i % display_step == 0:
                    print('Epoch {:>3}/{} Batch {:>4}/{} - Loss: {:>6.3f}, Seconds: {:>4.2f}'.format(
                        epoch_i,
                        epochs,
                        batch_i,
                        len(train_questions) // batch_size,
                        total_train_loss / display_step,
                        batch_time * display_step))
                    total_train_loss = 0

                if batch_i % validation_check == 0 and batch_i > 0:
                    total_valid_loss = 0
                    start_time = time.time()

                    batched=self.batch_data(valid_questions, valid_answers, batch_size)

                    for batch_ii, (questions_batch, answers_batch) in enumerate(batched):
                        valid_loss = sess.run(
                            self.cost, {self.input_data: questions_batch,
                                   self.targets: answers_batch,
                                   self.lr: learning_rate,
                                   self.sequence_length: answers_batch.shape[1],
                                   self.keep_prob: keep_probability})
                        total_valid_loss += valid_loss
                    end_time = time.time()
                    batch_time = end_time - start_time
                    avg_valid_loss = total_valid_loss / (len(valid_questions) / batch_size)
                    print('Valid Loss: {:>6.3f}, Seconds: {:>5.2f}'.format(avg_valid_loss, batch_time))

                    # Reduce learning rate, but not below its minimum value

                    learning_rate *= learning_rate_decay
                    if learning_rate < min_learning_rate:
                        learning_rate = min_learning_rate

                    summary_valid_loss.append(avg_valid_loss)
                    if avg_valid_loss <= min(summary_valid_loss):
                        print('New Record!')
                        stop_early = 0
                        saver = tf.train.Saver()
                        path = properties['checkpoint']
                        print("checkpoint : ",path)
                        saver.save(sess, path)

                    else:
                        print("No Improvement.")
                        stop_early += 1
                        if stop_early == stop:
                            break

            if stop_early == stop:
                print("Stopping Training.")
                break

    def pad_sentence_batch(self,sentence_batch, vocab_to_int):
        """Pad sentences with <PAD> so that each sentence of a batch has the same length"""
        max_sentence = max([len(sentence) for sentence in sentence_batch])
        return [sentence + [vocab_to_int['<PAD>']] * (max_sentence - len(sentence)) for sentence in sentence_batch]

    def batch_data(self, questions, answers, batch_size):
        """Batch questions and answers together"""
        for batch_i in range(0, len(questions) // batch_size):
            start_i = batch_i * batch_size
            questions_batch = questions[start_i:start_i + batch_size]
            answers_batch = answers[start_i:start_i + batch_size]
            pad_questions_batch = np.array(self.pad_sentence_batch(questions_batch, self.vocab_with_int))
            pad_answers_batch = np.array(self.pad_sentence_batch(answers_batch, self.vocab_with_int))
            yield pad_questions_batch, pad_answers_batch


    def load_and_predict(self, X_test, batch_size):
        self.log.info('Loading data and predicting')
