run:
	gunicorn --worker-class gthread --threads 5 -t 3600 -b 127.0.0.1:5003 camera_3:app