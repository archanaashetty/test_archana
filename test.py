import json
with open('/Users/archana.shetty/bundle-examples/knowledge_base/dashboard_nyc_taxi/db_get.json','r') as file:
    data=json.load(file)

serialized_json=data['serialized_dashboard']
print(serialized_json)