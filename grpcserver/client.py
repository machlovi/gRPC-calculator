from __future__ import print_function

import logging
import grpc
from grpc_generated_files import calculator_pb2,calculator_pb2_grpc



channel = grpc.insecure_channel('localhost:80')

stud = calculator_pb2_grpc.CalculatorStub(channel)

number=calculator_pb2.Number(value=16)
response=stud.SquareRoot(number)

print(response.value)