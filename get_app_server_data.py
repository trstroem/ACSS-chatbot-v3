from promptflow import tool
from azure.identity import DefaultAzureCredential
from azure.mgmt.subscription import SubscriptionClient
from azure.mgmt.workloads import WorkloadsMgmtClient

#import json
#from bson.json_util import dumps
import os

@tool
# Get all resource groups 
# (here, we could also easily get all subs for a tenant, and go from there)

def get_app_server_data(tenantId: str, clientId: str, clientSecret: str, subId: str, question: str):

    os.environ['AZURE_CLIENT_ID'] = clientId
    os.environ['AZURE_CLIENT_SECRET'] = clientSecret
    os.environ['AZURE_TENANT_ID'] = tenantId

    rg_list = []

    try:
        # Get list of all VIS from the subscription and disentangle the resource groups
        # For now, this is all we do. Further development will add more info.
        client = WorkloadsMgmtClient(
            credential=DefaultAzureCredential(),
            subscription_id=subId)

        #response = client.sap_virtual_instances.list_by_subscription()
        rg_list.append("You asked about app servers!")

    except Exception as e:
        return ("Get VIS info failed with error: {}".format(e), tenantId, "No available content")

    return rg_list
    