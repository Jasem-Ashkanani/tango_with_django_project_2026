import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()

from rango.models import Category, Page

def add_page(cat, title, url, views=0):
    page = Page.objects.get_or_create(category=cat, title=title)[0]
    page.url = url
    page.views = views
    page.save()
    return page

def add_cat(name, views=0, likes=0):
    cat = Category.objects.get_or_create(name=name)[0]
    cat.views = views
    cat.likes = likes
    cat.save()
    return cat

def populate():
    python_cat = add_cat('Python', views=128, likes=64)
    django_cat = add_cat('Django', views=64, likes=32)
    other_cat = add_cat('Other Frameworks', views=32, likes=16)

    add_page(python_cat, 'Official Python Tutorial', 'https://docs.python.org/3/tutorial/')
    add_page(python_cat, 'How to Think like a Computer Scientist', 'http://www.greenteapress.com/thinkpython/')
    add_page(python_cat, 'Learn Python in 10 Minutes', 'https://www.korokithakis.net/tutorials/python/')

    add_page(django_cat, 'Official Django Tutorial', 'https://docs.djangoproject.com/en/2.2/intro/tutorial01/')
    add_page(django_cat, 'Django Rocks', 'http://www.djangorocks.com/')
    add_page(django_cat, 'How to Tango with Django', 'http://www.tangowithdjango.com/')

    add_page(other_cat, 'Bottle', 'http://bottlepy.org/docs/dev/')
    add_page(other_cat, 'Flask', 'http://flask.pocoo.org')

if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()