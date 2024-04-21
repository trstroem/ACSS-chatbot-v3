from promptflow import tool
import requests

import json
import time
import random
from concurrent.futures import ThreadPoolExecutor
from functools import partial

from azure.identity import DefaultAzureCredential
from azure.mgmt.workloads import WorkloadsMgmtClient


def decode_str(string):
    return string.encode().decode("unicode-escape").encode("latin1").decode("utf-8")


def get_page_sentence(page, count: int = 10):
    # find all paragraphs
    paragraphs = page.split("\n")
    paragraphs = [p.strip() for p in paragraphs if p.strip()]

    # find all sentence
    sentences = []
    for p in paragraphs:
        sentences += p.split('. ')
    sentences = [s.strip() + '.' for s in sentences if s.strip()]
    # get first `count` number of sentences
    return ' '.join(sentences[:count])


def fetch_info_from_vis(vis: tuple, count: int = 10):
    # Get VIS info
        vis_info =[]

        client = WorkloadsMgmtClient(
            credential=DefaultAzureCredential(),
            subscription_id="2b331373-3d36-4585-bdb9-d3364786e775"
        )

        response = client.sap_virtual_instances.get(
            resource_group_name=vis[1],
            sap_virtual_instance_name=vis[0]
        )
        
        vis = (response.name, response.environment)
        vis_info.append(vis)

@tool
def search_result_from_vis(vis_list: list, count: int = 10):
    results = []
    partial_func_of_fetch_info_from_vis = partial(fetch_info_from_vis, count=count)
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = executor.map(partial_func_of_fetch_info_from_vis, vis_list)
        for feature in futures:
            results.append(feature)
    return results
