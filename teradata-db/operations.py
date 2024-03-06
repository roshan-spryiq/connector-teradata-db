""" Copyright start
  Copyright (C) 2024 Fortinet Inc.
  All rights reserved.
  FORTINET CONFIDENTIAL & FORTINET PROPRIETARY SOURCE CODE
  Copyright end """

import requests
from connectors.core.connector import get_logger, ConnectorError
import json
import base64
from os.path import join
logger = get_logger('teradata-db')


class TeraDataDb(object):
    def __init__(self,config):
        self.host_name = config.get('host_name')
        self.system_name = config.get('system_name')
        self.verify_ssl = config.get('verify_ssl')
        self.db_user = config.get('db_user') 
        self.db_password = config.get('db_password') 
        self.jwt_token = config.get('jwt_token') 
        self.base_auth = None  
        self.jwt_auth = None  
        self.select_authentication = config.get('select_authentication')
        if self.select_authentication == "Basic Authentication" and self.db_user is not None and self.db_password is not None:
            self.base_auth = self.generate_basic_auth_header(self.db_user, self.db_password)
        if  self.select_authentication == "JWT Authentication" and self.jwt_token is not None:
            self.jwt_auth = self.jwt_token
       
       
    def generate_basic_auth_header(self, db_user, db_password):
        
        credentials = f"{db_user}:{db_password}"
        credentials_b64 = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')
        return f"Basic {credentials_b64}"

    def make_api_call(self, endpoint=None, method='GET', headers=None, health_check=False, data=None):
        server_url = f'https://{self.host_name}/systems/{self.system_name}'
        if endpoint:    
            url = server_url + endpoint
        else:
            url = server_url
        
        if self.jwt_auth:
            headers = {'Content-Type':'application/json', 'Authorization': self.jwt_auth}
        else:
            headers = {'Content-Type':'application/json', 'Authorization': self.base_auth}
            
            
        
        logger.debug('Final url to make rest call is: {0}'.format(url))

        try:
            logger.debug('Making a request with {0} method and {1} headers.'.format(method, headers))
            response = requests.request(method, url, headers=headers, data=data)
            if response.status_code in [200]:
                if health_check:
                    return response
                try:
                    logger.debug(
                        'Converting the response into JSON format after returning with status code: {0}'.format(
                            response.status_code))
                    response_data = response.json()
                    return {'status': response_data['status'] if 'status' in response_data else 'Success',
                            'data': response_data}
                except Exception as e:
                    response_data = response.content
                    logger.error('Failed with an error: {0}. The response details are: {1}'.format(e, response_data))
                    return {'status': 'Failure', 'data': response_data}
            else:
                logger.error('Failed with response {0}'.format(response))
                raise ConnectorError(
                    {'status': 'Failure', 'status_code': str(response.status_code), 'response': response})
        except Exception as e:
            logger.exception(str(e))
            raise ConnectorError(str(e))


def check_health(config):
    try:
        obj = TeraDataDb(config)
        obj.make_api_call(endpoint='/queries', health_check=True)
        return True
    except Exception as err:
        raise ConnectorError(err)



def get_indicators_for_latest_feed(config, params):
    pass
operations = {
    'get_indicators_for_latest_feed': get_indicators_for_latest_feed
}
