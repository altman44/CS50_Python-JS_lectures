import requests, json

def main():
    error = input("First param: ") # enter 'error' 
    code = input("Second param: ") # enter 'code' or 'info'
    res = requests.get("https://data.fixer.io/api/latest?access_key=465532", params={"error": error, "code": code})
    if res.status_code != 200:
        raise Exception('ERROR: API request unsuccessful.')
    data = res.json()
    if data[error][code]:
        rate = data[error][code]
        print(f"jsonResponse.{error}.{code}: {rate}")
    else:
        print('Failed')

if __name__ == "__main__":
    main()