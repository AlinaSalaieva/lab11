import json

def load_atomic_masses(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def find_atomic_mass(data, element_name):
    return data.get(element_name, "Хімічний елемент не знайдено")

def elements_starting_with(data, letter):
    return {key: value for key, value in data.items() if key.startswith(letter)}

file_path = 'C:\\Users\\ALINA\\OneDrive\\Desktop\\Програмування\\lab11\\atomic_masses.json'
data = load_atomic_masses(file_path)

element_name = input("Введіть назву хімічного елемента для пошуку: ")
atomic_mass = find_atomic_mass(data, element_name)
print(f"Відносна атомна маса елемента {element_name}: {atomic_mass}")

letter = input("Введіть літеру для пошуку елементів: ")
elements = elements_starting_with(data, letter)
print(f"Елементи, назва яких починається з літери {letter}: {elements}")

