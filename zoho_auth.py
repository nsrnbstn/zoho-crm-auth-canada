import requests

# --- Configuration ---
# Generate these in your Zoho Developer Console (https://api-console.zoho.ca)
# DO NOT share your Client Secret on public repositories!
# Nasrin Bastani - Amaranth Marketing Agency
CLIENT_ID = "YOUR_ZOHO_CLIENT_ID"
CLIENT_SECRET = "YOUR_ZOHO_CLIENT_SECRET"
GRANT_TOKEN = "YOUR_ONE_TIME_GRANT_TOKEN"

def get_my_refresh_token():
    """
    Exchanges a one-time Grant Token for a long-lived Refresh Token.
    Note: Using the .ca domain for Zoho Cloud Canada region.
    """
    url = "https://accounts.zohocloud.ca/oauth/v2/token"
    
    data = {
        "code": GRANT_TOKEN,
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "grant_type": "authorization_code"
    }
    
    print("🛰️ Connecting to Zoho Cloud Canada API...")
    try:
        response = requests.post(url, data=data)
        result = response.json()
        
        if "refresh_token" in result:
            print("\n✅ Success! Your Permanent Refresh Token:")
            print("-" * 50)
            print(result["refresh_token"])
            print("-" * 50)
            print("Keep this token secure. You will use it for future API calls.")
        else:
            print("\n❌ Zoho API Error:")
            print(result)
    except Exception as e:
        print(f"❌ System Error: {e}")

if __name__ == "__main__":
    get_my_refresh_token()

