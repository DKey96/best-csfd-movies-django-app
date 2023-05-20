# Best CSFD movies

This project aims at:
- scraping [CSFD's](https://www.csfd.cz/zebricky/nejlepsi-filmy/?show=complete​) best 300 movies.
- creating a web app for getting information about the movies/actors.

### How to use?
#### Scraping the top 300 movies
- For scraping the top 300 movies out of CSFD's website, just run `python manage.py scrape_movies`.
- All the movies will be scraped and directly added into the database. (Currently used SQLite).
- For databases with allowed concurrency, there is also an asynchronous command `python manage.py scrape_movies_async`.

### Searching the movies
- To search the movies and browse the views, just run `python manage.py runserver` and go to the `localhost:8000`.
- You can then start searching for movies or actors via the search field.
