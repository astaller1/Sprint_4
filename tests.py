import pytest
from main import BooksCollector


@pytest.fixture
def collector():
    return BooksCollector()


class TestBooksCollector:

    def test_add_new_book_add_two_books(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_books_rating()) == 2

    @pytest.mark.parametrize('title', [
        'А', 
        'Преступление и наказание', 
        'Название, в котором ровно сорок символов'
    ])
    def test_add_new_book_valid_title_length(self, collector, title):
        collector.add_new_book(title)

        assert title in collector.books_genre

    @pytest.mark.parametrize('invalid_title', [
        '',
        'Название содержит ровно сорок один символ'
    ])
    def test_add_new_book_invalid_title_length(self, collector, invalid_title):
        collector.add_new_book(invalid_title)

        assert invalid_title not in collector.books_genre

    def test_add_new_book_dublicate_not_allowed(self, collector):
        collector.add_new_book('Возрождение')
        collector.add_new_book('Возрождение')

        assert len(collector.books_genre) == 1

    def test_set_book_genre_book_exists_and_genre_exists(self, collector):
        collector.add_new_book('Снеговик')
        collector.set_book_genre('Снеговик', 'Детективы')

        assert collector.books_genre['Снеговик'] == 'Детективы'

    def test_get_book_genre_book_and_genre_correctly_matched(self, collector):
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')

        assert collector.get_book_genre('Оно') == 'Ужасы'

    def test_get_books_with_specific_genre_filtration(self, collector):
        collector.add_new_book('Снеговик')
        collector.set_book_genre('Снеговик','Детективы')
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')

        assert collector.get_books_with_specific_genre('Детективы') == ['Снеговик']

    def test_get_books_genre_returns_current_dict(self, collector):
        collector.add_new_book('Оно')

        assert collector.get_books_genre() == {'Оно': ''}

    def test_get_books_for_children_returns_only_books_for_children(self, collector):
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')

        assert 'Гарри Поттер' in collector.get_books_for_children() and 'Оно' not in collector.get_books_for_children()

    def test_add_book_in_favorites_successfully_adds_book(self, collector):
        collector.add_new_book('Оно')
        collector.add_book_in_favorites('Оно')

        assert 'Оно' in collector.favorites

    def test_delete_book_from_favorites_successfully_removes_book(self, collector):
        collector.add_new_book('Возрождение')
        collector.add_book_in_favorites('Возрождение')
        collector.delete_book_from_favorites('Возрождение')
        
        assert 'Возрождение' not in collector.favorites

    def test_get_list_of_favorites_books_shows_current_favorite_list(self, collector):
        collector.add_new_book('Оно')
        collector.add_book_in_favorites('Оно')
        collector.delete_book_from_favorites('Оно')

        assert 'Оно' not in collector.get_list_of_favorites_books()
 