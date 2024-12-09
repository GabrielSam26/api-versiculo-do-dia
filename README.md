# 📖 API Versículo do Dia

Uma API simples desenvolvida em **Python** para obter o **versículo do dia** do site [DailyVerses.net](https://dailyverses.net/pt).  
Utiliza **Flask**, **Requests** e **BeautifulSoup4** para fazer a raspagem de dados e retornar o resultado em formato **JSON**.

![Retorno json api:](https://i.imgur.com/wpwHuCj.png)

---

## 🛠️ Tecnologias Utilizadas

![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.3.2-black?style=for-the-badge&logo=flask&logoColor=white)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-4-orange?style=for-the-badge)
![Requests](https://img.shields.io/badge/Requests-2.31-green?style=for-the-badge)

---

## 🚀 Como Usar

### 1. Clone o Repositório
```bash
git clone [https://github.com/seu-usuario/api-versiculo-do-dia.git](https://github.com/GabrielSam26/api-versiculo-do-dia.git)
cd api-versiculo-do-dia
pip install -r requirements.txt
python index.py

### 2. Rotas
'''rotas
As rotas disponiveis na api são /versiculo, em formato GET para acessar localhost acesse em: http://127.0.0.1:5000/versiculo
