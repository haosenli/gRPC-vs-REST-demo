from concurrent import futures
import grpc
import data_service_pb2
import data_service_pb2_grpc
import config


def getDataFromApi(count):
    with grpc.insecure_channel(f"localhost:{config.DATA_SERVER_PORT}") as channel:
        stub = data_service_pb2_grpc.DataServiceStub(channel)
        request = data_service_pb2.DataRequest(count=count)
        print("Retrieved data from data server")
        return stub.GetData(request)


class DataServiceServicer(data_service_pb2_grpc.DataServiceServicer):
    def GetData(self, request, context):
        resp = getDataFromApi(request.count)
        print("Returning data from data repeater 1")
        return data_service_pb2.DataResponse(data=resp.data)


def serve():
    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=10), options=config.OPTIONS
    )
    data_service_pb2_grpc.add_DataServiceServicer_to_server(
        DataServiceServicer(), server
    )
    server.add_insecure_port(f"[::]:{config.DATA_REPEATER_PORT1}")
    print(f"Running server on port: {config.DATA_REPEATER_PORT1}")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    # Get user Input
    # count = int(input("Please input max count of data items: "))
    # getDataFromApi(10)
    serve()
