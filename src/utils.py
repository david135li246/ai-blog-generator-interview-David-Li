def log_message(message):
    """Logs a message to the console."""
    print(f"[LOG] {message}")

def format_response(data):
    """Formats the response data into a JSON-friendly structure."""
    return {
        "status": "success",
        "data": data
    }

def handle_error(error_message):
    """Formats an error message for consistent output."""
    return {
        "status": "error",
        "message": error_message
    }