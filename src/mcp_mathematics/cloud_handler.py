from mcp_mathematics.calculator import mcp, setup_graceful_shutdown, start_memory_cleanup_timer

def handler():
    setup_graceful_shutdown()
    start_memory_cleanup_timer()
    return mcp

app = handler()