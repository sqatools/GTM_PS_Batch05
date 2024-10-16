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

update_mobile =  json.dumps({
      "name": "Apple MacBook Pro 160",
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

partial_update =  json.dumps({
      "name": "Apple MacBook Pro 18",
    })

json_headers = {
      'Content-Type': 'application/json'
    }

delete_details =  json.dumps({
      "name": "Apple MacBook Pro 18",
      "data": {
        "year": 2024,
        "price": 1849.99,
        "CPU model": "Intel Core i9",
        "Hard disk size": "1 TB"
      }
    })

json_headers = {
      'Content-Type': 'application/json'
    }

