import openai
import json
import nearai

hub_url = "https://api.near.ai/v1"
auth = nearai.config.load_config_file()["auth"]
signature = json.dumps(auth)

client = openai.OpenAI(base_url=hub_url, api_key=signature)

models = client.models.list()
print(models)