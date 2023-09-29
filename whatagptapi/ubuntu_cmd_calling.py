from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import paramiko
import io
import frappe

app = FastAPI()


# Define a function to run the command on the remote server
@frappe.whitelist()
def run_cmd(username , host, password=None, ssh_key=None, cmdd=None):
    # SSH connection settings
    host = host
    port = 22
    username = username
    

    # Create an SSH client
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # Connect to the client
    if (password is not None):
        client.connect(hostname=host, port=port, username=username, password=password)
    else:
        # Load the private key from the string
        private_key = paramiko.RSAKey.from_private_key(io.StringIO(ssh_key))
        # Connect to the SSH server using the private key
        client.connect(hostname=host, port=port, username=username, pkey=private_key)
    
    # Execute the command
      # Execute the command
    stdin, stdout, stderr = client.exec_command(cmdd)
    # Read the output
    output = stdout.read().decode("utf-8")
    error = stderr.read().decode("utf-8")
    # Close the client connection
    client.close()

    return output

@app.post("/run-cmd")
@frappe.whitelist()
def create_item(username , host, password, ssh_key, cmdd):
    
    # Validate the incoming data
    if (password is None) and (ssh_key is None):
        raise HTTPException(status_code=400, detail="Password or SSH key is required")
    try:
        # Run the command on the remote server
        response = run_cmd(username , host, password, ssh_key, cmdd)
        if response["error"]:
            raise HTTPException(status_code=400, detail=response["error"])
        else:
            return response["output"]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return details

#if "__main__" == "__main__":
#    import uvicorn
#    uvicorn.run(app, host="3.111.123.149", port=8000)
#@frappe.whitelist()
#def get(title=None):

