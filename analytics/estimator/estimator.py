import pandas as pd
from analytics.models import Execution


class ExecutionEstimator():
    """
    Execution result estimator
    """
    # load execution data
    _orm_train = Execution.objects.values()
    _orm_eval = Execution.objects.values()

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
            .survived.mean()