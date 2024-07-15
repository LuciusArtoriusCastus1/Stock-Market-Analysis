# Stock-Market-Analysis
A small web application which main feature is, tracking a stock market changes that also presents
some data visualizations. <br />
Provides ability to track different companies': <br />
price per share, current share price change, country, market capital etc.

Main languages are python and js. <br />
Parsing script is written using libraries as requests and beautifulsoup4.<br />
Visualizations created using pandas and matplotlib.<br />
Backend part of application is made using fastapi. <br />
Frontend part is made simply using js HTML and CSS. <br />

To start the app: <br />
1. Clone the GitHub repository<br />
```git clone https://github.com/LuciusArtoriusCastus1/Stock-Market-Analysis.git``` <br />
2. Set up the environment <br />
```python -m venv venv``` <br />
3. Activate the environment <br />
```venv\Scripts\activate``` <br />
4. Install requirements <br />
```pip install -r req.txt``` <br />
5. Start the fastapi server <br />
```fastapi dev app/backend/main.py --reload``` <br />
6. and after, open the ```index.html``` file from the ```app/frontend/templates``` in a browser <br />

# So, basically that's it! <br />