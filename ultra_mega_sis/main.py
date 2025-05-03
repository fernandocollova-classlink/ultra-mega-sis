from ultra_mega_sis.serve import serve


def main(host: str = "127.0.0.1", port: int = 8000):
    serve(host=host, port=port, debug=True)
