run:
	gunicorn --worker-class gthread --threads 5 -t 3600 -b 0.0.0.0:5001 --chdir ./camera_1 camera_1:app --daemon
	gunicorn --worker-class gthread --threads 5 -t 3600 -b 0.0.0.0:5002 --chdir ./camera_2 camera_2:app --daemon
	gunicorn --worker-class gthread --threads 5 -t 3600 -b 0.0.0.0:5003 --chdir ./camera_3 camera_3:app --daemon
	gunicorn --worker-class gthread --threads 5 -t 3600 -b 0.0.0.0:5004 --chdir ./camera_4 camera_4:app --daemon
	gunicorn --worker-class gthread --threads 5 -t 3600 -b 0.0.0.0:5005 --chdir ./camera_5 camera_5:app --daemon
	gunicorn --worker-class gthread --threads 5 -t 3600 -b 0.0.0.0:5006 --chdir ./camera_6 camera_6:app

kill:
	pkill gunicorn