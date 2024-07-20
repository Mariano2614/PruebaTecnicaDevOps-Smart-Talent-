import requests

def check_server_status(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"\nEsta pagina web esta runing: {response.status_code}")
        else:
            print(f"\nEl estado de este servicios esta: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Fallo al conectar con:{url}. Error: {e}")

if __name__ == "__main__":
    server_url = input("Enter the server URL: ")
    check_server_status(server_url)
