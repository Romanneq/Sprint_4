
from main import BooksCollector

class TestBooksCollector:

    def test_add_new_book_add_two_books(self): # Проверка добавления двух книг
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    import pytest


    @pytest.mark.parametrize('name', ['Гарри Поттер'])
    def test_get_list_of_favorites_books_get_list(self, name): # Проверка отображения новой книги в списке избранных книг
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        assert name in collector.get_list_of_favorites_books()

    @pytest.mark.parametrize('name', ['Гарри Поттер'])
    def test_get_list_of_favorites_books_list_not_empty(self, name): # Проверка отсутствия пустого списка после добавления книги в список избранных книг
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        assert collector.get_list_of_favorites_books() != []

    @pytest.mark.parametrize('name', ['Гарри Поттер'])
    def test_delete_book_from_favorites_delete_book(self, name): # Проверка удаления книги из списка избранных книг
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        collector.delete_book_from_favorites(name)
        assert name not in collector.favorites

    @pytest.mark.parametrize('name', ['Гарри Поттер'])
    def test_add_book_in_favorites_adding_to_favorites(self, name): # Проверка добавления книги в список избранных книг
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        assert name in collector.favorites

    @pytest.mark.parametrize('name, genre', [['Гарри Поттер','Фантастика']])
    def test_get_books_with_specific_genre_conclusion_list_genre(self, name,genre): # Проверка вывода списка книг с определенным жанром
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        books_with_specific_genre_names = collector.get_books_with_specific_genre(genre)
        books_with_specific_genre = [collector.get_book_genre(book) for book in books_with_specific_genre_names]
        assert genre in books_with_specific_genre

    @pytest.mark.parametrize('name, genre', [['Гарри Поттер', 'Фантастика']])
    def test_set_book_genre_establishment_genre(self, name, genre): # Проверка установления жанра у добавленной книги
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == genre

    @pytest.mark.parametrize('name', ['Гарри Поттер']) # Проверка добавления книги
    def test_add_new_book_add_book(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert len(collector.get_books_genre()) == 1

    @pytest.mark.parametrize('name, genre', [['Гарри Поттер', '']]) # Проверка добавления книги без жанра
    def test_add_new_book_not_genre(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == ''

    @pytest.mark.parametrize('name, genre', [['Гарри Поттер', 'Фантастика']])  # Проверка отсутствия книг с возрастным рейтингом в списке книг для детей.
    def test_get_books_for_children_not_genre_age_rating(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        list_names_books_for_children = collector.get_books_for_children()
        list_genre_for_children = [collector.get_book_genre(book) for book in list_names_books_for_children]
        assert collector.genre_age_rating not in list_genre_for_children