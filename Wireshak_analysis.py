import os
import pyshark

def run_nmap_scan(target_ip):
    """
    Run an Nmap scan on the target IP address.
    """
    print(f"Running Nmap scan on {target_ip}...")
    nmap_command = f"nmap -sS -O {target_ip}"  # SYN scan with OS detection
    os.system(nmap_command)

def capture_traffic(interface, capture_duration):
    """
    Capture network traffic using Wireshark (Pyshark).
    """
    print(f"Capturing traffic on interface {interface} for {capture_duration} seconds...")
    capture = pyshark.LiveCapture(interface=interface)
    capture.sniff(timeout=capture_duration)
    
    print("Captured packets:")
    for packet in capture.sniff_continuously(packet_count=10):  # Display first 10 packets
        print(packet)

def main():
    """
    Main function to run Nmap and Wireshark functionalities.
    """
    print("Welcome to the Network Security Tool!")
    
    # Nmap functionality
    target_ip = input("Enter the target IP address to scan: ")
    run_nmap_scan(target_ip)
    
    # Wireshark functionality
    interface = input("Enter the network interface to monitor (e.g., eth0, wlan0): ")
    capture_duration = int(input("Enter the capture duration in seconds: "))
    capture_traffic(interface, capture_duration)

if __name__ == "__main__":
    main()