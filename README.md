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

W ramach projektu zostały stworzone następujące endpoint'y

|           Endpoint           | HTTP Method |                    Wynik                     |
|:----------------------------:|:-----------:|:--------------------------------------------:|
|        `auth/users/`         |    POST     |                 Rejestracja                  |
|      `auth/jwt/create/`      |    POST     |                  Logowanie                   |
|       `auth/users/me/`       |     GET     |     Informacje o zalogowanym użytkowniku     |
|         `apk/users`          |     GET     |         Wyświetla listę użytkowników         |
|       `apk/users/:id`        |     GET     |     Wyświetla dane wybranego użytkownika     |
|         `apk/posts`          |     GET     |               Wyświetla posty                |
|       `apk/posts/:id`        |     GET     |     Wyświetla szczegóły wybranego postu      |
|     `apk/posts/:string`      |     GET     | Wyświetla postu wedle wpisanego ciągu znaków |
|       `apk/posts/add`        |    POST     |               Dodawanie postu                |
|     `apk/posts/edit/:id`     |     PUT     |                 Edycja postu                 |
|    `apk/posts/delete/:id`    |   DELETE    |                Usuwanie postu                |
| `apk/posts/:id/comments/add` |    POST     |        Dodawanie komentarza do postu         |
|   `apk/posts/:id/comments`   |     GET     |     Wyświetla komentarze wybranego postu     |
|      `apk/comment/:id`       |     GET     |    Wyświetla szczegóły danego komentarza     |
|        `apk/comment/edit`        |     PUT     |              Edycja komentarza               |
|       `apk/comment/delete`       |   DELETE    |             Usuwanie komentarza              |
|        `apk/comments/:id`        |     GET     |       Wyświetla komentarze użytkownika       |

