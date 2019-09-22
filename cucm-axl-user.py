from zeep import Client
from zeep.cache import SqliteCache
from zeep.transports import Transport
from zeep.exceptions import Fault
from zeep.plugins import HistoryPlugin
from zeep.helpers import serialize_object
from requests import Session
from requests.auth import HTTPBasicAuth
from urllib3 import disable_warnings
from urllib3.exceptions import InsecureRequestWarning
from lxml import etree

disable_warnings(InsecureRequestWarning)

print()
username = input('CUCM username: ')
password = getpass.getpass('CUCM password: ')
host = '<your CUCM pub FQDN>'

wsdl = 'file://C:/Users/<path to your>/AXL/12.5/axlsqltoolkit/schema/12.5/AXLAPI.wsdl'
location = 'https://{host}:8443/axl/'.format(host=host)
binding = "{http://www.cisco.com/AXLAPIService/}AXLAPIBinding"

session = Session()
session.verify = False
session.auth = HTTPBasicAuth(username, password)

transport = Transport(cache=SqliteCache(), session=session, timeout=20)
history = HistoryPlugin()
client = Client(wsdl=wsdl, transport=transport, plugins=[history])
service = client.create_service(binding, location)

def show_history():
    for item in [history.last_sent, history.last_received]:
        print(etree.tostring(item["envelope"], encoding="unicode", pretty_print=True))

try:
    resp = service.executeSQLQuery('select userid, firstname, lastname,fkdirectorypluginconfig from enduser where fkdirectorypluginconfig is Null order by userid')
    #print(resp)
    cucm_user_list = resp['return'].row
    for row in cucm_user_list:
        print(row[0].text,row[1].text,row[2].text)
except Fault:
    show_history()
