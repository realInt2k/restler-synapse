""" THIS IS AN AUTOMATICALLY GENERATED FILE!"""
from __future__ import print_function
import json
from engine import primitives
from engine.core import requests
from engine.errors import ResponseParsingException
from engine import dependencies
req_collection = requests.RequestCollection([])
# Endpoint: /_matrix/client/v3/rooms/!zoMbfQHLAEshTaknsN%3Alocalhost/send/m.room.message/{stupidMeessage}, method: Put
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
    primitives.restler_static_string("rooms"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("!zoMbfQHLAEshTaknsN%3Alocalhost"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("send"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("m.room.message"),
    primitives.restler_static_string("/"),
    primitives.restler_custom_payload_uuid4_suffix("stupidMeessage", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }", examples=["{\"body\":\"hello\",\"msgtype\":\"m.text\"}"]),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/rooms/!zoMbfQHLAEshTaknsN%3Alocalhost/send/m.room.message/{stupidMeessage}"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/rooms/!zoMbfQHLAEshTaknsN%3Alocalhost/send/m.reaction/{stupidMeessage}, method: Put
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
    primitives.restler_static_string("rooms"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("!zoMbfQHLAEshTaknsN%3Alocalhost"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("send"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("m.reaction"),
    primitives.restler_static_string("/"),
    primitives.restler_custom_payload_uuid4_suffix("stupidMeessage", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8008\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }", examples=["{\"m.relates_to\":{\"rel_type\":\"m.annotation\",\"event_id\":\"$jze-n6g469reZzarAuLF-kQPfgNSMynuDX9otPLe6KI\",\"key\":\"😁\"}}"]),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/rooms/!zoMbfQHLAEshTaknsN%3Alocalhost/send/m.reaction/{stupidMeessage}"
)
req_collection.add_request(request)

# Endpoint: /_matrix/client/v3/rooms/!zoMbfQHLAEshTaknsN%3Alocalhost/redact/{eventId}/{stupidMeessage}, method: Put
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
    primitives.restler_static_string("rooms"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("!zoMbfQHLAEshTaknsN%3Alocalhost"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("redact"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["bai2b1i9:matrix.org"]),
    primitives.restler_static_string("/"),
    primitives.restler_custom_payload_uuid4_suffix("stupidMeessage", quoted=False),
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
    "reason":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["Indecent material"]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/_matrix/client/v3/rooms/!zoMbfQHLAEshTaknsN%3Alocalhost/redact/{eventId}/{stupidMeessage}"
)
req_collection.add_request(request)
