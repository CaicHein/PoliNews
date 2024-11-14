#!/usr/bin/env bash
# exit on error
set -o errexit

echo "Instalando dependências..."
pip install -r requirements.txt

echo "Coletando arquivos estáticos..."
python manage.py collectstatic --no-input

echo "Aplicando migrações..."
python manage.py migrate

echo "Verificando superusuário..."
python << EOF
import os
from django.contrib.auth import get_user_model

User = get_user_model()
username = os.environ.get("DJANGO_SUPERUSER_USERNAME")
email = os.environ.get("DJANGO_SUPERUSER_EMAIL")
password = os.environ.get("DJANGO_SUPERUSER_PASSWORD")

if username and email and password:
    if not User.objects.filter(username=username).exists():
        print("Criando superusuário...")
        User.objects.create_superuser(username, email, password)
    else:
        print("Superusuário já existe.")
else:
    print("Variáveis de ambiente do superusuário não configuradas corretamente.")
EOF
