# Тесты для BooksCollector

## Реализованные тесты:

### Метод add_new_book
- `test_add_new_book` - параметризованный тест добавления книг с разной длиной названия (1 символ, 40 символов, пустая строка, >40 символов)
- `test_add_new_book_duplicate` - проверка невозможности добавления дубликата

### Метод set_book_genre  
- `test_set_book_genre_valid` - установка валидного жанра для существующей книги
- `test_set_book_genre_invalid_book` - попытка установить жанр несуществующей книге
- `test_set_book_genre_invalid_genre` - установка невалидного жанра

### Метод get_book_genre
- `test_get_book_genre_existing` - получение жанра существующей книги
- `test_get_book_genre_nonexistent` - получение жанра несуществующей книги

### Метод get_books_with_specific_genre
- `test_get_books_with_specific_genre` - параметризованный тест получения книг по разным жанрам (Фантастика, Ужасы, Детективы, Мультфильмы, Комедии, несуществующий жанр)

### Метод get_books_genre
- `test_get_books_genre` - получение полного словаря книг с жанрами

### Метод get_books_for_children
- `test_get_books_for_children` - фильтрация книг без возрастного рейтинга (исключает Ужасы и Детективы)

### Метод add_book_in_favorites
- `test_add_book_in_favorites_valid` - добавление валидной книги в избранное
- `test_add_book_in_favorites_nonexistent` - попытка добавить несуществующую книгу в избранное
- `test_add_book_in_favorites_duplicate` - проверка невозможности дублирования в избранном

### Метод delete_book_from_favorites
- `test_delete_book_from_favorites` - удаление книги из избранного
- `test_delete_book_from_favorites_not_in_favorites` - удаление книги, которой нет в избранном

### Метод get_list_of_favorites_books
- `test_get_list_of_favorites_books` - получение списка избранных книг

## Запуск тестов
```bash
pytest test.py -v