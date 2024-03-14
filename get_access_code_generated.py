import webbrowser

APP_KEY = '<APP_KEY>'
url = f'https://www.dropbox.com/oauth2/authorize?client_id={APP_KEY}&' \
      f'response_type=code&token_access_type=offline'

webbrowser.open(url)