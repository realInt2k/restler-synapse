import requests
import hmac, hashlib 

nonce_url = 'http://localhost:8008/_synapse/admin/v1/register'
response = requests.get(nonce_url)
data = response.json()
nonce = data["nonce"]
print(f"Nonce is : {nonce}")

username = "user1"
password = "123"
shared_secret = b"x1@@2fB#lBJpissU.cn^;JHd-mtaol5*d9HlRzICs+kP1^chE,"

def generate_mac(nonce, user, password, admin=False, user_type=None):

    mac = hmac.new(
      key=shared_secret,
      digestmod=hashlib.sha1,
    )

    mac.update(nonce.encode('utf8'))
    mac.update(b"\x00")
    mac.update(user.encode('utf8'))
    mac.update(b"\x00")
    mac.update(password.encode('utf8'))
    mac.update(b"\x00")
    mac.update(b"admin" if admin else b"notadmin")
    if user_type:
        mac.update(b"\x00")
        mac.update(user_type.encode('utf8'))

    return mac.hexdigest()

mac = generate_mac(nonce, username, password)

payload = {
    "nonce": nonce,
    "username": username,
    "displayname": username,
    "password": password,
    "admin": False,
    "mac": mac
}
reg_url = "http://localhost:8008/_synapse/admin/v1/register"
response = requests.post(reg_url, json=payload)
print(response.json())
