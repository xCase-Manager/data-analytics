from rest_framework.response import Response
from rest_framework import viewsets
import json, pandas as pd


class View(viewsets.ModelViewSet):
    """
    main view
    """
    def _filter(self, orm, key1, key2):
        """
        filtered by keys
        """
        return self._jsonResponse(self._getList(orm)
            .set_index([key1, key2])
            .count(level=key2)
            .to_json())
    
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