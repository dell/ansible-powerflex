#!/usr/bin/python

# Copyright: (c) 2025, Dell Technologies
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

""" Ansible module for managing device groups on Dell Technologies (Dell) PowerFlex"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

DOCUMENTATION = r'''
module: device_group
version_added: 'todo TTHE'
notes:
  - The I(check_mode) is supported.
'''

EXAMPLES = r'''
'''

RETURN = r'''
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.dellemc.powerflex.plugins.module_utils.storage.dell.libraries.powerflex_base \
    import PowerFlexBase
from ansible_collections.dellemc.powerflex.plugins.module_utils.storage.dell import utils

LOG = utils.get_logger('device_group')


class PowerFlexDeviceGroup(PowerFlexBase):
    """Class with device group operations"""

    def __init__(self):
        """ Define all parameters required by this module"""        
        mutually_exclusive = [["protection_domain_id", "protection_domain_name"],
                              ['device_group_name', 'device_group_id']]
        required_one_of = [["device_group_name", "device_group_id"]]
        ansible_module_params = {
            'argument_spec': get_powerflex_device_group_parameters(),
            'supports_check_mode': True,
            'mutually_exclusive': mutually_exclusive,
            'required_one_of': required_one_of
        }
        super().__init__(AnsibleModule, ansible_module_params)

        self.result = dict(
            changed=False,
            device_group_details={},
            diff={}
        )

    def validate_create_parameters(self, device_group_params):
        """Validate the input parameters
        :param device_group_params: The dict of device group parameters
        :type device_group_params: dict
        """
        if device_group_params['device_group_id']:
            self.module.fail_json(msg="Provide device_group_name only for creation of device group, "
                                  "device_group_id given.")
        if device_group_params['device_group_name'] is None or len(device_group_params['device_group_name'].strip()) == 0:
            self.module.fail_json(msg="Provide device_group_name for creation of device group.")
        if device_group_params['media_type'] is None or len(device_group_params['media_type'].strip()) == 0:
            self.module.fail_json(msg="Provide media_type for creation of device group.")
        protection_domain_identify = device_group_params["protection_domain_id"] \
            if device_group_params["protection_domain_id"] else device_group_params["protection_domain_name"]
        if protection_domain_identify is None or len(protection_domain_identify.strip()) == 0:
            self.module.fail_json(msg="Either protection_domain_id or protection_domain_name "
                                  "needs to be provided for creation of device group.")
        # if device_group_params['device_group_name'] is not None \ # todo TTHE dgName seems is required in new Array version
        #         and len(device_group_params['device_group_name'].strip()) == 0:
        #     self.module.fail_json(msg="Provide valid device_group_name for creation of device group.")

    def get_protection_domain(self, protection_domain_name=None, protection_domain_id=None):
        """Get protection domain details
            :param protection_domain_name: Name of the protection domain
            :param protection_domain_id: ID of the protection domain
            :return: Protection domain details
            :rtype: dict
        """
        name_or_id = protection_domain_id if protection_domain_id \
            else protection_domain_name
        try:
            pd_details = None
            if protection_domain_id:
                pd_details = self.powerflex_conn.protection_domain.get(
                    filter_fields={'id': protection_domain_id})

            if protection_domain_name:
                pd_details = self.powerflex_conn.protection_domain.get(
                    filter_fields={'name': protection_domain_name})

            if not pd_details:
                error_msg = "Unable to find the protection domain with " \
                            "'%s'. Please enter a valid protection domain " \
                            "name/id." % name_or_id
                LOG.error(error_msg)
                self.module.fail_json(msg=error_msg)

            return pd_details[0]

        except Exception as e:
            error_msg = "Failed to get the protection domain '%s' with " \
                        "error '%s'" % (name_or_id, str(e))
            LOG.error(error_msg)
            self.module.fail_json(msg=error_msg)

    def get_device_group(self, device_group_id=None, device_group_name=None):
        """Get device group details
            :param device_group_name: Name of the device group.
            :param device_group_id: ID of the device group.
            :return: device group details
        """
        try:
            device_group_details = None
            if device_group_id:
                device_group_details = self.powerflex_conn.device_group.get(
                    filter_fields={'id': device_group_id})

            if device_group_name:
                device_group_details = self.powerflex_conn.device_group.get(
                    filter_fields={'name': device_group_name})

            if not device_group_details:
                msg = "Unable to find the device group."
                LOG.info(msg)
                return None

            pd_details = self.get_protection_domain(protection_domain_id=device_group_details[0]['protectionDomainId'])
            device_group_details[0]['protectionDomainName'] = pd_details['name']
            return device_group_details[0]

        except Exception as e:
            errormsg = f'Failed to get the device group with error {str(e)}'
            LOG.error(errormsg)
            self.module.fail_json(msg=errormsg)

    def create_device_group(self, media_type, protection_domain_id,
                            device_group_name=None, spare_node_count=None, spare_device_count=None):
        """Create device group
            :param media_type: Media type of device group.
            :type media_type: str
            :param protection_domain_id: Protection Domain ID.
            :type protection_domain_id: str
            :param device_group_name: Name of the device group.
            :type device_group_name: str
            :param spare_node_count: todo TTHE update this description.
            :type spare_node_count: str
            :param spare_device_count: todo TTHE update this description.
            :type spare_device_count: str
            :return: Id of the device group, if created.
        """
        try:
            if self.module._diff:
                self.result.update({"diff": {"before": {},
                                             "after": {
                                                 "protection_domain_id": protection_domain_id,
                                                 "media_type": media_type,
                                                 "device_group_name": device_group_name,
                                                 "spare_node_count": spare_node_count,
                                                 "spare_device_count": spare_device_count}}})

            if not self.module.check_mode:
                device_group_id = self.powerflex_conn.device_group.create(
                    protection_domain_id=protection_domain_id,
                    media_type=media_type,
                    name=device_group_name,
                    spare_node_count=spare_node_count,
                    spare_device_count=spare_device_count)
                return device_group_id

        except Exception as e:
            errormsg = f'Creation of device group failed with error {str(e)}'
            LOG.error(errormsg)
            self.module.fail_json(msg=errormsg)

    def delete_device_group(self, device_group_details):
        """Delete device group
            :param device_group_details: The details of the device group.
            :return: Details of the device group.
        """
        device_group_id = device_group_details['id']
        try:
            if self.module._diff:
                self.result.update({"diff": {"before": device_group_details, "after": {}}})

            if not self.module.check_mode:
                self.powerflex_conn.device_group.delete(device_group_id)
            return self.get_device_group(device_group_id=device_group_id)

        except Exception as e:
            errormsg = (f'Deletion of device group {device_group_id} '
                        f'failed with error {str(e)}')
            LOG.error(errormsg)
            self.module.fail_json(msg=errormsg)

    def to_modify(self, device_group_details, spare_node_count, spare_device_count, new_name):
        """Whether to modify the device group or not
        :param device_group_details: Details of the device group.
        :param spare_node_count: todo TTHE .
        :param spare_device_count: TODO tthe.
        :param new_name: The new name of the device group.
        :return: Dictionary containing the attributes of device group which are to be updated.
        """
        modify_dict = {}

        if spare_node_count is not None and \
                device_group_details['spareNodeCount'] != spare_node_count:
            modify_dict['spare_node_count'] = spare_node_count

        if spare_device_count is not None and \
                device_group_details['spareDeviceCount'] != spare_device_count:
            modify_dict['spare_device_count'] = spare_device_count

        if new_name is not None:
            if len(new_name.strip()) == 0:
                self.module.fail_json(
                    msg="Provide valid name.")
            if new_name != device_group_details['name']:
                modify_dict['new_name'] = new_name

        return modify_dict

    def modify_device_group(self, device_group_details, modify_dict):
        """
        Modify the device group attributes
        :param device_group: Details of the device group.
        :param modify_dict: Dictionary containing the attributes of device group which are to be updated.
        :return: True, if the operation is successful.
        """
        try:
            msg = (f"Dictionary containing attributes which are to be"
                   f" updated is {str(modify_dict)}.")
            LOG.info(msg)
            
            if self.module._diff:
                self.result.update({"diff": {"before":
                                             {"device_group_name": device_group_details['name'],
                                              "spare_node_count": device_group_details['spareNodeCount'],
                                              "spare_device_count": device_group_details['spareDeviceCount']
                                             },
                                             "after": modify_dict}})

            if not self.module.check_mode:
                if modify_dict:
                    self.powerflex_conn.device_group.modify(
                        device_group_id=device_group_details['id'],
                        new_name=modify_dict['new_name'],
                        spare_node_count=modify_dict['spare_node_count'],
                        spare_device_count=modify_dict['spare_device_count'])
                    msg = (f"The device group attributes are updated to {str(modify_dict)} sucessfully.")
                    LOG.info(msg)
            return True, self.get_device_group(device_group_id=device_group_details['id'])

        except Exception as e:
            err_msg = (f"Failed to update the device group {device_group_details['id']}"
                       f" with error {str(e)}")
            LOG.error(err_msg)
            self.module.fail_json(msg=err_msg)


def get_powerflex_device_group_parameters():
    """This method provide parameter required for the device group module on PowerFlex"""
    return dict(
        device_group_name=dict(), 
        device_group_id=dict(),
        new_name=dict(),
        media_type=dict(type='str', choices=['SSD', 'PMEM']),
        protection_domain_id=dict(type='str'),
        protection_domain_name=dict(type='str'),
        spare_node_count=dict(type='int'),
        spare_device_count=dict(type='int'),
        state=dict(default='present', choices=['present', 'absent']),
        force=dict(type='bool', default=False) # todo TTHE is this needed?
    )


class DeviceGroupCreateHandler():
    def handle(self, device_group_object, device_group_params, device_group_details):
        create_flag = False
        if device_group_params['state'] == 'present' and not device_group_details:
            device_group_object.validate_create_parameters(device_group_params=device_group_params)
            protection_domain_id = device_group_params["protection_domain_id"]
            if device_group_params["protection_domain_name"]:
                protection_domain_id = device_group_object.get_protection_domain(
                    protection_domain_name=device_group_params["protection_domain_name"])["id"]

            device_group_id = device_group_object.create_device_group(
                media_type=device_group_params["media_type"],
                protection_domain_id=protection_domain_id,
                device_group_name=device_group_params["device_group_name"],
                spare_node_count=device_group_params["spare_node_count"],
                spare_device_count=device_group_params["spare_device_count"])

            device_group_object.result['changed'] = True
            create_flag = True
            if device_group_id:
                device_group_details = device_group_object.get_device_group(
                    device_group_name=device_group_params['device_group_name'],
                    device_group_id=device_group_params['device_group_id'])
                msg = (f"device group created successfully, fetched "
                       f"device group details {str(device_group_details)}")
                LOG.info(msg)
        DeviceGroupModifyHandler().handle(device_group_object, device_group_params,
                                          device_group_details, create_flag)


class DeviceGroupModifyHandler():
    def handle(self, device_group_object, device_group_params, device_group_details, create_flag=False):
        modify_dict = {}
        if not create_flag and device_group_params['state'] == 'present' and device_group_details:
            modify_dict = device_group_object.to_modify(
                device_group_details=device_group_details,
                new_name=device_group_params['new_name'],
                spare_node_count=device_group_params['spare_node_count'],
                spare_device_count=device_group_params['spare_device_count'])
        if modify_dict and device_group_params['state'] == 'present':
            changed, device_group_details = device_group_object.modify_device_group(
                device_group_details=device_group_details, modify_dict=modify_dict)
            device_group_object.result['changed'] |= changed
        DeviceGroupDeleteHandler().handle(device_group_object, device_group_params, device_group_details)


class DeviceGroupDeleteHandler():
    def handle(self, device_group_object, device_group_params, device_group_details):
        if device_group_params['state'] == 'absent' and device_group_details:
            device_group_details = device_group_object.delete_device_group(
                device_group_details=device_group_details)
            device_group_object.result['changed'] = True
        DeviceGroupExitHandler().handle(device_group_object, device_group_details)


class DeviceGroupExitHandler():
    def handle(self, device_group_object, device_group_details):
        device_group_object.result['device_group_details'] = device_group_details
        device_group_object.module.exit_json(**device_group_object.result)


class DeviceGroupHandler():
    def handle(self, device_group_object, device_group_params):
        device_group_details = device_group_object.get_device_group(
            device_group_name=device_group_params['device_group_name'],
            device_group_id=device_group_params['device_group_id'])
        DeviceGroupCreateHandler().handle(device_group_object, device_group_params, device_group_details)


def main():
    """ Create PowerFlex device group object and perform action on it
        based on user input from playbook"""
    device_group_obj = PowerFlexDeviceGroup()
    DeviceGroupHandler().handle(device_group_obj, device_group_obj.module.params)


if __name__ == '__main__':
    main()
