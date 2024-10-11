import pytest
from modules.api.ready_to_use_api import ReadyToUseAPI

class TestReadyToUseAPI:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.api_obj = ReadyToUseAPI()

    def test_total_entries(self):
        total_entry = self.api_obj.verify_total_mobile_entry()
        assert total_entry == 13

#command: python -m pytest -v .\tests\api\test_api_read.py