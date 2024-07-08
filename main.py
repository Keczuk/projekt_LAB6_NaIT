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


def save_to_json(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def main():
    parser = argparse.ArgumentParser(description='Zweryfikuj JSONA')
    parser.add_argument('--plik', type=str, help='Ścieżka do pliku JSON', required=True)
    parser.add_argument('--wyjscie', type=str, help='Ścieżka do zapisu pliku JSON', required=True)
    args = parser.parse_args()
    data = load_and_validate_json(args.plik)
    save_to_json(data, args.wyjscie)
    print(f'Dane zapisane do: {args.wyjscie}')

if __name__ == "__main__":
    main()
