import os
import re
import json
import sys
import urllib.request
from datetime import datetime

def parse_iso_time(iso_str):
    # Handles 2023-10-05T14:48:00Z format
    return datetime.strptime(iso_str.replace('Z', '+0000'), "%Y-%m-%dT%H:%M:%S%z").timestamp()

def main():
    comment_body = os.environ.get('COMMENT_BODY', '')
    pr_created_at_iso = os.environ.get('PR_CREATED_AT', '')
    
    print(f"Processing comment: {comment_body[:50]}...")
    
    # Extract URL
    url_pattern = r"https:\/\/replay.pokemonshowdown.com\/([\w-]+)"
    match = re.search(url_pattern, comment_body)
    
    if not match:
        print("No Pokemon Showdown replay URL found.")
        sys.exit(1) # Not an error, just no URL, so we don't do anything

    replay_id = match.group(1)
    json_url = f"https://replay.pokemonshowdown.com/{replay_id}.json"
    
    print(f"Fetching replay data from: {json_url}")
    
    try:
        with urllib.request.urlopen(json_url) as response:
            data = json.loads(response.read().decode())
    except Exception as e:
        print(f"Error fetching replay: {e}")
        sys.exit(1)

    # Check timestamps
    upload_time = data.get('uploadtime')
    if not upload_time:
        print("Invalid replay data: no uploadtime.")
        sys.exit(1)

    if pr_created_at_iso:
        pr_ts = parse_iso_time(pr_created_at_iso)
        if upload_time < pr_ts:
            print(f"Replay is too old! Played at {upload_time}, PR created at {pr_ts}")
            with open(os.environ['GITHUB_OUTPUT'], 'a') as fh:
                fh.write(f"failure_reason=Old replay from {datetime.fromtimestamp(upload_time)}\n")
            sys.exit(1)

    # Check for winner
    winner = data.get('winner')
    if not winner:
        log = data.get('log', '')
        if '|win|' not in log:
            print("No winner found in replay.")
            sys.exit(1)
        print("Winner found in log.")
    else:
        print(f"Winner: {winner}")

    print("Verification successful!")
    with open(os.environ['GITHUB_OUTPUT'], 'a') as fh:
        fh.write("verified=true\n")
        fh.write(f"winner={winner}\n")

if __name__ == "__main__":
    main()
