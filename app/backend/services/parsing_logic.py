import bs4
import requests
from .vizualizations import create_plot
from .refine_data import refine_numbers, refine_text


def parse_url(url):
    with requests.Session() as session:
        with session.get(url) as response:
            html = response.text
            soup = bs4.BeautifulSoup(html, 'html.parser')
            table = soup.find('table', class_='default-table table marketcap-table dataTable')
            body = table.find('tbody')
            head = table.find('thead')
            data_name = refine_text(head.find('th', tid=4).text)

            names = [name.text for name in body.find_all('div', class_='company-name')]
            cap_price = body.find_all('td', class_='td-right')
            data = [cap_price[i].text for i in range(1, len(cap_price), 3)]
            prices = [cap_price[i].text for i in range(2, len(cap_price), 3)]
            todays = body.find_all('td', class_='rh-sm')
            for i in range(len(todays)):
                if todays[i].find('span', class_='percentage-red'):
                    todays[i] = '-' + todays[i].text
                else:
                    todays[i] = todays[i].text
            countries = [country.text for country in body.find_all('span', class_='responsive-hidden')]

            data = [
                {
                    'Name':  refine_text(names[i]),
                    refine_text(data_name): data[i],
                    f'Refined {data_name}': refine_numbers(data[i]),
                    'Price': refine_text(prices[i]),
                    'Refined Price': refine_numbers(prices[i]),
                    'Today': refine_text(todays[i]),
                    'Refined Today': refine_numbers(todays[i]),
                    'Country': refine_text(countries[i])
                }
                for i in range(len(names))
            ]
            images = [
                create_plot(data, 'Name', 'Refined Price', 'Price', 'Top companies by price per share', 'price.png', False),
                create_plot(data, 'Name', f'Refined {data_name}', f'{data_name}', f'Top companies by {data_name}', f'{data_name.lower()}.png', False),
                create_plot(data, 'Name', 'Refined Today', 'Today', 'Top companies with biggest share growth', 'today_up.png', False),
                create_plot(data, 'Name', 'Refined Today', 'Today', 'Top companies with lowest share growth', 'today_down.png', True)
            ]

            return {'data': data, 'images': images, 'label': data_name}
