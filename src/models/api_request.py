import requests

class APIRequest:
    def __init__(self):
        self.url = "https://dadosabertos.ibama.gov.br/dados/RAPP/residuoSolidosGerador/relatorio.json"

    def get_data(self):
        try:
            response = requests.get(self.url, verify=False)
            if response.status_code == 200:
                return response.json()
            else:
                print(f"Erro {response.status_code}: Não foi possível obter dados.")
                return None
        except requests.exceptions.RequestException as e:
            print(f"Erro de requisição: {e}")
            return None
