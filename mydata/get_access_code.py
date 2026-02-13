import requests as req
def acquire_token(data, log):    
    # data is a dictionary containing the json payload specified in the corresponding engine setting (see SettingsFile.md)
    # log is a function that may be used to write logs to a network auth text file that will be saved in the RESTler results directory next to the network logs.

    SYNAPSE = "http://localhost:8008"
    USERNAME = "user1"
    PASSWORD = "123"

    payload = {
        "type": "m.login.password",
        "identifier": {
            "type": "m.id.user",
            "user": USERNAME
        },
        "password": PASSWORD
    }

    r = req.post(
        f"{SYNAPSE}/_matrix/client/v3/login",
        json=payload,
    )
    print(r.json())

    access_tok = r.json()['access_token']
    return access_tok


# headers = {
#    "Authorization": f"Bearer {access_tok}",
#    "Content-Type": "application/json",
# }

# r = requests.get(
#     f"{SYNAPSE}/_matrix/client/v3/admin/whois/@user1:localhost",
#     json=payload,
#     headers=headers
# )

# print(r.json())



#payload = {
#    "creation_content": "{}"
#}

#r = requests.post(
#    f"{SYNAPSE}/_matrix/client/v3/createRoom",
#    headers=headers,
#    json=payload,
#)

#print(r.status_code)
#print(r.json())
