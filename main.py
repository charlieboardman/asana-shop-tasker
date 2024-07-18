import os
from dotenv import load_dotenv
import asana
from asana.rest import ApiException
from pprint import pprint

from add_task import add_task

#load the api key with dotenv
load_dotenv()
token = os.getenv('ASANA_API_KEY')
board_id = os.getenv('BOARD_ID')

add_task('test lol', 'test with section','2002-01-12',token,board_id,'blackrunner')