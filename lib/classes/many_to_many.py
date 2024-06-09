class Author:
    def __init__(self, name, hometown):
        self._name = name
        if not isinstance(hometown, str):
            raise Exception("Hometown must be a string")
        self._hometown = hometown
        self._Articles = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise Exception
        if len(value) == 0:
            raise Exception
        self._name = value

    @property
    def hometown(self):
        return self._hometown

    @hometown.setter
    def hometown(self, value):
        raise Exception("The Author's homet own is immutable. You can't change it.")


    # Author has many Articles
    def Articles(self):
        return self._Articles

    def Magazines(self):
        Magazines = set()
        for Article in self._Articles:
            Magazines.add(Article.Magazine)
        return list(Magazines)

    def play_in_Magazine(self, Magazine, date):
        Article = Article(date, self, Magazine)
        self._Articles.append(Article)
        return Article

    def all_introductions(self):
        introductions = []
        for Article in self._Articles:
            introductions.append(Article.introduction())
        return introductions
class Article:
    all = []

    def __init__(self, date, Author, Magazine):
        self.date = date
        self.Author = Author
        self.Magazine = Magazine
        Article.all.append(self)

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        if not isinstance(value, str):
            raise Exception("Date must be a string")
        if len(value) == 0:
            raise Exception("Date cannot be empty")
        self._date = value

    @property
    def Magazine(self):
        return self._Magazine

    @Magazine.setter
    def Magazine(self, value):
        if not isinstance(value, Magazine):
            raise Exception("Magazine must be of type Magazine")
        self._Magazine = value

    @property
    def Author(self):
        return self._Author

    @Author.setter
    def Author(self, value):
        if not isinstance(value, Author):
            raise Exception("Author must be of type Author")
        self._Author = value

    def hometown_show(self):
        return self.Author.hometown == self.Magazine.city

    def introduction(self):
        return f"Hello {self.Magazine.city}!!!!! We are {self.Author.name} and we're from {self.Author.hometown}"

class Magazine:
    def __init__(self, name, city):
        self.name = name
        self.city = city

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise Exception("Name must be a string")
        if len(value) == 0:
            raise Exception("Name cannot be empty")
        self._name = value

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        if not isinstance(value, str):
            raise Exception("City must be a string")
        if len(value) == 0:
            raise Exception("City cannot be empty")
        self._city = value

    def Articles(self):
        Articles = []
        for Article in Article.all:
            if Article.Magazine == self:
                Articles.append(Article)
        return Articles

    def Authors(self):
        Authors = set()
        for Article in self.Articles():
            Authors.add(Article.Author)
        return list(Authors)
    


Author = Author(name="boygenius", hometown="NYC")
Magazine = Magazine(name="Theatre", city="NYC")
Article = Author.play_in_Magazine(Magazine=Magazine, date="Nov 22")
print(Article.introduction())