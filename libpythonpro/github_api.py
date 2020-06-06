import requests


def buscar_avatar(usuario):
    """
    Buscar el avatar de un usuario en github
    :param usuario: str con el nombre del usuario en GitHub
    :return: str con el link del avatar del usuario
    """
    url = f'https://api.github.com/users/{usuario}'
    resp = requests.get(url)
    return resp.json()['avatar_url']


if __name__ == '__main__':
    print(buscar_avatar('alexandersilvera'))

