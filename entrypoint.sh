python manage.py migrate --noinput
python manage.py collectstatic --noinput

echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='$SUPER_USER_NAME').exists() or User.objects.create_superuser('$SUPER_USER_NAME', '$SUPER_USER_EMAIL', '$SUPER_USER_PASSWORD')" | python manage.py shell

gunicorn api.wsgi:application --bind 0.0.0.0:8000 --timeout 120