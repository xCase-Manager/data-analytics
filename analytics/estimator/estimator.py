import pandas as pd
import tensorflow as tf
from analytics.models import Execution, Executioneval


class ExecutionEstimator():
    """
    Execution result estimator
    """
    # load execution data
    _orm_train = Execution.objects.values()
    _orm_eval = Executioneval.objects.values()

    # get training set
    _y_train = pd.DataFrame(self._orm_train).pop('passed')
    # get evaluation set
    _y_eval = pd.DataFrame(self._orm_eval).pop('passed')   

    def showFeatures(self):
        '''
        features list
        '''
        return self._y_train.head()

    def showStat(self):
        '''
        Statistical data
        '''
        return self._y_train.describe()

    def getTrainingSetNumber(self):
        '''
        Samples number
        '''
        return self._y_train.shape[0]
    
    def getTrainingSetNumber(self):
        '''
        Samples number
        '''
        return self._y_train.shape[0]

    def getTrainingSetNumber(self):
        '''
        Samples number
        '''
        return self._y_eval.shape[0]

    def getMean(self, attributeName):
        """
        get mean of feature attribute
        """
        pd.concat([self._orm_train, self._y_train], axis=1)
            .groupby(attributeName)
            .passed.mean()

    def make_input_fn(data_df, label_df, num_epochs=10, shuffle=True, batch_size=32):
        """
        tf-dataset converting function generation
        """
        def input_function():
            ds = tf.data.Dataset.from_tensor_slices((dict(data_df), label_df))
            if shuffle:
            ds = ds.shuffle(1000)
            ds = ds.batch(batch_size).repeat(num_epochs)
            return ds
        return input_function

    def assertAccuracy(self):
        """
        model accuracy assertion
        """
        CATEGORICAL_COLUMNS = ['status', 'tags', 'job']
        NUMERIC_COLUMNS = ['executionTime', 'start_date']

        feature_columns = []
        for feature_name in CATEGORICAL_COLUMNS:
            vocabulary = self._orm_train[feature_name].unique()
            feature_columns.append(tf.feature_column.categorical_column_with_vocabulary_list(feature_name, vocabulary))

        for feature_name in NUMERIC_COLUMNS:
            feature_columns.append(tf.feature_column.numeric_column(feature_name, dtype=tf.float32))

        # generate tf-dataset converting functions
        train_input_fn = make_input_fn(self._orm_train, self._y_train)
        eval_input_fn = make_input_fn(self._orm_eval, self._y_eval, num_epochs=1, shuffle=False)