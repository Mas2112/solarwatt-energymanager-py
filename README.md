# solarwatt-energymanager
An unofficial python package for querying data from the SOLARWATT Energy Manager.

The goal of this library is to make it easy to query the data, and provides a sort of documentation of what kinds of fields are available.

```
from solarwatt_energymanager import EnergyManager

em = EnergyManager('192.168.1.123')
em_guid = await em.test_connection()
print(f'EnergyManager GUID={em_guid}')
data = await em.get_data()
print(f'power_in={data.location_device.power_in}')
print(f'power_out={data.location_device.power_out}')
```