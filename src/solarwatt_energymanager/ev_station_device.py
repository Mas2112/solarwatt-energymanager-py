from typing import Final
from . import Device

class EVStationDevice:
    """
    The electric vehicle charging station.
    """

    DEVICE_CLASS: Final[str] = "com.kiwigrid.devices.evstation.EVStation"

    # Tag name constants
    TAG_POWER_AC_IN: Final[str] = "PowerACIn"
    TAG_POWER_AC_OUT: Final[str] = "PowerACOut"
    TAG_WORK_AC_IN: Final[str] = "WorkACIn"
    TAG_WORK_AC_OUT: Final[str] = "WorkACOut"
    TAG_STATE_OF_CHARGE: Final[str] = "StateOfCharge"
    TAG_MODE_STATION: Final[str] = "ModeStation"
    TAG_WORK_AC_IN_SESSION: Final[str] = "WorkACInSession"
    TAG_TEMPERATURE_BATTERY: Final[str] = "TemperatureBattery"

    def __init__(self, device: Device):
        """Wrapper for EVStation."""
        self.device = device

    @property
    def power_ac_in(self) -> float | None:
        """The power flowing into the vehicle."""
        return self.device.get_tag_value_as_float(EVStationDevice.TAG_POWER_AC_IN)

    @property
    def power_ac_out(self) -> float | None:
        """The power flowing out of the vehicle."""
        return self.device.get_tag_value_as_float(EVStationDevice.TAG_POWER_AC_OUT)

    @property
    def work_ac_in(self) -> float | None:
        """The energy sent to the vehicle."""
        return self.device.get_tag_value_as_float(EVStationDevice.TAG_WORK_AC_IN)

    @property
    def work_ac_out(self) -> float | None:
        """The energy pulled from the vehicle."""
        return self.device.get_tag_value_as_float(EVStationDevice.TAG_WORK_AC_OUT)

    @property
    def state_of_charge(self) -> float | None:
        """The vehicle state of charge."""
        return self.device.get_tag_value_as_float(EVStationDevice.TAG_STATE_OF_CHARGE)

    @property
    def mode_station(self) -> str | None:
        """The current mode of the station."""
        return self.device.get_tag_value_as_str(EVStationDevice.TAG_MODE_STATION)

    @property
    def work_ac_in_session(self) -> float | None:
        """The energy sent to the vehicle for the session."""
        return self.device.get_tag_value_as_float(EVStationDevice.TAG_WORK_AC_IN_SESSION)

    @property
    def temperature_battery(self) -> float | None:
        """The battery temperature."""
        return self.device.get_tag_value_as_float(EVStationDevice.TAG_TEMPERATURE_BATTERY)
