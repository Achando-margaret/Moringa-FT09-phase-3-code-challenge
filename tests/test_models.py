import unittest
from models.author import Author
from models.article import Article
from models.magazine import Magazine

class TestModels(unittest.TestCase):
    
    def test_author_creation(self):
        author = Author(1, "John Doe")
        self.assertEqual(author.id, 1)
        self.assertEqual(author.name, "John Doe")
    
    def test_article_creation(self):
        article = Article(1, "Test Title", "Test Content", 1, 1)
        self.assertEqual(article.id, 1)
        self.assertEqual(article.title, "Test Title")
        self.assertEqual(article.content, "Test Content")
        self.assertEqual(article.author_id, 1)
        self.assertEqual(article.magazine_id, 1)
    
    def test_magazine_creation(self):
        magazine = Magazine(1, "Tech Weekly", "Thriller")
        self.assertEqual(magazine.id, 1)
        self.assertEqual(magazine.name, "Tech Weekly")
        self.assertEqual(magazine.genre, "Thriller")
    
    def test_author_articles(self):
        author = Author(1, "John Doe")
        article1 = Article(1, "Title 1", "Content 1", 1, 1)
        article2 = Article(2, "Title 2", "Content 2", 1, 2)
        author.articles = [article1, article2]
        self.assertEqual(len(author.articles), 2)
        self.assertEqual(author.articles[0].title, "Title 1")
        self.assertEqual(author.articles[1].title, "Title 2")
    
    def test_magazine_articles(self):
        magazine = Magazine(1, "Tech Weekly", "Tech")
        article1 = Article(1, "Title 1", "Content 1", 1, 1)
        article2 = Article(2, "Title 2", "Content 2", 2, 1)
        magazine.articles = [article1, article2]
        self.assertEqual(len(magazine.articles), 2)
        self.assertEqual(magazine.articles[0].title, "Title 1")
        self.assertEqual(magazine.articles[1].title, "Title 2")
    
    def test_author_to_string(self):
        author = Author(1, "John Doe")
        self.assertEqual(str(author), "Author: John Doe")
    
    def test_article_to_string(self):
        article = Article(1, "Test Title", "Test Content", 1, 1)
        self.assertEqual(str(article), "Article: Test Title by Author ID: 1 in Magazine ID: 1")
    
    def test_magazine_to_string(self):
        magazine = Magazine(1, "Tech Weekly", "Tech")
        self.assertEqual(str(magazine), "Magazine: Tech Weekly, Genre: Tech")
    
    def test_invalid_author_creation(self):
        with self.assertRaises(ValueError):
            Author(0, "")
    
    def test_invalid_article_creation(self):
        with self.assertRaises(ValueError):
            Article(0, "", "", 0, 0)
    
    def test_invalid_magazine_creation(self):
        with self.assertRaises(ValueError):
            Magazine(0, "", "")

if __name__ == "__main__":
    unittest.main()
