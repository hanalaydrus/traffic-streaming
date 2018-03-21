run:
	gunicorn --worker-class gthread --threads 5 -t 3600 -b 127.0.0.1:5001 --chdir ./camera_1 camera_1:app --daemon
	gunicorn --worker-class gthread --threads 5 -t 3600 -b 127.0.0.1:5002 --chdir ./camera_2 camera_2:app --daemon
	gunicorn --worker-class gthread --threads 5 -t 3600 -b 127.0.0.1:5003 --chdir ./camera_3 camera_3:app --daemon
	gunicorn --worker-class gthread --threads 5 -t 3600 -b 127.0.0.1:5004 --chdir ./camera_4 camera_4:app --daemon
	gunicorn --worker-class gthread --threads 5 -t 3600 -b 127.0.0.1:5005 --chdir ./camera_5 camera_5:app --daemon
	gunicorn --worker-class gthread --threads 5 -t 3600 -b 127.0.0.1:5006 --chdir ./camera_6 camera_6:app --daemon

none:
	pkill gunicorn