#!/usr/bin/env bash
# exit on error
set -o errexit

echo "Instalando dependências..."
pip install -r requirements.txt

echo "Coletando arquivos estáticos..."
python manage.py collectstatic --no-input

echo "Aplicando migrações..."
python manage.py migrate

# Importar dados do arquivo JSON
python manage.py loaddata data.json
