import threading

TARGETS = {{PAYLOAD_TARGETS}}

exec("from {{PAYLOAD_NAME}} import exploit")


def main():
    if len(TARGETS) == 0:
        return
    for host in TARGETS:
        ct = threading.Thread(target=exploit, args=({{PAYLOAD_ARGS}}))
        ct.start()
