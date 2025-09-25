# eCarla UI Tests (Selenium + pytest)

Automatyczne testy UI dla sklepu internetowego eCarla.pl wykorzystujące Selenium WebDriver i pytest.

## 🔧 Wymagania

- Python 3.8+
- Chrome/Chromium browser
- ChromeDriver (automatycznie zarządzany przez webdriver-manager)

## 📦 Instalacja

1. **Sklonuj repozytorium:**

```bash
git clone https://github.com/Janka245/ecarla-tests-project
```

2. **Wejdź do folderu projektu:**

```bash
cd ecarla_tests_project
```

3. **Utwórz i aktywuj środowisko wirtualne:**

```bash
python -m venv venv
# lub
python3 -m venv venv

source venv/bin/activate  # macOS/Linux
# lub
venv\Scripts\activate     # Windows
```

4. **Zainstaluj zależności:**

```bash
pip install -r requirements.txt
```

## ⚙️ Konfiguracja

Utwórz plik `.env` w głównym katalogu projektu:

```env
BASE_URL=https://ecarla.pl
ECARLA_EMAIL=your_email@example.com
ECARLA_PASSWORD=your_password_here
```

### Zmienne środowiskowe:

- `BASE_URL` - URL sklepu eCarla (domyślnie: https://ecarla.pl)
- `ECARLA_EMAIL` - email do testów logowania
- `ECARLA_PASSWORD` - hasło do testów logowania

## 🚀 Uruchamianie testów

### Podstawowe uruchomienie:

```bash
pytest -v
```

### Uruchomienie z dodatkowymi opcjami:

```bash
# Uruchomienie konkretnego testu
pytest tests/test_ecarla_flows.py::test_search_by_name -v

# Uruchomienie w trybie headless
pytest -v --headless

# Uruchomienie z maksymalną szczegółowością
pytest -vvv --tb=long
```

## 📁 Struktura projektu

ecarla_tests_project/
├── .env # Zmienne środowiskowe (nie w repo)
├── .gitignore # Pliki ignorowane przez Git
├── README.md # Dokumentacja projektu
├── requirements.txt # Zależności Python
├── pytest.ini # Konfiguracja pytest
├── pages/ # Page Object Model
│ ├── init .py
│ ├── base_page.py # Bazowa klasa dla wszystkich stron
│ ├── home_page.py # Strona główna
│ ├── login_page.py # Strona logowania
│ ├── search_page.py # Modal wyszukiwania i strona wyników
│ ├── category_page.py # Strona kategorii produktów
│ └── product_page.py # Strona produktu
├── tests/ # Testy
│ ├── init .py
│ ├── conftest.py # Konfiguracja pytest i fixtures
│ ├── test_ecarla_flows.py # Główne testy flow
│ └── test_utils.py # Testy narzędzi pomocniczych
├── utils/ # Narzędzia pomocnicze
| └── helpers.py

## ✅ Pokryte funkcjonalności

### Podstawowe flow:

1. **Otwieranie strony głównej** - weryfikacja dostępności serwisu
2. **Logowanie** - test z prawidłowymi danymi uwierzytelniającymi
3. **Wyszukiwanie produktów**:
   - Wyszukiwanie po nazwie produktu
   - Wyszukiwanie po marce
4. **Sortowanie produktów**:
   - Sortowanie po cenie (rosnąco/malejąco)
   - Sortowanie po nazwie (A-Z/Z-A)
5. **Dodawanie do koszyka** - dodanie produktu i weryfikacja

### Szczegółowe testy:

- `test_open_homepage` - Otwieranie strony głównej
- `test_login_success` - Logowanie z prawidłowymi danymi
- `test_search_by_name_simple` - Wyszukiwanie "kolczyki"
- `test_search_by_brand` - Wyszukiwanie marki "Rainbow"
- `test_search_by_name` - Wyszukiwanie "pierścionki"
- `test_sort_by_price_ascending` - Sortowanie po cenie rosnąco
- `test_sort_by_price_descending` - Sortowanie po cenie malejąco
- `test_sort_by_name_A_Z` - Sortowanie po nazwie A-Z
- `test_sort_by_name_Z_A` - Sortowanie po nazwie Z-A
- `test_open_product_and_add_to_cart` - Dodawanie produktu do koszyka

## 🏗️ Architektura testów

### Page Object Model (POM)

Projekt wykorzystuje wzorzec Page Object Model dla lepszej organizacji i utrzymania kodu:

- **BasePage** - bazowa klasa z podstawowymi metodami Selenium
- **HomePage** - metody dla strony głównej (otwieranie, nawigacja)
- **LoginPage** - obsługa formularza logowania
- **SearchModal/SearchResultsPage** - wyszukiwanie i wyniki
- **CategoryPage** - strona kategorii z sortowaniem i filtrowaniem
- **ProductPage** - strona produktu z dodawaniem do koszyka

### Kolejność testów

Testy są wykonywane w określonej kolejności dzięki `pytest-order`:

1. Otwieranie strony głównej
2. Logowanie
3. Wyszukiwanie (różne warianty)
4. Sortowanie (różne opcje)
5. Dodawanie do koszyka

## 📊 Raporty

### HTML Report (pytest-html)

Automatycznie generowany w `reports/report.html` po każdym uruchomieniu.

### Logi

Szczegółowe logi zapisywane w `reports/test_run.log` z konfigurowalnymi poziomami.

## 📝 Licencja

Ten projekt jest licencjonowany na warunkach licencji MIT.

---

**Uwaga:** Ten projekt służy wyłącznie celom edukacyjnym i testowym. Upewnij się, że masz odpowiednie uprawnienia do testowania aplikacji eCarla.pl.
