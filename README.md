# Chat with ACSS

This is a sample flow to ask ACSS for data about SAP on Azure Virtual Instances.

## Prerequisites:

You will need an Azure OpenAI instance, with one deployment. The deployment should use the gpt-4 model (although gpt-35 should also work. I haven't tried). You can create this by opening the Azure AI Studio from your Azure portal, then selecting Deployments under the Management menu on the left. Create a new deployment and select the gpt-4 (or 3.5 if that's what you have available) model. Leave other options "as-is".

You also need an ACSS (Azure Center for SAP Solutions) instance with at least one SAP VIS (virtual instance) registered. This does not need to be in the same subscription - or even tenant - as your ML deployment. See next paragraph.

Finally, you will need a Service Principal for interacting with the ACSS instance. This SP must have Reader rights on the subscription (or tenant) where the ACSS instance resides.

With all of this done, you should be ready to deploy the flow in Azure ML Studio. See next section.

## How to deploy

There are several ways to recreate this flow, but the process described below is probably the easiest:
1. Download this repository to your local machine - if you download as zip, make sure to unzip the file to a local folder before the next step below.

2. From Azure ML Studio, select Flows, then Create, then (on the bottom of the screen) select Upload from local. Select the file folder where you downloaded the repository in the previous step. Make sure the folder has no sub-folders; all files (like the "flow.dag.yaml") must be present in the folder you refer to. IMPORTANT: Also remember to select type "chat" for the flow! (If you forget this, and create a flow as type Standard, the chat function won't work).

![Upload](/images/upload.png?raw=true "Uploading from a local folder")


3. Once the flow is imported, select a "runtime" at the top of the flow builder (selecting "automatic" is fine - this will take 2-3 minutes to spin up).

![Runtime](/images/runtime.png?raw=true "Flow runtime selector")


4. Now, edit the steps as follows: Enter the Azure OpenAI connection and deployment details, followed by the SP ID, secret, tenant ID and subscription ID mentioned above (the AOAI connection and deployment should be selectable from dropdown boxes; these are located at the top of the "extract_query_from_question" and "augmented_chat" steps, respectively). For each step, start by clicking the big blue "Validate and parse input" button located at the bottom of the step in order to allow for entering secrets into the right input variables - you need to have the "runtime" described above up & running for this to work. Save the flow when done.

![Connection](/images/connection.png?raw=true "Connection details")

![Inputs](/images/inputs.png?raw=true "Validation and Input section")


5. Now, you can run the flow (use the Chat option to chat with it) - and check the results of the call to ACSS. If everything is configured properly, you should be able to see JSON output with details of your SAP VIS instances. The Chat functionality should also allow you to ask questions related to your ACSS implementation; note that when testing this from the flow builder, it will take some seconds for each reply to arrive.

![Outputs](/images/outputs.png?raw=true "Output section")


6. Finally, Deploy your flow to an endpoint by clicking the Deploy button on top of your screen. This process takes a few minutes. When completed, you can click on the Endpoints pane on the left of the screen and test the flow in chat mode. Try asking questions like "How many SAP systems do I have", "What are their respective resource groups", or "what are the kernel patch levels for the applications servers". Enjoy!

7. From here, you should be able to consume the endpoint from any front-end you like. Build a new App or integrate the endpoint into an existing one of your preference!


## Tools used in this flow
- LLM tool
- Python tool
