"""
Contains the definition of the EnergyManager devices and the parsing logic.

Not all devices here are modelled. This should be expanded as needed.
This has not been tested with MyReserve battery.

The following assumptions are made, and may need to be adjusted:
- Only one location device exists
- Only one energy manager device exists
- Only one battery may exist - needs to be extended for more batteries


The JSON data has the structure:
result: {
    items: [{
        tagValues: {
            tagName: string,
            guid: string,
            value: Any
        },
        deviceModel: [{
            deviceClass: string
        }, {
            deviceClass: string
        }],
        guid: string
    }]
}
"""

from typing import Any, Dict, Final, List, Optional
from src.battery_converter_device import BatteryConverterDevice
from src.device import Device

from src.energy_manager_device import EnergyManagerDevice
from src.location_device import LocationDevice


class EnergyManagerData:
    """Contains all of the energy manager devices and the getter methods."""

    devices: Dict[str, Device] = {}

    def __init__(self, json: dict):
        self.load_json(json)

    def load_json(self, json: dict) -> None:
        """Read the json data from the EnergyManager."""
        if "result" in json:
            result = json["result"]
            if "items" in result:
                items = result["items"]
                for item in items:
                    device = Device()
                    device.read_json_item(item)
                    self.devices[device.guid] = device

    def get_devices_by_class(self, device_class: str) -> Optional[List[Device]]:
        """Get the devices with the specified class."""
        return (d for d in self.devices.values() if device_class in d.device_classes)

    def get_device_by_class(self, device_class: str) -> Optional[Device]:
        """Get the first instance of the device with the specified class."""
        return next(
            (d for d in self.devices.values() if device_class in d.device_classes), None
        )
    
    def get_device_by_guid(self, guid: str) -> Optional[Device]:
        """Get the device by GUID."""
        return self.devices.get(guid)

    @property
    def energy_manager_device(self) -> Optional[EnergyManagerDevice]:
        """Get the EnergyManagerDevice. Assumption that there is only one EnergyManager device."""
        device = self.get_device_by_class(EnergyManagerDevice.DEVICE_CLASS)
        return EnergyManagerDevice(device) if device else None

    @property
    def location_device(self) -> Optional[LocationDevice]:
        """Get the LocationDevice. Assumption that there is only one location device."""
        device = self.get_device_by_class(LocationDevice.DEVICE_CLASS)
        return LocationDevice(device) if device else None

    @property
    def battery_converter_devices(self) -> Optional[List[BatteryConverterDevice]]:
        """Get the BatteryConverterDevice objects."""
        devices = self.get_devices_by_class(BatteryConverterDevice.DEVICE_CLASS)
        return list(map(lambda device: BatteryConverterDevice(device), devices))
