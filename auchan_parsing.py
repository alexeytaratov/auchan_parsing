import requests
import json

cookies = {
    'mindboxDeviceUUID': 'af8e1051-e4d7-4ba9-9f68-04d5295e70ad',
    'directCrm-session': '%7B%22deviceGuid%22%3A%22af8e1051-e4d7-4ba9-9f68-04d5295e70ad%22%7D',
    'popmechanic_sbjs_migrations': 'popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1',
    'tmr_lvid': '7e4c1ec5053652b1afa5a401e604fcc8',
    'tmr_lvidTS': '1729177193458',
    '_ym_uid': '1729177194236981825',
    '_ym_d': '1729177194',
    '_ymab_param': 'p6X-219m83MfzeslZBAnuWQ-SpsPTi7fg71Z-U9s0C_tcTbsF_3dwCwYA-BMHcIpSAxCrO_kLZ_amM4_LAS9PTuwnvM',
    'haveChat': 'true',
    'region_id': '1',
    'merchant_ID_': '1',
    'methodDelivery_': '1',
    '_GASHOP': '001_Mitishchi',
    'rrpvid': '540825392657238',
    '_userGUID': '0:m2dfgfao:KLNp_EkdBweYWr~MI55nrWsztDBgkD7b',
    '_userGUID': '0:m2dfgfao:KLNp_EkdBweYWr~MI55nrWsztDBgkD7b',
    'rcuid': '67112669f20f8995ff2ed49c',
    'utm_source': 'scaleo',
    'domain_sid': 'xYXbL0fB7OxwIsaPgXHUU%3A1729363243839',
    'rrlevt': '1729428049365',
    'digi_uc': '|v:172917:81776:39968:undefined!172936:982820!172944:933431|s:172936:982820',
    'qrator_ssid': '1729443751.364.gZcqyy0bOfGD4ABm-2khkk5i78c5e9kjp0sguvl6lduj4drdf',
    'dSesn': 'f1bdbf7c-922d-4c46-df8a-f82b28c2851e',
    '_dvs': '0:m2hkt35b:rNTAe0~hWp5W2sLAvOybPxXN3AIgsQwv',
    'click_id': '1f23ab06265c591ae226044d56f3491e',
    '_ym_isad': '2',
    '_ym_visorc': 'w',
    'qrator_jsid': '1729443762.060.zz0IQfw2exau5BM1-ru23u8j76du0ajngvee3fk5d61iqhru5',
    'tmr_detect': '0%7C1729444379637',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'ru,en;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json;charset=UTF-8',
    # 'Cookie': 'mindboxDeviceUUID=af8e1051-e4d7-4ba9-9f68-04d5295e70ad; directCrm-session=%7B%22deviceGuid%22%3A%22af8e1051-e4d7-4ba9-9f68-04d5295e70ad%22%7D; popmechanic_sbjs_migrations=popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1; tmr_lvid=7e4c1ec5053652b1afa5a401e604fcc8; tmr_lvidTS=1729177193458; _ym_uid=1729177194236981825; _ym_d=1729177194; _ymab_param=p6X-219m83MfzeslZBAnuWQ-SpsPTi7fg71Z-U9s0C_tcTbsF_3dwCwYA-BMHcIpSAxCrO_kLZ_amM4_LAS9PTuwnvM; haveChat=true; region_id=1; merchant_ID_=1; methodDelivery_=1; _GASHOP=001_Mitishchi; rrpvid=540825392657238; _userGUID=0:m2dfgfao:KLNp_EkdBweYWr~MI55nrWsztDBgkD7b; _userGUID=0:m2dfgfao:KLNp_EkdBweYWr~MI55nrWsztDBgkD7b; rcuid=67112669f20f8995ff2ed49c; utm_source=scaleo; domain_sid=xYXbL0fB7OxwIsaPgXHUU%3A1729363243839; rrlevt=1729428049365; digi_uc=|v:172917:81776:39968:undefined!172936:982820!172944:933431|s:172936:982820; qrator_ssid=1729443751.364.gZcqyy0bOfGD4ABm-2khkk5i78c5e9kjp0sguvl6lduj4drdf; dSesn=f1bdbf7c-922d-4c46-df8a-f82b28c2851e; _dvs=0:m2hkt35b:rNTAe0~hWp5W2sLAvOybPxXN3AIgsQwv; click_id=1f23ab06265c591ae226044d56f3491e; _ym_isad=2; _ym_visorc=w; qrator_jsid=1729443762.060.zz0IQfw2exau5BM1-ru23u8j76du0ajngvee3fk5d61iqhru5; tmr_detect=0%7C1729444379637',
    'Origin': 'https://www.auchan.ru',
    'Referer': 'https://www.auchan.ru/catalog/syry/syry-ashan/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
    'X-NewRelic-ID': 'undefined',
    'X-Token-CMD': '',
    'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjEwMDAwMDAiLCJhcCI6IjMzMjQxMTMiLCJpZCI6IjFjNjc1NGQzNmJlNTA4OTIiLCJ0ciI6IjdmYzk5ZDAzODNiMjJlNTVlM2Q5Njg0ZTBhYTc5ZTIwIiwidGkiOjE3Mjk0NDQzOTEwNTB9fQ==',
    'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'traceparent': '00-7fc99d0383b22e55e3d9684e0aa79e20-1c6754d36be50892-01',
    'tracestate': '1000000@nr=0-1-1000000-3324113-1c6754d36be50892----1729444391050',
}

params = {
    'merchantId': '1',
    'page': '1',
    'perPage': '110',
    'deliveryAddressSelected': '0',
}

json_data = {
    'filter': {
        'category': 'syry_ashan',
        'promo_only': False,
        'active_only': False,
        'cashback_only': False,
    },
}

response = requests.post(
    'https://www.auchan.ru/v1/catalog/products',
    params=params,
    cookies=cookies,
    headers=headers,
    json=json_data,
)

response.raise_for_status()

data = response.json()

products_list = []
for product in data['items']:
    if 'stock' in product and isinstance(product['stock']['qty'], (int, float)):
        product_dict = {}
        if 'title' in product:
            product_dict['title'] = product['title']
        if 'price' in product:
            product_dict['promo_price'] = product['price']['value']
        if 'oldPrice' in product and isinstance(product['oldPrice'], dict):
            product_dict['oldPrice'] = product['oldPrice']['value']
        else:
            product_dict['price'] = product['price']['value']
            del product_dict['promo_price']
        if 'price' in product:
            product_dict['brand'] = product['brand']['name']
        if 'gimaId' in product:
            product_dict['articleId'] = product['gimaId']
        if 'code' in product:
            product_dict['url'] = 'https://www.auchan.ru/product/' + product['code']
        products_list.append(product_dict)

with open("result.json", 'w', encoding='utf-8') as file:
    json.dump(products_list, file, ensure_ascii=False, indent=4)