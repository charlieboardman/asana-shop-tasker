import os
from dotenv import load_dotenv
import asana
from asana.rest import ApiException
from pprint import pprint

#load the api key with dotenv
load_dotenv()
token = os.getenv('ASANA_API_KEY')
board_id = os.getenv('BOARD_ID')

#These are task specific and will be filled in by the loop
name = 'Test py task'
description = 'Task from Python'
due_on = '2010-01-01'

configuration = asana.Configuration()
configuration.access_token = token
api_client = asana.ApiClient(configuration)

# create an instance of the API class
tasks_api_instance = asana.TasksApi(api_client)
body = {
    "data": {
        "name": name,
        "projects": board_id,
        "notes": description,
        "due_on": due_on
    }
} # dict | The task to create.


opts = {
    'opt_fields': "gid,name,notes,projects,created_at"
}

try:
    # Create a task
    api_response = tasks_api_instance.create_task(body, opts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->create_task: %s\n" % e)