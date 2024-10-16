import pytest
from modules.api.ready_to_use_api import ReadyToUseAPI

class TestReadyToUseAPI:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.api_obj = ReadyToUseAPI()

    def test_total_entries(self):
        total_entry = self.api_obj.verify_total_mobile_entry()
        assert total_entry[0] == 13
        assert total_entry[1] == 200

    def test_specific_list_id_entries(self):
        response_data = self.api_obj.verify_to_get_details_for_id_lists([5, 7, 8])
        assert len(response_data[0]) == 3
        assert response_data[1] == 200

    def test_create_new_entry_in_db(self):
        response_data = self.api_obj.create_new_entry_of_mobile_details()
        assert response_data[1] == 200
        #self.api_obj.log.info(f"new id: {response_data[0]['id']}")

    def test_update_specific_list_id(self):
        response_data = self.api_obj.create_new_entry_of_mobile_details()
        new_id = response_data[0]['id']
        assert response_data[1] == 200
        response_data = self.api_obj.update_mobile_details(new_id)
        assert response_data[1] == 200

    def test_partial_update_specific_list_id(self):
        response_data = self.api_obj.create_new_entry_of_mobile_details()
        new_id = response_data[0]['id']
        response_data = self.api_obj.partial_update_mobile_details(new_id)
        assert response_data[1] == 200
        print(f"server new ID : {new_id}")

    def test_delete_specific_list_id(self):
        response_data = self.api_obj.create_new_entry_of_mobile_details()
        new_id = response_data[0]['id']
        response_data = self.api_obj.delete_mobile_details(new_id)
        assert response_data[1] == 200

#command: python -m pytest -v .\tests\api\test_ready_api.p