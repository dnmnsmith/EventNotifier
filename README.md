# EventNotifier
EventNotifier for weather/home monitoring system. Re-write in Python/gRpc

Relies on PythonServer.proto in the server to define the RPC for google RPC.

Generate using:

<b>python -m grpc_tools.protoc -I..\PythonServer --python_out=.  --grpc_python_out=. PythonServer.proto</b>
