#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate

# create superuser if missing
python << EOF
import os
from django.contrib.auth import get_user_model

User = get_user_model()

# Verifica se o superusuário já existe, caso contrário, cria um novo
if not User.objects.filter(username=os.environ["DJANGO_SUPERUSER_USERNAME"]).exists():
    User.objects.create_superuser(
        os.environ["DJANGO_SUPERUSER_USERNAME"],
        os.environ["DJANGO_SUPERUSER_EMAIL"],
        os.environ["DJANGO_SUPERUSER_PASSWORD"]
    )
EOF