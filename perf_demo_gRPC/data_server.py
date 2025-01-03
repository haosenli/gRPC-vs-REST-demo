import grpc
from concurrent import futures
import data_service_pb2
import data_service_pb2_grpc
import data_provider
import config


class DataServiceServicer(data_service_pb2_grpc.DataServiceServicer):
    def GetData(self, request, context):
        data = data_provider.get_items(request.count)
        print("Returning data from data server")
        return data_service_pb2.DataResponse(data=data)


def serve():
    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=10), options=config.OPTIONS
    )
    data_service_pb2_grpc.add_DataServiceServicer_to_server(
        DataServiceServicer(), server
    )
    server.add_insecure_port(f"[::]:{config.DATA_SERVER_PORT}")
    print(f"Running server on port: {config.DATA_SERVER_PORT}")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
