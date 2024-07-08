import argparse
import json
import jsonschema
from jsonschema import validate
from jsonschema.exceptions import ValidationError, SchemaError

def load_and_validate_json(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        print(f"Błąd: Nie znaleziono pliku '{file_path}'. Upewnij się, że podana ścieżka jest poprawna.")
        return None
    except json.JSONDecodeError as e:
        print(f"Błąd: Plik nie jest poprawnym plikiem JSON. Szczegóły: {e}")
        return None

    schema = {
        "type": "object",
        "properties": {
            "name": {"type": "string"},
            "age": {"type": "number"},
        },
        "required": ["name", "age"]
    }

    try:
        validate(instance=data, schema=schema)
    except ValidationError as e:
        print(f"Błąd walidacji: {e.message}")
        print("Dokładne dane, które nie spełniają wymagań schematu:")
        print(json.dumps(data, indent=4))
        return None
    except SchemaError as e:
        print(f"Błąd w schemacie JSON: {e.message}")
        return None

    return data

def main():
    parser = argparse.ArgumentParser(description='Opis_kiedys_dodac')
    parser.add_argument('--plik', type=str, help='Ścieżka do pliku JSON', required=True)
    args = parser.parse_args()
    data = load_and_validate_json(args.plik)
    if data:
        print(f'Wczytane dane: {data}')

if __name__ == "__main__":
    main()
