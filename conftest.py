import pytest
import yaml
import psycopg2


@pytest.fixture(scope="session")
def connect_to_db_postgre():
    conn = psycopg2.connect(
        database="Everything_Sales",
        user='postgres',
        password='admin',
        host='localhost',
        port='5432'
    )
    yield conn
    conn.close()


#@pytest.fixture(scope="session")
def smoke_tests_queries(config_name):
    with open(config_name, 'r') as stream:
        queries = yaml.safe_load(stream)
    return queries['smoke_tests']


def critical_tests_queries(config_name):
    with open(config_name, 'r') as stream:
        queries = yaml.safe_load(stream)
    return queries['critical_tests']