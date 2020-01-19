import json
import traceback
import json
import urllib.request

from tasks.api_keys import KeyRing
from server.entities.resource import Resources, ResourceType
from tasks.tasks import celery_app

# Which resources are this plugin able to work with
RESOURCE_TARGET = [ResourceType.IPv4]

# Plugin Metadata {a decription, if target is actively reached and name}
PLUGIN_DESCRIPTION = "Use a GeoIP service to geolocate an IP address"
PLUGIN_IS_ACTIVE = False
PLUGIN_NAME = "geoip"
PLUGIN_AUTOSTART = True
PLUGIN_DISABLE = False

API_KEY = KeyRing().get("ipstack")

class Plugin:
    description = PLUGIN_DESCRIPTION
    is_active = PLUGIN_IS_ACTIVE
    name = PLUGIN_NAME
    autostart = PLUGIN_AUTOSTART

    def __init__(self, resource, project_id):
        self.project_id = project_id
        self.resource = resource

    def do(self):
        resource_type = self.resource.get_type()

        try:
            to_task = {
                "ip": self.resource.get_data()["address"],
                "resource_id": self.resource.get_id_as_string(),
                "project_id": self.project_id,
                "resource_type": resource_type.value,
                "plugin_name": Plugin.name,
            }
            geoip_task.delay(**to_task)

        except Exception as e:
            tb1 = traceback.TracebackException.from_exception(e)
            print("".join(tb1.format()))

def geoip(ip):
    try:
        URL = f"http://api.ipstack.com/{ip}?access_key={API_KEY}&format=1"
        response = urllib.request.urlopen(URL).read()
        return json.loads(response)

    except Exception as e:
        tb1 = traceback.TracebackException.from_exception(e)
        print("".join(tb1.format()))
        return None

@celery_app.task
def geoip_task(plugin_name, project_id, resource_id, resource_type, ip):
    try:
        query_result = geoip(ip)
        if not query_result:
            return

        # TODO: See if ResourceType.__str__ can be use for serialization
        resource_type = ResourceType(resource_type)
        resource = Resources.get(resource_id, resource_type)
        resource.set_plugin_results(
            plugin_name, project_id, resource_id, resource_type, query_result
        )

    except Exception as e:
        tb1 = traceback.TracebackException.from_exception(e)
        print("".join(tb1.format()))
