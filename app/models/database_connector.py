from elasticsearch import Elasticsearch
import mysql.connector
from . import config
import certifi

class DatabaseConnector:
    def __init__(self, db_type, environment):
        self.db_type = db_type
        self.environment = environment
        self.connection = None

    def connect(self):
        if self.db_type == "elasticsearch":
            self.connect_elasticsearch()
        elif self.db_type == "mysql":
            self.connect_mysql()
        else:
            raise ValueError("Invalid database type. Supported types: elasticsearch, mysql")

    def connect_elasticsearch(self):
        if self.environment == "prod":
            es_url = config.ELASTICSEARCH_PROD_URL
            
        elif self.environment == "dev":
            es_url = config.ELASTICSEARCH_DEV_URL
            
        else:
            raise ValueError("Invalid environment. Supported environments: prod, dev")

        self.connection = Elasticsearch([es_url], ca_certs=certifi.where(), verify_certs=False, timeout=120)

    def connect_mysql(self):
        
        # Extract MySQL connection details from the URL
        if self.environment == "prod":
            prod_url = config.MYSQL_PROD_URL
            credentials = self.split_url(prod_url)
            host = credentials["host"]
            user = credentials["user"]
            password = credentials["password"]
            database = credentials["database"]
            
        elif self.environment == "dev":
            dev_url = config.MYSQL_DEV_URL
            credentials = self.split_url(dev_url)
            host = credentials["host"]
            user = credentials["user"]
            password = credentials["password"]
            database = credentials["database"]
            
        else:
            raise ValueError("Invalid environment. Supported environments: prod, dev")

        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            connection_timeout=120, 
        )

    def split_url(self, url):
        
        url_parts = url.split('://')[1].split('@')
        credentials = url_parts[0].split(':')
        db_host_port = url_parts[1].split('/')[0]
        db_host = db_host_port.split(':')[0]
        db_name = url_parts[1].split('/')[1].split('?')[0]
        db_user = credentials[0]
        db_password = credentials[1]
        db_port = config.MYSQL_PORT
        
        return {
                "host": db_host,
                "user": db_user,
                "password": db_password,
                "database": db_name
            }