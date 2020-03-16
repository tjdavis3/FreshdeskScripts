
import requests
import json
import time
import urllib
from environs import Env

env = Env()
env.read_env()

API_KEY=env("API_KEY")
DOMAIN=env.str('DOMAIN', 'magna5.freshdesk.com')
PASSWORD=env.str('PASSWORD','x')

BASE_URL = 'https://' + DOMAIN + '/api/v2/'

M5CO = '1234567890'

def search_tickets(m5co):
  response = []
  search_str = urllib.quote("\"cf_m5_account:%s\"" % m5co)
  print BASE_URL + 'search/tickets?query=%s' % search_str
  #r = requests.get(BASE_URL + 'ticket_fields', auth = (API_KEY, PASSWORD ))
  r = requests.get(BASE_URL + 'search/tickets?query=%s' % search_str, auth = (API_KEY, PASSWORD))
  #r = requests.get(BASE_URL + 'tickets', auth = (API_KEY, PASSWORD))

  if r.status_code == 200:
    print "Request processed successfully, the response is given below"
    response =  r.json()
  else:
    print "Failed to read tickets, errors are displayed below,"
    print r.status_code
    response = json.loads(r.content)
    print response["errors"]

    print "x-request-id : " + r.headers['x-request-id']
    print "Status Code : " + str(r.status_code)
  return response


tickets = search_tickets(M5CO)
print tickets
