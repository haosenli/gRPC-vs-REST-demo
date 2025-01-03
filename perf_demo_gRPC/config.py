DATA_SERVER_PORT = 5001
DATA_REPEATER_PORT1 = 5002
DATA_REPEATER_PORT2 = 5003

OPTIONS = [
    ("grpc.max_send_message_length", 1024 * 1024 * 10),  # 10MB
    ("grpc.max_receive_message_length", 1024 * 1024 * 10),  # 10MB
]
