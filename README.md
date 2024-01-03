![PyAssist](https://github.com/Szumapman/PyAssist_m2w_h1/assets/36560916/57e54e7f-c609-4e50-9432-a63c3ecd677d)

# _PyAssist_

### version 2.1 (2wh1)

> PyAssist to narzędzie wiersza poleceń oparte na języku Python, które zostało zaprojektowane w celu efektywnego zarządzania książką adresową i notatkami. Dzięki PyAssist możesz łatwo dodawać, edytować, usuwać, wyszukiwać i eksportować rekordy w swojej książce adresowej. Narzędzie umożliwia również sprawne zarządzanie notatkami, oferując różnorodne funkcje. Dodatkowo pozwala ono na błyskawiczne uporządkowanie wskazanego katalogu poprzez segregację znajdujących się w nim i jego podkatalogach plików.

> PyAssist is a Python-based command-line utility designed to assist you in managing your address book and notes efficiently. With PyAssist, you can easily add, edit, delete, search, and export records in your address book. The tool also enables efficient management of notes, offering a variety of functions. In addition, it allows you to instantly organize the indicated directory by segregating the files in it and its subdirectories.

## Język / Language

- [Polski / Polish](#spis-treści)
- [Angielski / English](#table-of-contents)

## Spis treści

- [Informacje ogólne](#informacje-ogólne)
- [Konfiguracja](#konfiguracja)
- [Instalacja](#instalacja)
- [Uruchomienie programu](#uruchomienie-programu)
- [Licencja](#licencja)
- [Autor](#autor)
- [Kontakt](#kontakt)

## Informacje ogólne

### Zdefiniowanie problemu rozwiązywanego przez Pyassist

Projekt rozwiązuje problem związany z efektywnym organizowaniem i zarządzaniem informacjami z książki adresowej oraz notatek. Tradycyjne metody korzystania z kontaktów i notatek mogą być uciążliwe, a PyAssist ma na celu dostarczenie zoptymalizowanego i efektywnego rozwiązania. Dodatkowo pomaga on w zapanowaniu nad często pojawiającym się problemem z bałeganem w intensywnie wykorzystywanych katalogach takich jak np. pulpit, czy pobrane.

### Cele projektu

Główne cele PyAssist obejmują:

1. Uproszczenie procesu zarządzania rekordami książki adresowej.
2. Dostarczenie wygodnego i potężnego narzędzia do robienia notatek oraz organizacji.
3. Oferowanie funkcji sortowania plików w określonym katalogu.

### Potrzeba stworzenia projektu

Potrzeba stworzenia tego projektu wynika z potrzeby wszechstronnego i przyjaznego użytkownikowi narzędzia wiersza poleceń do zarządzania informacjami osobistymi. PyAssist został stworzony, aby zapewnić intuicyjny interfejs obsługi kontaktów i notatek, pozwalając użytkownikom skupić się na produktywności, zamiast zajmować się uciążliwymi zadaniami organizacyjnymi.

### Menu główne

Po uruchomieniu PyAssist zostaniesz powitany w menu głównym, gdzie możesz wybrać spośród następujących opcji:

- `addressbook:` Dostęp do menu zarządzania książką adresową.
- `notes:` Dostęp do menu zarządzania notatkami.
- `sort:` Sortowanie plików w określonym katalogu.
- `exit:` Wyjście z PyAssist.
- `help:` Wyświetla zestawienie dostępnych komend wraz z opisem.

### Menu książki adresowej

W menu książki adresowej możesz wykonywać następujące czynności:

- `add:` Dodaj nowy rekord do książki adresowej.
- `edit:` Edytuj istniejący rekord w książce adresowej.
- `show:` Wyświetl wszystkie rekordy lub określony rekord w książce adresowej.
- `delete:` Usuń rekord z książki adresowej.
- `export:` Wyeksportuj książkę adresową do pliku CSV.
- `import:` Importuj dane z pliku CSV do książki adresowej.
- `birthday:` Przeglądaj nadchodzące urodziny w określonym zakresie dni.
- `search:` Szukaj określonego rekordu w książce adresowej.
- `save:` Zapisuje książkę adresową.
- `up:` Powrót do menu głównego.
- `exit:` Wyjście z programu.
- `help:` Wyświetla zestawienie dostępnych komend wraz z opisem.

### Menu notatek

W menu notatek możesz zarządzać swoimi notatkami:

- `show:` Wyświetl wszystkie notatki.
- `search:` Szukaj określonej notatki.
- `add:` Stwórz nową notatkę.
- `edit:` Edytuj istniejącą notatkę.
- `delete:` Usuń notatkę.
- `sort:` Sortuje notatki po tagach.
- `export:` Wyeksportuj notatki do pliku CSV.
- `import:` Importuj dane z pliku CSV do notatek.
- `save:` Zapisuje notatki.
- `up:` Powrót do menu głównego.
- `exit:` Wyjście z programu.
- `help:` Wyświetla zestawienie dostępnych komend wraz z opisem.

### Sortowanie plików

PyAssist umożliwia sortowanie plików w określonym katalogu. Po prostu wybierz opcję "sort" z menu głównego i podaj ścieżkę do tego katalogu.

### Wyjście z Pyassist

Aby wyjść z PyAssist i zapisać dane, wybierz opcję "exit".

## Konfiguracja

Upewnij się, że na Twoim komputerze zainstalowany jest Python 3.11 lub nowszy.

Aplikacja korzysta z następujących bibliotek:

- 'pyfiglet'
- 'cowsay'
- 'prompt_toolkit'

## Instalacja

1. Pobierz repozytorium:

```
git clone https://github.com/Szumapman/PyAssist_m2w_h1
```

2. Przejdź do katalogu z aplikacją np.:

```
cd PyAssist
```

3. Zainstaluj program:

Aby zainstalować pakiet z kodu źródłowego, wykonaj w konsoli polecenie

```
pip install -e .
```

w folderze, w którym znajduje się plik setup.py.

## Uruchomienie programu

Uruchom aplikację za pomocą następującej komendy:

```
pyassist
```

## Licencja

Ta aplikacja jest udostępniana na [licencji MIT](https://github.com/Szumapman/PyAssist_m2w_h1/blob/main/LICENSE).

## Autor

- 'Paweł Szumański'

## Kontakt

Jeśli masz pytania, sugestie lub chciałbyś się skontaktować w sprawie aplikacji:

- GitHub [Paweł Szumański](https://github.com/Szumapman)

**_Ten projekt bazuje cześciowo na:_ [PyAssist 1.0](https://github.com/Szumapman/PyAssist)**

**_Ten plik README.md bazuje na swoim odpowiedniku z PyAssist 1.0 dostępnym tu:_ [PyAssist 1.0 README.md](https://github.com/Szumapman/PyAssist/blob/main/README.md)**

## Table of Contents

- [General Information](#general-information)
- [Setup](#setup)
- [Installation](#installation)
- [Running the application](#running-the-application)
- [Licence](#licence)
- [Author](#author)
- [Contact](#contact)

## General Information

### Problem Statement

The project solves the problem of efficiently organizing and managing address book information and notes. Traditional methods of using contacts and notes can be cumbersome, and PyAssist aims to provide an optimized and efficient solution. In addition, it helps bring the common problem of clutter in heavily used directories such as the desktop and downloads under control.

### Project Goals

The primary goals of PyAssist include:

- Simplifying the process of managing address book records.
- Providing a convenient and powerful tool for note-taking and organization.
- Offering functionalities for sorting files in a specified directory.

### Motivation

The motivation behind the project stems from the need for a versatile and user-friendly command-line tool for personal information management. PyAssist was developed to offer an intuitive interface for handling contacts and notes, allowing users to focus on productivity rather than dealing with cumbersome organizational tasks.

### Main Menu

Upon launching PyAssist, you'll be greeted with the main menu, where you can choose from the following options:

- `addressbook`: Access the address book management menu.
- `notes`: Access the notes management menu.
- `sort`: Sort files in a specified directory.
- `exit`: Exit PyAssist.
- `help:` Displays a list of available commands with a description.

### Address Book Menu

In the address book menu, you can perform the following actions:

- `add`: Add a new record to the address book.
- `edit`: Edit an existing record in the address book.
- `show`: Display all records or a specific record in the address book.
- `delete`: Delete a record from the address book.
- `export`: Export the address book to a CSV file.
- `import`: Import data from a CSV file to the address book.
- `birthday`: View upcoming birthdays within a specified number of days.
- `search`: Search for a specific record in the address book.
- `save:` Save address book.
- `up:` Back to main menu.
- `exit:` Exit from the program.
- `help:` Displays a list of available commands with a description.

### Notes Menu

In the notes menu, you can manage your notes:

- `show`: Display all notes.
- `search`: Search for a specific note.
- `add`: Create a new note.
- `edit`: Edit an existing note.
- `delete`: Delete a note.
- `sort:` Sort notes by tags.
- `export:` Export the notres to a CSV file.
- `import:` Import data from a CSV file to the notes.
- `save:` Save notes.
- `up:` Back to main menu.
- `exit:` Exit from the program.
- `help:` Displays a list of available commands with a description.

### Sort Files

PyAssist allows you to sort files in a specific directory. Simply select the "sort" option from the main menu and enter the path to that directory.

### Exit

To exit PyAssist and save your data, choose the "exit" option.

## Setup

Make sure that Python 3.11 is installed on your computer.

The application uses the following libraries:

- 'pyfiglet'
- 'cowsay'
- 'prompt_toolkit'

## Installation

1. Download the repository:

```
git clone https://github.com/Szumapman/PyAssist_m2w_h1
```

2. navigate to the directory with the application:

```
cd PyAssist
```

3. Install dependencies:

To install the package from the source code, type `pip install -e .` in the folder where setup.py is located

## Running the application

Run the application using the following command:

```
pyassist
```

## Licence

This application is made available under the [MIT licence](https://github.com/Szumapman/PyAssist_m2w_h1/blob/main/LICENSE).

## Author

- 'Paweł Szumański'

## Contact

If you have any questions, suggestions or would like to get in touch about the application:

- GitHub [Paweł Szumański](https://github.com/Szumapman)

**_This project is based in part on:_ [PyAssist 1.0](https://github.com/Szumapman/PyAssist)**

**_This README.md file is based on its PyAssist 1.0 counterpart available here:_ [PyAssist 1.0 README.md](https://github.com/Szumapman/PyAssist/blob/main/README.md)**
