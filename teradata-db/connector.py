""" Copyright start
  Copyright (C) 2024 Fortinet Inc.
  All rights reserved.
  FORTINET CONFIDENTIAL & FORTINET PROPRIETARY SOURCE CODE
  Copyright end """

from connectors.core.connector import Connector, get_logger, ConnectorError
from .operations import _check_health, operations
logger = get_logger('teradata-db')


class TeraDataDb(Connector):

    def execute(self, config, operation, params, **kwargs):
        try:
            action = operations.get(operation)
            result = action(config, params)
            return result
        except Exception as err:
            logger.error(str(err))
            raise ConnectorError(str(err))

    def check_health(self, config):
        return _check_health(config)