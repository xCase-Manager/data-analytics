import pandas as pd
from analytics.models import Job, Execution


class ExecutionEstimator():
    """
    Execution result estimator
    """
    # load execution data
    orm_train = Execution.objects.values()
    orm_eval = Execution.objects.values()

    # get training set
    _y_train = pd.DataFrame(orm).pop('passed')
    # get evaluation set
    _y_eval = pd.DataFrame(orm).pop('passed')   

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