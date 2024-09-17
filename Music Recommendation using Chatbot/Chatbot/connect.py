from azureml.core import Workspace
import urllib.request
from azureml.core.model import Model


ws = Workspace(workspace_name='demo_ml_wsp', subscription_id="372e3a20-5e5d-4c31-a597-2c2f8da66c95", resource_group="demo")
print("Completed")
model = Model.register(ws, model_name="chatbot-model", model_path="chatbotmodel.h5")

# "372e3a20-5e5d-4c31-a597-2c2f8da66c95"