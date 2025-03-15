import requests
import pandas as pd

class Projeto_api:

    def __init__(self, empresa, owner):
        self._api = 'https://api.github.com'
        self._empresa = empresa
        self._owner = owner
        self._token = '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'
        self._headers = {'Authorization':"Bearer" + self._token,
                        'X-GitHub-Api-Version': '2022-11-28'}
        self._url = Projeto_api.create_url(self)

    def create_url(self):
        url = f'{self._api}/users/{self._owner}/repos'
        print(url)
        return url
        
    def extract_repos(self, n_paginas):
        repos_list = []
        for page_num in range(1,n_paginas+1):
            try:
                url_page = f'{self._url}?page={page_num}'
                response = requests.get(url_page, headers=self._headers)
                repos_list.append(response.json())
            except:
                repos_list.append(None)
        print("Repositório extraido com sucesso")
        return repos_list

    @staticmethod
    def get_repos_language(repositorio):
        list_name = {'Repositorio':[],
                    'Linguagem':[]}
        for page in repositorio:
            for repos in page:
                r = repos['name']
                linguagem = repos['language']
                list_name['Repositorio'].append(r)
                if linguagem == None:
                    list_name['Linguagem'].append('Não Definido no repositório')
                else:
                    list_name['Linguagem'].append(linguagem)
        dados = pd.DataFrame(data=list_name)
        print('Dados separados com sucesso')
        return dados

    def salvar(self, dados):
        try:
            path = f'/home/everton_pc/projeto_Requests/data_processed/dados_{self._empresa}.csv'
            dados.to_csv(path)
            print(f'dados_{self._empresa}.csv salvo com sucesso')
        except:
           print('Dados não salvos')