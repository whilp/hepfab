import random

from functools import partial

from fabric.api import env
from fabric import api as fab

__all__ = ["kick", "restart", "service", "start", "status", "stop"]

def service(servicename, command):
    """Run a System V init script."""
    env.service = servicename
    env.cmd = command
    fab.sudo("/sbin/service %(service)s %(cmd)s" % env)

restart = partial(service, command="restart")
restart.__doc__ = """Restart a service."""

start = partial(service, command="start")
start.__doc__ = """Start a service."""

status = partial(service, command="status")
status.__doc__ = """Check a service's status."""

stop = partial(service, command="stop")
stop.__doc__ = """Stop a service."""

def kick(command="/bin/true", maxsleep=3600):
    """Sleep, run a command and reboot."""
    env.seconds = random.randint(0, maxsleep)
    env.cmd = command
    fab.sudo(("""/usr/bin/nohup %(shell)s""" 
        """ "/bin/sleep %(seconds)d && %(cmd)s && /sbin/shutdown -r now" """
        """ < /dev/null > /dev/null 2>&1 &"""
        ) % env)
