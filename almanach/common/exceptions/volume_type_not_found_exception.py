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
from almanach.common.exceptions.almanach_exception import AlmanachException


class VolumeTypeNotFoundException(AlmanachException):

    def __init__(self, volume_type_id, message=None):
        if not message:
            message = "Unable to find volume_type id '{volume_type_id}'".format(volume_type_id=volume_type_id)

        super(VolumeTypeNotFoundException, self).__init__(message)
