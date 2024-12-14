import re

def validate_ip(ip):
    ip_regex = re.compile(
        r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}'
        r'(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
    )
    return re.match(ip_regex, ip) is not None

def validate_domain(domain):
    domain_regex = re.compile(
        r'^(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,}$'
    )
    return re.match(domain_regex, domain) is not None

def validate_port(port):
    try:
        port = int(port)
        if port < 1 or port > 65535:
            raise ValueError("Port number must be between 1 and 65535.")
        return port
    except ValueError:
        raise ValueError("Port number must be an integer.")

def validate_positive_float(value):
    try:
        value = float(value)
        if value <= 0:
            raise ValueError("Value must be a positive number.")
        return value
    except ValueError:
        raise ValueError("Value must be a number.")

def validate_positive_integer(value):
    try:
        value = int(value)
        if value <= 0:
            raise ValueError("Value must be a positive integer.")
        return value
    except ValueError:
        raise ValueError("Value must be an integer.")