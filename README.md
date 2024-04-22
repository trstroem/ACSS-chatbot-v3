# Chat with ACSS

This is a sample flow to ask ACSS for data about SAP on Azure Virtual Instances.

## Prerequisites:

You will need an Azure OpenAI instance, with one deployment. The deployment should use the gpt-4 model. You can create this by opening the Azure AI Studio from your Azure portal, then selecting Deployments under the Management menu on the left. Create a new deployment and select the gpt-4 model. Leave other options as is.

You also need an ACSS (Azure Center for SAP Solutions) instance with at least one SAP VIS (virtual instance) registered.

Finally, you will need a Service Principal for interacting with the ACSS instance. This SP must have Reader rights on the subscription where the ACSS instance exists.

Once you have the Azure OpenAI deployment and your Service Principal, you will need to enter some secrets into the flow.dag.yaml file. The placeholders for these secrets are currently marked in brackets - [] - and refer to your Azure tenant ID, subscription, SP ID and secret, as well as the Azure OpenAI deployment name and connection.

## How to deploy

There are several ways to recreate this flow, but the process described below is probably the easiest:
1. Download this repository to your local machine
2. From Azure ML Studio, select Flows, then Create, then (on the bottom of the screen) select Upload from local.
3. In the Azure ML Studio, edit the steps of the flow by entering the Azure OpenAI connection and deployment details, followed by the secrets described above (the AOAI connection and deployment should be selectable from dropdown boxes).

## Tools used in this flow
- LLM tool
- Python tool
