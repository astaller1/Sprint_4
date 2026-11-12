# qa_python
### Список реализованных автотестов (11 тест-кейсов)

В проекте реализовано 11 тестов, которые покрывают каждый метод класса `BooksCollector`:

1. **`test_add_new_book_valid_title_length`** (параметризованный)  
   Метод `add_new_book`. Проверяет успешное добавление в словарь книг с валидным количеством символов в названии (граничные значения: 1 и 40 символов).

2. **`test_add_new_book_invalid_title_length`** (параметризованный)  
   Метод `add_new_book`. Проверяет негативный сценарий с невалидным количеством символов (пустая строка и 41 символ).

3. **`test_add_new_book_dublicate_not_allowed`**  
   Метод `add_new_book`. Проверяет негативный сценарий с дублирующимся названием книги.

4. **`test_set_book_genre_book_exists_and_genre_exists`**  
   Метод `set_book_genre`. Проверяет установку валидного жанра существующей книги.

5. **`test_get_book_genre_book_and_genre_correctly_matched`**  
   Метод `get_book_genre`. Проверяет корректное получение жанра книги по ее названию.

6. **`test_get_books_with_specific_genre_filtration`**  
   Метод `get_books_with_specific_genre`. Проверяет фильтрацию библиотеки по выбранному жанру.

7. **`test_get_books_genre_returns_current_dict`**  
   Метод `get_books_genre`. Проверяет вывод текущего словаря `books_genre`.

8. **`test_get_books_for_children_returns_only_books_for_children`**  
   Метод `get_books_for_children`. Проверяет фильтрацию книг, подходящих для детей (исключение жанров с возрастным рейтингом).

9. **`test_add_book_in_favorites_successfully_adds_book`**  
   Метод `add_book_in_favorites`. Проверяет добавление существующей книги в список избранного.

10. **`test_delete_book_from_favorites_successfully_removes_book`**  
    Метод `delete_book_from_favorites`. Проверяет успешное удаление книги из избранного.

11. **`test_get_list_of_favorites_books_shows_current_favorite_list`**  
    Метод `get_list_of_favorites_books`. Проверяет получение актуального списка избранного.