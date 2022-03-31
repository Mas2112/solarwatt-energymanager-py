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