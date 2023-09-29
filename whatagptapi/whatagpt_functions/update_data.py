import frappe
import requests

@frappe.whitelist()
def update_data(doctype, documentName, params=None):
    header = {
     "Authorization": "token cd44217d68c187d:2c48de9b37526f8"  # Use appropriate token type (Bearer, etc.)
    }
    # Define the URL and parameters
    #params = {
        # "field_name": 'value'
        # "subscription": 'Standard',  # Note that the fields should be a JSON string
        # "limit_page_length": "0"
    #}
    url = f"https://demo.customized.bestoerp.com/api/resource/{doctype}/{documentName}"
    
    # Make the API request
    request = requests.put(url, params=params, headers=header)
    if request.status_code == 200:
        api_request = request.json()
        return api_request,f"Data updated"

    else:
        return f"API request failed with status code {request.status_code}"