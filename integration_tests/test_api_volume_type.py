# Copyright 2016 Internap.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from uuid import uuid4
from hamcrest import assert_that, equal_to

from base_api_volume_testcase import BaseApiVolumeTestCase
from builders import messages


class ApiVolumeTypeTest(BaseApiVolumeTestCase):
    def test_volume_type_create(self):
        volume_type_query = "{url}/volume_type"
        volume_type_id = str(uuid4())
        data = dict(
                type_id=volume_type_id,
                type_name=messages.DEFAULT_VOLUME_NAME
        )

        response = self.almanachHelper.post(url=volume_type_query, data=data)
        assert_that(response.status_code, equal_to(201))

        volume_type_get_query = "{url}/volume_type/{volume_type_id}"

        response = self.almanachHelper.get(url=volume_type_get_query, volume_type_id=volume_type_id)
        assert_that(response.status_code, equal_to(200))
        assert_that(response.json(), equal_to({'volume_type_id': data['type_id'],
                                               'volume_type_name': data['type_name']}))
