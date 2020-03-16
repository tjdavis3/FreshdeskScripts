
import requests
import json
import time
from environs import Env

env = Env()
env.read_env()

API_KEY=env("API_KEY")
DOMAIN=env.str('DOMAIN', 'magna5.freshdesk.com')
PASSWORD=env.str('PASSWORD','x')
BASE_URL = 'https://' + DOMAIN + '/api/v2/'

def get_companies():
  response = []
  r = requests.get(BASE_URL + "companies?per_page=100", auth = (API_KEY, PASSWORD))

  if r.status_code == 200:
    print "Request processed successfully, the response is given below"
    response =  r.json()
  else:
    print "Failed to read tickets, errors are displayed below,"
    response = json.loads(r.content)
    print response["errors"]

    print "x-request-id : " + r.headers['x-request-id']
    print "Status Code : " + str(r.status_code)
  return response

def del_company(id):
  r = requests.delete(BASE_URL + 'companies/' + str(id), auth = (API_KEY, PASSWORD))
  if r.status_code == 204:
    print "ID %s deleted" % id
  else:
    print "%s: %s" % (id, r.status_code)


while True:
  companies=get_companies()
  if len(companies) == 0:
    break
  for company in companies:
    if company.get('name', '') == 'harvester':  continue
    del_company(company.get('id', ''))
   # time.sleep(1)
    
