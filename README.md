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

2. From Azure ML Studio, select Flows, then Create, then (on the bottom of the screen) select Upload from local. Select the file folder where you downloaded the repository in the previous step. Also remember to select type "chat" for the flow - THIS IS IMPORTANT!

3. Once the flow is imported, select a runtime at the top of the flow builder (selecting "automatic" is fine - this will take 2-3 minutes to spin up).

4. Enter the Azure OpenAI connection and deployment details, followed by the secrets described above (the AOAI connection and deployment should be selectable from dropdown boxes; these are located at the top of the "extract_query_from_question" and "augmented_chat" steps, respectively). For each step, click the "Validate and parse input" button at the bottom of the step in order to allow for entering secrets into the right input variables - you need to have the "runtime" described above up & running for this to work.

5. Now, you can run the flow (use the Chat option to chat with it) - and check the results of the call to ACSS. If everything is configured properly, you should be able to see JSON output with details of your SAP VIS instances.

6. Finally, Deploy your flow to an endpoint by clicking the Deploy button on top of your screen. This process takes a few minutes. When completed, you can select the Endpoints pane on the left of the screen and test the flow in chat mode. Try asking questions like "How many SAP systems do I have", "What are their respective resource groups", or "what are the kernel patch levels for the applications servers". Enjoy!


## Tools used in this flow
- LLM tool
- Python tool
