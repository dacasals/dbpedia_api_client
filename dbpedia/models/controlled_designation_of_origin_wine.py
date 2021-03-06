# coding: utf-8

"""
    DBpedia

    This is the API of the DBpedia Ontology  # noqa: E501

    The version of the OpenAPI document: v0.0.1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from dbpedia.configuration import Configuration


class ControlledDesignationOfOriginWine(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'approximate_calories': 'list[float]',
        'ingredient': 'list[object]',
        'taste': 'list[str]',
        'description': 'list[str]',
        'type_of_yeast': 'list[str]',
        'discontinued': 'list[str]',
        'label': 'list[str]',
        'type': 'list[str]',
        'percentage_alcohol': 'list[int]',
        'creator_of_dish': 'list[object]',
        'serving_temperature': 'list[str]',
        'introduced': 'list[str]',
        'type_of_storage': 'list[str]',
        'id': 'str',
        'type_of_grain': 'list[str]'
    }

    attribute_map = {
        'approximate_calories': 'approximateCalories',
        'ingredient': 'ingredient',
        'taste': 'taste',
        'description': 'description',
        'type_of_yeast': 'typeOfYeast',
        'discontinued': 'discontinued',
        'label': 'label',
        'type': 'type',
        'percentage_alcohol': 'percentageAlcohol',
        'creator_of_dish': 'creatorOfDish',
        'serving_temperature': 'servingTemperature',
        'introduced': 'introduced',
        'type_of_storage': 'typeOfStorage',
        'id': 'id',
        'type_of_grain': 'typeOfGrain'
    }

    def __init__(self, approximate_calories=None, ingredient=None, taste=None, description=None, type_of_yeast=None, discontinued=None, label=None, type=None, percentage_alcohol=None, creator_of_dish=None, serving_temperature=None, introduced=None, type_of_storage=None, id=None, type_of_grain=None, local_vars_configuration=None):  # noqa: E501
        """ControlledDesignationOfOriginWine - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._approximate_calories = None
        self._ingredient = None
        self._taste = None
        self._description = None
        self._type_of_yeast = None
        self._discontinued = None
        self._label = None
        self._type = None
        self._percentage_alcohol = None
        self._creator_of_dish = None
        self._serving_temperature = None
        self._introduced = None
        self._type_of_storage = None
        self._id = None
        self._type_of_grain = None
        self.discriminator = None

        self.approximate_calories = approximate_calories
        self.ingredient = ingredient
        self.taste = taste
        self.description = description
        self.type_of_yeast = type_of_yeast
        self.discontinued = discontinued
        self.label = label
        self.type = type
        self.percentage_alcohol = percentage_alcohol
        self.creator_of_dish = creator_of_dish
        self.serving_temperature = serving_temperature
        self.introduced = introduced
        self.type_of_storage = type_of_storage
        if id is not None:
            self.id = id
        self.type_of_grain = type_of_grain

    @property
    def approximate_calories(self):
        """Gets the approximate_calories of this ControlledDesignationOfOriginWine.  # noqa: E501

        Approximate calories per serving.  # noqa: E501

        :return: The approximate_calories of this ControlledDesignationOfOriginWine.  # noqa: E501
        :rtype: list[float]
        """
        return self._approximate_calories

    @approximate_calories.setter
    def approximate_calories(self, approximate_calories):
        """Sets the approximate_calories of this ControlledDesignationOfOriginWine.

        Approximate calories per serving.  # noqa: E501

        :param approximate_calories: The approximate_calories of this ControlledDesignationOfOriginWine.  # noqa: E501
        :type: list[float]
        """

        self._approximate_calories = approximate_calories

    @property
    def ingredient(self):
        """Gets the ingredient of this ControlledDesignationOfOriginWine.  # noqa: E501

        An ingredient is a substance that forms part of a mixture (in a general sense). Here it is used in the context of recipes that specify which ingredients are used to prepare a specific dish or drink.  # noqa: E501

        :return: The ingredient of this ControlledDesignationOfOriginWine.  # noqa: E501
        :rtype: list[object]
        """
        return self._ingredient

    @ingredient.setter
    def ingredient(self, ingredient):
        """Sets the ingredient of this ControlledDesignationOfOriginWine.

        An ingredient is a substance that forms part of a mixture (in a general sense). Here it is used in the context of recipes that specify which ingredients are used to prepare a specific dish or drink.  # noqa: E501

        :param ingredient: The ingredient of this ControlledDesignationOfOriginWine.  # noqa: E501
        :type: list[object]
        """

        self._ingredient = ingredient

    @property
    def taste(self):
        """Gets the taste of this ControlledDesignationOfOriginWine.  # noqa: E501

        Description not available  # noqa: E501

        :return: The taste of this ControlledDesignationOfOriginWine.  # noqa: E501
        :rtype: list[str]
        """
        return self._taste

    @taste.setter
    def taste(self, taste):
        """Sets the taste of this ControlledDesignationOfOriginWine.

        Description not available  # noqa: E501

        :param taste: The taste of this ControlledDesignationOfOriginWine.  # noqa: E501
        :type: list[str]
        """

        self._taste = taste

    @property
    def description(self):
        """Gets the description of this ControlledDesignationOfOriginWine.  # noqa: E501

        small description  # noqa: E501

        :return: The description of this ControlledDesignationOfOriginWine.  # noqa: E501
        :rtype: list[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ControlledDesignationOfOriginWine.

        small description  # noqa: E501

        :param description: The description of this ControlledDesignationOfOriginWine.  # noqa: E501
        :type: list[str]
        """

        self._description = description

    @property
    def type_of_yeast(self):
        """Gets the type_of_yeast of this ControlledDesignationOfOriginWine.  # noqa: E501

        Description not available  # noqa: E501

        :return: The type_of_yeast of this ControlledDesignationOfOriginWine.  # noqa: E501
        :rtype: list[str]
        """
        return self._type_of_yeast

    @type_of_yeast.setter
    def type_of_yeast(self, type_of_yeast):
        """Sets the type_of_yeast of this ControlledDesignationOfOriginWine.

        Description not available  # noqa: E501

        :param type_of_yeast: The type_of_yeast of this ControlledDesignationOfOriginWine.  # noqa: E501
        :type: list[str]
        """

        self._type_of_yeast = type_of_yeast

    @property
    def discontinued(self):
        """Gets the discontinued of this ControlledDesignationOfOriginWine.  # noqa: E501

        Description not available  # noqa: E501

        :return: The discontinued of this ControlledDesignationOfOriginWine.  # noqa: E501
        :rtype: list[str]
        """
        return self._discontinued

    @discontinued.setter
    def discontinued(self, discontinued):
        """Sets the discontinued of this ControlledDesignationOfOriginWine.

        Description not available  # noqa: E501

        :param discontinued: The discontinued of this ControlledDesignationOfOriginWine.  # noqa: E501
        :type: list[str]
        """

        self._discontinued = discontinued

    @property
    def label(self):
        """Gets the label of this ControlledDesignationOfOriginWine.  # noqa: E501

        short description of the resource  # noqa: E501

        :return: The label of this ControlledDesignationOfOriginWine.  # noqa: E501
        :rtype: list[str]
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this ControlledDesignationOfOriginWine.

        short description of the resource  # noqa: E501

        :param label: The label of this ControlledDesignationOfOriginWine.  # noqa: E501
        :type: list[str]
        """

        self._label = label

    @property
    def type(self):
        """Gets the type of this ControlledDesignationOfOriginWine.  # noqa: E501

        type of the resource  # noqa: E501

        :return: The type of this ControlledDesignationOfOriginWine.  # noqa: E501
        :rtype: list[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ControlledDesignationOfOriginWine.

        type of the resource  # noqa: E501

        :param type: The type of this ControlledDesignationOfOriginWine.  # noqa: E501
        :type: list[str]
        """

        self._type = type

    @property
    def percentage_alcohol(self):
        """Gets the percentage_alcohol of this ControlledDesignationOfOriginWine.  # noqa: E501

        percentage of alcohol present in a beverage  # noqa: E501

        :return: The percentage_alcohol of this ControlledDesignationOfOriginWine.  # noqa: E501
        :rtype: list[int]
        """
        return self._percentage_alcohol

    @percentage_alcohol.setter
    def percentage_alcohol(self, percentage_alcohol):
        """Sets the percentage_alcohol of this ControlledDesignationOfOriginWine.

        percentage of alcohol present in a beverage  # noqa: E501

        :param percentage_alcohol: The percentage_alcohol of this ControlledDesignationOfOriginWine.  # noqa: E501
        :type: list[int]
        """

        self._percentage_alcohol = percentage_alcohol

    @property
    def creator_of_dish(self):
        """Gets the creator_of_dish of this ControlledDesignationOfOriginWine.  # noqa: E501

        The person that creates (invents) the food (eg. Caesar Cardini is the creator of the Caesar salad).  # noqa: E501

        :return: The creator_of_dish of this ControlledDesignationOfOriginWine.  # noqa: E501
        :rtype: list[object]
        """
        return self._creator_of_dish

    @creator_of_dish.setter
    def creator_of_dish(self, creator_of_dish):
        """Sets the creator_of_dish of this ControlledDesignationOfOriginWine.

        The person that creates (invents) the food (eg. Caesar Cardini is the creator of the Caesar salad).  # noqa: E501

        :param creator_of_dish: The creator_of_dish of this ControlledDesignationOfOriginWine.  # noqa: E501
        :type: list[object]
        """

        self._creator_of_dish = creator_of_dish

    @property
    def serving_temperature(self):
        """Gets the serving_temperature of this ControlledDesignationOfOriginWine.  # noqa: E501

        Serving temperature for the food (e.g.: hot, cold, warm or room temperature).  # noqa: E501

        :return: The serving_temperature of this ControlledDesignationOfOriginWine.  # noqa: E501
        :rtype: list[str]
        """
        return self._serving_temperature

    @serving_temperature.setter
    def serving_temperature(self, serving_temperature):
        """Sets the serving_temperature of this ControlledDesignationOfOriginWine.

        Serving temperature for the food (e.g.: hot, cold, warm or room temperature).  # noqa: E501

        :param serving_temperature: The serving_temperature of this ControlledDesignationOfOriginWine.  # noqa: E501
        :type: list[str]
        """

        self._serving_temperature = serving_temperature

    @property
    def introduced(self):
        """Gets the introduced of this ControlledDesignationOfOriginWine.  # noqa: E501

        Description not available  # noqa: E501

        :return: The introduced of this ControlledDesignationOfOriginWine.  # noqa: E501
        :rtype: list[str]
        """
        return self._introduced

    @introduced.setter
    def introduced(self, introduced):
        """Sets the introduced of this ControlledDesignationOfOriginWine.

        Description not available  # noqa: E501

        :param introduced: The introduced of this ControlledDesignationOfOriginWine.  # noqa: E501
        :type: list[str]
        """

        self._introduced = introduced

    @property
    def type_of_storage(self):
        """Gets the type_of_storage of this ControlledDesignationOfOriginWine.  # noqa: E501

        Description not available  # noqa: E501

        :return: The type_of_storage of this ControlledDesignationOfOriginWine.  # noqa: E501
        :rtype: list[str]
        """
        return self._type_of_storage

    @type_of_storage.setter
    def type_of_storage(self, type_of_storage):
        """Sets the type_of_storage of this ControlledDesignationOfOriginWine.

        Description not available  # noqa: E501

        :param type_of_storage: The type_of_storage of this ControlledDesignationOfOriginWine.  # noqa: E501
        :type: list[str]
        """

        self._type_of_storage = type_of_storage

    @property
    def id(self):
        """Gets the id of this ControlledDesignationOfOriginWine.  # noqa: E501

        identifier  # noqa: E501

        :return: The id of this ControlledDesignationOfOriginWine.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ControlledDesignationOfOriginWine.

        identifier  # noqa: E501

        :param id: The id of this ControlledDesignationOfOriginWine.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def type_of_grain(self):
        """Gets the type_of_grain of this ControlledDesignationOfOriginWine.  # noqa: E501

        Description not available  # noqa: E501

        :return: The type_of_grain of this ControlledDesignationOfOriginWine.  # noqa: E501
        :rtype: list[str]
        """
        return self._type_of_grain

    @type_of_grain.setter
    def type_of_grain(self, type_of_grain):
        """Sets the type_of_grain of this ControlledDesignationOfOriginWine.

        Description not available  # noqa: E501

        :param type_of_grain: The type_of_grain of this ControlledDesignationOfOriginWine.  # noqa: E501
        :type: list[str]
        """

        self._type_of_grain = type_of_grain

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ControlledDesignationOfOriginWine):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ControlledDesignationOfOriginWine):
            return True

        return self.to_dict() != other.to_dict()
