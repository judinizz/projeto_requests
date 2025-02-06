import requests 
import base64
from config import api_token

class ManipulaRepos:
    def __init__(self, username):
        self.username = username
        self.api_base_url = 'https://api.github.com'
        self.api_token = api_token
        self.headers = {
                            'Authorization': f'Bearer {self.api_token}',
                            'Accept': 'application/vnd.github.v3+json',
                            'X-GitHub-Api-Version': '2022-11-28'
                        }
        
    def create_repo(self, name_repo, description, private):
        url = f'{self.api_base_url}/user/repos'
        data = {
        'name': name_repo,
        'description': description,
        'private': private
        }
        response = requests.post(url, json=data, headers=self.headers)
        if response.status_code == 201:
            print(f'Repositorio "{name_repo}" criado com sucesso!')
        else:
            print(f'Erro ao criar repositório "{name_repo}"')

    def add_file(self, name_repo, file_name, message):
        url = f'{self.api_base_url}/repos/{self.username}/{name_repo}/contents/{file_name}'

        with open(file_name, 'rb') as file:
            file_content = file.read()

        encoded_content = base64.b64encode(file_content)

        data = {
            'message': message,
            'content': encoded_content.decode('utf-8')
        }
        response = requests.put(url, json=data, headers=self.headers)
        print(f'Status code do upload de arquivo: {response.status_code}')
        

