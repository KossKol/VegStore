import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

django.setup()

from store.models import Profile

data = ({'id': '1'},
        {'id': '2'},
        {'id': '3'},
        {'id': '4'},
        {'id': '5'},
        {'id': '6'}
        )

objects_to_create = [Profile(user_id=val['id']) for val in data]

Profile.objects.bulk_create(objects_to_create)