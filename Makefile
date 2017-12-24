run:
	gunicorn -w 2 -t 3600 -b 127.0.0.1:5000 wsgi:app