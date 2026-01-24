""" THIS IS AN AUTOMATICALLY GENERATED FILE!"""
from __future__ import print_function
import json
from engine import primitives
from engine.core import requests
from engine.errors import ResponseParsingException
from engine import dependencies
req_collection = requests.RequestCollection([])
# Endpoint: /_matrix/client/v1/room_summary/{roomIdOrAlias}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("room_summary"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }", examples=["#monkeys:matrix.org"]),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("via="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["matrix.org"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("via="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["elsewhere.ca"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v1/room_summary/{roomIdOrAlias}"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v1/rooms/{roomId}/hierarchy, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("rooms"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["!space:example.org"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("hierarchy"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("suggested_only="),
    primitives.restler_fuzzable_bool("true", examples=["true"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1", examples=["20"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("max_depth="),
    primitives.restler_fuzzable_int("1", examples=["5"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("from="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["next_batch_token"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v1/rooms/{roomId}/hierarchy"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v1/rooms/{roomId}/relations/{eventId}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("rooms"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["!636q39766251:matrix.org"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("relations"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["$asfDuShaf7Gafaw"]),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("from="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["page2_token"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("to="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["page3_token"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1", examples=["20"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("dir="),
    primitives.restler_fuzzable_group("dir", ['b','f']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("recurse="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v1/rooms/{roomId}/relations/{eventId}"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v1/rooms/{roomId}/relations/{eventId}/{relType}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("rooms"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["!636q39766251:matrix.org"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("relations"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["$asfDuShaf7Gafaw"]),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["org.example.my_relation"]),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("from="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["page2_token"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("to="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["page3_token"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1", examples=["20"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("dir="),
    primitives.restler_fuzzable_group("dir", ['b','f']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("recurse="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v1/rooms/{roomId}/relations/{eventId}/{relType}"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v1/rooms/{roomId}/relations/{eventId}/{relType}/{eventType}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("rooms"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["!636q39766251:matrix.org"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("relations"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["$asfDuShaf7Gafaw"]),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["org.example.my_relation"]),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["m.room.message"]),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("from="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["page2_token"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("to="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["page3_token"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1", examples=["20"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("dir="),
    primitives.restler_fuzzable_group("dir", ['b','f']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("recurse="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v1/rooms/{roomId}/relations/{eventId}/{relType}/{eventType}"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v1/rooms/{roomId}/threads, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("rooms"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["!room:example.org"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("threads"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("include="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["all"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1", examples=["20"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("from="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["next_batch_token"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v1/rooms/{roomId}/threads"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v1/rooms/{roomId}/timestamp_to_event, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("rooms"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["!636q39766251:matrix.org"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("timestamp_to_event"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("ts="),
    primitives.restler_fuzzable_int("1", examples=["1432684800000"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("dir="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["f"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v1/rooms/{roomId}/timestamp_to_event"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/createRoom, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("createRoom"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "creation_content":"""),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }", examples=["{\"m.federate\":false}"]),
    primitives.restler_static_string(""",
    "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["The Grand Duke Pub"]),
    primitives.restler_static_string(""",
    "preset":"""),
    primitives.restler_fuzzable_group("preset", ['private_chat','public_chat','trusted_private_chat']  ,quoted=True, examples=["public_chat"]),
    primitives.restler_static_string(""",
    "room_alias_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["thepub"]),
    primitives.restler_static_string(""",
    "topic":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["All about happy hour"]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/createRoom"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/directory/room/{roomAlias}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("directory"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("room"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["#monkeys:matrix.org"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/directory/room/{roomAlias}"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/directory/room/{roomAlias}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("directory"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("room"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["#monkeys:matrix.org"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/directory/room/{roomAlias}"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/directory/room/{roomAlias}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("directory"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("room"),
    primitives.restler_static_string("/"),
    primitives.restler_custom_payload_uuid4_suffix("roomAlias", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "room_id":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["!abnjk1jdasj98:capuchins.com"]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/directory/room/{roomAlias}"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/room_keys/keys, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("room_keys"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("keys"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("version="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["1"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/room_keys/keys"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/room_keys/keys, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("room_keys"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("keys"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("version="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["1"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/room_keys/keys"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/room_keys/keys, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("room_keys"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("keys"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("version="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["1"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "rooms":"""),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }", examples=["{\"!room:example.org\":{\"sessions\":{\"sessionid1\":{\"first_message_index\":1,\"forwarded_count\":0,\"is_verified\":true,\"session_data\":{\"ciphertext\":\"base64+ciphertext+of+JSON+data\",\"ephemeral\":\"base64+ephemeral+key\",\"mac\":\"base64+mac+of+ciphertext\"}}}}}"]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/room_keys/keys"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/room_keys/keys/{roomId}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("room_keys"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("keys"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["!roomid:example.org"]),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("version="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["1"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/room_keys/keys/{roomId}"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/room_keys/keys/{roomId}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("room_keys"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("keys"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["!roomid:example.org"]),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("version="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["1"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/room_keys/keys/{roomId}"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/room_keys/keys/{roomId}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("room_keys"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("keys"),
    primitives.restler_static_string("/"),
    primitives.restler_custom_payload_uuid4_suffix("roomId", quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("version="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["1"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "sessions":"""),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }", examples=["{\"sessionid1\":{\"first_message_index\":1,\"forwarded_count\":0,\"is_verified\":true,\"session_data\":{\"ciphertext\":\"base64+ciphertext+of+JSON+data\",\"ephemeral\":\"base64+ephemeral+key\",\"mac\":\"base64+mac+of+ciphertext\"}}}"]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/room_keys/keys/{roomId}"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/room_keys/keys/{roomId}/{sessionId}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("room_keys"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("keys"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["!roomid:example.org"]),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["sessionid"]),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("version="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["1"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/room_keys/keys/{roomId}/{sessionId}"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/room_keys/keys/{roomId}/{sessionId}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("room_keys"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("keys"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["!roomid:example.org"]),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["sessionid"]),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("version="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["1"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/room_keys/keys/{roomId}/{sessionId}"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/room_keys/keys/{roomId}/{sessionId}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("room_keys"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("keys"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["!roomid:example.org"]),
    primitives.restler_static_string("/"),
    primitives.restler_custom_payload_uuid4_suffix("sessionId", quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("version="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["1"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "first_message_index":"""),
    primitives.restler_fuzzable_int("1", examples=["1"]),
    primitives.restler_static_string(""",
    "forwarded_count":"""),
    primitives.restler_fuzzable_int("1", examples=["0"]),
    primitives.restler_static_string(""",
    "is_verified":"""),
    primitives.restler_fuzzable_bool("true", examples=["false"]),
    primitives.restler_static_string(""",
    "session_data":"""),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }", examples=["{\"ciphertext\":\"base64+ciphertext+of+JSON+data\",\"ephemeral\":\"base64+ephemeral+key\",\"mac\":\"base64+mac+of+ciphertext\"}"]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/room_keys/keys/{roomId}/{sessionId}"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/user/{userId}/rooms/{roomId}/tags/{tag}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["@alice:example.com"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("rooms"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["!726s6s6q:example.com"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("tags"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["u.work"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/user/{userId}/rooms/{roomId}/tags/{tag}"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/user/{userId}/rooms/{roomId}/tags/{tag}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("_matrix"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("client"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["@alice:example.com"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("rooms"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["!726s6s6q:example.com"]),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("tags"),
    primitives.restler_static_string("/"),
    primitives.restler_custom_payload_uuid4_suffix("tag", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "order":"""),
    primitives.restler_fuzzable_number("1.23", examples=["0.25"]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/user/{userId}/rooms/{roomId}/tags/{tag}"
)
req_collection.add_request(request)
