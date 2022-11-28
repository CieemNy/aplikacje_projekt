## Repozytorium dla projektu zaliczeniowego w ramach przedmiotu Aplikacje-WWW<br/>
### Temat Projektu: **Mini prywatne forum/blog** 
Damian Banach & Bartek Gryciuk

## Paczki użyte w projekcie
* Python 3.9.13
* Django 4.1.2
* Django REST Framework 3.14.0
* Djoser 2.1.0

## Schemat Bazy Danych
![alt text](https://github.com/CieemNy/aplikacje_projekt/blob/feat_comments/db_schema.png?raw=true)

## Endpointy
| Endpoint | HTTP Method | Wynik |
| :--------: | :--------: | :--------: |
| `apk/users` | GET | Wyświetla listę użytkowników |
| `apk/users/:id` | GET | Wyświetla dane wybranego użytkownika |
| `apk/posts` | GET | Wyświetla posty |
| `apk/posts/:id` | GET | Wyświetla szczegóły wybranego postu |
| `apk/posts/:string` | GET | Wyświetla postu wedle wpisanego ciągu znaków |
| `apk/posts/add` | POST | Dodawanie postu |
| `apk/posts/edit/:id` | PUT | Edycja postu |
| `apk/posts/delete/:id` | DELETE | Usuwanie postu |
| `apk/posts/:id/comments/add` | POST | Dodawanie komentarza do postu |
| `apk/posts/:id/comments` | GET | Wyświetla komentarze wybranego postu |
