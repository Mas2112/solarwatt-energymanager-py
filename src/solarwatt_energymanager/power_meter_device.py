from typing import Final
from . import Device

class PowerMeterDevice:
    """
    The Power Meter device which reads raw values from the power meter.
    """

    DEVICE_CLASS: Final[str] = "com.kiwigrid.devices.powermeter.PowerMeter"

    # Tag name constants
    TAG_POWER_IN: Final[str] = "PowerIn"
    TAG_POWER_OUT: Final[str] = "PowerOut"
    TAG_WORK_IN: Final[str] = "WorkIn"
    TAG_WORK_OUT: Final[str] = "WorkOut"

    def __init__(self, device: Device):
        """Wrapper for PowerMeter."""
        self.device = device

    @property
    def power_in(self) -> float | None:
        """The power coming in, in W."""
        return self.device.get_tag_value_as_float(PowerMeterDevice.TAG_POWER_IN)

    @property
    def power_out(self) -> float | None:
        """The power going out, in W."""
        return self.device.get_tag_value_as_float(PowerMeterDevice.TAG_POWER_OUT)

    @property
    def work_in(self) -> float | None:
        """The energy coming in, in Wh."""
        return self.device.get_tag_value_as_float(PowerMeterDevice.TAG_WORK_IN)

    @property
    def work_out(self) -> float | None:
        """The energy going out, in Wh."""
        return self.device.get_tag_value_as_float(PowerMeterDevice.TAG_WORK_OUT)
