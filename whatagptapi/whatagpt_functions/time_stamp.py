import frappe
from datetime import datetime

@frappe.whitelist()
def time_stamp():
    # Get the current datetime
    current_datetime = datetime.now()

    # Format the datetime as "DD-MM-YYYY HH:MM:SS"
    formatted_timestamp = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    return formatted_timestamp
    