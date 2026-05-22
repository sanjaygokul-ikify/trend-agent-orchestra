import prometheus_client

def setup_metrics():
    prometheus_client.start_http_server(8000)
