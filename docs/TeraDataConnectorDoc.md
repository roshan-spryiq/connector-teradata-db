## About the connector
Teradata DB is one of the popular Relational Database Management System. It is mainly suitable for building large scale data warehousing applications. Teradata Query Service is a REST API for Vantage that you can use to run standard SQL statements without managing client-side drivers.
<p>This document provides information about the Teradata DB Connector, which facilitates automated interactions, with a Teradata DB server using FortiSOAR&trade; playbooks. Add the Teradata DB Connector as a step in FortiSOAR&trade; playbooks and perform automated operations with Teradata DB.</p>

### Version information

Connector Version: 1.0.0


Authored By: spryIQ.co

Certified: No
## Installing the connector
<p>From FortiSOAR&trade; 5.0.0 onwards, use the <strong>Connector Store</strong> to install the connector. For the detailed procedure to install a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/installing-a-connector/1/installing-a-connector" target="_top">here</a>.<br>You can also use the following <code>yum</code> command as a root user to install connectors from an SSH session:</p>
`yum install cyops-connector-tearadata-db`

## Prerequisites to configuring the connector
- You must have the URL of Teradata DB server to which you will connect and perform automated operations and credentials to access that server.
- The FortiSOAR&trade; server should have outbound connectivity to port 443 on the Teradata DB server.

## Minimum Permissions Required
- N/A

## Configuring the connector
For the procedure to configure a connector, click [here](https://docs.fortinet.com/document/fortisoar/0.0.0/configuring-a-connector/1/configuring-a-connector)
### Configuration parameters
<p>In FortiSOAR&trade;, on the Connectors page, click the <strong>Teradata DB</strong> connector row (if you are in the <strong>Grid</strong> view on the Connectors page) and in the <strong>Configurations&nbsp;</strong> tab enter the required configuration details:&nbsp;</p>
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Host Name<br></td><td>Host name where Query Service is installed.<br>
<tr><td>Port<br></td><td>Specify port number for the server. By default port is 1443.<br>
<tr><td>Verify SSL<br></td><td>Specifies whether the SSL certificate for the server is to be verified or not. <br/>By default, this option is set as True.<br></td></tr>
<tr><td>Select Authentication<br></td><td>Provide valid credentials to access the target Analytics Database using HTTP Basic or JWT authentication.<br>
<strong>If you choose 'Basic Authentication'</strong><ul><li>DB User : Specify database username.</li><li>DB Password : Specify database password.</li></ul><strong>If you choose 'JWT Authentication'</strong><ul><li>JWT Token: Specify JWT bearer token.</li></ul></td></tr></tbody></table>

## Actions supported by the connector
The following automated operations can be included in playbooks and you can also use the annotations to access operations from FortiSOAR&trade; release 4.10.0 and onwards:
<table border=1><thead><tr><th>Function<br></th><th>Description<br></th><th>Annotation and Category<br></th></tr></thead><tbody><tr><td>Get List Of All Databases<br></td><td>Retrieves a list of all database on a registered system.<br></td><td>get_list_of_all_databases <br/>Investigation<br></td></tr>
<tr><td>Get Specific Database By Name<br></td><td>Retrieves specific database by name on a registered system.<br></td><td>get_specific_database_by_name <br/>Investigation<br></td></tr>
<tr><td>Get List Of All Functions<br></td><td>Retrieves a list of all functions on a registered system.<br></td><td>get_list_of_all_functions <br/>Investigation<br></td></tr>
<tr><td>Get List Of All Macros<br></td><td>Retrieves a list of all macros on a registered system.<br></td><td>get_list_of_all_macros <br/>Investigation<br></td></tr>
<tr><td>Get List Of All Procedures<br></td><td>Retrieves a list of all procedures on a registered system.<br></td><td>get_list_of_all_procedures <br/>Investigation<br></td></tr>
<tr><td>Get List Of All Tables<br></td><td>Retrieves a list of all tables on a registered system.<br></td><td> <br/>Investigation<br></td></tr>
<tr><td>Get Specific Table By Name<br></td><td>Retrieves specific table by name on a registered system.<br></td><td>get_specific_table_by_name <br/>Investigation<br></td></tr>
<tr><td>Get List Of All Views<br></td><td>Retrieves a list of all views on a registered system.<br></td><td>get_list_of_all_views <br/>Investigation<br></td></tr>
<tr><td>Get Specific View By Name<br></td><td>Retrieves specific view by name on a registered system.<br></td><td>get_specific_view_by_name <br/>Investigation<br></td></tr>
<tr><td>Get List Of All Queries<br></td><td>Retrieves a list of all queries on a registered system.<br></td><td>get_list_of_all_queries <br/>Investigation<br></td></tr>
<tr><td>Submit A Query<br></td><td>Submit a query to a registered system.<br></td><td>Submit_a_query <br/>Investigation<br></td></tr>
<tr><td>Get Query By Id<br></td><td>Retrieves specific query by id on a registered system.<br></td><td>get_query_by_id    <br/>Investigation<br></td></tr>
<tr><td>Get Query Results By ID<br></td><td>Retrieves results by id on a registered system.<br></td><td>get_query_results_by_id <br/>Investigation<br></td></tr>
<tr><td>Get List Of All Systems<br></td><td>Retrieves a list of all systems on a registered system.<br></td><td>get_list_of_all_systems    <br/>Investigation<br></td></tr>
</tbody></table>

### operation: Get List Of All Databases
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>System Name<br></td><td>The name of the system for which all databases should be retrieved.<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "db_kind": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "name": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "system": ""
</code><code><br>}</code>

### operation: Get Specific Database By Name
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>System Name<br></td><td>Specify the name of the system for which all databases should be retrieved.<br>
</td></tr><tr><td>Database Name<br></td><td>Specify the name of the database to retrieve.<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "db_kind": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "name": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "system": ""
</code><code><br>}</code>

### operation: Get List Of All Functions
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>System Name<br></td><td>Specify the name of the system on which the database resides.<br>
</td></tr><tr><td>Database Name<br></td><td>Specify the name of the database on the specified system for which all functions should be retrieved.<br>
</td></tr></tbody></table>

#### Output

 No output schema is available at this time.

### operation: Get List Of All Macros
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>System Name<br></td><td>Specify the name of the system on which the database resides.<br>
</td></tr><tr><td>Database Name<br></td><td>Specify the name of the database on the specified system for which all macros should be retrieved.<br>
</td></tr></tbody></table>

#### Output

 No output schema is available at this time.

### operation: Get List Of All Procedures
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>System Name<br></td><td>Specify the name of the system on which the database resides.<br>
</td></tr><tr><td>Database Name<br></td><td>Specify the name of the database on the specified system for which all macros should be retrieved.<br>
</td></tr></tbody></table>

#### Output

 No output schema is available at this time.

### operation: Get List Of All Tables
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>System Name<br></td><td>Specify the name of the system on which the database resides.<br>
</td></tr><tr><td>Database Name<br></td><td>Specify the name of the database to retrieve.<br>
</td></tr></tbody></table>

#### Output

 No output schema is available at this time.

### operation: Get Specific Table By Name
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>System Name<br></td><td>Specify the name of the system on which the database resides.<br>
</td></tr><tr><td>Database Name<br></td><td>Specify the name of the database to retrieve.<br>
</td></tr><tr><td>Table Name<br></td><td>Specify the name of the table to retrieve.<br>
</td></tr></tbody></table>

#### Output

 No output schema is available at this time.

### operation: Get List Of All Views
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>System Name<br></td><td>Specify the name of the system on which the database resides.<br>
</td></tr><tr><td>Database Name<br></td><td>Specify the name of the database to retrieve.<br>
</td></tr></tbody></table>

#### Output

 No output schema is available at this time.

### operation: Get Specific View By Name
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>System Name<br></td><td>Specify the name of the system on which the database resides.<br>
</td></tr><tr><td>Database Name<br></td><td>Specify the name of the database to retrieve.<br>
</td></tr><tr><td>View Name<br></td><td>Specify the name of the view to retrieve.<br>
</td></tr></tbody></table>

#### Output

 No output schema is available at this time.

### operation: Get List Of All Queries
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>System Name<br></td><td>Specify the name of the system on which the database resides.<br>
</td></tr><tr><td>Session<br></td><td>Specify the session number for which all queries should be retrieved.<br>
</td></tr><tr><td>State<br></td><td>Specify a QueryState value that will be used to filter the results.<br>
</td></tr><tr><td>Client ID<br></td><td>Specify a client ID that will be used to filter the results.<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "batch": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "client_id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "params": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "query": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "query_bands": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "app": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    },
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "query_duration": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "query_id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "query_state": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "query_timeout": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "queue_order": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "queue_duration": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "queue_timeout": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "session": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "status_code": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "system": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "user": ""
</code><code><br>}</code>

### operation: Submit A Query
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>System Name<br></td><td>Specify the name of the system on which the database resides.<br>
</td></tr><tr><td>Query Request<br></td><td>Specify the details of the query to submit to the database.<br>
</td></tr></tbody></table>

#### Output

 No output schema is available at this time.

### operation: Get Query By Id
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>System Name<br></td><td>Specify the name of the system on which the database resides.<br>
</td></tr><tr><td>ID<br></td><td>Specify The ID of the query to retrieve.<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "batch": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "client_id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "params": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "query": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "query_bands": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "app": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    },
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "query_duration": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "query_id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "query_state": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "query_timeout": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "queue_order": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "queue_duration": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "queue_timeout": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "session": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "status_code": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "system": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "user": ""
</code><code><br>}</code>

### operation: Get Query Results By ID
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>System Name<br></td><td>Specify the name of the system on which the database resides.<br>
</td></tr><tr><td>ID<br></td><td>Specify The ID of the query to retrieve.<br>
</td></tr><tr><td>Row Offset<br></td><td>Specify the number of rows by which the returned results should be offset.<br>
</td></tr><tr><td>Row Limit<br></td><td>Specify the maximum number of rows that should be present in the returned results<br>
</td></tr></tbody></table>

#### Output

 No output schema is available at this time.

### operation: Get List Of All Systems
#### Input parameters
None.

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "systemType": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "name": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "host": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "logMech": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "encryptData": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "defaultCharSet": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "useXViews": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "maxIdleSeconds": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "defaultTransactionMode": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "defaultDatabase": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "maxImplicitSessionsPerUser": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "maxExplicitSessionsPerUser": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "maxQueuedRequestsPerUser": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "includeUsersInList": ""
</code><code><br>}</code>
## Included playbooks
The `Sample - tearadata-db - 1.0.0` playbook collection comes bundled with the Teradata DB connector. These playbooks contain steps using which you can perform all supported actions. You can see bundled playbooks in the **Automation** > **Playbooks** section in FortiSOAR<sup>TM</sup> after importing the Teradata DB connector.

- Get List Of All Databases
- Get Specific Database By Name
- Get List Of All Functions
- Get List Of All Macros
- Get List Of All Procedures
- Get List Of All Tables
- Get Specific Table By Name
- Get List Of All Views
- Get Specific View By Name
- Get List Of All Queries
- Submit A Query
- Get Query By Id
- Get Query Results By ID
- Get List Of All Systems

**Note**: If you are planning to use any of the sample playbooks in your environment, ensure that you clone those playbooks and move them to a different collection, since the sample playbook collection gets deleted during connector upgrade and delete.
