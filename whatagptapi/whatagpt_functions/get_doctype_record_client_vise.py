import frappe
import requests

@frappe.whitelist()
def get_doctype_record_client_vise(doctype, client_id=None):
    header = {
     "Authorization": "token cd44217d68c187d:2c48de9b37526f8"  # Use appropriate token type (Bearer, etc.)
    }
    # Define the URL and parameters
    url = f"https://demo.customized.bestoerp.com/api/resource/{doctype}"
    params = {
        "filters": f'[["client_id", "=", "{client_id}"]]',  # Note that the filter should be a JSON string
        "fields": '["*"]',  # Note that the fields should be a JSON string
        "limit_page_length": "0"
    }

    # Make the API request
    request = requests.get(url, params=params, headers=header)
    
    if request.status_code == 200:
        # Parse the response JSON
        # Extract data from the API response as needed  
        # For example, you can access api_response["output"] to get the output of the command
        # Return the "title" value along with the API response data
        api_request = request.json()
        data = api_request.get("data", [])
        if not data:
            return f"No client exsist"
        else:
            # Extract "name" values into a list
            # names = [item.get("name") for item in data]
            # return names
            return  data

    else:
        return f"API request failed with status code {request.status_code}"