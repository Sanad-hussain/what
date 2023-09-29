import frappe
import requests  # Import the requests library # pip install requests

@frappe.whitelist()
def run_cmdd(title=None):
    # Fetch data from the API
    data = frappe.db.sql(f"""select * from `tabapi`;""", as_dict=True)
    
    # Check if data is not empty
    if data:
        # Get the last element (dictionary) from the list
        last_element = data[1]
        
        # Extract the "title" field from the last element
        new_site_title = last_element.get("title")
        cmd = f"./create_site.sh {new_site_title} BestoERP@999"
        # Define the payload for the external API
        payload = {
  "client_id": "your_client_id",
  "time_stamp": "2023-09-22 00:21:28",
  "message_type": "Response",
  "mesaage": "api"
}

        header = {
           "Authorization": "token cd44217d68c187d:2c48de9b37526f8"  # Use appropriate token type (Bearer, etc.)
       }
        
        # Make the API request
        response = requests.post("https://demo.customized.bestoerp.com/api/resource/Chat History", json=payload, headers=header)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the response JSON
            api_response = response.json()
            
            # Extract data from the API response as needed
            
            # For example, you can access api_response["output"] to get the output of the command
            
            # Return the "title" value along with the API response data
            return {
                "new_site_title": new_site_title,
                "api_response": api_response["data"]["name"],
            }
        
        # If the request was not successful, handle the error or return an appropriate message
        else:
            return f"API request failed with status code {response.status_code}"
    
    # If data is empty, return an appropriate message or handle it as needed
    return "No data available"

