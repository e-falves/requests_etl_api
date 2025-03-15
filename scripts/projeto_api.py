from scripts.classe import Projeto_api

#Dados Amazon
amazon = Projeto_api('amazon', 'amzn')
amazon_repos = amazon.extract_repos(6)
amazon_dados = amazon.get_repos_language(amazon_repos)
amazon.salvar(amazon_dados)

#Dados Netflix
netflix = Projeto_api('netflix', 'netflix')
netflix_repos = netflix.extract_repos(8)
netflix_dados = netflix.get_repos_language(netflix_repos)
netflix.salvar(netflix_dados)

#Dados Spotify
spotify = Projeto_api('spotify', 'spotify')
spotify_repos = spotify.extract_repos(10)
spotify_dados = spotify.get_repos_language(spotify_repos)
spotify.salvar(spotify_dados)