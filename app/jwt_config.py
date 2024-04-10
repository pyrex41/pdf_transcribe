import os

DS_JWT = {
    "ds_client_id": os.getenv("DOCUSIGN_INTEGRATION"),
    "ds_impersonated_user_id":
    os.getenv("DOCUSIGN_USER_ID"),  # Get this from secrets, DS_INTEGRATION
    "private_key_file":
    "./app/pk2.key",  # Create a new file in your repo source folder named private.key then copy and paste your RSA private key there and save it.
    "authorization_server": "account-d.docusign.com",
}
