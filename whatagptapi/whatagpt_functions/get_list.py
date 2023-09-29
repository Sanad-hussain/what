import frappe
import requests

@frappe.whitelist()
def get_list(doctype, params=None):
    header = {
     "Authorization": "token cd44217d68c187d:2c48de9b37526f8"  # Use appropriate token type (Bearer, etc.)
    }
    # Define the URL and parameters
    url = f"https://demo.customized.bestoerp.com/api/resource/{doctype}"
    params = {
        "fields": '["*"]',  # Note that the fields should be a JSON string
        "limit_page_length": "0"
    }

    # Make the API request
    request = requests.get(url, params=params, headers=header)

    # Make the API request
    request = requests.get(url, params=params, headers=header)
    
    if request.status_code == 200:
        
        api_request = request.json()
        data = api_request.get("data", [])
        if not data:
            return f"No record exsist"
        else:
            #Extract "name" values into a list
            #names = [item.get("name") for item in data]
            #return names
            return  data

    else:
        return f"API request failed with status code {request.status_code}"