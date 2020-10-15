from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.exceptions import APIException
import json, pandas as pd, numpy as np, tensorflow as tf
import tensorflow_probability as tfp


class View(viewsets.ModelViewSet):
    """
    main view
    """
    def _filter(self, orm, key1, key2):
        """
        filtered by keys
        """
        try:
            return self._jsonResponse(self._getList(orm)
                .set_index([key1, key2])
                .count(level=key2)
                .to_json())
        except KeyError:
            raise APIException("could not process request")
    
    def _recordsNumber(self, orm):
        """
        records number
        """
        return self._jsonResponse(
            str(self._getList(orm).shape[0]))
    
    def _getList(self, orm):
        """
        list orm entries
        """
        return pd.DataFrame(orm)

    def _jsonResponse(self, payload):
        """
        response formatter
        """
        return Response(json.loads(payload))