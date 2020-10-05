import socket

def list_of_services_by_ports(lower=0, upper=65535):
    """
    list services provided by a given range of ports
    """
    protocol = 'tcp'
    list_services = []
    for port in range(lower, upper):
        try:
            service = socket.getservbyport(port, protocol)
            if service is not None:
                list_services.append((port, service))
        except OSError as os:
            error = os

    return list_services
