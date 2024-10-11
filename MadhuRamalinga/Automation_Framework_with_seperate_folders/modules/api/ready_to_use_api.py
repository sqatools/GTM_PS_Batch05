from base.api_base import APIBase
from api_data.api_test_data import *

class ReadyToUseAPI(APIBase):
    def verify_total_mobile_entry(self):
        response = self.get_method(url=api_url)
        response_content = response
        return len(response_content)