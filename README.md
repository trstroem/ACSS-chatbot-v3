# Chat with ACSS

This is a sample flow to ask ACSS for data about SAP on aAzure Virtual Instances.

See <a href="https://platform.openai.com/docs/api-reference/chat/create#chat/create-role" target="_blank">OpenAI Chat</a> for more about message role.
    ```jinja
    # system:
    You are a chatbot having a conversation with a human.

    # user:
    {{question}}
    ```
- how to consume chat history in prompt.
    ```jinja
    {% for item in chat_history %}
    # user:s
    {{item.inputs.question}}
    # assistant:
    {{item.outputs.answer}}
    {% endfor %}
    ```

## Tools used in this flow
- LLM tool
- Python tool
