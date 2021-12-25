from typing import Any, Dict, List


class Device:
    """The base definition for an EnergyManager device."""

    # The unique ID of the device.
    guid: str = ""

    # The device classes defined for this device.
    device_classes: List[str] = []

    # The tag items of the device.
    tag_items: Dict[str, Any] = {}

    def read_json_item(self, item):
        """Read the item JSON data into this object."""
        self.guid = item["guid"] if "guid" in item else ""
        self.device_classes = Device.get_item_device_classes(item)
        self.tag_items = Device.get_tag_items(item)

    def get_tag_value_as_str(self, tag_name) -> str:
        """Get the item tag value as a string."""
        try:
            if tag_name in self.tag_items:
                return str(self.tag_items[tag_name])
            return ""
        except Exception:
            return ""

    def get_tag_value_as_int(self, tag_name) -> int:
        """Get the item tag value as an int."""
        try:
            return int(float(self.tag_items[tag_name]))
        except Exception:
            return int(0)

    def get_tag_value_as_float(self, tag_name) -> float:
        """Get the item tag value as a float."""
        try:
            return float(self.tag_items[tag_name])
        except Exception:
            return float(0)

    @staticmethod
    def get_item_device_classes(item: dict) -> List[str]:
        """Get the devices classes of the items."""
        classes: List[str] = []
        if "deviceModel" in item:
            device_model_items = item["deviceModel"]
            for device_model_item in device_model_items:
                if "deviceClass" in device_model_item:
                    classes.append(device_model_item["deviceClass"])
        return classes

    @staticmethod
    def get_tag_items(item: dict) -> Dict[str, Any]:
        """Get the tag items of the item."""
        items: Dict[str, Any] = {}
        if "tagValues" in item:
            tag_values = item["tagValues"]
            for tag_name, tag_value in tag_values.items():
                items[tag_name] = tag_value["value"] if "value" in tag_value else ""
        return items

