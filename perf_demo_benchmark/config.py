GRPC_API_PORT = 5003
REST_API_PORT = 6003

OPTIONS = [
    ("grpc.max_send_message_length", 1024 * 1024 * 10),  # 10MB
    ("grpc.max_receive_message_length", 1024 * 1024 * 10),  # 10MB
]
