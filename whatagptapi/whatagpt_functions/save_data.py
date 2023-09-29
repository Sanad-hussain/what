import frappe
import requests
from ..whatagpt_functions.time_stamp import time_stamp

# Define the global header variable
header = {
    "Authorization": "token cd44217d68c187d:2c48de9b37526f8"
}

@frappe.whitelist()
def save_data():
    doctype = "Chat Topic"
    payload_request = {
           "topic_name": "chat_topic12311",
            "system_content":"system_content",
            "created_on":time_stamp(),
            "client_id":"307d3347-32b8-4025-aa45-6943a4e46e62"
        }
    global header
    # Make the API request
    request = requests.post("https://demo.customized.bestoerp.com/api/resource/"+doctype, json=payload_request, headers=header)
    if request.status_code == 200:
      # Parse the response JSON
      # Extract data from the API response as needed  
      # For example, you can access api_response["output"] to get the output of the command
      # Return the "title" value along with the API response data
      api_request = request.json()
      name_value = api_request.get("data", {}).get("name")

      if name_value:
        return name_value
      else:
            return "No 'name' value found in the response."

    else:
        return f"API request failed with status code {request.status_code}"