import requests
from infraestructure.exceptions import ApiError
from domain.interfaces.Ievent import IEvent
class Event_Service:
    def get(self):
        path=f"https://eonet.gsfc.nasa.gov/api/v2.1/events"
        r = requests.get(path, headers={})
        if r.status_code == 200:
            item_result = []
            data_api = r.json()
            events = data_api['events']
            for item in events:
                item_event =IEvent(id= item['id'],
                    title = item['title'],
                    description = item['description'],
                    categories = ",".join([i['title'] for i in item['categories']]),
                    sources = ",".join([i['url'] for i in item['sources']]))
                print(item_event)
                item_result.append(item_event.__dict__)
            return item_result
        else:
            raise ApiError(message="Eternal API Not Response",code=r.status_code)