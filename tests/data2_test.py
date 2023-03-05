import json
import os
import unittest

from src.solarwatt_energymanager import EnergyManagerData
from src.solarwatt_energymanager import LocationDevice

TESTJSON_FILENAME = os.path.join(os.path.dirname(__file__), 'data2.json')

class Data2TestCase(unittest.TestCase):
    
    def setUp(self) -> None:
        self.jsondata = open(TESTJSON_FILENAME, encoding='utf-8').read()
        self.data = EnergyManagerData(json.loads(self.jsondata))
        return super().setUp()

    def test_energy_manager_device(self):
        emd = self.data.energy_manager_device
        self.assertEqual('ERC04-100009999', emd.device.guid)
        self.assertEqual('ERC04', emd.model)
        self.assertEqual('7.32.1.0', emd.firmware)

    def test_location_device(self):
        location: LocationDevice = self.data.location_device
        self.assertEqual('urn:kiwigrid:location:ERC04-100009999:0', location.device.guid)
        self.assertEqual(414.18704999999983, location.power_buffered)
        self.assertEqual(15.000000000000057, location.power_buffered_from_grid)
        self.assertEqual(399.1870499999998, location.power_buffered_from_producers)
        self.assertEqual(715.6345500000002, location.power_consumed)
        self.assertEqual(0, location.power_consumed_from_grid)
        self.assertEqual(715.6345500000002, location.power_consumed_from_producers)
        self.assertEqual(0, location.power_consumed_from_storage)
        self.assertEqual(15, location.power_in)
        self.assertEqual(0, location.power_out)
        self.assertEqual(0, location.power_out_from_producers)
        self.assertEqual(0, location.power_out_from_storage)
        self.assertEqual(1114.8216, location.power_produced)
        self.assertEqual(0, location.power_released)
        self.assertEqual(1114.8216, location.power_self_consumed)
        self.assertEqual(715.6345500000002, location.power_self_supplied)

        self.assertEqual(4283488.229601957, location.work_buffered)
        self.assertEqual(190299.73033571048, location.work_buffered_from_grid)
        self.assertEqual(4093188.49926621, location.work_buffered_from_producers)
        self.assertEqual(5.149921483863968E8, location.work_consumed)
        self.assertEqual(9871556.30100375, location.work_consumed_from_grid)
        self.assertEqual(5.010200705441038E8, location.work_consumed_from_producers)
        self.assertEqual(4100520.9465282103, location.work_consumed_from_storage)
        self.assertEqual(1.0002511231978636E7, location.work_in)
        self.assertEqual(1.5119937024394229E7, location.work_out)
        self.assertEqual(1.4587953669700034E7, location.work_out_from_producers)
        self.assertEqual(56328.72487912017, location.work_out_from_storage)
        self.assertEqual(5.1970121513078356E8, location.work_produced)
        self.assertEqual(4156849.6714072325, location.work_released)
        self.assertEqual(5.051132596381548E8, location.work_self_consumed)
        self.assertEqual(5.0512059208542913E8, location.work_self_supplied)

    def test_battery_converter_devices(self):
        devices = self.data.battery_converter_devices
        self.assertIsNotNone(devices)
        self.assertEqual(1, len(devices))
        battery = devices[0]
        self.assertEqual(3.706000000000001, battery.current_battery_in)
        self.assertEqual(0, battery.current_battery_out)
        self.assertEqual(0.56, battery.current_grm_in)
        self.assertEqual(-3.08, battery.current_grm_out)
        self.assertEqual(0, battery.current_dc_string_in)
        self.assertEqual('CHARGING', battery.mode_converter)
        self.assertEqual(414.18704999999983, battery.power_ac_in)
        self.assertEqual(0, battery.power_ac_out)
        self.assertEqual(90, battery.state_of_charge)
        self.assertEqual(97, battery.state_of_health)
        self.assertEqual(25, battery.temperature_battery)
        self.assertEqual(560.4, battery.voltage_grm_in)
        self.assertEqual(98.5, battery.voltage_grm_out)
        self.assertEqual(4.097, battery.voltage_battery_cell_mean)
        self.assertEqual(98.29999999999998, battery.voltage_battery_string)
        self.assertEqual(2.3768629316151318E8, battery.work_ac_in)
        self.assertEqual(5526783.750943889, battery.work_ac_out)

if __name__ == '__main__':
    unittest.main()
