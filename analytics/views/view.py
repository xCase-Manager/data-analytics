from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.exceptions import APIException
import json, pandas as pd, numpy as np, tensorflow as tf
import tensorflow_probability as tfp
import tensorflow_transform as tft
import tensorflow_transform.beam as tft_beam
from tensorflow_transform.tf_metadata import dataset_metadata
from tensorflow_transform.tf_metadata import dataset_schema
from .json_encoder import JsonEncoder


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
    
    def _recordsShape(self, orm):
        """
        records shape
        """
        return self._jsonResponse(
            json.dumps(self._getList(orm).shape))
    
    def _recordsSize(self, orm):
        """
        records size
        """
        return self._jsonResponse(
          json.dumps({'size': self._getList(orm).size}, 
          cls=JsonEncoder))

    def _recordsNdim(self, orm):
        """
        records ndim
        """
        return self._jsonResponse(
          json.dumps({'dimension': self._getList(orm).ndim}, 
          cls=JsonEncoder))
    
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

    def _probability(self, orm):
        """
        probability process
        """
        # Load data
        status = self._getList(orm)[['status']]
        dataset = tf.data.Dataset.from_tensor_slices((
          self._getList(orm)[['tags', 'status']],
          status.values))

        data = []
        for i, batch in enumerate(dataset):
            data.append(batch[0])

         # 2) Model creation
        model = tf.keras.models.Sequential()
        model.add(tf.keras.layers.Input(shape=data[0].shape[2:])) 
        model.add(tf.keras.layers.Flatten())
        model.add(tf.keras.layers.Dense(512, activation='elu'))
        model.add(tf.keras.layers.Dense(1, activation='softmax'))

        # 3) Compile and fit
        model.compile(loss='categorical_crossentropy', optimizer='adam')
        model.fit(x=data[0], y=data[1], batch_size=2, epochs=2, shuffle=False)