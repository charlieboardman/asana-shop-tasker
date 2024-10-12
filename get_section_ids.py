import asana
from asana.rest import ApiException
from pprint import pprint

def get_section_ids(token,project_gid):

    configuration = asana.Configuration()
    configuration.access_token = token
    api_client = asana.ApiClient(configuration)

    # create an instance of the API class
    sections_api_instance = asana.SectionsApi(api_client)
    opts = {
        'limit': 50, # int | Results per page. The number of objects to return per page. The value must be between 1 and 100. 
        'opt_fields': "name" # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
    }

    try:
        # Get sections in a project
        api_response = sections_api_instance.get_sections_for_project(project_gid, opts)
        api_response_list = []
        for data in api_response:
            api_response_list.append(data)
    except ApiException as e:
        print("Exception when calling SectionsApi->get_sections_for_project: %s\n" % e)
        return

    return api_response_list