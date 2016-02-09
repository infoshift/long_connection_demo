api:
	gunicorn -b 0.0.0.0:80 api:app --access-logfile - --error-logfile - --timeout 240 -k gevent

web:
	gunicorn -b 0.0.0.0:80 web:app --access-logfile - --error-logfile - --timeout 120 -k gevent
