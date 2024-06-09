from classes.many_to_many import Author
from classes.many_to_many import Article
from classes.many_to_many import Magazine

import pytest

class TestMagazine:
    """Magazine in many_to_many.py"""
    
    def test_has_name(self):
        """Magazine is instantiated with a name"""
        Magazine = Magazine(name="Ace of Spades", city="SAC")

        assert Magazine.name == "Ace of Spades"

    def test_name_is_mutable_string(self):
        """names are mutable strings"""
        Magazine_1 = Magazine(name="Ace of Spades", city="SAC")
        assert isinstance(Magazine_1.name, str)

        Magazine_1.name = "MoonDust"
        assert isinstance(Magazine_1.name, str)
        assert Magazine_1.name == "MoonDust"

        # comment out the next two lines if using Exceptions
        # Magazine_1.name = 7
        # assert Magazine_1.name == "MoonDust"

        # uncomment the next two lines if using Exceptions
        with pytest.raises(Exception):
            Magazine_1.name = 7

    def test_name_has_length(self):
        """names are longer than 0 characters"""
        Magazine_1 = Magazine(name="Ace of Spades", city="SAC")
        assert len(Magazine_1.name) > 0

        # comment out the next two lines if using Exceptions
        # Magazine_1.name = ""
        # assert Magazine_1.name == "Ace of Spades"

        # uncomment the next two lines if using Exceptions
        with pytest.raises(Exception):
            Magazine_1.name = ""

    def test_has_city(self):
        """Magazine is instantiated with a city"""
        Magazine = Magazine(name="Ace of Spades", city="SAC")

        assert Magazine.city == "SAC"

    def test_city_is_mutable_string(self):
        """cities are mutable strings"""
        Magazine_1 = Magazine(name="Ace of Spades", city="SAC")
        assert isinstance(Magazine_1.city, str)

        Magazine_1.city = "NYC"
        assert isinstance(Magazine_1.city, str)
        assert Magazine_1.city == "NYC"

        # comment out the next two lines if using Exceptions
        # Magazine_1.city = 7
        # assert Magazine_1.city == "NYC"

        # uncomment the next two lines if using Exceptions
        with pytest.raises(Exception):
            Magazine_1.city = 7

    def test_city_has_length(self):
        """cities are longer than 0 characters"""
        Magazine_1 = Magazine(name="Ace of Spades", city="SAC")
        assert len(Magazine_1.city) > 0

        # comment out the next two lines if using Exceptions
        # Magazine_1.city = ""
        # assert Magazine_1.city == "SAC"

        # uncomment the next two lines if using Exceptions
        with pytest.raises(Exception):
            Magazine_1.city = ""

    def test_Articles(self):
        """Magazine has many Articles"""
        Author = Author(name="boygenius", hometown="NYC")
        Magazine = Magazine(name="Theatre Max", city="NYC")
        Article_1 = Article(date="Nov 22", Author=Author, Magazine=Magazine)
        Article_2 = Article(date="Nov 27", Author=Author, Magazine=Magazine)

        assert len(Magazine.Articles()) == 2
        assert Article_1 in Magazine.Articles()
        assert Article_2 in Magazine.Articles()

    def test_Articles_of_type_Article(self):
        """Articles must be of type Article"""
        Author = Author(name="boygenius", hometown="NYC")
        Magazine = Magazine(name="Theatre Max", city="NYC")
        Article(date="Nov 22", Author=Author, Magazine=Magazine)
        Article(date="Nov 27", Author=Author, Magazine=Magazine)

        assert all(isinstance(Article, Article) for Article in Magazine.Articles())

    def test_Authors(self):
        """Magazine has many Authors"""
        Author_1 = Author(name="boygenius", hometown="NYC")
        Author_2 = Author(name="Triple Genius", hometown="LA")
        Magazine_1 = Magazine(name="Theatre", city="NYC")
        Article(date="Nov 22", Author=Author_1, Magazine=Magazine_1)
        Article(date="Nov 27", Author=Author_2, Magazine=Magazine_1)

        assert len(Magazine_1.Authors()) == 2
        assert Author_1 in Magazine_1.Authors()
        assert Author_2 in Magazine_1.Authors()

    def test_Authors_of_type_Author(self):
        """Authors must be of type Author"""
        Author_1 = Author(name="boygenius", hometown="NYC")
        Author_2 = Author(name="Triple Genius", hometown="LA")
        Magazine_1 = Magazine(name="Theatre", city="NYC")
        Article(date="Nov 22", Author=Author_1, Magazine=Magazine_1)
        Article(date="Nov 27", Author=Author_2, Magazine=Magazine_1)

        assert all(isinstance(Author, Author) for Author in Magazine_1.Authors())

    def test_Authors_are_unique(self):
        """Authors are unique"""
        Author_1 = Author(name="boygenius", hometown="NYC")
        Author_2 = Author(name="Triple Genius", hometown="LA")
        Magazine_1 = Magazine(name="Theatre", city="NYC")
        Article(date="Nov 22", Author=Author_1, Magazine=Magazine_1)
        Article(date="Nov 27", Author=Author_2, Magazine=Magazine_1)
        Article(date="Nov 29", Author=Author_2, Magazine=Magazine_1)

        assert len(set(Magazine_1.Authors())) == len(Magazine_1.Authors())
        assert len(Magazine_1.Authors()) == 2
        assert Author_1 in Magazine_1.Authors()
        assert Author_2 in Magazine_1.Authors()

    # def test_Article_on(self):
    #     """returns the first Article on that date or None if no Articles exist"""
    #     Author = Author(name="boygenius", hometown="NYC")
    #     Magazine = Magazine(name="Theatre", city="NYC")
    #     Magazine2 = Magazine(name="Ace of Spades", city="SAC")
    #     Author.play_in_Magazine(Magazine=Magazine, date="Nov 22")
    #     Author.play_in_Magazine(Magazine=Magazine2, date="Nov 27")

    #     assert Magazine.Article_on("Nov 22") == Author.Articles()[0]
    #     assert Magazine2.Article_on("Nov 27") == Author.Articles()[1]
    #     assert Magazine.Article_on("Nov 25") is None
