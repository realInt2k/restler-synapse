import requests
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

    r = requests.post(
        f"{SYNAPSE}/_matrix/client/v3/login",
        json=payload,
    )
    print(r.json())

    access_tok = r.json()['access_token']
    return access_tok
