.DEFAULT_GOAL := all

EventNotifier:
	python -m grpc_tools.protoc -I../dsws --python_out=.  --grpc_python_out=. dsws.proto


all: EventNotifier

clean:
	rm -f dsws_pb2.py
	rm -f dsws_pb2_grpc.py

install:
	mkdir -p /usr/local/bin/EventNotifier
	cp dsws_pb2_grpc.py  dsws_pb2.py  __init__.py  __main__.py /usr/local/bin/EventNotifier
	cp notifyEvent /usr/local/bin
	chmod 775 /usr/local/bin/notifyEvent
