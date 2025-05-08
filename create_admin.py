import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GYM.settings')
django.setup()

from django.contrib.auth.models import User

# Create superuser
if not User.objects.filter(username='niraj').exists():
    User.objects.create_superuser(
        username='niraj',
        email='acharyaniraj2058@gmail.com',
        password='niraj123'
    )
    print('Superuser created successfully!')
else:
    print('Superuser already exists!') 