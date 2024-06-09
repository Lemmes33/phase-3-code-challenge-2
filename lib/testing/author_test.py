import pytest
from classes.many_to_many import Author
from classes.many_to_many import Article
from classes.many_to_many import Magazine

class TestAuthor:
    """Author in many_to_many.py"""
    
    def test_has_name(self):
        """Author is instantiated with a name"""
        Author_1 = Author(name="boygenius", hometown="NYC")
        Author_2 = Author(name="spicegurls", hometown="London")

        assert Author_1.name == "boygenius"
        assert Author_2.name == "spicegurls"

    def test_name_is_mutable_string(self):
        """names are mutable strings"""
        Author_1 = Author(name="boygenius", hometown="NYC")
        assert isinstance(Author_1.name, str)

        Author_1.name = "spicegurls"
        assert isinstance(Author_1.name, str)
        assert Author_1.name == "spicegurls" 

        # comment out the next two lines if using Exceptions
        # Author_1.name = 7
        # assert Author_1.name == "spicegurls"

        # uncomment the next two lines if using Exceptions
        with pytest.raises(Exception):
            Author_1.name = 7

    def test_name_has_length(self):
        """names are longer than 0 characters"""
        Author_1 = Author(name="boygenius", hometown="NYC")
        assert len(Author_1.name) > 0

        # comment out the next two lines if using Exceptions
        # Author_1.name = ""
        # assert Author_1.name == "boygenius"

        # uncomment the next two lines if using Exceptions
        with pytest.raises(Exception):
            Author_1.name = ""

    def test_has_hometown(self):
        """Author is instantiated with a hometown"""
        Author_1 = Author(name="boygenius", hometown="NYC")
        Author_2 = Author(name="spicegurls", hometown="London")

        assert Author_1.hometown == "NYC"
        assert Author_2.hometown == "London"

    def test_hometown_is_immutable_string(self):
        """hometowns are immutable strings"""
        Author_1 = Author(name="boygenius", hometown="NYC")
        assert isinstance(Author_1.hometown, str)

        # comment out the next three lines if using Exceptions
        # Author_1.hometown = "Boston"
        # assert isinstance(Author_1.hometown, str)
        # assert Author_1.hometown == "NYC"

        # comment out the next two lines if using Exceptions
        # Author_1.hometown = 7
        # assert Author_1.hometown == "NYC"

        # uncomment the next two lines if using Exceptions
        with pytest.raises(Exception):
            Author_1.hometown = "Boston"

        # uncomment the next two lines if using Exceptions
        with pytest.raises(Exception):
            Author_1 = Author(name="boygenius", hometown=7)

    def test_hometown_has_length(self):
        """hometowns are longer than 0 characters"""
        Author_1 = Author(name="boygenius", hometown="NYC")
        assert len(Author_1.hometown) > 0

        # comment out the next two lines if using Exceptions
        # Author_1.hometown = ""
        # assert Author_1.hometown == "NYC"

        # uncomment the next two lines if using Exceptions
        with pytest.raises(Exception):
            Author_1.hometown = ""

    def test_Articles(self):
        """Author has many Articles"""
        Author = Author(name="boygenius", hometown="NYC")
        Magazine = Magazine(name="Theatre", city="NYC")
        Article_1 = Article(date="Nov 22", Author=Author, Magazine=Magazine)
        Article_2 = Article(date="Nov 27", Author=Author, Magazine=Magazine)

        assert len(Author.Articles()) == 2
        assert Article_1 in Author.Articles()
        assert Article_2 in Author.Articles()

    def test_Articles_of_type_Article(self):
        """Articles must be of type Article"""
        Author = Author(name="boygenius", hometown="NYC")
        Magazine = Magazine(name="Theatre", city="NYC")
        Article(date="Nov 22", Author=Author, Magazine=Magazine)
        Article(date="Nov 27", Author=Author, Magazine=Magazine)

        assert all(isinstance(Article, Article) for Article in Author.Articles())

    def test_Magazines(self):
        """Author has many Magazines"""
        Author = Author(name="boygenius", hometown="NYC")
        Magazine_1 = Magazine(name="Theatre", city="NYC")
        Magazine_2 = Magazine(name="Ace of Spades", city="SAC")
        Article(date="Nov 22", Author=Author, Magazine=Magazine_1)
        Article(date="Nov 27", Author=Author, Magazine=Magazine_2)

        assert len(Author.Magazines()) == 2
        assert Magazine_1 in Author.Magazines()
        assert Magazine_2 in Author.Magazines()

    def test_Magazines_of_type_Magazine(self):
        """Magazines must be of type Magazine"""
        Author = Author(name="boygenius", hometown="NYC")
        Magazine_1 = Magazine(name="Theatre", city="NYC")
        Magazine_2 = Magazine(name="Ace of Spades", city="SAC")
        Article(date="Nov 22", Author=Author, Magazine=Magazine_1)
        Article(date="Nov 27", Author=Author, Magazine=Magazine_2)

        assert all(isinstance(Magazine, Magazine) for Magazine in Author.Magazines())

    def test_Magazines_are_unique(self):
        """Magazines are unique"""
        Author = Author(name="boygenius", hometown="NYC")
        Magazine_1 = Magazine(name="Theatre", city="NYC")
        Magazine_2 = Magazine(name="Ace of Spades", city="SAC")
        Article(date="Nov 22", Author=Author, Magazine=Magazine_1)
        Article(date="Nov 27", Author=Author, Magazine=Magazine_2)
        Article(date="Nov 29", Author=Author, Magazine=Magazine_2)

        assert len(set(Author.Magazines())) == len(Author.Magazines())
        assert len(Author.Magazines()) == 2
        assert Magazine_1 in Author.Magazines()
        assert Magazine_2 in Author.Magazines()

    def test_play_in_Magazine(self):
        """creates and returns a new Article for that Author"""
        Author = Author(name="boygenius", hometown="NYC")
        Magazine = Magazine(name="Theatre", city="NYC")
        Magazine2 = Magazine(name="Ace of Spades", city="SAC")
        Article_1 = Author.play_in_Magazine(Magazine=Magazine, date="Nov 22")

        assert len(Author.Articles()) == 1
        assert Author.Articles()[0].Author == Author
        assert Author.Articles()[0].Magazine == Magazine
        assert isinstance(Article_1, Article)

        Article_2 = Author.play_in_Magazine(Magazine=Magazine2, date="Nov 27")
        assert len(Author.Articles()) == 2
        assert Author.Articles()[1].Author == Author
        assert Author.Articles()[1].Magazine == Magazine2
        assert isinstance(Article_2, Article)

    def test_all_introductions(self):
        """returns all introductions for the Author"""
        Author = Author(name="boygenius", hometown="NYC")
        Magazine = Magazine(name="Theatre", city="NYC")
        Magazine2 = Magazine(name="Ace of Spades", city="SAC")
        Author.play_in_Magazine(Magazine=Magazine, date="Nov 22")
        Author.play_in_Magazine(Magazine=Magazine2, date="Nov 27")

        assert (
            Author.all_introductions()[0]
            == "Hello NYC!!!!! We are boygenius and we're from NYC"
        )
        assert (
            Author.all_introductions()[1]
            == "Hello SAC!!!!! We are boygenius and we're from NYC"
        )
