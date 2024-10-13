import os
from dotenv import load_dotenv
from modules import helpers

load_dotenv()

auth = os.environ["AUTH"]
tsg = os.environ["TSG_ID"]

login = helpers.Authentication()
token = login.getToken(auth, tsg)

blacklist_group_id = "7991b7fb-da47-4708-9c63-3f42e51e62b9"

address = input("What is the /32 IP you want to block? Eg: 1.2.3.4 :")
address_name = helpers.createAddress(address, token)
helpers.updateAddressGroup(address_name, blacklist_group_id, token)
