# lib/magazine.py

from lib.article import Article

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (2 <= len(value) <= 16):
            raise Exception("Name must be a string between 2 and 16 characters")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise Exception("Category must be a non-empty string")
        self._category = value

    def articles(self):
        return [a for a in Article.all if a.magazine == self]

    def contributors(self):
        return list(set(article.author for article in self.articles()))

    def article_titles(self):
        titles = [a.title for a in self.articles()]
        return titles if titles else None

    def contributing_authors(self):
        authors = [a.author for a in self.articles()]
        return list({a for a in authors if authors.count(a) > 2}) or None

    @classmethod
    def top_publisher(cls):
        mags = {}
        for a in Article.all:
            mags[a.magazine] = mags.get(a.magazine, 0) + 1
        return max(mags, key=mags.get) if mags else None
