import frappe
import requests

@frappe.whitelist()
def get_client_chat_topic(client_id, chat_topic):
    header = {
     "Authorization": "token cd44217d68c187d:2c48de9b37526f8"  # Use appropriate token type (Bearer, etc.)
    }
    # Define the URL and parameters
    url = f"https://demo.customized.bestoerp.com/api/resource/Chat Topic"
    params = {
        "filters": f'[["client_id", "=", "{client_id}"]]',
        "filters": f'[["ID", "=", "{chat_topic}"]]',  # Note that the filter should be a JSON string
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
            # Get the latest response message
            latest_response = None
            for item in data:
                if item.get("message_type") == "Response" and item.get("message"):
                    latest_response = item["message"]
            if latest_response:
                return data
            else:
                return "No response messages found"
    else:
        return f"API request failed with status code {request.status_code}"