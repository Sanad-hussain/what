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
    "username": "ubuntu",
    "ssh_key": "-----BEGIN RSA PRIVATE KEY-----\nMIIEogIBAAKCAQEAzlFdDyRghLfzYofymPV9SH6Q9zWmVUIvjD1M5HFDuOYKdQFloCNrCTCTjmI8XumCCBgKNqmBKcHngFJZAtdVmQuNoEDfC6MnaA18pfrqFK9FuO8jgfweRHmUSiSEhK0GiSFFpnoXcQeVYktYjYGOu/Sc70Is/Kak2cgvQI0leaSvggfmoAZH4/POC6dISKPRZS7/8ZufW2jdRvsT+S3XaXsp65OwQZrVXClfOmNtdpJPmj+UsEp3zdoi5lhPHym6ECVB/D3MjvqamjB03pHc6l8Ir19OmR+4A3dS1AC+5ehGtJjCH+ErskyCjOYuyjMI7Q28KqcJ91MSII2Cq8nFowIDAQABAoIBAGBtOpcnI00kREZaz5GZutI1BT/k/TZ/1oUu6U8jeMlkCqMg4gR0SURkRbKYSyr46+MoiS1/D3UawT4CPsPLLKB4+9pYN2bS/Envc8CHgvvj5yxF6EyKLwNF5363jpAL5jAVMt5Z1bboGnN0T5DjaniCHQ7d2PTEVevLWfpLfaZZ8QMGuoGu4DfNG/WQ2iZUw2b1VjUsCHUTrz+UIqrrBdhvbN1dKrjBBwL+CwVscVtYq+/XDwc8K2QewpZjC5//82OuNljFeledqJSkwbS/E/k4eVCuIFCzBfE2Kq9FhI0PGRwaHVptTSmuB/iiJJSMDHkGyj+uQFDzlr7gWua962ECgYEA74VUJexGaOVOqSi8tMVuEGF2mCA+7h7YOYXUO214fzvPLfauhnz2XhLm//DpIJ3Ck+4ExBP5+ikh8SYgCyTHp0rXMT8nbfVF2bS+10hjPR6k9Nkd8UNKWgBui09Bv4lmhjS/tQzj5dGU8AFk+JJUzdJ7fnN4JujO+6QCh0QUPKkCgYEA3IM7VlIEsK/NlMq9HLAZvaPqtbmj/NUG80KemDtb4D+MA1adUZGYUM59pVAzr9JtBDsoJylmrxX7wMbou4C68FKn3I+WwMdoGAyQXpKmCOJwjsEMQC0i7CSZL8dW6SQ2JU0n4vaEY457ncn8oUJpD/w0gX5Yho8cM+Kqj0vA82sCgYAeIiL9BmWxSrADvhlHkNMRAoH+D4h7QqwnSHvz4gjX0Pl2qeM5Dj2chjpDltZtgQt6uuYkmPLJEyWvBgHgBQeNN3AtROm7/rCD/CZKRVQe210bZLlMog+XlRhTNGxsIWghmD9KEs4VGrHnI/XFA/vhTQq2VOaX1pA7vl2HEPyOyQKBgGIkRhR1DIFWvTirwt8xwUMV4TBgHww4A4/g5pT6VjnIDpitw/a5xgCw5lrdByQJk1t+uLA1TO4/6nwyCwLomEq9ftg7T+0c0sdhUB/HRP5PSak/YiRt8k0HPOZ24ceBxldzr3zkGqf0ki/35egfloL2zKeVg/DfYL3289Iy9P1hAoGAWl736qgMuTnN6UqHjqUu5mS+j/MAl9XYL6jwK8+nVPkQnv+l2oV12JZPHx+Q3fRJ3pIfvIuVxDRCl3kPs5rOj/yB8Ac9taEp+UOO9M1iu9HEBVq/XccIQx97qg+8PY3wldIgL/X+gydZ4nrhl9dr9J74N6w5yrA0I5/63cJ89bg=\n-----END RSA PRIVATE KEY-----",
    "cmd": "ls",
    "host": "3.111.123.149"
}
        
        # Make the API request
        response = requests.post("https://utilapi.bestoerp.com/run-cmd", json=payload)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the response JSON
            api_response = response.json()
            
            # Extract data from the API response as needed
            # For example, you can access api_response["output"] to get the output of the command
            
            # Return the "title" value along with the API response data
            return {
                "new_site_title": new_site_title,
                "api_response": api_response
            }
        
        # If the request was not successful, handle the error or return an appropriate message
        else:
            return f"API request failed with status code {response.status_code}"
    
    # If data is empty, return an appropriate message or handle it as needed
    return "No data available"

