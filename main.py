import os
import sys
import subprocess
import psutil
import socket

def get_network_info():
    print("\n📡 Network Info")
    print("----------------------")
    interface = os.popen("route get 8.8.8.8 | awk '/interface/ {print $2}'").read().strip()
    print(f"Interface: {interface}")
    
    private_ip = os.popen("ipconfig getifaddr en0").read().strip()
    print(f"Private IP: {private_ip}")
    
    public_ip = os.popen("curl -s ifconfig.me").read().strip()
    print(f"Public IP: {public_ip}")
    
    print("\n🌐 Testing Network Speed...")
    os.system("speedtest")
    
    ping = os.popen("ping -c 1 8.8.8.8 | awk -F'/' 'END {print $5}'").read().strip()
    print(f"Ping: {ping} ms")
    
    print("\n🔓 Open Ports:")
    os.system("netstat -an | grep LISTEN")
    print("\n")

def get_cpu_info():
    print("\n🖥️ CPU Info")
    print("----------------------")
    os.system("sysctl -n machdep.cpu.brand_string")
    print(f"Usage: {psutil.cpu_percent()}%")
    print("\n")

def get_ram_info():
    print("\n💾 RAM Info")
    print("----------------------")
    total_memory = psutil.virtual_memory().total / (1024 ** 3)
    used_memory = psutil.virtual_memory().used / (1024 ** 3)
    print(f"Total: {total_memory:.2f} GB | Unused: {used_memory:.2f} GB")
    print("\n")

def get_gpu_info():
    print("\n🎮 GPU Info")
    print("----------------------")
    os.system("system_profiler SPDisplaysDataType | grep 'Chipset Model'") 
    print("\n")

def show_help():
    print("""
    Usage: main.py [option]
    
    Options:
    - all       Show all system & network info
    - net       Show network info (IP, Speed, Ping, Ports, Devices)
    - cpu       Show CPU usage & model
    - ram       Show RAM usage
    - gpu       Show GPU info
    - help      Show this help message
    """)
    
if __name__ == "__main__":
    if len(sys.argv) < 2:
        show_help()
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == "-net":
        get_network_info()
    elif command == "-cpu":
        get_cpu_info()
    elif command == "-ram":
        get_ram_info()
    elif command == "-gpu":
        get_gpu_info()
    elif command == "-all":
        get_network_info()
        get_cpu_info()
        get_ram_info()
        get_gpu_info()
    else:
        show_help()
