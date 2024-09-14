import json
import os
import unittest

from src.solarwatt_energymanager import EnergyManagerData
from src.solarwatt_energymanager import LocationDevice

TESTJSON_FILENAME = os.path.join(os.path.dirname(__file__), 'data4.json')

class Data4TestCase(unittest.TestCase):
    
    def setUp(self) -> None:
        self.jsondata = open(TESTJSON_FILENAME, encoding='utf-8').read()
        self.data = EnergyManagerData(json.loads(self.jsondata))
        return super().setUp()

    def test_energy_manager_device(self):
        emd = self.data.energy_manager_device
        self.assertEqual('ERC05-000009999', emd.device.guid)
        self.assertEqual('ERC05-000009999', emd.device.get_device_name())
        self.assertEqual('ERC05', emd.model)
        self.assertEqual('7.32.1.0', emd.firmware)

    def test_location_device(self):
        location: LocationDevice = self.data.location_device
        self.assertEqual('aaaaaaaa-bbbb-cccc-dddd-000000000006', location.device.guid)
        self.assertEqual('MeinePV', location.device.get_device_name())
        self.assertEqual(0, location.power_buffered)
        self.assertEqual(0, location.power_buffered_from_grid)
        self.assertEqual(0, location.power_buffered_from_producers)
        self.assertEqual(486, location.power_consumed)
        self.assertEqual(486, location.power_consumed_from_grid)
        self.assertEqual(0, location.power_consumed_from_producers)
        self.assertEqual(0, location.power_consumed_from_storage)
        self.assertEqual(486, location.power_in)
        self.assertEqual(0, location.power_out)
        self.assertEqual(0, location.power_out_from_producers)
        self.assertEqual(0, location.power_out_from_storage)
        self.assertEqual(0, location.power_produced)
        self.assertEqual(0, location.power_released)
        self.assertEqual(0, location.power_self_consumed)
        self.assertEqual(0, location.power_self_supplied)

        self.assertEqual(4293592.651751408, location.work_buffered)
        self.assertEqual(163482.13659905153, location.work_buffered_from_grid)
        self.assertEqual(4130110.515152343, location.work_buffered_from_producers)
        self.assertEqual(2.6361184384432405E7, location.work_consumed)
        self.assertEqual(1.100550531791622E7, location.work_consumed_from_grid)
        self.assertEqual(1.1393130585996052E7, location.work_consumed_from_producers)
        self.assertEqual(3962548.4805204007, location.work_consumed_from_storage)
        self.assertEqual(1.1161651551775163E7, location.work_in)
        self.assertEqual(1.6508402135813877E7, location.work_out)
        self.assertEqual(1.6345010418122537E7, location.work_out_from_producers)
        self.assertEqual(54846.03054258226, location.work_out_from_storage)
        self.assertEqual(3.1868251519271553E7, location.work_produced)
        self.assertEqual(4017393.9949877583, location.work_released)
        self.assertEqual(1.5523241101147508E7, location.work_self_consumed)
        self.assertEqual(1.5355679066514947E7, location.work_self_supplied)

    def test_battery_converter_devices(self):
        devices = self.data.battery_converter_devices
        self.assertIsNotNone(devices)
        self.assertEqual(1, len(devices))
        battery1 = devices[0]
        self.assertEqual('aaaaaaaa-bbbb-cccc-dddd-000000000007', battery1.device.guid)
        self.assertEqual('MyReserve a3a3a3a3a3a3', battery1.device.get_device_name())
        self.assertEqual(0.01, battery1.current_battery_in)
        self.assertEqual(0, battery1.current_battery_out)
        self.assertEqual(0, battery1.current_grm_in)
        self.assertEqual(0, battery1.current_grm_out)
        self.assertEqual(None, battery1.current_dc_string_in)
        self.assertEqual('OFF', battery1.mode_converter)
        self.assertEqual(0, battery1.power_ac_in)
        self.assertEqual(0, battery1.power_ac_out)
        self.assertEqual(4, battery1.state_of_charge)
        self.assertEqual(96, battery1.state_of_health)
        self.assertEqual(21, battery1.temperature_battery)
        self.assertEqual(2.2, battery1.voltage_grm_in)
        self.assertEqual(1.7000000000000002, battery1.voltage_grm_out)
        self.assertEqual(3.317, battery1.voltage_battery_cell_mean)
        self.assertEqual(79.59999999999998, battery1.voltage_battery_string)
        self.assertEqual(4294169.497789343, battery1.work_ac_in)
        self.assertEqual(4018079.4006808116, battery1.work_ac_out)

    def test_ev_station_device(self):
        devices = self.data.ev_station_devices
        self.assertIsNotNone(devices)
        self.assertEqual(2, len(devices))
        ev1 = devices[0]
        self.assertEqual('urn:keba:evstation:88888888', ev1.device.guid)
        self.assertEqual('Keba P30 c-series 22222222', ev1.device.get_device_name())
        self.assertEqual(0, ev1.power_ac_in)
        self.assertEqual(None, ev1.power_ac_out)
        self.assertEqual(1911056.2, ev1.work_ac_in)
        self.assertEqual(None, ev1.work_ac_out)
        self.assertEqual(14195.2, ev1.work_ac_in_session)
        self.assertEqual(None, ev1.state_of_charge)
        self.assertEqual('STANDBY', ev1.mode_station)
        self.assertEqual(None, ev1.temperature_battery)
        ev2 = devices[1]
        self.assertEqual('urn:keba:evstation:99999999', ev2.device.guid)
        self.assertEqual('Keba P30 x-series 99999999', ev2.device.get_device_name())
        self.assertEqual(0, ev2.power_ac_in)
        self.assertEqual(None, ev2.power_ac_out)
        self.assertEqual(4115966.3, ev2.work_ac_in)
        self.assertEqual(None, ev2.work_ac_out)
        self.assertEqual(10460.6, ev2.work_ac_in_session)
        self.assertEqual(None, ev2.state_of_charge)
        self.assertEqual('STANDBY', ev2.mode_station)
        self.assertEqual(None, ev2.temperature_battery)

    def test_s0_counter_device(self):
        devices = self.data.s0_counter_devices
        self.assertIsNotNone(devices)
        self.assertEqual(1, len(devices))
        s0 = devices[0]
        self.assertEqual('aaaaaaaa-bbbb-cccc-dddd-000000000005', s0.device.guid)
        self.assertEqual('S0-1 (Wärmepumpe)', s0.device.get_device_name())
        self.assertEqual(0, s0.power_in)
        self.assertEqual(0, s0.power_out)
        self.assertEqual(1403148.0, s0.work_in)
        self.assertEqual(0, s0.work_out)
        self.assertEqual(1404518, s0.count_pulses)

if __name__ == '__main__':
    unittest.main()
