import pytest
from modules.api.ready_to_use_api import ReadyTOUseAPI

class TestReadyToUseAPI:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.api_obj = ReadyTOUseAPI()

    def test_total_entries(self):
         total_entry = self.api_obj.verify_total_mobile_entry()
         assert total_entry == 13
