import csv

def load_ip_dict(file_path):
    ip_dict = {}
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            ip, url = row
            ip_dict[ip.strip()] = url.strip()
    return ip_dict

def find_site_by_ip(ip_dict, ip):
    return ip_dict.get(ip, "Сайт з такою IP-адресою не знайдено")

file_path = 'ip_addresses.csv'
ip_dict = load_ip_dict(file_path)

ip_to_search = input("Введіть IP-адресу для пошуку: ")
site_name = find_site_by_ip(ip_dict, ip_to_search)
print(f"URL-адреса сайта для IP-адреси {ip_to_search}: {site_name}")
