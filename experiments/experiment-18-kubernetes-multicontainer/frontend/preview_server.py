"""Serve the StudySpark frontend locally and proxy API calls to port 5000."""

from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


FRONTEND = Path(__file__).resolve().parent
API = "http://127.0.0.1:5000"


class PreviewHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(FRONTEND), **kwargs)

    def _proxy_api(self):
        body = self.rfile.read(int(self.headers.get("Content-Length", "0")))
        request = Request(
            API + self.path,
            data=body or None,
            headers={"Content-Type": self.headers.get("Content-Type", "application/json")},
            method=self.command,
        )
        try:
            with urlopen(request, timeout=5) as response:
                payload, status = response.read(), response.status
        except HTTPError as error:
            payload, status = error.read(), error.code
        except URLError:
            payload, status = b'{"error":"API is not running on port 5000"}', 502
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

    def do_GET(self):
        if self.path.startswith("/api/") or self.path == "/health":
            return self._proxy_api()
        return super().do_GET()

    def do_POST(self):
        return self._proxy_api()


if __name__ == "__main__":
    server = ThreadingHTTPServer(("127.0.0.1", 8080), PreviewHandler)
    print("StudySpark preview: http://127.0.0.1:8080 (Flask API on 127.0.0.1:5000)")
    server.serve_forever()
