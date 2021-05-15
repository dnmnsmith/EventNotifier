import argparse
import sys
import pathlib

from concurrent import futures
import logging

import grpc
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2

import PythonServer_pb2
import PythonServer_pb2_grpc

def main():
    parser = argparse.ArgumentParser()

    ipGroup = parser.add_mutually_exclusive_group(required=False)
    ipGroup.add_argument("-s", "--server", help="Server Name", default="webpi2")

    parser.add_argument("-p", "--port", type=int, help="Server Port", default=50051)
    parser.add_argument("-m", "--measurement", help="Measurement Name", default="Temperature")   

    locGroup = parser.add_mutually_exclusive_group(required=True)
    locGroup.add_argument("-c", "--sensor", help="Sensor Code", default=None)
    locGroup.add_argument("-l", "--location", help="Location", default=None)
    
    parser.add_argument("-v", "--value", help="value", default=None)

    args = parser.parse_args()

    with grpc.insecure_channel(target="{}:{}".format(args.server, args.port),
                            options=[('grpc.lb_policy_name', 'pick_first'),
                                    ('grpc.enable_retries', 0),
                                    ('grpc.keepalive_timeout_ms', 10000)
                                    ]) as channel:
        stub = PythonServer_pb2_grpc.EventServerStub(channel)

        if args.location:
            # Timeout in seconds.
            # Please refer gRPC Python documents for more detail. https://grpc.io/grpc/python/grpc.html
            response = stub.NotifyLocationEvent(
                PythonServer_pb2.LocationEvent(
                    Location=args.location, 
                    MeasType=args.measurement,
                    MeasValue=args.value),
                timeout=10)
        else:
            response = stub.NotifySensorEvent(
                PythonServer_pb2.SensorEvent(
                    Sensor=args.sensor, 
                    MeasType=args.measurement,
                    MeasValue=args.value),
                timeout=10)
            
if __name__ == "__main__":
    # execute only if run as a script
    main()
