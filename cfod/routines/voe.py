"""CHIME/FRB Virtual Observatory Event."""
import logging
from typing import Union

from cfod.routines.actor import Actor

logging.basicConfig(format="%(levelname)s:%(message)s")
log = logging.getLogger(__name__)


class VOE:
    """CHIME/FRB Virtual Observatory Event Object."""

    def __init__(
        self,
        email: str,
        action: Actor,
        format: str = "dict",
        testing: bool = False,
        debug: bool = False,
        **kwargs
    ) -> None:
        """
        CHIME/FRB Virtual Observatory Event.

        Parameters
        ----------
        email : str
            Registered email with CHIME/FRB VOE Service.
        actor : Actor
            Action to take, upon recieveing an event.
        format : str, optional
            Format of the VOE Event, by default "dict".
            Valid Options:
        testing : bool, optional
            Enable test mode, by default False
        debug : bool, optional
            Enable depper logging, by default False
        """
        self.email = email
        self.actor = action(**kwargs)
        self.format = format
        self.testing = testing
        self.debug = debug
        self._introspect()

    def _introspect(self):
        if self.debug:
            log.setLevel(logging.DEBUG)
        else:
            log.setLevel(logging.ERROR)

    def perform_action(self, event: Union[str, dict]):
        """
        Perform action.

        Parameters
        ----------
        event : [type]
            [description]
        """
        self.actor.action(event)