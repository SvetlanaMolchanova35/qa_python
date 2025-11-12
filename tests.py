import pytest
from main import BooksCollector


class TestBooksCollector:

    def setup_method(self):
        """Создаём новый экземпляр BooksCollector перед каждым тестом."""
        self.collector = BooksCollector()

    # Тестируем add_new_book
    @pytest.mark.parametrize(
        "book_name, expected",
        [
            ("К", True),  # 1 символ
            ("Короткий", True),  # короткая строка
            ("a" * 40, True),  # ровно 40 символов
            ("", False),  # пустая строка
            ("a" * 41, False),  # больше 40 символов
        ]
    )
    def test_add_new_book(self, book_name, expected):
        self.collector.add_new_book(book_name)
        if expected:
            assert book_name in self.collector.books_genre
            assert self.collector.books_genre[book_name] == ''
        else:
            assert book_name not in self.collector.books_genre

    def test_add_new_book_duplicate(self):
        """Повторное добавление книги не должно работать."""
        self.collector.add_new_book("Повторяшка")
        self.collector.add_new_book("Повторяшка")
        assert len(self.collector.books_genre) == 1

    # Тестируем set_book_genre
    def test_set_book_genre_valid(self):
        """Установка жанра для существующей книги из списка genre."""
        self.collector.add_new_book("Детектив")
        self.collector.set_book_genre("Детектив", "Детективы")
        assert self.collector.get_book_genre("Детектив") == "Детективы"

    def test_set_book_genre_invalid_book(self):
        """Нельзя установить жанр для книги, которой нет в словаре."""
        self.collector.set_book_genre("Нет в списке", "Фантастика")
        assert self.collector.get_book_genre("Нет в списке") is None

    def test_set_book_genre_invalid_genre(self):
        """Жанр должен быть из списка genre."""
        self.collector.add_new_book("Книга")
        self.collector.set_book_genre("Книга", "Неизвестный жанр")
        assert self.collector.get_book_genre("Книга") == ''

    # Тестируем get_book_genre
    def test_get_book_genre_existing(self):
        """Получение жанра существующей книги."""
        self.collector.add_new_book("Фантастика")
        self.collector.set_book_genre("Фантастика", "Фантастика")
        assert self.collector.get_book_genre("Фантастика") == "Фантастика"

    def test_get_book_genre_nonexistent(self):
        """Получение жанра для несуществующей книги."""
        assert self.collector.get_book_genre("Не существует") is None

    # Тестируем get_books_with_specific_genre с параметризацией
    @pytest.mark.parametrize(
        "genre, expected_books",
        [
            ("Фантастика", ["Фантастика1", "Фантастика2"]),
            ("Ужасы", ["Ужасы1"]),
            ("Детективы", []),
            ("Мультфильмы", []),
            ("Комедии", []),
            ("Неизвестный", []),  # несуществующий жанр
        ]
    )
    def test_get_books_with_specific_genre(self, genre, expected_books):
        """Параметризованный тест получения книг по разным жанрам."""
        # Добавляем тестовые данные
        books_data = [
            ("Фантастика1", "Фантастика"),
            ("Фантастика2", "Фантастика"), 
            ("Ужасы1", "Ужасы"),
            ("Комедия1", "Комедии"),
        ]
        
        for book_name, book_genre in books_data:
            self.collector.add_new_book(book_name)
            self.collector.set_book_genre(book_name, book_genre)
        
        result = self.collector.get_books_with_specific_genre(genre)
        assert sorted(result) == sorted(expected_books)

    # Тестируем get_books_genre
    def test_get_books_genre(self):
        """Возвращает полный словарь books_genre."""
        self.collector.add_new_book("Книга1")
        self.collector.set_book_genre("Книга1", "Фантастика")
        self.collector.add_new_book("Книга2")
        self.collector.set_book_genre("Книга2", "Детективы")

        result = self.collector.get_books_genre()
        expected = {"Книга1": "Фантастика", "Книга2": "Детективы"}
        assert result == expected

    # Тестируем get_books_for_children
    def test_get_books_for_children(self):
        """Книги без возрастного рейтинга (не в genre_age_rating)."""
        # genre_age_rating = ['Ужасы', 'Детективы']
        # Без рейтинга: ['Фантастика', 'Мультфильмы', 'Комедии']
        
        self.collector.add_new_book("Мультик")
        self.collector.set_book_genre("Мультик", "Мультфильмы")
        self.collector.add_new_book("Комедия")
        self.collector.set_book_genre("Комедия", "Комедии")
        self.collector.add_new_book("Фантастика")
        self.collector.set_book_genre("Фантастика", "Фантастика")
        self.collector.add_new_book("Ужасы")
        self.collector.set_book_genre("Ужасы", "Ужасы")
        self.collector.add_new_book("Детектив")
        self.collector.set_book_genre("Детектив", "Детективы")

        result = self.collector.get_books_for_children()
        expected = ["Мультик", "Комедия", "Фантастика"]
        assert sorted(result) == sorted(expected)

    # Тестируем add_book_in_favorites
    def test_add_book_in_favorites_valid(self):
        """Добавление книги в избранное."""
        self.collector.add_new_book("Любимая")
        self.collector.add_book_in_favorites("Любимая")
        assert "Любимая" in self.collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_nonexistent(self):
        """Нельзя добавить в избранное книгу, которой нет в books_genre."""
        self.collector.add_book_in_favorites("Нет в списке")
        assert len(self.collector.get_list_of_favorites_books()) == 0

    def test_add_book_in_favorites_duplicate(self):
        """Повторное добавление в избранное не должно работать."""
        self.collector.add_new_book("Дубликат")
        self.collector.add_book_in_favorites("Дубликат")
        self.collector.add_book_in_favorites("Дубликат")
        assert len(self.collector.get_list_of_favorites_books()) == 1

    # Тестируем delete_book_from_favorites
    def test_delete_book_from_favorites(self):
        """Удаление книги из избранного."""
        self.collector.add_new_book("Удалить")
        self.collector.add_book_in_favorites("Удалить")
        self.collector.delete_book_from_favorites("Удалить")
        assert "Удалить" not in self.collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_not_in_favorites(self):
        """Удаление книги, которой нет в избранном, не должно вызывать ошибку."""
        self.collector.delete_book_from_favorites("Не в избранном")
        assert len(self.collector.get_list_of_favorites_books()) == 0

    # Тестируем get_list_of_favorites_books
    def test_get_list_of_favorites_books(self):
        """Возвращает список избранных книг."""
        self.collector.add_new_book("Фаворит1")
        self.collector.add_new_book("Фаворит2")
        self.collector.add_book_in_favorites("Фаворит1")
        self.collector.add_book_in_favorites("Фаворит2")

        result = self.collector.get_list_of_favorites_books()
        expected = ["Фаворит1", "Фаворит2"]
        assert sorted(result) == sorted(expected)