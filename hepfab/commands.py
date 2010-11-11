from functools import partial

from fabric import api as fab

__all__ = ["restart", "service", "start", "stop"]

def service(servicename, command):
    """Run a System V init script."""
    fab.sudo("/sbin/service %s %s" % (servicename, command))

restart = partial(service, command="restart")
restart.__doc__ = """Restart a service."""

start = partial(service, command="start")
start.__doc__ = """Start a service."""

stop = partial(service, command="stop")
stop.__doc__ = """Stop a service."""
