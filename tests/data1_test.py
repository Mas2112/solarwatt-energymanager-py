import json
import os
import unittest

from src.solarwatt_energymanager import EnergyManagerData
from src.solarwatt_energymanager import LocationDevice

TESTJSON_FILENAME = os.path.join(os.path.dirname(__file__), 'data1.json')

class Data1TestCase(unittest.TestCase):
    
    def setUp(self) -> None:
        self.jsondata = open(TESTJSON_FILENAME, encoding='utf-8').read()
        self.data = EnergyManagerData(json.loads(self.jsondata))
        return super().setUp()

    def test_energy_manager_device(self):
        emd = self.data.energy_manager_device
        self.assertEqual('ERC05-000099999', emd.device.get_device_name())
        self.assertEqual('ERC05-000099999', emd.device.guid)
        self.assertEqual('ERC05', emd.model)
        self.assertEqual('7.32.1.0', emd.firmware)

    def test_location_device(self):
        location: LocationDevice = self.data.location_device
        self.assertEqual('aaaaaaaa-bbbb-cccc-dddd-000000000003', location.device.guid)
        self.assertEqual('Standort 1', location.device.get_device_name())
        self.assertEqual(3, location.power_buffered)
        self.assertEqual(1, location.power_buffered_from_grid)
        self.assertEqual(2, location.power_buffered_from_producers)
        self.assertEqual(300, location.power_consumed)
        self.assertEqual(85, location.power_consumed_from_grid)
        self.assertEqual(215, location.power_consumed_from_producers)
        self.assertEqual(4, location.power_consumed_from_storage)
        self.assertEqual(85, location.power_in)
        self.assertEqual(5, location.power_out)
        self.assertEqual(6, location.power_out_from_producers)
        self.assertEqual(7, location.power_out_from_storage)
        self.assertEqual(215, location.power_produced)
        self.assertEqual(0, location.power_released)
        self.assertEqual(215, location.power_self_consumed)
        self.assertEqual(215, location.power_self_supplied)

        self.assertEqual(1.1111111111, location.work_buffered)
        self.assertEqual(2.2222222222, location.work_buffered_from_grid)
        self.assertEqual(3.3333333333, location.work_buffered_from_producers)
        self.assertEqual(2092768.4277269384, location.work_consumed)
        self.assertEqual(991239.2512747848, location.work_consumed_from_grid)
        self.assertEqual(1101529.1764520113, location.work_consumed_from_producers)
        self.assertEqual(4.444444444, location.work_consumed_from_storage)
        self.assertEqual(991239.2512747848, location.work_in)
        self.assertEqual(2684420.79755769, location.work_out)
        self.assertEqual(2681016.453911554, location.work_out_from_producers)
        self.assertEqual(5.5555555555, location.work_out_from_storage)
        self.assertEqual(3782545.6303635743, location.work_produced)
        self.assertEqual(0, location.work_released)
        self.assertEqual(1101529.1764520113, location.work_self_consumed)
        self.assertEqual(1101529.1764520113, location.work_self_supplied)

    def test_battery_converter_devices(self):
        battery_converter_devices = self.data.battery_converter_devices
        self.assertIsNotNone(battery_converter_devices)
        self.assertEqual(0, len(battery_converter_devices))

if __name__ == '__main__':
    unittest.main()
