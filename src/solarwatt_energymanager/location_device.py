from typing import Final
from . import Device

class LocationDevice:
    """
    The Location EnergyManager device. Contains most of the interesting info.

    The power tags contain the instantaneous power readings in W.
    The work tags contain the accumulated energy values in Wh.
    """

    DEVICE_CLASS: Final[str] = "com.kiwigrid.devices.location.Location"

    # Tag name constants
    TAG_POWER_BUFFERED: Final[str] = "PowerBuffered"
    TAG_POWER_BUFFERED_FROM_GRID: Final[str] = "PowerBufferedFromGrid"
    TAG_POWER_BUFFERED_FROM_PRODUCERS: Final[str] = "PowerBufferedFromProducers"
    TAG_POWER_CONSUMED: Final[str] = "PowerConsumed"
    TAG_POWER_CONSUMED_FROM_GRID: Final[str] = "PowerConsumedFromGrid"
    TAG_POWER_CONSUMED_FROM_PRODUCERS: Final[str] = "PowerConsumedFromProducers"
    TAG_POWER_CONSUMED_FROM_STORAGE: Final[str] = "PowerConsumedFromStorage"
    TAG_POWER_IN: Final[str] = "PowerIn"
    TAG_POWER_OUT: Final[str] = "PowerOut"
    TAG_POWER_OUT_FROM_PRODUCERS: Final[str] = "PowerOutFromProducers"
    TAG_POWER_OUT_FROM_STORAGE: Final[str] = "PowerOutFromStorage"
    TAG_POWER_PRODUCED: Final[str] = "PowerProduced"
    TAG_POWER_RELEASED: Final[str] = "PowerReleased"
    TAG_POWER_SELF_CONSUMED: Final[str] = "PowerSelfConsumed"
    TAG_POWER_SELF_SUPPLIED: Final[str] = "PowerSelfSupplied"

    TAG_WORK_BUFFERED: Final[str] = "WorkBuffered"
    TAG_WORK_BUFFERED_FROM_GRID: Final[str] = "WorkBufferedFromGrid"
    TAG_WORK_BUFFERED_FROM_PRODUCERS: Final[str] = "WorkBufferedFromProducers"
    TAG_WORK_CONSUMED: Final[str] = "WorkConsumed"
    TAG_WORK_CONSUMED_FROM_GRID: Final[str] = "WorkConsumedFromGrid"
    TAG_WORK_CONSUMED_FROM_PRODUCERS: Final[str] = "WorkConsumedFromProducers"
    TAG_WORK_CONSUMED_FROM_STORAGE: Final[str] = "WorkConsumedFromStorage"
    TAG_WORK_IN: Final[str] = "WorkIn"
    TAG_WORK_OUT: Final[str] = "WorkOut"
    TAG_WORK_OUT_FROM_PRODUCERS: Final[str] = "WorkOutFromProducers"
    TAG_WORK_OUT_FROM_STORAGE: Final[str] = "WorkOutFromStorage"
    TAG_WORK_PRODUCED: Final[str] = "WorkProduced"
    TAG_WORK_RELEASED: Final[str] = "WorkReleased"
    TAG_WORK_SELF_CONSUMED: Final[str] = "WorkSelfConsumed"
    TAG_WORK_SELF_SUPPLIED: Final[str] = "WorkSelfSupplied"

    def __init__(self, device: Device):
        """Wrapper for LocationDevice."""
        self.device = device

    @property
    def power_buffered(self) -> float | None:
        """The power being stored to battery, in W."""
        return self.device.get_tag_value_as_float(LocationDevice.TAG_POWER_BUFFERED)

    @property
    def power_buffered_from_grid(self) -> float | None:
        """The power being stored to battery from the grid, in W."""
        return self.device.get_tag_value_as_float(LocationDevice.TAG_POWER_BUFFERED_FROM_GRID)

    @property
    def power_buffered_from_producers(self) -> float | None:
        """The power being stored to battery from the producers (eg - solar), in W."""
        return self.device.get_tag_value_as_float(LocationDevice.TAG_POWER_BUFFERED_FROM_PRODUCERS)

    @property
    def power_consumed(self) -> float | None:
        """The power being consumed, in W."""
        return self.device.get_tag_value_as_float(LocationDevice.TAG_POWER_CONSUMED)

    @property
    def power_consumed_from_grid(self) -> float | None:
        """The power being consumed from the grid, in W."""
        return self.device.get_tag_value_as_float(LocationDevice.TAG_POWER_CONSUMED_FROM_GRID)

    @property
    def power_consumed_from_producers(self) -> float | None:
        """The power being consumed from producers (eg - solar), in W."""
        return self.device.get_tag_value_as_float(LocationDevice.TAG_POWER_CONSUMED_FROM_PRODUCERS)

    @property
    def power_consumed_from_storage(self) -> float | None:
        """The power being consumed from battery, in W."""
        return self.device.get_tag_value_as_float(LocationDevice.TAG_POWER_CONSUMED_FROM_STORAGE)

    @property
    def power_in(self) -> float | None:
        """The power coming in from the grid, in W."""
        return self.device.get_tag_value_as_float(LocationDevice.TAG_POWER_IN)

    @property
    def power_out(self) -> float | None:
        """The power going out to the grid, in W."""
        return self.device.get_tag_value_as_float(LocationDevice.TAG_POWER_OUT)

    @property
    def power_out_from_producers(self) -> float | None:
        """The power going out to the grid from producers (eg - solar), in W."""
        return self.device.get_tag_value_as_float(LocationDevice.TAG_POWER_OUT_FROM_PRODUCERS)

    @property
    def power_out_from_storage(self) -> float | None:
        """The power going out to the grid from battery, in W."""
        return self.device.get_tag_value_as_float(LocationDevice.TAG_POWER_OUT_FROM_STORAGE)

    @property
    def power_produced(self) -> float | None:
        """The power produced (eg - solar), in W."""
        return self.device.get_tag_value_as_float(LocationDevice.TAG_POWER_PRODUCED)

    @property
    def power_released(self) -> float | None:
        """The power relased from the battery, in W."""
        return self.device.get_tag_value_as_float(LocationDevice.TAG_POWER_RELEASED)

    @property
    def power_self_consumed(self) -> float | None:
        """The power self consumed from producers, in W."""
        return self.device.get_tag_value_as_float(LocationDevice.TAG_POWER_SELF_CONSUMED)

    @property
    def power_self_supplied(self) -> float | None:
        """The power self supplied (to storage?), in W."""
        return self.device.get_tag_value_as_float(LocationDevice.TAG_POWER_SELF_SUPPLIED)

    @property
    def work_buffered(self) -> float | None:
        """The energy being stored to battery, in Wh."""
        return self.device.get_tag_value_as_float(LocationDevice.TAG_WORK_BUFFERED)

    @property
    def work_buffered_from_grid(self) -> float | None:
        """The energy being stored to battery from the grid, in Wh."""
        return self.device.get_tag_value_as_float(LocationDevice.TAG_WORK_BUFFERED_FROM_GRID)

    @property
    def work_buffered_from_producers(self) -> float | None:
        """The energy being stored to battery from the producers (eg - solar), in Wh."""
        return self.device.get_tag_value_as_float(LocationDevice.TAG_WORK_BUFFERED_FROM_PRODUCERS)

    @property
    def work_consumed(self) -> float | None:
        """The energy being consumed, in Wh."""
        return self.device.get_tag_value_as_float(LocationDevice.TAG_WORK_CONSUMED)

    @property
    def work_consumed_from_grid(self) -> float | None:
        """The energy being consumed from the grid, in Wh."""
        return self.device.get_tag_value_as_float(LocationDevice.TAG_WORK_CONSUMED_FROM_GRID)

    @property
    def work_consumed_from_producers(self) -> float | None:
        """The energy being consumed from producers (eg - solar), in Wh."""
        return self.device.get_tag_value_as_float(LocationDevice.TAG_WORK_CONSUMED_FROM_PRODUCERS)

    @property
    def work_consumed_from_storage(self) -> float | None:
        """The energy being consumed from battery, in Wh."""
        return self.device.get_tag_value_as_float(LocationDevice.TAG_WORK_CONSUMED_FROM_STORAGE)

    @property
    def work_in(self) -> float | None:
        """The energy coming in from the grid, in Wh."""
        return self.device.get_tag_value_as_float(LocationDevice.TAG_WORK_IN)

    @property
    def work_out(self) -> float | None:
        """The energy going out to the grid, in Wh."""
        return self.device.get_tag_value_as_float(LocationDevice.TAG_WORK_OUT)

    @property
    def work_out_from_producers(self) -> float | None:
        """The energy going out to the grid from producers (eg - solar), in Wh."""
        return self.device.get_tag_value_as_float(LocationDevice.TAG_WORK_OUT_FROM_PRODUCERS)

    @property
    def work_out_from_storage(self) -> float | None:
        """The energy going out to the grid from battery, in Wh."""
        return self.device.get_tag_value_as_float(LocationDevice.TAG_WORK_OUT_FROM_STORAGE)

    @property
    def work_produced(self) -> float | None:
        """The energy produced (eg - solar), in Wh."""
        return self.device.get_tag_value_as_float(LocationDevice.TAG_WORK_PRODUCED)

    @property
    def work_released(self) -> float | None:
        """The energy relased from the battery, in Wh."""
        return self.device.get_tag_value_as_float(LocationDevice.TAG_WORK_RELEASED)

    @property
    def work_self_consumed(self) -> float | None:
        """The energy self consumed from producers, in Wh."""
        return self.device.get_tag_value_as_float(LocationDevice.TAG_WORK_SELF_CONSUMED)

    @property
    def work_self_supplied(self) -> float | None:
        """The energy self supplied (to storage?), in Wh."""
        return self.device.get_tag_value_as_float(LocationDevice.TAG_WORK_SELF_SUPPLIED)
