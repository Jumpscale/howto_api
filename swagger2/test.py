from js9 import j

from bravado.requests_client import RequestsClient
from bravado.client import SwaggerClient

http_client = RequestsClient()

# http_client.set_api_key("my.zerotier.com", api_key="", param_name='api_key', param_in='query')
http_client.session.headers["Authorization"] = "bearer MQMmvJEGWfAccGYQ93UMjxn5vMSu4q2m"

# dd = j.data.serializer.json.load("zerotier_swagger.json")
dd = j.data.serializer.json.load("zerotier_1file.json")
cl = SwaggerClient.from_spec(dd, http_client=http_client)

from IPython import embed
embed(colors='Linux')
