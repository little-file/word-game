import requests

def turkce_mi(kelime):
    url = f"https://sozluk.gov.tr/gts?ara={kelime}"
    response = requests.get(url)
    data = response.json()
    
    if data["error"]:
        return False
    else:
        return True, url 

kelime = input("Bir kelime girin: ")

turkce, url = turkce_mi(kelime) 

print("URL:", url)

if turkce:
    print("Girdiğiniz kelime Türkçe bir kelime.")
else:
    print("Girdiğiniz kelime Türkçe bir kelime değil.")
