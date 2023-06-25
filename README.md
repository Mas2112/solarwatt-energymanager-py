# solarwatt-energymanager
An unofficial python package for querying data from the SOLARWATT Energy Manager.

This package provides well defined types so that it is easy to find the data you need.

Note: Most of the interesting data is located in the location_device. Multiple batteries are supported.

# Usage
```
import solarwatt_energymanager as em

mgr = em.EnergyManager('192.168.178.62')
guid = await mgr.test_connection()
print(f'EnergyManager GUID={guid}')
data = await mgr.get_data()
print(f'power_in={data.location_device.power_in}')
print(f'power_out={data.location_device.power_out}')
```

# Changelog

## [1.3.0] - 2023-06-25

### Changed
- get_tag_value_as_* methods return None instead of empty string or zero if an error occurs

## [1.2.1] - 2023-03-05

### Added
- Added support to read IdName from Device via get_device_name()

## [1.2.0] - 2023-03-04

### Added
- Added support for S0 counters and EV stations.

## [1.1.0] - 2023-04-04

### Changed
- Renamed voltage_battery_cell_string to voltage_battery_string.

