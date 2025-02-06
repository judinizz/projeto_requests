from dados_repos import DataRepos


Dados_amzn = DataRepos('amzn')
lista_repos_amzn = Dados_amzn.list_repos()
lista_nomes_amzn = Dados_amzn.information_repos(lista_repos_amzn, 'name')
lista_linguagens_amzn = Dados_amzn.information_repos(lista_repos_amzn, 'language')
dataframe_amzn = Dados_amzn.create_df(lista_nomes_amzn, 'Nome do repositório', lista_linguagens_amzn, 'Linguagens')
dataframe_amzn.to_csv('dados/linguagens_repos_amazon.csv')


Dados_sptf = DataRepos('spotify')
lista_repos_sptf = Dados_sptf.list_repos()
lista_nomes_sptf = Dados_sptf.information_repos(lista_repos_sptf, 'name')
lista_tamanho_sptf = Dados_sptf.information_repos(lista_repos_sptf, 'size')
dataframe_sptf = Dados_sptf.create_df(lista_nomes_sptf, 'Nome do repositório', lista_tamanho_sptf, 'Tamanho em KB')
dataframe_sptf.to_csv('dados/tamanho_repos_spotify.csv')

