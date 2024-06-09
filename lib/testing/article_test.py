from classes.many_to_many import Author
from classes.many_to_many import Article
from classes.many_to_many import Magazine

import pytest

class TestArticle:
    """Article in many_to_many.py"""
    
    def test_has_date(self):
        """Article is initialized with a date"""
        Author = Author(name="boygenius", hometown="NYC")
        Magazine = Magazine(name="Theatre", city="NYC")
        Article = Article(date="Nov 5", Author=Author, Magazine=Magazine)

        assert Article.date == "Nov 5"

    def test_date_is_mutable_string(self):
        """dates are mutable strings"""
        Author = Author(name="boygenius", hometown="NYC")
        Magazine = Magazine(name="Theatre", city="NYC")
        Article = Article(date="Nov 5", Author=Author, Magazine=Magazine)

        Article.date = "Nov 15"
        assert isinstance(Article.date, str)
        assert Article.date == "Nov 15"

        # comment out the next two lines if using Exceptions
        # Article.date = 15
        # assert Article.date == "Nov 15"

        # uncomment the next two lines if using Exceptions
        with pytest.raises(Exception):
            Article.date = 15

    def test_date_has_length(self):
        """dates are longer than 0 characters"""
        Author = Author(name="boygenius", hometown="NYC")
        Magazine = Magazine(name="Theatre", city="NYC")
        Article = Article(date="Nov 5", Author=Author, Magazine=Magazine)

        assert len(Article.date) > 0

        # comment out the next two lines if using Exceptions
        # Article.date = ""
        # assert Article.date == "Nov 5"

        # uncomment the next two lines if using Exceptions
        with pytest.raises(Exception):
            Article.date = ""

    def test_has_Magazine(self):
        """Article is initialized with a Magazine"""
        Author = Author(name="boygenius", hometown="NYC")
        Magazine = Magazine(name="Theatre", city="NYC")
        Article = Article(date="Nov 5", Author=Author, Magazine=Magazine)

        assert Article.Magazine == Magazine

    def test_Magazine_of_type_Magazine(self):
        """Magazine is of type Magazine"""
        Author = Author(name="boygenius", hometown="NYC")
        Magazine = Magazine(name="Theatre", city="NYC")
        Article = Article(date="Nov 5", Author=Author, Magazine=Magazine)

        # comment out the next two lines if using Exceptions
        # Article.Magazine = "My house"
        # assert Article.Magazine.name == "Theatre"

        assert isinstance(Article.Magazine, Magazine)

        # uncomment the next two lines if using Exceptions
        with pytest.raises(Exception):
            Article.Magazine = "My house"

    def test_Magazine_is_mutable(self):
        """Magazine is mutable"""
        Author = Author(name="boygenius", hometown="NYC")
        Magazine_1 = Magazine(name="Theatre", city="NYC")
        Magazine_2 = Magazine(name="House Extended", city="LA")
        Article = Article(date="Nov 5", Author=Author, Magazine=Magazine_1)

        Article.Magazine = Magazine_2
        assert Article.Magazine.name == "House Extended"
        assert isinstance(Article.Magazine, Magazine)

    def test_has_Author(self):
        """Article is initialized with a Author"""
        Author = Author(name="boygenius", hometown="NYC")
        Magazine = Magazine(name="Theatre", city="NYC")
        Article = Article(date="Nov 5", Author=Author, Magazine=Magazine)

        assert Article.Author == Author

    def test_Author_of_type_Author(self):
        """Article's Author is of type Author"""
        Author = Author(name="boygenius", hometown="NYC")
        Magazine = Magazine(name="Theatre", city="NYC")
        Article = Article(date="Nov 5", Author=Author, Magazine=Magazine)

        # comment out the next two lines if using Exceptions
        # Article.Author = "My friends"
        # assert Article.Author.name == "boygenius"

        assert isinstance(Article.Author, Author)

        # uncomment the next two lines if using Exceptions
        with pytest.raises(Exception):
            Article.Author = "My friends"

    def test_Author_is_mutable(self):
        """Article's Author is mutable"""
        Author_1 = Author(name="boygenius", hometown="NYC")
        Author_2 = Author(name="girlgenius", hometown="Boston")
        Magazine_1 = Magazine(name="Theatre", city="NYC")
        Article = Article(date="Nov 5", Author=Author_1, Magazine=Magazine_1)

        Article.Author = Author_2
        assert Article.Author.name == "girlgenius"
        assert isinstance(Article.Author, Author)

    def test_hometown_show(self):
        """returns True if Article is in Author's hometown, False otherwise"""
        Author = Author(name="boygenius", hometown="NYC")
        Magazine = Magazine(name="Theatre", city="NYC")
        Magazine2 = Magazine(name="Ace of Spades", city="Sac")

        Author.play_in_Magazine(Magazine=Magazine, date="Nov 3")
        Author.play_in_Magazine(Magazine=Magazine2, date="Nov 5")

        assert Author.Articles()[0].hometown_show() is True
        assert Author.Articles()[1].hometown_show() is False

    def test_introduction(self):
        """returns a string with the Author's introduction for this Article"""
        Author = Author(name="boygenius", hometown="NYC")
        Magazine = Magazine(name="Theatre", city="NYC")
        Magazine2 = Magazine(name="Ace of Spades", city="Sac")

        Author.play_in_Magazine(Magazine=Magazine, date="Nov 3")
        Author.play_in_Magazine(Magazine=Magazine2, date="Nov 5")

        assert (
            Author.Articles()[0].introduction()
            == "Hello NYC!!!!! We are boygenius and we're from NYC"
        )
        assert (
            Author.Articles()[1].introduction()
            == "Hello Sac!!!!! We are boygenius and we're from NYC"
        )

    def test_get_all_Articles(self):
        """Article class has all attribute"""
        Article.all = []
        Author = Author(name="boygenius", hometown="NYC")
        Magazine = Magazine(name="Theatre", city="NYC")
        Magazine2 = Magazine(name="Ace of Spades", city="Sac")

        Article_1 = Author.play_in_Magazine(Magazine=Magazine, date="Nov 3")
        Article_2 = Author.play_in_Magazine(Magazine=Magazine2, date="Nov 5")

        assert len(Article.all) == 2
        assert Article_1 in Article.all
        assert Article_2 in Article.all
