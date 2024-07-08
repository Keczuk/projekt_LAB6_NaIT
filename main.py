import argparse

def main():
    parser = argparse.ArgumentParser(description='Opis twojego programu')
    parser.add_argument('--plik', type=str, help='Ścieżka do pliku JSON')
    args = parser.parse_args()
    print(f'Ścieżka do pliku: {args.plik}')

if __name__ == "__main__":
    main()
