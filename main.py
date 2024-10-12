import os
#from dotenv import load_dotenv
import asana
from asana.rest import ApiException
from pprint import pprint

from add_task import add_task
from get_section_ids import get_section_ids

#load the api key with dotenv
#load_dotenv()
#token = os.getenv('ASANA_API_KEY')
#board_id = os.getenv('BOARD_ID')

sections_response = get_section_ids(token,board_id)
sections = [response['name'] for response in sections_response]

#Compare downloaded sections against list of sections
#Remove sections on asana that don't exist on the local list
#Add sections on asana that exist on the local list but not asana

#add_task('test lol', 'test with section','2002-01-12',token,board_id,'blackrunner')