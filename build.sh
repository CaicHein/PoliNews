#!/usr/bin/env bash
# exit on error
set -o errexit

# Instala as dependências
pip install -r requirements.txt

# Coleta arquivos estáticos
python manage.py collectstatic --no-input

# Aplica migrações
python manage.py migrate

# Cria superusuário, se ainda não existir
python << END
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
END
