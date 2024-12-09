import requests
from bs4 import BeautifulSoup
from flask import Flask, jsonify
from werkzeug.middleware.proxy_fix import ProxyFix


# Sessão para pool de conexões
sessao = requests.Session()
sessao.headers.update({
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
})

# Inicializando o app Flask
app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)


# Rota da API
@app.route('/versiculo', methods=['GET'])
def versiculo():
    try:
        url = "https://dailyverses.net/pt"
        response = sessao.get(url, timeout=10)  # Timeout para evitar travamentos
        response.raise_for_status()  # Levanta exceções para erros HTTP

        soup = BeautifulSoup(response.content, 'html.parser')
        div_b1 = soup.find('div', class_='b1')

        if div_b1:
            texto = div_b1.find('span', class_='v1').get_text(strip=True)
            referencia = div_b1.find('a', class_='vc').get_text(strip=True)
            link = div_b1.find('a', class_='vc')['href']

            return jsonify({
                'texto': texto,
                'referencia': referencia,
                'link': f"https://dailyverses.net{link}"
            })

        return jsonify({'error': 'Conteúdo não encontrado'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Rodando o servidor Flask
if __name__ == '__main__':
    app.run(debug=True)
