from django.core.management.base import BaseCommand
from books.scraper import scrape_books

class Command(BaseCommand):
    help = 'Scrape books from books.toscrape.com'

    def handle(self, *args, **kwargs):
        self.stdout.write('Starting scraper...')
        count = scrape_books(max_pages=3)
        self.stdout.write(f'Successfully scraped {count} books!')