# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ConfigValues(object):
    """
    Configuration values can be string, objects or parameters.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ConfigValues object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param config_param_values:
            The value to assign to the config_param_values property of this ConfigValues.
        :type config_param_values: dict(str, ConfigParameterValue)

        :param parent_ref:
            The value to assign to the parent_ref property of this ConfigValues.
        :type parent_ref: ParentReference

        """
        self.swagger_types = {
            'config_param_values': 'dict(str, ConfigParameterValue)',
            'parent_ref': 'ParentReference'
        }

        self.attribute_map = {
            'config_param_values': 'configParamValues',
            'parent_ref': 'parentRef'
        }

        self._config_param_values = None
        self._parent_ref = None

    @property
    def config_param_values(self):
        """
        Gets the config_param_values of this ConfigValues.
        configParamValues


        :return: The config_param_values of this ConfigValues.
        :rtype: dict(str, ConfigParameterValue)
        """
        return self._config_param_values

    @config_param_values.setter
    def config_param_values(self, config_param_values):
        """
        Sets the config_param_values of this ConfigValues.
        configParamValues


        :param config_param_values: The config_param_values of this ConfigValues.
        :type: dict(str, ConfigParameterValue)
        """
        self._config_param_values = config_param_values

    @property
    def parent_ref(self):
        """
        Gets the parent_ref of this ConfigValues.

        :return: The parent_ref of this ConfigValues.
        :rtype: ParentReference
        """
        return self._parent_ref

    @parent_ref.setter
    def parent_ref(self, parent_ref):
        """
        Sets the parent_ref of this ConfigValues.

        :param parent_ref: The parent_ref of this ConfigValues.
        :type: ParentReference
        """
        self._parent_ref = parent_ref

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
