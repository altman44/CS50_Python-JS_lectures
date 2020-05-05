import requests

def main():
    res = requests.get("https://data.fixer.io/api/latest?access_key=465532")
    if res.status_code != 200:
        raise Exception("ERROR: API request unsuccessful.")
    
    data = res.json()
    success = data['success']
    rate = data['error']['code']
    print(f"Success: {success}")
    print(f"Error code received: {rate}")

if __name__ == "__main__":
    main()