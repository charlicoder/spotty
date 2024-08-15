from django.core.management.base import BaseCommand
from pathlib import Path
import json
from apps.books.models import Book
import pandas as pd


class Command(BaseCommand):
    help = 'Loading books data into RDS'

    def populate_data(self):
        file_path = Path(__file__).parent.parent.parent.parent.parent / f'data/500k_books.json'
        try:
            df = pd.read_json(file_path)
            for i in range(100, 10000, 100):
                j = i+100
                books = df[i:j]
                book_list = []
                for i, book in books.iterrows():
                    book_instance = Book(
                        id=book['id'],
                        title=book['title'],
                        authorid=book['author_id'],  # assuming author_id is a ForeignKey field
                        description=book['description'],
                        publisher=book['publisher'],
                        series_name=book['series_name'],
                        average_rating=book['average_rating']
                    )
                    
                    book_list.append(book_instance)

                Book.objects.bulk_create(book_list)
                
                
                    

        except Exception as e:
            print(f"{e}")

    def handle(self, *args, **options):
        # Your custom code goes here
        self.populate_data()
        self.stdout.write(self.style.SUCCESS('Successfully loaded books data!'))