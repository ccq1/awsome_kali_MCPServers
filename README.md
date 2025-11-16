# awsome-kali-MCPServers

## Overview
Welcome to awsome-kali-MCPServers! This repository is a collection of Model Context Protocol (MCP) servers designed specifically for Kali Linux environments. The goal is to enhance reverse engineering, security testing, and automation workflows by integrating powerful tools and flexible features. Whether you're a security researcher or a developer, this project aims to streamline your tasks with Kali Linux.

## Quick Start
Follow these steps to quickly get started with `kali-mcps`:
1. **Build the Docker Image**
First, build the Docker image, temporarily named kali-mcps. Run the following command in the project root directory:
```bash
docker build -t kali-mcps:latest .
```
2. **Launch an MCP Client**
Ensure you have an MCP client installed, such as claude desktop, cline, goose, or roo code. Open your chosen MCP client.
3. **Configure the MCP Client**
In your MCP client, create a configuration file (e.g., config.json) with the following content:
```json
{
  "mcpServers": {
    "kali-docker": {
      "command": "docker",
      "args": ["run", "-i", "kali-mcps:latest"]
    }
  }
}
```
- `"kali-docker"` is the server name, which you can customize.
- `"command": "docker"` specifies that Docker will be used to run the container.
- `"args"` defines the Docker run parameters: `-i` enables interactive mode, and `kali-mcps:latest` is the image you just built.

4. **Use Kali Tools**
Once configured, connect to the kali-mcps container via the MCP client and start using the built-in Kali tools (e.g., Nmap, nm, objdump, strings, tshark) for your tasks. Examples include:
- Run `basic_scan` for basic network scanning.
- Run `disassemble` to disassemble a target file.
- Run `capture_live` to capture real-time network traffic.

<p align="center">
  <img width="482" alt="image" src="https://github.com/user-attachments/assets/0e9fff0a-059d-424b-bb36-450a1d11adf9" />
</p>

## What to Expect
Network Analysis: Tools for sniffing and analyzing traffic.
Binary Understanding: Support for reverse engineering and function analysis.
Automation: Scripts and servers to simplify repetitive tasks.

## New Features
Since the last update, we have added the following features, integrating a series of tools based on the FastMCP framework:

### 1. Network Scanning (Nmap)
- `basic_scan`: Basic network scanning.
- `intense_scan`: In-depth network scanning.
- `stealth_scan`: Stealth network scanning.
- `quick_scan`: Quick network scanning.
- `vulnerability_scan`: Vulnerability scanning.

### 2. Symbol Analysis (nm)
- `basic_symbols`: Lists basic symbols.
- `dynamic_symbols`: Lists dynamic symbols.
- `demangle_symbols`: Decodes symbols.
- `numeric_sort`: Sorts symbols numerically.
- `size_sort`: Sorts symbols by size.
- `undefined_symbols`: Lists undefined symbols.

### 3. Binary Analysis (objdump)
- `file_headers`: Lists file headers.
- `disassemble`: Disassembles the target file.
- `symbol_table`: Lists the symbol table.
- `section_headers`: Lists section headers.
- `full_contents`: Lists full contents.

### 4. String Extraction (strings)
- `basic_strings`: Basic string extraction.
- `min_length_strings`: Extracts strings with a specified minimum length.
- `offset_strings`: Extracts strings with offsets.
- `encoding_strings`: Extracts strings based on encoding.

### 5. Network Traffic Analysis (Wireshark/tshark)
- `capture_live`: Captures network traffic in real-time.
- `analyze_pcap`: Analyzes pcap files.
- `extract_http`: Extracts HTTP data.
- `protocol_hierarchy`: Lists protocol hierarchy.
- `conversation_statistics`: Provides conversation statistics.
- `expert_info`: Analyzes expert information.
### 6. Sandbox Support (Docker)
A new sandbox feature has been added, enabling secure command execution in an isolated container environment:

Runs commands using Docker containers, with the default image being ubuntu-systemd:22.04.
Configurable memory limit (default: 2GB), CPU limit (default: 1 core), network mode, and timeout duration.
Supports bidirectional file copying between the host and the container.
Automatically cleans up container resources.

### 7. Repository Utilities (Git)
- `git_status`: Quickly review the current repository state before committing.
- `git_commit`: Stage (optional) and commit your work with a custom message directly from the MCP client.


## TODO
- [ ] **Docker Sandbox Support**: Add containerized environments for safe testing and execution.
- [ ] **Network Tools Integration**: Support for tools like Nmap and Wireshark for advanced network analysis.
- [ ] **Reverse Engineering Tools**: Integrate Ghidra and Radare2 for enhanced binary analysis.
- [ ] **Agent Support**: Enable agent-based functionality for distributed tasks or remote operations.
 
## Current Status
This project is still in its early stages. I’m working on preparing the content, including server configurations, tool integrations, and documentation. Nothing is fully ready yet, but stay tuned—exciting things are coming soon!

## Stay Updated
Feel free to star or watch this repository to get updates as I add more features and files. Contributions and suggestions are welcome once the groundwork is laid out.
