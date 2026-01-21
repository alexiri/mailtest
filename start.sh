#!/usr/bin/env sh
set -e

python manage.py migrate --noinput

python manage.py runserver 0.0.0.0:8000 &
server_pid=$!

python - <<'PY'
import socket
import time
from sdnotify import SystemdNotifier

host = "127.0.0.1"
port = 8000
deadline = time.time() + 60

while time.time() < deadline:
	try:
		with socket.create_connection((host, port), timeout=1):
			SystemdNotifier().notify("READY=1")
			break
	except OSError:
		time.sleep(0.5)
else:
	SystemdNotifier().notify("STATUS=Server failed to start")
PY

wait "$server_pid"
