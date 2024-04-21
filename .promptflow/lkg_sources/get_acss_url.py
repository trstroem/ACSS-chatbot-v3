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

def get_acss_url(tenantId: str, clientId: str, clientSecret: str, subId: str, question: str):

    os.environ['AZURE_CLIENT_ID'] = clientId
    os.environ['AZURE_CLIENT_SECRET'] = clientSecret
    os.environ['AZURE_TENANT_ID'] = tenantId

    rg_list = []

    try:
        # Get list of all VIS from the subscription and extract vital info
        # Then, for all VMs, get additional info
        client = WorkloadsMgmtClient(
            credential=DefaultAzureCredential(),
            subscription_id=subId)

        response = client.sap_virtual_instances.list_by_subscription()

        all_objects = list(response)

        for object in all_objects:

            vis_app_server_list = []

            #vis_info = object.name + ";" + object.environment + ";" + str(object.configuration.infrastructure_configuration)
            vis_id = object.name
            vis_location = object.location
            vis_environment = object.environment
            vis_status = object.status
            vis_health = object.health 

            infra_object = object.configuration.infrastructure_configuration
            vis_rg = infra_object.app_resource_group

            # App
            vis_app_vm_size = infra_object.application_server.virtual_machine_configuration.vm_size
            vis_app_image = infra_object.application_server.virtual_machine_configuration.image_reference.publisher
            vis_app_sku = infra_object.application_server.virtual_machine_configuration.image_reference.sku
            vis_app_instance_count = infra_object.application_server.instance_count

            # - Get additional info about each app server
            response = client.sap_application_server_instances.list(
                resource_group_name=vis_rg,
                sap_virtual_instance_name=object.name,
            )
            for item in response:
                vis_app_server_info = (item.name, item.hostname, item.kernel_version, item.kernel_patch, item.vm_details[0].virtual_machine_id)
                vis_app_server_list.append(vis_app_server_info)

            # DB
            vis_db_vm_size = infra_object.database_server.virtual_machine_configuration.vm_size
            vis_db_image = infra_object.database_server.virtual_machine_configuration.image_reference.publisher
            vis_db_sku = infra_object.database_server.virtual_machine_configuration.image_reference.sku
            vis_db_instance_count = infra_object.database_server.instance_count

            vis_info = (vis_id, vis_rg, vis_location, vis_environment, vis_app_vm_size, vis_app_image, vis_app_sku, vis_app_instance_count, vis_app_server_list, vis_db_vm_size, vis_db_image, vis_db_sku, vis_db_instance_count, vis_status, vis_health)
            rg_list.append(vis_info)

    except Exception as e:
        return ("Get VIS info failed with error: {}".format(e), tenantId, "No available content")

    return rg_list
    