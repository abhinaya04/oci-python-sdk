# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .projection_rule import ProjectionRule
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TypeListRule(ProjectionRule):
    """
    The type list rule which defines how fields are projected.
    """

    #: A constant which can be used with the matching_strategy property of a TypeListRule.
    #: This constant has a value of "NAME_OR_TAGS"
    MATCHING_STRATEGY_NAME_OR_TAGS = "NAME_OR_TAGS"

    #: A constant which can be used with the matching_strategy property of a TypeListRule.
    #: This constant has a value of "TAGS_ONLY"
    MATCHING_STRATEGY_TAGS_ONLY = "TAGS_ONLY"

    #: A constant which can be used with the matching_strategy property of a TypeListRule.
    #: This constant has a value of "NAME_ONLY"
    MATCHING_STRATEGY_NAME_ONLY = "NAME_ONLY"

    #: A constant which can be used with the rule_type property of a TypeListRule.
    #: This constant has a value of "INCLUDE"
    RULE_TYPE_INCLUDE = "INCLUDE"

    #: A constant which can be used with the rule_type property of a TypeListRule.
    #: This constant has a value of "EXCLUDE"
    RULE_TYPE_EXCLUDE = "EXCLUDE"

    def __init__(self, **kwargs):
        """
        Initializes a new TypeListRule object with values from keyword arguments. The default value of the :py:attr:`~oci.data_integration.models.TypeListRule.model_type` attribute
        of this class is ``TYPE_LIST_RULE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this TypeListRule.
            Allowed values for this property are: "NAME_PATTERN_RULE", "TYPE_LIST_RULE", "NAME_LIST_RULE", "TYPED_NAME_PATTERN_RULE", "RENAME_RULE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type model_type: str

        :param key:
            The value to assign to the key property of this TypeListRule.
        :type key: str

        :param model_version:
            The value to assign to the model_version property of this TypeListRule.
        :type model_version: str

        :param parent_ref:
            The value to assign to the parent_ref property of this TypeListRule.
        :type parent_ref: ParentReference

        :param is_java_regex_syntax:
            The value to assign to the is_java_regex_syntax property of this TypeListRule.
        :type is_java_regex_syntax: bool

        :param config_values:
            The value to assign to the config_values property of this TypeListRule.
        :type config_values: ConfigValues

        :param object_status:
            The value to assign to the object_status property of this TypeListRule.
        :type object_status: int

        :param description:
            The value to assign to the description property of this TypeListRule.
        :type description: str

        :param is_skip_remaining_rules_on_match:
            The value to assign to the is_skip_remaining_rules_on_match property of this TypeListRule.
        :type is_skip_remaining_rules_on_match: bool

        :param scope:
            The value to assign to the scope property of this TypeListRule.
        :type scope: object

        :param is_cascade:
            The value to assign to the is_cascade property of this TypeListRule.
        :type is_cascade: bool

        :param matching_strategy:
            The value to assign to the matching_strategy property of this TypeListRule.
            Allowed values for this property are: "NAME_OR_TAGS", "TAGS_ONLY", "NAME_ONLY", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type matching_strategy: str

        :param is_case_sensitive:
            The value to assign to the is_case_sensitive property of this TypeListRule.
        :type is_case_sensitive: bool

        :param rule_type:
            The value to assign to the rule_type property of this TypeListRule.
            Allowed values for this property are: "INCLUDE", "EXCLUDE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type rule_type: str

        :param types:
            The value to assign to the types property of this TypeListRule.
        :type types: list[BaseType]

        """
        self.swagger_types = {
            'model_type': 'str',
            'key': 'str',
            'model_version': 'str',
            'parent_ref': 'ParentReference',
            'is_java_regex_syntax': 'bool',
            'config_values': 'ConfigValues',
            'object_status': 'int',
            'description': 'str',
            'is_skip_remaining_rules_on_match': 'bool',
            'scope': 'object',
            'is_cascade': 'bool',
            'matching_strategy': 'str',
            'is_case_sensitive': 'bool',
            'rule_type': 'str',
            'types': 'list[BaseType]'
        }

        self.attribute_map = {
            'model_type': 'modelType',
            'key': 'key',
            'model_version': 'modelVersion',
            'parent_ref': 'parentRef',
            'is_java_regex_syntax': 'isJavaRegexSyntax',
            'config_values': 'configValues',
            'object_status': 'objectStatus',
            'description': 'description',
            'is_skip_remaining_rules_on_match': 'isSkipRemainingRulesOnMatch',
            'scope': 'scope',
            'is_cascade': 'isCascade',
            'matching_strategy': 'matchingStrategy',
            'is_case_sensitive': 'isCaseSensitive',
            'rule_type': 'ruleType',
            'types': 'types'
        }

        self._model_type = None
        self._key = None
        self._model_version = None
        self._parent_ref = None
        self._is_java_regex_syntax = None
        self._config_values = None
        self._object_status = None
        self._description = None
        self._is_skip_remaining_rules_on_match = None
        self._scope = None
        self._is_cascade = None
        self._matching_strategy = None
        self._is_case_sensitive = None
        self._rule_type = None
        self._types = None
        self._model_type = 'TYPE_LIST_RULE'

    @property
    def is_skip_remaining_rules_on_match(self):
        """
        Gets the is_skip_remaining_rules_on_match of this TypeListRule.
        skipRemainingRulesOnMatch


        :return: The is_skip_remaining_rules_on_match of this TypeListRule.
        :rtype: bool
        """
        return self._is_skip_remaining_rules_on_match

    @is_skip_remaining_rules_on_match.setter
    def is_skip_remaining_rules_on_match(self, is_skip_remaining_rules_on_match):
        """
        Sets the is_skip_remaining_rules_on_match of this TypeListRule.
        skipRemainingRulesOnMatch


        :param is_skip_remaining_rules_on_match: The is_skip_remaining_rules_on_match of this TypeListRule.
        :type: bool
        """
        self._is_skip_remaining_rules_on_match = is_skip_remaining_rules_on_match

    @property
    def scope(self):
        """
        Gets the scope of this TypeListRule.
        Reference to a typed object, this can be either a key value to an object within the document, a shall referenced to a TypedObject or a full TypedObject definition.


        :return: The scope of this TypeListRule.
        :rtype: object
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """
        Sets the scope of this TypeListRule.
        Reference to a typed object, this can be either a key value to an object within the document, a shall referenced to a TypedObject or a full TypedObject definition.


        :param scope: The scope of this TypeListRule.
        :type: object
        """
        self._scope = scope

    @property
    def is_cascade(self):
        """
        Gets the is_cascade of this TypeListRule.
        cascade


        :return: The is_cascade of this TypeListRule.
        :rtype: bool
        """
        return self._is_cascade

    @is_cascade.setter
    def is_cascade(self, is_cascade):
        """
        Sets the is_cascade of this TypeListRule.
        cascade


        :param is_cascade: The is_cascade of this TypeListRule.
        :type: bool
        """
        self._is_cascade = is_cascade

    @property
    def matching_strategy(self):
        """
        Gets the matching_strategy of this TypeListRule.
        matchingStrategy

        Allowed values for this property are: "NAME_OR_TAGS", "TAGS_ONLY", "NAME_ONLY", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The matching_strategy of this TypeListRule.
        :rtype: str
        """
        return self._matching_strategy

    @matching_strategy.setter
    def matching_strategy(self, matching_strategy):
        """
        Sets the matching_strategy of this TypeListRule.
        matchingStrategy


        :param matching_strategy: The matching_strategy of this TypeListRule.
        :type: str
        """
        allowed_values = ["NAME_OR_TAGS", "TAGS_ONLY", "NAME_ONLY"]
        if not value_allowed_none_or_none_sentinel(matching_strategy, allowed_values):
            matching_strategy = 'UNKNOWN_ENUM_VALUE'
        self._matching_strategy = matching_strategy

    @property
    def is_case_sensitive(self):
        """
        Gets the is_case_sensitive of this TypeListRule.
        caseSensitive


        :return: The is_case_sensitive of this TypeListRule.
        :rtype: bool
        """
        return self._is_case_sensitive

    @is_case_sensitive.setter
    def is_case_sensitive(self, is_case_sensitive):
        """
        Sets the is_case_sensitive of this TypeListRule.
        caseSensitive


        :param is_case_sensitive: The is_case_sensitive of this TypeListRule.
        :type: bool
        """
        self._is_case_sensitive = is_case_sensitive

    @property
    def rule_type(self):
        """
        Gets the rule_type of this TypeListRule.
        ruleType

        Allowed values for this property are: "INCLUDE", "EXCLUDE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The rule_type of this TypeListRule.
        :rtype: str
        """
        return self._rule_type

    @rule_type.setter
    def rule_type(self, rule_type):
        """
        Sets the rule_type of this TypeListRule.
        ruleType


        :param rule_type: The rule_type of this TypeListRule.
        :type: str
        """
        allowed_values = ["INCLUDE", "EXCLUDE"]
        if not value_allowed_none_or_none_sentinel(rule_type, allowed_values):
            rule_type = 'UNKNOWN_ENUM_VALUE'
        self._rule_type = rule_type

    @property
    def types(self):
        """
        Gets the types of this TypeListRule.
        types


        :return: The types of this TypeListRule.
        :rtype: list[BaseType]
        """
        return self._types

    @types.setter
    def types(self, types):
        """
        Sets the types of this TypeListRule.
        types


        :param types: The types of this TypeListRule.
        :type: list[BaseType]
        """
        self._types = types

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
