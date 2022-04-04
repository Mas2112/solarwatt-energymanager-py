import json
import os
import unittest

from src.solarwatt_energymanager import EnergyManagerData
from src.solarwatt_energymanager import LocationDevice

TESTJSON_FILENAME = os.path.join(os.path.dirname(__file__), 'data3.json')

class Data3TestCase(unittest.TestCase):
    
    def setUp(self) -> None:
        self.jsondata = open(TESTJSON_FILENAME).read()
        self.data = EnergyManagerData(json.loads(self.jsondata))
        return super().setUp()

    def test_energy_manager_device(self):
        emd = self.data.energy_manager_device
        self.assertEqual('ERC05-000012345', emd.device.guid)
        self.assertEqual('ERC05', emd.model)
        self.assertEqual('7.32.1.0', emd.firmware)

    def test_location_device(self):
        location: LocationDevice = self.data.location_device
        self.assertEqual('aaaaaaaa-bbbb-cccc-dddd-000000000004', location.device.guid)
        self.assertEqual(0, location.power_buffered)
        self.assertEqual(0, location.power_buffered_from_grid)
        self.assertEqual(0, location.power_buffered_from_producers)
        self.assertEqual(3334, location.power_consumed)
        self.assertEqual(0, location.power_consumed_from_grid)
        self.assertEqual(2481.224, location.power_consumed_from_producers)
        self.assertEqual(852.7759999999998, location.power_consumed_from_storage)
        self.assertEqual(0, location.power_in)
        self.assertEqual(0, location.power_out)
        self.assertEqual(0, location.power_out_from_producers)
        self.assertEqual(1.1368683772161603E-13, location.power_out_from_storage)
        self.assertEqual(2481.224, location.power_produced)
        self.assertEqual(852.776, location.power_released)
        self.assertEqual(2481.224, location.power_self_consumed)
        self.assertEqual(3334, location.power_self_supplied)

        self.assertEqual(342637.0619042938, location.work_buffered)
        self.assertEqual(3426.0528680366665, location.work_buffered_from_grid)
        self.assertEqual(339211.0090362565, location.work_buffered_from_producers)
        self.assertEqual(978077.2563316077, location.work_consumed)
        self.assertEqual(1143.5562620432531, location.work_consumed_from_grid)
        self.assertEqual(655589.9383950429, location.work_consumed_from_producers)
        self.assertEqual(321343.76167454466, location.work_consumed_from_storage)
        self.assertEqual(1168.7634251943657, location.work_in)
        self.assertEqual(36.44303735421888, location.work_out)
        self.assertEqual(23.60045816845463, location.work_out_from_producers)
        self.assertEqual(3256.0831291010977, location.work_out_from_storage)
        self.assertEqual(994824.5478894478, location.work_produced)
        self.assertEqual(324599.8448036454, location.work_released)
        self.assertEqual(994800.9474312791, location.work_self_consumed)
        self.assertEqual(976933.7000695658, location.work_self_supplied)

    def test_battery_converter_devices(self):
        devices = self.data.battery_converter_devices
        self.assertIsNotNone(devices)
        self.assertEqual(3, len(devices))
        battery1 = devices[0]
        self.assertEqual('aaaaaaaa-bbbb-cccc-dddd-000000000002', battery1.device.guid)
        self.assertEqual(1.46, battery1.current_battery_in)
        self.assertEqual(0, battery1.current_battery_out)
        self.assertEqual(0, battery1.current_grm_in)
        self.assertEqual(0, battery1.current_grm_out)
        self.assertEqual(2.14, battery1.current_dc_string_in)
        self.assertEqual('CHARGING', battery1.mode_converter)
        self.assertEqual(0, battery1.power_ac_in)
        self.assertEqual(481.59999999999997, battery1.power_ac_out)
        self.assertEqual(51, battery1.state_of_charge)
        self.assertEqual(0, battery1.state_of_health)
        self.assertEqual(0, battery1.temperature_battery)
        self.assertEqual(529.5, battery1.voltage_grm_in)
        self.assertEqual(0, battery1.voltage_grm_out)
        self.assertEqual(0, battery1.voltage_battery_cell_mean)
        self.assertEqual(224.3, battery1.voltage_battery_string)
        self.assertEqual(135948.58624138884, battery1.work_ac_in)
        self.assertEqual(127860.89102430471, battery1.work_ac_out)
        battery2 = devices[1]
        self.assertEqual('aaaaaaaa-bbbb-cccc-dddd-000000000003', battery2.device.guid)
        self.assertEqual(0, battery2.current_battery_in)
        self.assertEqual(0.01, battery2.current_battery_out)
        self.assertEqual(0, battery2.current_grm_in)
        self.assertEqual(0, battery2.current_grm_out)
        self.assertEqual(1.06, battery2.current_dc_string_in)
        self.assertEqual('OFF', battery2.mode_converter)
        self.assertEqual(0, battery2.power_ac_in)
        self.assertEqual(371.176, battery2.power_ac_out)
        self.assertEqual(24, battery2.state_of_charge)
        self.assertEqual(0, battery2.state_of_health)
        self.assertEqual(0, battery2.temperature_battery)
        self.assertEqual(631.0, battery2.voltage_grm_in)
        self.assertEqual(0, battery2.voltage_grm_out)
        self.assertEqual(0, battery2.voltage_battery_cell_mean)
        self.assertEqual(216.0, battery2.voltage_battery_string)
        self.assertEqual(129879.73267930634, battery2.work_ac_in)
        self.assertEqual(124903.30850069378, battery2.work_ac_out)
        battery3 = devices[2]
        self.assertEqual('aaaaaaaa-bbbb-cccc-dddd-000000000001', battery3.device.guid)
        self.assertEqual(0.01, battery3.current_battery_in)
        self.assertEqual(0, battery3.current_battery_out)
        self.assertEqual(0, battery3.current_grm_in)
        self.assertEqual(0, battery3.current_grm_out)
        self.assertEqual(1.47, battery3.current_dc_string_in)
        self.assertEqual('OFF', battery3.mode_converter)
        self.assertEqual(0, battery3.power_ac_in)
        self.assertEqual(0, battery3.power_ac_out)
        self.assertEqual(28, battery3.state_of_charge)
        self.assertEqual(0, battery3.state_of_health)
        self.assertEqual(0, battery3.temperature_battery)
        self.assertEqual(596.1, battery3.voltage_grm_in)
        self.assertEqual(0, battery3.voltage_grm_out)
        self.assertEqual(0, battery3.voltage_battery_cell_mean)
        self.assertEqual(218.1, battery3.voltage_battery_string)
        self.assertEqual(76935.05782958351, battery3.work_ac_in)
        self.assertEqual(71837.17347263735, battery3.work_ac_out)

if __name__ == '__main__':
    unittest.main()
