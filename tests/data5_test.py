import json
import os
import unittest

from src.solarwatt_energymanager import EnergyManagerData

TESTJSON_FILENAME = os.path.join(os.path.dirname(__file__), 'data5.json')

class Data5TestCase(unittest.TestCase):
    
    def setUp(self) -> None:
        self.jsondata = open(TESTJSON_FILENAME, encoding='utf-8').read()
        self.data = EnergyManagerData(json.loads(self.jsondata))
        return super().setUp()

    def test_power_meter_device(self):
        devices = self.data.power_meter_devices
        self.assertIsNotNone(devices)
        self.assertEqual(1, len(devices))
        pm = devices[0]
        self.assertEqual('urn:sml:09-RE-DA-CT-ED-RE-DA-CT-ED-bf', pm.device.guid)
        self.assertEqual('EDL Zaehler (09-RE-DA-CT-ED-RE-DA-CT-ED-bf', pm.device.get_device_name())
        self.assertEqual(242.10000000000002, pm.power_in)
        self.assertEqual(0, pm.power_out)
        self.assertEqual(2.75862576E7, pm.work_in)
        self.assertEqual(1.7510368900000002E7, pm.work_out)

if __name__ == '__main__':
    unittest.main()
