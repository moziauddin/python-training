# Install requests in the project interpreter or sudo pip install requests

import requests
import json


auth_url = "http://10.0.0.100/service.php/auth/login"
print(auth_url)
auth_res = requests.get(auth_url, auth=('admin', 'h3r1tag3'))
auth_token = json.loads(auth_res.text)["authToken"]
print(auth_token)
get_url="http://10.0.0.100/service.php/model/ca_loans?pretty=1&authToken="+auth_token
get_res = requests.get(get_url)
print(get_url)
print(get_res.text)


# End-point: fin
# Format: http://localhost/service.php/find/<table_name>?q=<your_query>
# Sample Queries:
# http://localhost/service.php/item/<table_name>/id/<record_id>
# Item: get_url="http://10.0.0.100/service.php/item/ca_objects/id/1?pretty=1&authToken="+auth_token
# get_res = requests.get(get_url)
# get_url="http://10.0.0.100/service.php/find/ca_objects?q=*&pretty=1&authToken="+auth_token
# get_res = requests.get(get_url)
# get_url="http://10.0.0.100/service.php/browse/ca_objects?pretty=1&authToken="+auth_token
# get_res = requests.options(get_url)
# Include Deleted
# curl -XGET 'http://10.0.0.100/service.php/item/ca_entities/id/1?include_deleted=1&pretty=1'
# Edit Format item with id :: Can be used to PUT new items to collective access
# get_url="http://10.0.0.100/service.php/item/ca_objects/id/1?format=edit&pretty=1&authToken="+auth_token
# get_res = requests.get(get_url)
# GET and PUT Example:
# $ curl -XGET 'http://localhost/service.php/item/ca_objects/id/1?pretty=1&format=edit' > edit.json
# // edit object in edit.json
# $ curl -XPUT http://localhost/service.php/item/ca_objects/id/1 -d @new.json