import frappe
import requests

# Define the global header variable
header = {
    "Authorization": "token cd44217d68c187d:2c48de9b37526f8"
}

@frappe.whitelist()
def save_data(doctype, payload_request):
    global header
    # Make the API request
    request = requests.post("https://demo.customized.bestoerp.com/api/resource/"+doctype, json=payload_request, headers=header)
    if request.status_code == 200:
      # Parse the response JSON
      # Extract data from the API response as needed  
      # For example, you can access api_response["output"] to get the output of the command
      # Return the "title" value along with the API response data
      api_request = request.json()

      return  api_request.get("data", {}).get("name")

    else:
        return f"API request failed with status code {request.status_code}"
    
@frappe.whitelist()
def save_chat(doctype, payload_request, payload_response):

    # calling save_data function to save data
    request = save_data(doctype, payload_request)
    response = save_data(doctype, payload_response)
    if request== "1" and response == "1":

      return f"1"
    else:
      return request