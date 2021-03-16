import airflow_client
from airflow_client.api import dag_api
from .console import AirflowConsole
from airflow_client.model import *
from airflow_client.rest import ApiException
import os
import sys
from pprint import pprint
import traceback
import logging
import json
from optparse import OptionParser

usage_str = (
    "Usage: airflow-cli command action\n\n"
    "Commands:\n"
    "   dags list : List all the DAGs\n"
)


def get_client():
    # Configure the Host and HTTP basic authorization
    configuration = airflow_client.Configuration(
        host="http://localhost:8080/api/v1",
        username="admin",
        password="admin"
    )

    return airflow_client.ApiClient(configuration)


def main():
    parser = OptionParser(usage=usage_str)
    (options, args) = parser.parse_args()

    if len(args) < 1:
        sys.stderr.write(usage_str)
        sys.exit(0)

    cmd = args.pop(0)

    if cmd == 'dags':
        with get_client() as api_client:
            api_instance = dag_api.DAGApi(api_client)

            try:
                api_response = api_instance.get_dags()
                AirflowConsole().print_as(
                    data=sorted(api_response.dags, key=lambda d: d.dag_id),
                    output='table',
                    mapper=lambda x: {
                        "dag_id": x.dag_id,
                        "filepath": x.fileloc,
                        "owner": x.owners,
                        "paused": x.is_paused,
                    },
                )
            except airflow_client.ApiException as e:
                print(f"Exception when calling DAGApi->get_dags: {e}\\n")


if __name__ == '__main__':
    try:
        sys.exit(main())
    except Exception as e:
        sys.stderr.write(e)
        sys.exit(1)
