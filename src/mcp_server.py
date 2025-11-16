from mcp.server.fastmcp import FastMCP
from pydantic import BaseModel, Field
import os
from src.kali_mcps.nmap.actions import basic_scan_action, intense_scan_action, stealth_scan_action, quick_scan_action, vulnerability_scan_action
from src.kali_mcps.nm.actions import basic_symbols_action, dynamic_symbols_action, demangle_symbols_action, numeric_sort_action, size_sort_action, undefined_symbols_action
from src.kali_mcps.objdump.actions import file_headers_action, disassemble_action, symbol_table_action, section_headers_action, full_contents_action
from src.kali_mcps.strings.actions import basic_strings_action, min_length_strings_action, offset_strings_action, encoding_strings_action
from src.kali_mcps.wireshark.actions import capture_live_action, analyze_pcap_action, extract_http_action, protocol_hierarchy_action, conversation_statistics_action, expert_info_action
from src.kali_mcps.traceroute.actions import traceroute_action
from src.kali_mcps.git.actions import git_status_action, git_commit_action
mcp = FastMCP("kali-tools")


IS_SAFE = os.environ.get("IS_SAFE", "false").lower() == "true"  # is safe mode, if true, the command will be executed in the sandbox

# nmap start
@mcp.tool()
def basic_scan(target: str):
    """Perform a basic network scan using nmap.

    Args:
        target (str): The target IP address or hostname to scan.

    Returns:
        str: The output results of the basic scan.
    """
    return basic_scan_action(target)

@mcp.tool()
def intense_scan(target: str):
    """Perform an intense network scan using nmap.

    Args:
        target (str): The target IP address or hostname to scan.

    Returns:
        str: The output results of the intense scan.
    """
    return intense_scan_action(target)

@mcp.tool()
def stealth_scan(target: str):
    """Perform a stealth network scan using nmap.

    Args:
        target (str): The target IP address or hostname to scan.

    Returns:
        str: The output results of the stealth scan.
    """
    return stealth_scan_action(target)

@mcp.tool()
def quick_scan(target: str):
    """Perform a quick network scan using nmap.

    Args:
        target (str): The target IP address or hostname to scan.

    Returns:
        str: The output results of the quick scan.
    """
    return quick_scan_action(target)

@mcp.tool()
def vulnerability_scan(target: str):
    """Perform a vulnerability scan using nmap.

    Args:
        target (str): The target IP address or hostname to scan.

    Returns:
        str: The output results of the vulnerability scan.
    """
    return vulnerability_scan_action(target)
# nmap end

# nm start
@mcp.tool()
def basic_symbols(target: str):
    """Perform a basic symbol listing using nm.

    Args:
        target (str): The target file or executable to analyze.

    Returns:
        str: The output results of the basic symbol listing.
    """
    return basic_symbols_action(target)

@mcp.tool()
def dynamic_symbols(target: str):
    """Perform a dynamic symbol listing using nm.

    Args:
        target (str): The target file or executable to analyze.

    Returns:
        str: The output results of the dynamic symbol listing.
    """
    return dynamic_symbols_action(target)

@mcp.tool()
def demangle_symbols(target: str):
    """Perform a demangling of symbols using nm.

    Args:
        target (str): The target file or executable to analyze.

    Returns:
        str: The output results of the demangling of symbols.
    """
    return demangle_symbols_action(target)

@mcp.tool()
def numeric_sort(target: str):
    """Perform a numeric sort of symbols using nm.

    Args:
        target (str): The target file or executable to analyze.

    Returns:
        str: The output results of the numeric sort of symbols.
    """
    return numeric_sort_action(target)

@mcp.tool()
def size_sort(target: str):
    """Perform a size sort of symbols using nm.

    Args:
        target (str): The target file or executable to analyze.

    Returns:
        str: The output results of the size sort of symbols.
    """
    return size_sort_action(target)

@mcp.tool()
def undefined_symbols(target: str):
    """Perform an undefined symbol listing using nm.

    Args:
        target (str): The target file or executable to analyze.

    Returns:
        str: The output results of the undefined symbol listing.
    """
    return undefined_symbols_action(target)
# nm end

# objdump start
@mcp.tool()
def file_headers(target: str):
    """Perform a file header listing using objdump.

    Args:
        target (str): The target file or executable to analyze.

    Returns:
        str: The output results of the file header listing.
    """
    return file_headers_action(target)

@mcp.tool()
def disassemble(target: str):
    """Perform a disassembly of the target file using objdump.

    Args:
        target (str): The target file or executable to analyze.

    Returns:
        str: The output results of the disassembly of the target file.
    """
    return disassemble_action(target)

@mcp.tool()
def symbol_table(target: str):
    """Perform a symbol table listing using objdump.

    Args:
        target (str): The target file or executable to analyze.

    Returns:
        str: The output results of the symbol table listing.
    """
    return symbol_table_action(target)

@mcp.tool()
def section_headers(target: str):
    """Perform a section header listing using objdump.

    Args:
        target (str): The target file or executable to analyze.

    Returns:
        str: The output results of the section header listing.
    """
    return section_headers_action(target)

@mcp.tool()
def full_contents(target: str):
    """Perform a full contents listing using objdump.

    Args:
        target (str): The target file or executable to analyze.

    Returns:
        str: The output results of the full contents listing.
    """
    return full_contents_action(target)
# objdump end

# strings start
@mcp.tool()
def basic_strings(target: str):
    """Perform a basic string listing using strings.

    Args:
        target (str): The target file or executable to analyze.

    Returns:
        str: The output results of the basic string listing.
    """
    return basic_strings_action(target)

@mcp.tool()
def min_length_strings(target: str):
    """Perform a minimum length string listing using strings.

    Args:
        target (str): The target file or executable to analyze.

    Returns:
        str: The output results of the minimum length string listing.
    """
    return min_length_strings_action(target)

@mcp.tool()
def offset_strings(target: str):
    """Perform an offset string listing using strings.

    Args:
        target (str): The target file or executable to analyze.

    Returns:
        str: The output results of the offset string listing.
    """
    return offset_strings_action(target)

@mcp.tool()
def encoding_strings(target: str):
    """Perform an encoding string listing using strings.

    Args:
        target (str): The target file or executable to analyze.

    Returns:
        str: The output results of the encoding string listing.
    """
    return encoding_strings_action(target)
# strings end

# tshark start
@mcp.tool()
def capture_live(interface: str, duration: int = 30, filter: str = ""):
    """Perform a live capture of network traffic using tshark.

    Args:
        interface (str): The network interface to capture from.
        duration (int): The duration of the capture in seconds.
        filter (str): The filter to apply to the capture.

    Returns:
        str: The output results of the live capture of network traffic.
    """
    return capture_live_action(interface, duration, filter)


@mcp.tool()
def analyze_pcap(pcap_file: str, display_filter: str = ""):
    """Perform an analysis of a pcap file using tshark.

    Args:
        pcap_file (str): The path to the pcap file to analyze.
        display_filter (str): The filter to apply to the analysis.

    Returns:
        str: The output results of the analysis of the pcap file.
    """
    return analyze_pcap_action(pcap_file, display_filter)

@mcp.tool()
def extract_http(pcap_file: str):
    """Perform an HTTP extraction from a pcap file using tshark.

    Args:
        pcap_file (str): The path to the pcap file to extract HTTP from.    

    Returns:
        str: The output results of the HTTP extraction from the pcap file.
    """
    return extract_http_action(pcap_file)  

@mcp.tool()
def protocol_hierarchy(pcap_file: str):
    """Perform a protocol hierarchy listing using tshark.

    Args:
        pcap_file (str): The path to the pcap file to analyze.  

    Returns:
        str: The output results of the protocol hierarchy listing.
    """
    return protocol_hierarchy_action(pcap_file)    

@mcp.tool()
def conversation_statistics(pcap_file: str):
    """Perform a conversation statistics listing using tshark.

    Args:
        pcap_file (str): The path to the pcap file to analyze.  

    Returns:
        str: The output results of the conversation statistics listing.
    """
    return conversation_statistics_action(pcap_file)   

@mcp.tool() 
def expert_info(pcap_file: str):
    """Perform an expert information listing using tshark.

    Args:
        pcap_file (str): The path to the pcap file to analyze.  

    Returns:
        str: The output results of the expert information listing.
    """
    return expert_info_action(pcap_file)   
# tshark end

# traceroute start
@mcp.tool()
def traceroute(target: str):
    """
    Perform a traceroute to the target.

    Args:
        target (str): The target IP address or hostname to traceroute to.

    Returns:
        str: The output results of the traceroute.  
    """
    return traceroute_action(target)
# traceroute end

# git start
@mcp.tool()
def git_status():
    """Show the current git status for the repository."""

    stdout, stderr = git_status_action()
    if stderr:
        return f"STDERR:\n{stderr}\nSTDOUT:\n{stdout}" if stdout else f"STDERR:\n{stderr}"
    return stdout


class GitCommitParams(BaseModel):
    message: str = Field(..., description="Commit message to use for git commit")
    add_all: bool = Field(default=True, description="Whether to run git add -A before committing")


@mcp.tool()
def git_commit(params: GitCommitParams):
    """Create a git commit with the provided message (optionally staging all changes first)."""

    stdout, stderr = git_commit_action(params.message, params.add_all)
    if stderr:
        return f"STDERR:\n{stderr}\nSTDOUT:\n{stdout}" if stdout else f"STDERR:\n{stderr}"
    return stdout

# git end

# run server, using stdio transport
if __name__ == "__main__":
    print("Starting server is running")
    mcp.run(transport="stdio")