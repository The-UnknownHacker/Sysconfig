# Sysinfo - An All in One Info CLI tool

This script provides a set of tools for fetching basic system and network information from your machine. It can be used to view details like CPU usage, RAM, network information (IP addresses, speed, and open ports), and GPU information.
Its quite useful for linux machines and combines all the different tools together to give you a unified experience  

## Features

- **Network Info**: Displays your interface, private IP, public IP, ping, and network speed.
- **CPU Info**: Shows CPU usage and model.
- **RAM Info**: Displays total and unused memory.
- **GPU Info**: Shows GPU details (macOS specific).
- **Open Ports**: Lists any open ports on your machine.

## Prerequisites

- Python 3.x
- `psutil` library (`pip install psutil`)
- `speedtest-cli` tool (for network speed testing) - install via `pip install speedtest-cli`
- A Unix-like operating system (macOS/Linux)

## Usage

To use the script, run it from the command line with one of the following options:

```
python main.py [option]
```

### Options

- **`-all`**: Show all system and network information.
- **`-net`**: Show network information (IP, speed, ping, open ports).
- **`-cpu`**: Show CPU usage and model.
- **`-ram`**: Show RAM usage.
- **`-gpu`**: Show GPU info (macOS only).
- **`-help`**: Show the help message.

### Example Commands

- Show network info:
  ```
  python main.py -net
  ```

- Show all system and network info:
  ```
  python main.py -all
  ```

- Show CPU info:
  ```
  python main.py -cpu
  ```

- Show RAM info:
  ```
  python main.py -ram
  ```

- Show GPU info (macOS only):
  ```
  python main.py -gpu
  ```

- Show help:
  ```
  python main.py -help
  ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
