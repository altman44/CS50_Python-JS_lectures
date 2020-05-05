import requests

def main():
    res = requests.get("https://data.fixer.io/api/latest?access_key=465532")
    print(res.status_code)
    if res.status_code != 200:
        raise Exception("ERROR: API request unsuccessful.")
    data = res.json()
    print(data)

if __name__ == "__main__":
    main()