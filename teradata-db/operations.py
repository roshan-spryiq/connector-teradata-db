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
        self.server_url = config.get('host_name')
        self.port = config.get('port')
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
            self.jwt_auth = f"Bearer {self.jwt_token}"
            
        if not self.server_url.startswith('https://'):
            self.server_url = 'https://{0}'.format(self.server_url)     
    def generate_basic_auth_header(self, db_user, db_password):
        
        credentials = f"{db_user}:{db_password}"
        credentials_b64 = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')
        return f"Basic {credentials_b64}"

    def make_api_call(self, endpoint=None, method='GET', headers=None, health_check=False, data=None):
        url =  f"{self.server_url}:{self.port}/systems"
        if endpoint:    
            url = url + endpoint
        else:
            url =  url
        
        if self.jwt_auth:
            headers = {'Content-Type':'application/json', 'Authorization': self.jwt_auth}
        else:
            headers = {'Content-Type':'application/json', 'Authorization': self.base_auth}
        logger.debug('Final url to make rest call is: {0}'.format(url))

        try:
            logger.debug('Making a request with {0} method and {1} headers.'.format(method, headers))
            response = requests.request(method, url, headers=headers, data=data, verify=self.verify_ssl)
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


def _check_health(config):
    try:
        obj = TeraDataDb(config)
        obj.make_api_call(health_check=True)
        return True
    except Exception as err:
        raise ConnectorError(err)



def get_list_of_all_databases(config, params):
    obj = TeraDataDb(config)
    system_name = params.get('system_name')
    endpoint = f'/{system_name}/databases'  
    return obj.make_api_call(endpoint=endpoint)

def get_specific_database_by_name(config, params):
    obj = TeraDataDb(config)
    system_name = params.get('system_name')
    database_name = params.get('database_name')
    endpoint = f'/{system_name}/databases/{database_name}'
    return obj.make_api_call(endpoint=endpoint)

def get_list_of_all_functions(config, params):
    obj = TeraDataDb(config)
    system_name = params.get('system_name')
    database_name = params.get('database_name')
    endpoint = f'/{system_name}/databases/{database_name}/functions'
    return obj.make_api_call(endpoint=endpoint)

def get_list_of_all_macros(config, params):
    obj = TeraDataDb(config)
    system_name = params.get('system_name')
    database_name = params.get('database_name')
    endpoint = f'/{system_name}/databases/{database_name}/macros'
    return obj.make_api_call(endpoint=endpoint)
    
def get_list_of_all_procedures(config, params):
    obj = TeraDataDb(config)
    system_name = params.get('system_name')
    database_name = params.get('database_name')
    endpoint = f'/{system_name}/databases/{database_name}/procedures'
    return obj.make_api_call(endpoint=endpoint)  

def get_list_of_all_tables(config, params):
    obj = TeraDataDb(config)
    system_name = params.get('system_name')
    database_name = params.get('database_name')
    endpoint = f'/{system_name}/databases/{database_name}/tables'
    return obj.make_api_call(endpoint=endpoint)

def get_specific_table_by_name(config, params):
    obj = TeraDataDb(config)
    system_name = params.get('system_name')
    database_name = params.get('database_name')
    table_name = params.get('table_name')
    endpoint = f'/{system_name}/databases/{database_name}/tables/{table_name}'
    return obj.make_api_call(endpoint=endpoint)    

def get_list_of_all_views(config, params):
    obj = TeraDataDb(config)
    system_name = params.get('system_name')
    database_name = params.get('database_name')
    endpoint = f'/{system_name}/databases/{database_name}/views'
    return obj.make_api_call(endpoint=endpoint) 

def get_specific_view_by_name(config, params):
    obj = TeraDataDb(config)
    system_name = params.get('system_name')
    database_name = params.get('database_name')
    view_name = params.get('view_name')
    endpoint = f'/{system_name}/databases/{database_name}/views/{view_name}'
    return obj.make_api_call(endpoint=endpoint)    

def get_list_of_all_queries(config, params):
    obj = TeraDataDb(config)
    system_name = params.get('system_name')
    session = params.get('session')
    state = params.get('state')
    clientId = params.get('clientId')
    
    endpoint = f'/{system_name}/queries'
    params = []
    if session:
        params.append(f'session={session}')
    if state:
        params.append(f'state={state}')

    if clientId:
        params.append(f'clientId={clientId}')  
    if params:
        endpoint +='?'+ '&'.join(params)  
    return obj.make_api_call(endpoint=endpoint)   

def submit_a_query(config, params):
    obj = TeraDataDb(config)
    system_name = params.get('system_name')
    query_request = params.get('query_request')
    endpoint =  f'/{system_name}/queries'
    return obj.make_api_call(endpoint=endpoint, method='POST', data=json.dumps(query_request)) 

def get_query_by_id(config, params):
    obj = TeraDataDb(config)
    system_name = params.get('system_name')
    query_id = params.get('id')
    endpoint =  f'/{system_name}/queries/{query_id}'
    return obj.make_api_call(endpoint=endpoint)         

def get_query_results_by_id(config, params):
    obj = TeraDataDb(config)
    system_name = params.get('system_name')
    query_id = params.get('id')
    row_offset = params.get('row_offset')
    row_limit = params.get('row_limit')
    
    endpoint = f'/{system_name}/queries/{query_id}/results'
    params = []
    
    if row_offset:
        params.append(f'rowOffset={row_offset}')
    if row_limit:
        params.append(f'rowLimit={row_limit}')

    if params:
        endpoint +='?'+ '&'.join(params)  
    return obj.make_api_call(endpoint=endpoint)   

def get_list_of_all_systems(config, params):
    obj = TeraDataDb(config)
    return obj.make_api_call()    

operations = {
    'get_list_of_all_databases': get_list_of_all_databases,
    'get_specific_database_by_name': get_specific_database_by_name,
    'get_list_of_all_functions': get_list_of_all_functions,
    'get_list_of_all_macros': get_list_of_all_macros,
    'get_list_of_all_procedures': get_list_of_all_procedures,
    'get_list_of_all_tables': get_list_of_all_tables,
    'get_specific_table_by_name': get_specific_table_by_name,
    'get_list_of_all_views': get_list_of_all_views,
    'get_specific_view_by_name': get_specific_view_by_name,
    'get_list_of_all_queries':get_list_of_all_queries,
    'submit_a_query': submit_a_query,
    'get_query_by_id': get_query_by_id,
    'get_query_results_by_id': get_query_results_by_id,
    'get_list_of_all_systems': get_list_of_all_systems
    
}
