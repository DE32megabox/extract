import pandas as pd
import requests
import os

def ice_breaking():
    print("""
*********+**+++++++++++=:::::::::::::::::::::::::::::::-::::::::::::::::::::::::::=*****************
**+++++++++++++++++++++=:::::::::::::::::::::::::::=#%%%%%%+::-:::::::::::::::::::=*****************
+++++++++++++++++++++++=:::::::::::::::-:::::::::=%%%#+*%%%%%===::::::::::::::::::=*****************
+++++++++++++++++++++++-:::::::::::::::=-::-=:::-%%#+==+*%%+*%*+-:::::::::::::::::-*****************
+++++++++++++++++++++++-:::::::::::::::==::=-::-%%#+++++*%%#++%*=---::::::::::::::-++***************
++++++++++++++++++++++=::::::::::::::::-+:=+:::+%%####*#%%@@@#==+=++=:::::::::::::-++++++*++++******
++++++++++++++++++++===:::::::::::::--+++++-:::*@#*##*+*##%@@@*+*#*#+::::::::::::::+++++++++++++++++
+++++++++++++++========:::::::::::::+***#++-:::#%+==++=+*++*%@@#%*+**+:::::::::::::+++++++++++++++++
+++++++++++============:::::::::::::=*#####-::-%@#####%%###%@@@@%%%@@%%%%%#+-::::::=++++++++++++++++
+++++++===============-:::::::::::::=**##%#+*=+%@@#####%%%%%@@@@@@@@@@%%%%%%%%%-:::=++++++++++++++++
++++=+================-:::::::::::::=#%%%@@%%%%%%%@%#*###%%@@@@@@@@%%%@@@@@@%%%%=::-++++++++++++++++
+=====================-:::::::::::=%%%%%%%%%%%%@@@@@@@@@@@@@@@@@%@@@@%%@@@@%@@@@%=--=++++==+++++++++
======================-::::::::::=#%%%%%%%@@@%%%%@@@@@@@@@@@@@@@@@@@@%##%%%#**#@@*+====+***++==+++++
======================-:::::::::-#%%%%%%@@@@#**%%@@@@@@##%@@@@@@@%%%%#***#**###%%%*****++++****++==+
======================-:::::::--=%%@@%#%%*++****##%@@@@@@@@@@@@%#%#####%%###%%###%%%#%%+++++++*#****
======================:::::::-==+*%@@**+***#**#*%#%%#%@@@@@@@%%%*****%#+##**+++*==+*+++++===++++++**
=================-===--=::::==-=****#+====+**+=-*****#@@@@@@@%%*%##**#*--=%##%#===+++==**#***+++++++
==============---=+*++*===-=+****#+*++====++*===+*++**%%@@@@@%*#*+++*#++******+++++*+========+**##**
============--===++**==*+==**+++=+++++++++*++**%%***##@@@@@@%%*+++****###*++++*+++++=============+++
========-====++++=--++**++***++**###++++++**##########@@@@@%#**+++++*+++++**##*+++++=============+++
======:::=++***+==++++++***+######%#++++***+**######%@@@@@@@#+****+**##*++++++++***+-===========++++
===-::---+**************=::::::::::-+++****+++**##%%@@@@@@@@@%++***+++++++++++++****+========+%@@@@@
-:::----+++++*******+-::::::::::::::-******####%%%%@@@@@@@@@@@@@%****++++++++++****++++*##%@@@@@@@@@
------*+++++++*+--:::-----::::::-::::=########%%%@@@@@@@@@@@@@@@@@##*********#####*++++%@@@@@@@@@@@@
--=#*++++***+-:::-------------::*####*=***##%%%%%@@@@@@@@@@@@@@@@@@%#%%%%%%%%%%%#*+++++*@@@@@@@@@@@@
***+++****=:---------------------=+***==***#####%%*@@@@@@@@@@@@@@@@@%##%%%%%%###***++++*@@@@@@@@@@@@
********==+**+++==------------------=+++*+****##%#*+%@@@@@@@@@@@@@@@@*#########******+*#@@@@@@@@@@@@
*+++***+---=------=------------------===+++++***##@%%@@@@@@@@@@@@@@@@@%###########****#@@@@@@@@@@@@@
###*#**##*+=++===----------------------===++===+%%%#*@@@@@@@@@@@@@@@@@@@%############%@@@@@@@@@@@@@@
*#*##*******++++=====-------------------===******+++++*@@@@@@@@@@@@@@@@@@@@%###%%%%%@@@@@@@@@@@@@@@@
""")
    return

def get_key():
    key = os.getenv('MOVIE_API_KEY')
    return key

def req2df(load_dt='20210101', url_param={}):
    code, data = req(load_dt, url_param)
    movie = data['boxOfficeResult']['dailyBoxOfficeList']
    df = pd.DataFrame(movie)
    print(df)
    return df

def req(load_dt="20210101", url_param={}):
    url = gen_url(load_dt, url_param)
    r = requests.get(url)

    code = r.status_code
    data = r.json()
    return code, data

def gen_url(dt="20210101", url_param={}):
    base_url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json"
    key = get_key()
    url = f"{base_url}?key={key}&targetDt={dt}"

    for key, value in url_param.items():
        url = url + f"&{key}={value}"

    print(f"url: {url}")
    return url

# ice_breaking()



