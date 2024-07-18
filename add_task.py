import os
from dotenv import load_dotenv
import asana
from asana.rest import ApiException
from pprint import pprint

sections_gids_dict = {}
with open('asana_sections.csv','r') as f:
    sections_gids = [x.strip('\n') for x in f.readlines()]
    sections_gids = [x.split(',') for x in sections_gids]
    for vehicle in sections_gids:
        name = vehicle[0]
        gid = vehicle[1]
        sections_gids_dict[name] = gid

#due_on is a str in ISO format, 2000-12-31
def add_task(name: str,description: str,due_on: str, token: str, board_id: str, section_name: str):

    section_id = sections_gids_dict[section_name]

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
            "due_on": due_on,
            "section_gid": section_id
        }
    } # dict | The task to create.


    opts = {
        'opt_fields': "gid,name,notes,projects,created_at"
    }

    try:
        # Create a task
        api_response = tasks_api_instance.create_task(body, opts)
        return(api_response)
    except ApiException as e:
        return("Exception when calling TasksApi->create_task: %s\n" % e)