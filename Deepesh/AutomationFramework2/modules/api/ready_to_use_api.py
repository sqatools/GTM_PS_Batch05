from base.api_base import APIBase
from api_data.api_test_data import *


class ReadyTOUseAPI(APIBase):
    def verify_total_mobile_entry(self):
        response = self.get_method(url=api_url)
        response_content = response[0]
        res_status_code = response[1]
        return len(response_content), res_status_code

    def verify_to_get_details_for_id_list(self, id_list):
        current_url = f"{api_url}?"
        for id in id_list:
            current_url = f"{current_url}id={id}&"
        response = self.get_method(url=current_url)
        response_content = response[0]
        res_status_code = response[1]
        return response_content, res_status_code

    def create_new_entry_of_mobile_details(self):
        response = self.post_method(url=api_url, header=json_headers, payload=create_entry_payload)
        return response
