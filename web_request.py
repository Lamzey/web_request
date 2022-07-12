import requests

response = requests.get(input())

if response.status_code == 200:
    print('Success, The Site Is Working')
elif response.status_code == 400:
    print('Oops, Page Not Found!')
else:
    print('We Are Working On The Website')