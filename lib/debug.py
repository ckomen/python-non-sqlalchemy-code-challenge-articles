#!/usr/bin/env python3

import ipdb

from classes.many_to_many import Article, Author, Magazine

if __name__ == '__main__':
    print("HELLO! :) Let's debug :vibing_potato:")

    # Sample data
    author1 = Author("Carrie Bradshaw")
    author2 = Author("Topher Grace")

    mag1 = Magazine("Vogue", "Fashion")
    mag2 = Magazine("Architectural Digest", "Architecture")

    article1 = Article(author1, mag1, "How to wear a tutu with style")
    article2 = Article(author1, mag2, "Buildings and You")
    article3 = Article(author1, mag1, "Fashion for Fall")
    article4 = Article(author1, mag1, "The Skirt Awakens")
    article5 = Article(author2, mag1, "Actor Turned Author")

    # Test calls
    print("Author1 Articles:", author1.articles())
    print("Author1 Magazines:", author1.magazines())
    print("Magazine1 Contributors:", mag1.contributors())
    print("Magazine1 Article Titles:", mag1.article_titles())
    print("Magazine1 Contributing Authors:", mag1.contributing_authors())
    print("Top Publisher:", Magazine.top_publisher())

    ipdb.set_trace()
