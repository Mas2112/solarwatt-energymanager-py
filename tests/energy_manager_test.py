import json
import os
from unittest.async_case import IsolatedAsyncioTestCase
from src.solarwatt_energymanager.energy_manager import CannotConnect
from src.solarwatt_energymanager import EnergyManager

TESTJSON_FILENAME = os.path.join(os.path.dirname(__file__), 'data1.json')

class TestEnergyManager(EnergyManager):
    async def query_json_data(self):
        jsondata = open(TESTJSON_FILENAME).read()
        return json.loads(jsondata)

class ExceptionEnergyManager(EnergyManager):
    async def query_json_data(self):
        raise Exception('test')

class EnergyManagerTest(IsolatedAsyncioTestCase):
    async def test_test_connection_succcess(self):
        em = TestEnergyManager('localhost')
        guid = await em.test_connection()
        self.assertEqual('ERC05-000099999', guid)

    async def test_test_connection_error(self):
        em = ExceptionEnergyManager('localhost')
        with self.assertRaises(CannotConnect):
            await em.test_connection()

    async def test_get_data(self):
        em = TestEnergyManager('localhost')
        data = await em.get_data()
        self.assertEqual('ERC05', data.energy_manager_device.model)
