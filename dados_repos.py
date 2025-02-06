import requests
import pandas as pd 
from config import api_token

class DataRepos:
    def __init__(self, owner):
        self.owner = owner
        self.api_base_url = 'https://api.github.com'
        self.api_token = api_token
        self.headers = {
                            'Authorization': f'Bearer {self.api_token}',
                            'Accept': 'application/vnd.github.v3+json',
                            'X-GitHub-Api-Version': '2022-11-28'
                        }

    def list_repos(self):
        repos_list = []
        page_num = 1

        while True:
            url_page = f'{self.api_base_url}/users/{self.owner}/repos?page={page_num}'
            response = requests.get(url_page, headers=self.headers)

            if response.status_code != 200:
                print(f'Erro ao buscar repositórios: {response.status_code} - {response.json()}')
                break

            if len(response.json())==0:
                print(page_num)
                break

            repos_list.append(response.json())
            page_num+=1

        return repos_list

    def information_repos(self, repos_list, key):
        repos_inf = []

        for page in repos_list:
            for repo in page:
                repos_inf.append(repo[key])

        return repos_inf
    
    def create_df(self, list1, column_name1, list2, column_name2):
        dataframe = pd.DataFrame()
        dataframe[column_name1] = list1
        dataframe[column_name2] = list2

        return dataframe

    
def main():
    Dados = DataRepos('amzn')
    lista_repos = Dados.list_repos()
    lista_nomes = Dados.information_repos(lista_repos, 'name')
    #print(lista_nomes)
    lista_linguagens = Dados.information_repos(lista_repos, 'language')
    #print(lista_linguagens)
    dataframe = Dados.create_df(lista_nomes, 'Nomes dos repos', lista_linguagens, 'Linguagens')
    print(dataframe)

main()


