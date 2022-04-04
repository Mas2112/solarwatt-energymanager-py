from typing import Final
from . import Device

class BatteryConverterDevice:
    """The battery converter EnergyManager device. Contains info about flow to and from battery."""

    DEVICE_CLASS: Final = "com.kiwigrid.devices.batteryconverter.BatteryConverter"

    # Tag name constants
    TAG_CURRENT_BATTERY_IN: Final[str] = "CurrentBatteryIn"
    TAG_CURRENT_BATTERY_OUT: Final[str] = "CurrentBatteryOut"
    TAG_CURRENT_GRM_IN: Final[str] = "CurrentGRMIn"
    TAG_CURRENT_GRM_OUT: Final[str] = "CurrentGRMOut"
    TAG_CURRENT_STRING_DC_IN: Final[str] = "CurrentStringDCIn"
    TAG_MODE_CONVERTER: Final[str] = "ModeConverter"
    TAG_POWER_AC_IN: Final[str] = "PowerACIn"
    TAG_POWER_AC_OUT: Final[str] = "PowerACOut"
    TAG_STATE_OF_CHARGE: Final[str] = "StateOfCharge"
    TAG_STATE_OF_HEALTH: Final[str] = "StateOfHealth"
    TAG_TEMPERATURE_BATTERY: Final[str] = "TemperatureBattery"
    TAG_VOLTAGE_GRM_IN: Final[str] = "VoltageGRMIn"
    TAG_VOLTAGE_GRM_OUT: Final[str] = "VoltageGRMOut"
    TAG_VOLTAGE_BATTERY_CELL_MEAN: Final[str] = "VoltageBatteryCellMean"
    TAG_VOLTAGE_BATTERY_STRING: Final[str] = "VoltageBatteryString"
    TAG_WORK_AC_IN: Final[str] = "WorkACIn"
    TAG_WORK_AC_OUT: Final[str] = "WorkACOut"

    def __init__(self, device: Device):
        """Wrap the device with BatteryConverterDevice."""
        self.device = device

    @property
    def current_battery_in(self) -> float:
        """The battery input current, in A."""
        return self.device.get_tag_value_as_float(BatteryConverterDevice.TAG_CURRENT_BATTERY_IN)

    @property
    def current_battery_out(self) -> float:
        """The battery output current, in A."""
        return self.device.get_tag_value_as_float(BatteryConverterDevice.TAG_CURRENT_BATTERY_OUT)

    @property
    def current_grm_in(self) -> float:
        """The GRM input current, in A."""
        return self.device.get_tag_value_as_float(BatteryConverterDevice.TAG_CURRENT_GRM_IN)

    @property
    def current_grm_out(self) -> float:
        """The GRM output current, in A."""
        return self.device.get_tag_value_as_float(BatteryConverterDevice.TAG_CURRENT_GRM_OUT)

    @property
    def current_dc_string_in(self) -> float:
        """The battery DC input current, in A."""
        return self.device.get_tag_value_as_float(BatteryConverterDevice.TAG_CURRENT_STRING_DC_IN)

    @property
    def mode_converter(self) -> str:
        """The current charging mode: CHARGING, ???"""
        return self.device.get_tag_value_as_str(BatteryConverterDevice.TAG_MODE_CONVERTER)

    @property
    def power_ac_in(self) -> float:
        """The input AC power, in W."""
        return self.device.get_tag_value_as_float(BatteryConverterDevice.TAG_POWER_AC_IN)

    @property
    def power_ac_out(self) -> float:
        """The output AC power, in W."""
        return self.device.get_tag_value_as_float(BatteryConverterDevice.TAG_POWER_AC_OUT)

    @property
    def state_of_charge(self) -> int:
        """The current battery charge state, in %."""
        return self.device.get_tag_value_as_int(BatteryConverterDevice.TAG_STATE_OF_CHARGE)

    @property
    def state_of_health(self) -> int:
        """The current battery health, in %."""
        return self.device.get_tag_value_as_int(BatteryConverterDevice.TAG_STATE_OF_HEALTH)

    @property
    def temperature_battery(self) -> int:
        """The current battery temperature, in C."""
        return self.device.get_tag_value_as_int(BatteryConverterDevice.TAG_TEMPERATURE_BATTERY)

    @property
    def voltage_grm_in(self) -> float:
        """The GRM input voltage, in V."""
        return self.device.get_tag_value_as_float(BatteryConverterDevice.TAG_VOLTAGE_GRM_IN)

    @property
    def voltage_grm_out(self) -> float:
        """The GRM output voltage, in V."""
        return self.device.get_tag_value_as_float(BatteryConverterDevice.TAG_VOLTAGE_GRM_OUT)

    @property
    def voltage_battery_cell_mean(self) -> float:
        """The mean battery cell voltage, in V."""
        return self.device.get_tag_value_as_float(BatteryConverterDevice.TAG_VOLTAGE_BATTERY_CELL_MEAN)

    @property
    def voltage_battery_string(self) -> float:
        """The battery string voltage, in V."""
        return self.device.get_tag_value_as_float(BatteryConverterDevice.TAG_VOLTAGE_BATTERY_STRING)

    @property
    def work_ac_in(self) -> float:
        """The accumulated amount of AC energy received, in Wh."""
        return self.device.get_tag_value_as_float(BatteryConverterDevice.TAG_WORK_AC_IN)

    @property
    def work_ac_out(self) -> float:
        """The accumulated amount of AC energy sent, in Wh."""
        return self.device.get_tag_value_as_float(BatteryConverterDevice.TAG_WORK_AC_OUT)
