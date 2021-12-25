# solarwatt-energymanager
An unofficial python package for querying data from the SOLARWATT Energy Manager.

The goal of this library is to make it easy to query the data, and provides a sort of documentation of what kinds of fields are available.

```
em = EnergyManager('192.168.1.10')
data = em.get_data()
print(data.location_device.power_in)
print(data.location_device.power_out)
```