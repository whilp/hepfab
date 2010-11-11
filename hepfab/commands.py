import random

from functools import partial

from fabric import api as fab

__all__ = ["kick", "restart", "service", "start", "stop"]

def service(servicename, command):
    """Run a System V init script."""
    fab.sudo("/sbin/service %s %s" % (servicename, command))

restart = partial(service, command="restart")
restart.__doc__ = """Restart a service."""

start = partial(service, command="start")
start.__doc__ = """Start a service."""

stop = partial(service, command="stop")
stop.__doc__ = """Stop a service."""

def kick(command="/bin/true", maxsleep=3600):
    """Sleep, run a command and reboot."""
    seconds = random.randint(0, maxsleep)
    fab.sudo(("""/usr/bin/nohup %s""" 
        """ "/bin/sleep %s && %s && /sbin/shutdown -r now" """
        """ < /dev/null > /dev/null 2>&1 &"""
        ) % (fab.env.shell, seconds, command))
