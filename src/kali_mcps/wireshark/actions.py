import asyncio
from src.kali_mcps.base.kali_command import KaliCommand

class TsharkCommand(KaliCommand):
    def __init__(self):
        super().__init__("tshark", 
                        network_enabled=True,  # 需要网络访问
                        memory_limit="2g",     # 需要更多内存
                        timeout=300)           # 需要更长的超时时间

async def capture_live(interface: str, duration: int = 30, filter: str = "") -> tuple[str, str]:
    """
    Capture live traffic from network interface
    For example: tshark -i eth0 -a duration:30 -f "port 80"
    """
    cmd = TsharkCommand()
    command = ["tshark", "-i", interface, "-a", f"duration:{duration}"]
    if filter:
        command.extend(["-f", filter])
    return await cmd.execute(command)

async def analyze_pcap(pcap_file: str, display_filter: str = "") -> tuple[str, str]:
    """
    Analyze existing pcap file
    For example: tshark -r file.pcap -Y "http"
    """
    cmd = TsharkCommand()
    command = ["tshark", "-r", pcap_file]
    if display_filter:
        command.extend(["-Y", display_filter])
    return await cmd.execute(command)

async def extract_http(pcap_file: str) -> tuple[str, str]:
    """
    Extract HTTP objects from pcap file
    For example: tshark -r file.pcap -Y "http" -T fields -e http.request.method -e http.request.uri
    """
    cmd = TsharkCommand()
    command = [
        "tshark", "-r", pcap_file,
        "-Y", "http",
        "-T", "fields",
        "-e", "http.request.method",
        "-e", "http.request.uri"
    ]
    return await cmd.execute(command)

async def protocol_hierarchy(pcap_file: str) -> tuple[str, str]:
    """
    Show protocol hierarchy statistics
    For example: tshark -r file.pcap -q -z io,phs
    """
    cmd = TsharkCommand()
    command = ["tshark", "-r", pcap_file, "-q", "-z", "io,phs"]
    return await cmd.execute(command)

async def conversation_statistics(pcap_file: str) -> tuple[str, str]:
    """
    Show conversation statistics
    For example: tshark -r file.pcap -q -z conv,ip
    """
    cmd = TsharkCommand()
    command = ["tshark", "-r", pcap_file, "-q", "-z", "conv,ip"]
    return await cmd.execute(command)

async def expert_info(pcap_file: str) -> tuple[str, str]:
    """
    Show expert information (errors, warnings, notes)
    For example: tshark -r file.pcap -q -z expert
    """
    cmd = TsharkCommand()
    command = ["tshark", "-r", pcap_file, "-q", "-z", "expert"]
    return await cmd.execute(command)

if __name__ == "__main__":
    # Test example
    pcap_file = "capture.pcap"
    print(asyncio.run(protocol_hierarchy(pcap_file)))
