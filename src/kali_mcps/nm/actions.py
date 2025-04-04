import asyncio
from src.kali_mcps.base.kali_command import CommandRunner

class NmCommand(CommandRunner):
    def __init__(self):
        super().__init__("nm", network_enabled=False, memory_limit="1g", timeout=120)

def basic_symbols_action(target: str) -> tuple[str, str]:
    """
    Basic symbol listing
    For example: nm /path/to/file
    """ 
    cmd = NmCommand()
    command = ["nm", target]
    return cmd.execute(command)

def dynamic_symbols_action(target: str) -> tuple[str, str]:
    """
    Display dynamic symbols
    For example: nm -D /path/to/file
    """
    cmd = NmCommand()
    command = ["nm", "-D", target]
    return cmd.execute(command)

def demangle_symbols_action(target: str) -> tuple[str, str]:
    """
    Demangle C++ symbols
    For example: nm -C /path/to/file
    """
    cmd = NmCommand()
    command = ["nm", "-C", target]
    return cmd.execute(command)

def numeric_sort_action(target: str) -> tuple[str, str]:
    """
    Sort symbols numerically by address
    For example: nm -n /path/to/file
    """
    cmd = NmCommand()
    command = ["nm", "-n", target]
    return cmd.execute(command)

def size_sort_action(target: str) -> tuple[str, str]:
    """
    Sort symbols by size
    For example: nm -S /path/to/file
    """
    cmd = NmCommand()
    command = ["nm", "-S", target]
    return cmd.execute(command)

def undefined_symbols_action(target: str) -> tuple[str, str]:
    """
    Display only undefined symbols
    For example: nm -u /path/to/file
    """
    cmd = NmCommand()
    command = ["nm", "-u", target]
    return cmd.execute(command)

if __name__ == "__main__":
    # Test example
    target_file = "/bin/ls"
    print(basic_symbols_action(target_file))
