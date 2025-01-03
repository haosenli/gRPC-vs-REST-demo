import grpc
import data_service_pb2
import data_service_pb2_grpc
import config
import time
import requests

BENCHMARK_RESULT = {
    "GRPC": {},
    "REST": {},
}


def benchmarkGrpcApi(count):
    t0 = time.time()
    with grpc.insecure_channel(
        f"localhost:{config.GRPC_API_PORT}", options=config.OPTIONS
    ) as channel:
        stub = data_service_pb2_grpc.DataServiceStub(channel)
        request = data_service_pb2.DataRequest(count=count)
        stub.GetData(request)
    t1 = time.time()
    t_diff = t1 - t0
    print(f"gRPC: Retrieved {count} items in {t_diff} seconds")
    BENCHMARK_RESULT["GRPC"][count] = t_diff


def benchmarkRestApi(count):
    t0 = time.time()
    requests.get(f"http://localhost:{config.REST_API_PORT}/items?count={count}")
    t1 = time.time()
    print(f"REST: Retrieved {count} items in {t1 - t0} seconds")
    BENCHMARK_RESULT["REST"][count] = t1 - t0


def comparePerf(count):
    perf_diff = BENCHMARK_RESULT["REST"][count] / BENCHMARK_RESULT["GRPC"][count]
    perf_diff = float(f"{perf_diff:.2f}")
    print(f"REST is {perf_diff}x slower than gRPC with {count} items")


def benchmark1():
    print("benchmark 1: single calls with various data sizes")

    benchmarkGrpcApi(10)
    benchmarkGrpcApi(100)
    benchmarkGrpcApi(1000)
    benchmarkGrpcApi(4000)
    print()

    benchmarkRestApi(10)
    benchmarkRestApi(100)
    benchmarkRestApi(1000)
    benchmarkRestApi(4000)
    print()

    comparePerf(10)
    comparePerf(100)
    comparePerf(1000)
    comparePerf(4000)
    print()


def benchmark2():
    print("benchmark 2: multiple calls with small data size")

    calls = 10

    t0 = time.time()
    for i in range(calls):
        benchmarkGrpcApi(10)
    t1 = time.time()

    for i in range(calls):
        benchmarkRestApi(10)
    t2 = time.time()

    print()
    print(
        f"GRPC: Completed {calls} requests in {(t1-t0):.2f} seconds. Average mean: {((t1-t0)/calls):.2f}"
    )
    print(
        f"REST: Completed {calls} requests in {(t2-t1):.2f} seconds. Average mean: {((t2-t1)/calls):.2f}"
    )


if __name__ == "__main__":
    benchmark1()
    benchmark2()
