from typing import Final
from . import Device


class EnergyManagerDevice(Device):
    """The EnergyManager device itself. Needed to get the device model and serial number."""

    DEVICE_CLASS: Final = "com.kiwigrid.devices.em.EnergyManager"

    # Tag name constants
    TAG_MODEL: Final[str] = "IdModelCode"
    TAG_FIRMWARE: Final[str] = "IdFirmware"

    def __init__(self, device: Device):
        """Wrap the device with EnergyManagerDevice."""
        self.device = device

    @property
    def model(self) -> str:
        """Get the EnergyManager model."""
        return self.device.get_tag_value_as_str(EnergyManagerDevice.TAG_MODEL)

    @property
    def firmware(self) -> str:
        """Get the EnergyManager firmware."""
        return self.device.get_tag_value_as_str(EnergyManagerDevice.TAG_FIRMWARE)

