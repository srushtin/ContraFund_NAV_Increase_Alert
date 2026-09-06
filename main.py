import requests
import smtplib
from dotenv import load_dotenv
import os

load_dotenv()

with smtplib.SMTP("smtp.gmail.com",587) as connection:

    connection.starttls()
    connection.login(user=os.getenv('email'),password=os.getenv('pwd'))
    scheme_code=119835
    res = requests.get(f"https://api.mfapi.in/mf/{scheme_code}")
    data = res.json()
    scheme_name = data['meta']['scheme_name']
    nav_data = data['data']

    current_nav = float(nav_data[0]['nav'])
    earlier_nav = float(nav_data[1]['nav'])
    one_year_all_time_high = max([float(nav_value['nav']) for nav_value in nav_data[:365]])
    nav_list=""
    for nav in nav_data[1:31]:
        nav_list+=f"{nav['date']} : {nav['nav']}\n"

    if current_nav > earlier_nav:
        body=(f'Subject:{scheme_name} - NAV has increased to {current_nav} from {earlier_nav}\n\n'
              f'Current NAV: {current_nav}\n'
              f'One year all time high: {one_year_all_time_high}\n'
              f'Last 30 day\'s NAVs:\n{nav_list}')

        connection.sendmail(from_addr=os.getenv('email'), to_addrs=os.getenv('email'),msg=body)

