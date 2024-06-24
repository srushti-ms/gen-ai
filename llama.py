from clarifai.client.workflow import Workflow

# Your PAT (Personal Access Token) can be found in the Account's Security section

# Initialize the workflow_url
workflow_url = "https://clarifai.com/bbu01lcjfv0p/llama2Tutorial/workflows/workflow-5f8ab3"
text_classfication_workflow = Workflow(
    url= workflow_url , pat="def9763c0b344cde9b85670645f68ba5"
)
result = text_classfication_workflow.predict_by_bytes(b"I hate you", input_type="text")
print(result.results[0].outputs[0].data)
