from typing import Final
from . import Device

class S0CounterDevice:
    """
    The S0 Counter device. The EnergyManager has two inputs available for S0 energy meters.
    """

    DEVICE_CLASS: Final[str] = "com.kiwigrid.devices.s0counter.S0Counter"

    # Tag name constants
    TAG_POWER_IN: Final[str] = "PowerIn"
    TAG_POWER_OUT: Final[str] = "PowerOut"
    TAG_WORK_IN: Final[str] = "WorkIn"
    TAG_WORK_OUT: Final[str] = "WorkOut"
    TAG_COUNT_PULSES: Final[str] = "CountPulses"

    def __init__(self, device: Device):
        """Wrapper for S0Counter."""
        self.device = device

    @property
    def power_in(self) -> float:
        """The power coming in, in W."""
        return self.device.get_tag_value_as_float(S0CounterDevice.TAG_POWER_IN)

    @property
    def power_out(self) -> float:
        """The power going out, in W."""
        return self.device.get_tag_value_as_float(S0CounterDevice.TAG_POWER_OUT)

    @property
    def work_in(self) -> float:
        """The energy coming in, in Wh."""
        return self.device.get_tag_value_as_float(S0CounterDevice.TAG_WORK_IN)

    @property
    def work_out(self) -> float:
        """The energy going out, in Wh."""
        return self.device.get_tag_value_as_float(S0CounterDevice.TAG_WORK_OUT)

    @property
    def count_pulses(self) -> int:
        """The pulse counter."""
        return self.device.get_tag_value_as_int(S0CounterDevice.TAG_COUNT_PULSES)
