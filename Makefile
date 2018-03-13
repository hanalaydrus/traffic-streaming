run1:
	gunicorn --worker-class gthread --threads 5 -t 3600 -b 127.0.0.1:5000 camera_1:app
run2:
	gunicorn --worker-class gthread --threads 5 -t 3600 -b 127.0.0.1:5001 camera_2:app
run3:
	gunicorn --worker-class gthread --threads 5 -t 3600 -b 127.0.0.1:5002 camera_3:app
run4:
	gunicorn --worker-class gthread --threads 5 -t 3600 -b 127.0.0.1:5003 camera_4:app
run5:
	gunicorn --worker-class gthread --threads 5 -t 3600 -b 127.0.0.1:5004 camera_5:app
run6:
	gunicorn --worker-class gthread --threads 5 -t 3600 -b 127.0.0.1:5005 camera_6:app