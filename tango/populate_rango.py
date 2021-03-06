import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'tango.settings')

import django
django.setup()

from rango.models import Category, Page


def populate():
    python_pages = [
        {'title': 'Official Python Tutorial',
         'url': 'https://docs.python.org/3/tutorial/',
         'views': 128},
        {'title': 'How to Think like a Computer Scientist',
         'url': 'https://greenteapress.com/wp/think-python/',
         'views': 64},
        {'title': 'Learn Python in 10 Minutes',
         'url': 'https://www.stavros.io/tutorials/python/',
         'views': 32},
    ]


    django_pages = [
        {"title": "Official Django Tutorial",
         "url": "https://docs.djangoproject.com/en/1.10/intro/tutorial01//",
         'views': 16},
        {"title": "Django Rocks",
         "url": "http://www.djangorocks.com/",
         'views': 8},
        {"title": "How to Tango with Django",
         "url": "http://www.tangowithdjango.com/",
         'views': 4}]

    other_pages = [
        {"title": "Bottle",
         "url": "http://bottlepy.org/docs/dev/",
         'views': 2},
        {"title": "Flask",
         "url": "http://flask.pocoo.org",
         'views': 1}]

    categories = {
        'Python': {'pages': python_pages,
                   'views': 128,
                   'likes': 64},
        'Django': {'pages': django_pages,
                   'views': 64,
                   'likes': 32},
        'Other Frameworks': {'pages': other_pages,
                             'views': 32,
                             'likes': 16}
    }

    for category, data in categories.items():
        c = add_cat(category, data['views'], data['likes'])
        for p in data['pages']:
            add_page(c, p['title'], p['url'], p['views'])

    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print(f'{str(c)} - {str(p)}')


def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url = url
    p.views = views
    p.save()

    return p


def add_cat(name, views=0, likes=0):
    c = Category.objects.get_or_create(name=name)[0]
    c.views = views
    c.likes = likes
    c.save()

    return c


if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()
