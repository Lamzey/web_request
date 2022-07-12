import requests
import socket

print("Enter your website in this manner ==> 'https://www.facilitar.org' to know if it's working or not.")
response = requests.get(input())

if response.status_code == 200:
    print('Success, The Site Is Working')
elif response.status_code == 400:
    print('Oops, Page Not Found!')
else:
    print('We Are Working On The Website')

print("Enter your website in this manner ==> 'www.facilitar.org' to get the IP Address.")
web = input()
ip_add = socket.gethostbyname(web)

print("The IP Address For " + web + " is " + ip_add)