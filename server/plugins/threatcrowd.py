import traceback
import json
import requests

URL_IP = "https://www.threatcrowd.org/searchApi/v2/ip/report/?ip={ip}"
URL_DOMAIN = "https://www.threatcrowd.org/searchApi/v2/domain/report/?domain={domain}"
URL_EMAIL = "https://www.threatcrowd.org/searchApi/v2/email/report/?email={email}"
URL_HASH = "https://www.threatcrowd.org/searchApi/v2/file/report/?resource={hash}"

from server.entities.resource import Resources, ResourceType
from tasks.tasks import celery_app

# Which resources are this plugin able to work with
RESOURCE_TARGET = [ResourceType.DOMAIN, ResourceType.IPv4, ResourceType.EMAIL, ResourceType.HASH]

# Plugin Metadata {a decription, if target is actively reached and name}
PLUGIN_DESCRIPTION = "Allows you to quickly identify related infrastructure and malware"
PLUGIN_IS_ACTIVE = False
PLUGIN_NAME = "threatcrowd"
PLUGIN_AUTOSTART = False
PLUGIN_DISABLE = False


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
                "target": self.resource.get_data()["canonical_name"],
                "resource_id": self.resource.get_id_as_string(),
                "project_id": self.project_id,
                "resource_type": resource_type.value,
                "plugin_name": Plugin.name,
            }
            threatcrowd_task.delay(**to_task)

        except Exception as e:
            tb1 = traceback.TracebackException.from_exception(e)
            print("".join(tb1.format()))


def send_request(url):
    try:
        response = {}
        threatcrowd_response = requests.get(url)
        if not threatcrowd_response.status_code == 200:
            print("Response error!")
            return None
        else:
            response = json.loads(threatcrowd_response.content)
            print(response)
        return response

    except Exception as e:
        tb1 = traceback.TracebackException.from_exception(e)
        print("".join(tb1.format()))
        return None


def threatcrowd_ip(ip):
    url = URL_IP.format(**{"ip": ip})
    send_request(url)


def threatcrowd_domain(domain):
    url = URL_DOMAIN.format(**{"domain": domain})
    send_request(url)


def threatcrowd_email(email):
    url = URL_EMAIL.format(**{"email": email})
    send_request(url)


def threatcrowd_hash(hash):
    url = URL_HASH.format(**{"hash": hash})
    send_request(url)


@celery_app.task
def threatcrowd_task(plugin_name, project_id, resource_id, resource_type, target):
    try:
        resource_type = ResourceType(resource_type)
        if resource_type == ResourceType.IPv4:
            query_result = threatcrowd_ip(target)
        elif resource_type == ResourceType.DOMAIN:
            query_result = threatcrowd_domain(target)
        elif resource_type == ResourceType.EMAIL:
            query_result = threatcrowd_email(target)
        elif resource_type == ResourceType.HASH:
            query_result = threatcrowd_hash(target)
        else:
            print("ThreatCrowd resource type does not found")

        if not query_result:
            return

        # TODO: See if ResourceType.__str__ can be use for serialization
        resource = Resources.get(resource_id, resource_type)
        resource.set_plugin_results(
            plugin_name, project_id, resource_id, resource_type, query_result
        )

    except Exception as e:
        tb1 = traceback.TracebackException.from_exception(e)
        print("".join(tb1.format()))
