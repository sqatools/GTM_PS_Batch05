import json
api_url = "https://api.restful-api.dev/objects"

create_entry_payload =  json.dumps({
      "name": "Apple MacBook Pro 16",
      "data": {
        "year": 2019,
        "price": 1849.99,
        "CPU model": "Intel Core i9",
        "Hard disk size": "1 TB"
      }
    })

json_headers = {
      'Content-Type': 'application/json'
    }

