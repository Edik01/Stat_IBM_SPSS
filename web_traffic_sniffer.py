import pyshark

def capture_http_sites(interface, duration):
    print(f"🔍 Capturing HTTP traffic on {interface} for {duration} seconds...\n")

    # HTTP-запросы, в которых можно видеть сайт (Host + Request URI)
    capture = pyshark.LiveCapture(
        interface=interface,
        display_filter="http.request"
    )

    capture.sniff(timeout=duration)

    print("📡 Visited websites:")
    for packet in capture:
        try:
            host = packet.http.host
            uri = packet.http.request_uri
            print(f"🌐 http://{host}{uri}")
        except AttributeError:
            continue

if __name__ == "__main__":
    interface = input("Enter your network interface (e.g., \\Device\\NPF_{...}): ")
    duration = int(input("How many seconds to monitor: "))
    capture_http_sites(interface, duration)
