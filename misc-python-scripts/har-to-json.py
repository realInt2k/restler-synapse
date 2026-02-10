#!/usr/bin/env python3
"""
Grok
HAR to pretty Matrix sync log converter

1. Reads a HAR file
2. Creates { "timestamp": {request/response info} } structure
3. Recursively parses any string in response.body that is valid JSON
4. Writes prettified result to output file

"""

import json
import sys
from datetime import datetime


def is_likely_json_string(s: str) -> bool:
    s = s.strip()
    return len(s) > 1 and ((s.startswith('{') and s.endswith('}')) or
                           (s.startswith('[') and s.endswith(']')))


def deep_parse_json(value):
    if isinstance(value, str) and is_likely_json_string(value):
        try:
            parsed = json.loads(value)
            # Recurse into the parsed structure
            if isinstance(parsed, dict):
                return {k: deep_parse_json(v) for k, v in parsed.items()}
            elif isinstance(parsed, list):
                return [deep_parse_json(item) for item in parsed]
            return parsed
        except (json.JSONDecodeError, TypeError, ValueError):
            pass  # not valid JSON → keep as string
    elif isinstance(value, dict):
        return {k: deep_parse_json(v) for k, v in value.items()}
    elif isinstance(value, list):
        return [deep_parse_json(item) for item in value]
    
    return value


def har_to_timestamped_dict(har_data):
    result = {}
    
    for entry in har_data.get("log", {}).get("entries", []):
        ts = entry.get("startedDateTime")
        if not ts:
            continue  
            
        # Basic request info
        req = entry.get("request", {})
        resp = entry.get("response", {})
        
        url = req.get("url") #string
        if "_matrix/client/v3/sync" in url:
            continue
        
        item = {
            "method": req.get("method"),
            "url": url,
            # "headers": [
            #     {"name": h["name"], "value": h["value"]}
            #     for h in req.get("headers", [])
            # ],
            "payload": None,
            "response": {
                "status": resp.get("status"),
                "statusText": resp.get("statusText"),
                # "headers": [
                #     {"name": h["name"], "value": h["value"]}
                #     for h in resp.get("headers", [])
                # ],
                "body": None
            },
            # "timings": entry.get("timings", {})
        }
        
        # POST/PUT payload
        post_data = req.get("postData")
        if post_data:
            if "text" in post_data:
                item["payload"] = post_data["text"]
            elif "params" in post_data:
                item["payload"] = post_data["params"]
        
        # Response body (string at first)
        content = resp.get("content", {})
        if "text" in content and content["text"]:
            item["response"]["body"] = content["text"]
        elif "size" in content and content["size"] == 0:
            item["response"]["body"] = None
        
        result[ts] = item
    
    return result


def main():
    if len(sys.argv) != 3:
        print(__doc__.strip())
        print("\nError: Need exactly two arguments")
        print("   python this_script.py  input.har  output.json")
        sys.exit(1)
    
    input_path = sys.argv[1]
    output_path = sys.argv[2]
    
    try:
        with open(input_path, encoding="utf-8") as f:
            har = json.load(f)
    except Exception as e:
        print(f"Error reading HAR file: {e}")
        sys.exit(2)
    
    print(f"Processing {len(har.get('log', {}).get('entries', []))} entries...")
    
    timestamped = har_to_timestamped_dict(har)
    
    print(f"Extracted {len(timestamped)} requests. Parsing JSON bodies...")
    
    # Recursively beautify any JSON strings in bodies
    for ts, entry in timestamped.items():
        if "response" in entry and "body" in entry["response"]:
            entry["response"]["body"] = deep_parse_json(
                entry["response"]["body"]
            )
        if "payload" in entry:
            entry["payload"] = deep_parse_json(entry["payload"])
    
    # Sort by timestamp (optional but nicer)
    sorted_result = dict(sorted(
        timestamped.items(),
        key=lambda x: datetime.fromisoformat(x[0].replace("Z", "+00:00"))
    ))
    
    try:
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(sorted_result, f, indent=2, ensure_ascii=False)
        print(f"\nDone! Written prettified result to:")
        print(f"  → {output_path}")
        print(f"    ({len(sorted_result)} entries)")
    except Exception as e:
        print(f"Error writing output: {e}")
        sys.exit(3)


if __name__ == "__main__":
    main()
