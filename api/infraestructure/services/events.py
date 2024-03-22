import requests
from infraestructure.exceptions import ApiError
from domain.interfaces.Ievent import IEvent
from infraestructure.db_service import DB_Services
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
    
    def post(self):
        items = self.get()
        for i in items:
            print(i['id'])
            item_event =IEvent(
                id= i['id'],
                title = i['title'],
                description = i['description'],
                categories = i['categories'],
                sources =  i['sources']
                )
            #i = items[0]
            try:
                result = DB_Services.send_request(f"INSERT INTO events (api_id, title, description, categories, sources) VALUES ('{i['id']}', '{i['title']}', '{i['description']}', '{i['categories']}', '{i['sources']}')", commit=True)
                print("RESLT ::: ",result)
            except Exception as e:
                print(str(e))
        return True
    
    def single_get(self,id):
        result  = None
        try:
            result = DB_Services.send_request(f"SELECT * FROM events WHERE id='{id}'")
            
            result = result[0]
            print("RESLT ::: ",result," - ",str(type(result)))
        except Exception as e:
            print(str(e))
        return result
