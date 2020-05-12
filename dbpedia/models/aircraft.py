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


class Aircraft(object):
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
        'number_of_bombs': 'list[int]',
        'gun': 'list[str]',
        'production_years': 'list[str]',
        'program_cost': 'list[float]',
        'mass': 'list[object]',
        'description': 'list[str]',
        'engine_type': 'list[object]',
        'type': 'list[str]',
        'introduction_date': 'list[str]',
        'aircraft_type': 'list[str]',
        'diameter': 'list[object]',
        'design_company': 'list[object]',
        'number_built': 'list[int]',
        'discharge': 'list[float]',
        'assembly': 'list[object]',
        'id': 'str',
        'rebuilder': 'list[object]',
        '_class': 'list[object]',
        'model_start_date': 'list[str]',
        'height': 'list[object]',
        'model_end_date': 'list[str]',
        'number_of_launches': 'list[int]',
        'wing_area': 'list[float]',
        'wingspan': 'list[float]',
        'model_end_year': 'list[str]',
        'aircraft_user': 'list[object]',
        'length': 'list[object]',
        'weight': 'list[object]',
        'label': 'list[str]',
        'version': 'list[object]',
        'number_of_seats': 'list[int]',
        'mission': 'list[object]',
        'model_start_year': 'list[str]',
        'unit_cost': 'list[float]',
        'width': 'list[object]',
        'discharge_average': 'list[float]',
        'number_of_crew': 'list[int]',
        'number_of_rockets': 'list[int]',
        'related_mean_of_transportation': 'list[object]',
        'power_type': 'list[object]'
    }

    attribute_map = {
        'number_of_bombs': 'numberOfBombs',
        'gun': 'gun',
        'production_years': 'productionYears',
        'program_cost': 'programCost',
        'mass': 'mass',
        'description': 'description',
        'engine_type': 'engineType',
        'type': 'type',
        'introduction_date': 'introductionDate',
        'aircraft_type': 'aircraftType',
        'diameter': 'diameter',
        'design_company': 'designCompany',
        'number_built': 'numberBuilt',
        'discharge': 'discharge',
        'assembly': 'assembly',
        'id': 'id',
        'rebuilder': 'rebuilder',
        '_class': 'class',
        'model_start_date': 'modelStartDate',
        'height': 'height',
        'model_end_date': 'modelEndDate',
        'number_of_launches': 'numberOfLaunches',
        'wing_area': 'wingArea',
        'wingspan': 'wingspan',
        'model_end_year': 'modelEndYear',
        'aircraft_user': 'aircraftUser',
        'length': 'length',
        'weight': 'weight',
        'label': 'label',
        'version': 'version',
        'number_of_seats': 'numberOfSeats',
        'mission': 'mission',
        'model_start_year': 'modelStartYear',
        'unit_cost': 'unitCost',
        'width': 'width',
        'discharge_average': 'dischargeAverage',
        'number_of_crew': 'numberOfCrew',
        'number_of_rockets': 'numberOfRockets',
        'related_mean_of_transportation': 'relatedMeanOfTransportation',
        'power_type': 'powerType'
    }

    def __init__(self, number_of_bombs=None, gun=None, production_years=None, program_cost=None, mass=None, description=None, engine_type=None, type=None, introduction_date=None, aircraft_type=None, diameter=None, design_company=None, number_built=None, discharge=None, assembly=None, id=None, rebuilder=None, _class=None, model_start_date=None, height=None, model_end_date=None, number_of_launches=None, wing_area=None, wingspan=None, model_end_year=None, aircraft_user=None, length=None, weight=None, label=None, version=None, number_of_seats=None, mission=None, model_start_year=None, unit_cost=None, width=None, discharge_average=None, number_of_crew=None, number_of_rockets=None, related_mean_of_transportation=None, power_type=None, local_vars_configuration=None):  # noqa: E501
        """Aircraft - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._number_of_bombs = None
        self._gun = None
        self._production_years = None
        self._program_cost = None
        self._mass = None
        self._description = None
        self._engine_type = None
        self._type = None
        self._introduction_date = None
        self._aircraft_type = None
        self._diameter = None
        self._design_company = None
        self._number_built = None
        self._discharge = None
        self._assembly = None
        self._id = None
        self._rebuilder = None
        self.__class = None
        self._model_start_date = None
        self._height = None
        self._model_end_date = None
        self._number_of_launches = None
        self._wing_area = None
        self._wingspan = None
        self._model_end_year = None
        self._aircraft_user = None
        self._length = None
        self._weight = None
        self._label = None
        self._version = None
        self._number_of_seats = None
        self._mission = None
        self._model_start_year = None
        self._unit_cost = None
        self._width = None
        self._discharge_average = None
        self._number_of_crew = None
        self._number_of_rockets = None
        self._related_mean_of_transportation = None
        self._power_type = None
        self.discriminator = None

        self.number_of_bombs = number_of_bombs
        self.gun = gun
        self.production_years = production_years
        self.program_cost = program_cost
        self.mass = mass
        self.description = description
        self.engine_type = engine_type
        self.type = type
        self.introduction_date = introduction_date
        self.aircraft_type = aircraft_type
        self.diameter = diameter
        self.design_company = design_company
        self.number_built = number_built
        self.discharge = discharge
        self.assembly = assembly
        if id is not None:
            self.id = id
        self.rebuilder = rebuilder
        self._class = _class
        self.model_start_date = model_start_date
        self.height = height
        self.model_end_date = model_end_date
        self.number_of_launches = number_of_launches
        self.wing_area = wing_area
        self.wingspan = wingspan
        self.model_end_year = model_end_year
        self.aircraft_user = aircraft_user
        self.length = length
        self.weight = weight
        self.label = label
        self.version = version
        self.number_of_seats = number_of_seats
        self.mission = mission
        self.model_start_year = model_start_year
        self.unit_cost = unit_cost
        self.width = width
        self.discharge_average = discharge_average
        self.number_of_crew = number_of_crew
        self.number_of_rockets = number_of_rockets
        self.related_mean_of_transportation = related_mean_of_transportation
        self.power_type = power_type

    @property
    def number_of_bombs(self):
        """Gets the number_of_bombs of this Aircraft.  # noqa: E501

        Description not available  # noqa: E501

        :return: The number_of_bombs of this Aircraft.  # noqa: E501
        :rtype: list[int]
        """
        return self._number_of_bombs

    @number_of_bombs.setter
    def number_of_bombs(self, number_of_bombs):
        """Sets the number_of_bombs of this Aircraft.

        Description not available  # noqa: E501

        :param number_of_bombs: The number_of_bombs of this Aircraft.  # noqa: E501
        :type: list[int]
        """

        self._number_of_bombs = number_of_bombs

    @property
    def gun(self):
        """Gets the gun of this Aircraft.  # noqa: E501

        Description not available  # noqa: E501

        :return: The gun of this Aircraft.  # noqa: E501
        :rtype: list[str]
        """
        return self._gun

    @gun.setter
    def gun(self, gun):
        """Sets the gun of this Aircraft.

        Description not available  # noqa: E501

        :param gun: The gun of this Aircraft.  # noqa: E501
        :type: list[str]
        """

        self._gun = gun

    @property
    def production_years(self):
        """Gets the production_years of this Aircraft.  # noqa: E501

        Description not available  # noqa: E501

        :return: The production_years of this Aircraft.  # noqa: E501
        :rtype: list[str]
        """
        return self._production_years

    @production_years.setter
    def production_years(self, production_years):
        """Sets the production_years of this Aircraft.

        Description not available  # noqa: E501

        :param production_years: The production_years of this Aircraft.  # noqa: E501
        :type: list[str]
        """

        self._production_years = production_years

    @property
    def program_cost(self):
        """Gets the program_cost of this Aircraft.  # noqa: E501

        Description not available  # noqa: E501

        :return: The program_cost of this Aircraft.  # noqa: E501
        :rtype: list[float]
        """
        return self._program_cost

    @program_cost.setter
    def program_cost(self, program_cost):
        """Sets the program_cost of this Aircraft.

        Description not available  # noqa: E501

        :param program_cost: The program_cost of this Aircraft.  # noqa: E501
        :type: list[float]
        """

        self._program_cost = program_cost

    @property
    def mass(self):
        """Gets the mass of this Aircraft.  # noqa: E501

        Description not available  # noqa: E501

        :return: The mass of this Aircraft.  # noqa: E501
        :rtype: list[object]
        """
        return self._mass

    @mass.setter
    def mass(self, mass):
        """Sets the mass of this Aircraft.

        Description not available  # noqa: E501

        :param mass: The mass of this Aircraft.  # noqa: E501
        :type: list[object]
        """

        self._mass = mass

    @property
    def description(self):
        """Gets the description of this Aircraft.  # noqa: E501

        small description  # noqa: E501

        :return: The description of this Aircraft.  # noqa: E501
        :rtype: list[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Aircraft.

        small description  # noqa: E501

        :param description: The description of this Aircraft.  # noqa: E501
        :type: list[str]
        """

        self._description = description

    @property
    def engine_type(self):
        """Gets the engine_type of this Aircraft.  # noqa: E501

        Description not available  # noqa: E501

        :return: The engine_type of this Aircraft.  # noqa: E501
        :rtype: list[object]
        """
        return self._engine_type

    @engine_type.setter
    def engine_type(self, engine_type):
        """Sets the engine_type of this Aircraft.

        Description not available  # noqa: E501

        :param engine_type: The engine_type of this Aircraft.  # noqa: E501
        :type: list[object]
        """

        self._engine_type = engine_type

    @property
    def type(self):
        """Gets the type of this Aircraft.  # noqa: E501

        type of the resource  # noqa: E501

        :return: The type of this Aircraft.  # noqa: E501
        :rtype: list[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Aircraft.

        type of the resource  # noqa: E501

        :param type: The type of this Aircraft.  # noqa: E501
        :type: list[str]
        """

        self._type = type

    @property
    def introduction_date(self):
        """Gets the introduction_date of this Aircraft.  # noqa: E501

        Description not available  # noqa: E501

        :return: The introduction_date of this Aircraft.  # noqa: E501
        :rtype: list[str]
        """
        return self._introduction_date

    @introduction_date.setter
    def introduction_date(self, introduction_date):
        """Sets the introduction_date of this Aircraft.

        Description not available  # noqa: E501

        :param introduction_date: The introduction_date of this Aircraft.  # noqa: E501
        :type: list[str]
        """

        self._introduction_date = introduction_date

    @property
    def aircraft_type(self):
        """Gets the aircraft_type of this Aircraft.  # noqa: E501

        Description not available  # noqa: E501

        :return: The aircraft_type of this Aircraft.  # noqa: E501
        :rtype: list[str]
        """
        return self._aircraft_type

    @aircraft_type.setter
    def aircraft_type(self, aircraft_type):
        """Sets the aircraft_type of this Aircraft.

        Description not available  # noqa: E501

        :param aircraft_type: The aircraft_type of this Aircraft.  # noqa: E501
        :type: list[str]
        """

        self._aircraft_type = aircraft_type

    @property
    def diameter(self):
        """Gets the diameter of this Aircraft.  # noqa: E501

        Description not available  # noqa: E501

        :return: The diameter of this Aircraft.  # noqa: E501
        :rtype: list[object]
        """
        return self._diameter

    @diameter.setter
    def diameter(self, diameter):
        """Sets the diameter of this Aircraft.

        Description not available  # noqa: E501

        :param diameter: The diameter of this Aircraft.  # noqa: E501
        :type: list[object]
        """

        self._diameter = diameter

    @property
    def design_company(self):
        """Gets the design_company of this Aircraft.  # noqa: E501

        Description not available  # noqa: E501

        :return: The design_company of this Aircraft.  # noqa: E501
        :rtype: list[object]
        """
        return self._design_company

    @design_company.setter
    def design_company(self, design_company):
        """Sets the design_company of this Aircraft.

        Description not available  # noqa: E501

        :param design_company: The design_company of this Aircraft.  # noqa: E501
        :type: list[object]
        """

        self._design_company = design_company

    @property
    def number_built(self):
        """Gets the number_built of this Aircraft.  # noqa: E501

        Description not available  # noqa: E501

        :return: The number_built of this Aircraft.  # noqa: E501
        :rtype: list[int]
        """
        return self._number_built

    @number_built.setter
    def number_built(self, number_built):
        """Sets the number_built of this Aircraft.

        Description not available  # noqa: E501

        :param number_built: The number_built of this Aircraft.  # noqa: E501
        :type: list[int]
        """

        self._number_built = number_built

    @property
    def discharge(self):
        """Gets the discharge of this Aircraft.  # noqa: E501

        Description not available  # noqa: E501

        :return: The discharge of this Aircraft.  # noqa: E501
        :rtype: list[float]
        """
        return self._discharge

    @discharge.setter
    def discharge(self, discharge):
        """Sets the discharge of this Aircraft.

        Description not available  # noqa: E501

        :param discharge: The discharge of this Aircraft.  # noqa: E501
        :type: list[float]
        """

        self._discharge = discharge

    @property
    def assembly(self):
        """Gets the assembly of this Aircraft.  # noqa: E501

        Description not available  # noqa: E501

        :return: The assembly of this Aircraft.  # noqa: E501
        :rtype: list[object]
        """
        return self._assembly

    @assembly.setter
    def assembly(self, assembly):
        """Sets the assembly of this Aircraft.

        Description not available  # noqa: E501

        :param assembly: The assembly of this Aircraft.  # noqa: E501
        :type: list[object]
        """

        self._assembly = assembly

    @property
    def id(self):
        """Gets the id of this Aircraft.  # noqa: E501

        identifier  # noqa: E501

        :return: The id of this Aircraft.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Aircraft.

        identifier  # noqa: E501

        :param id: The id of this Aircraft.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def rebuilder(self):
        """Gets the rebuilder of this Aircraft.  # noqa: E501

        Description not available  # noqa: E501

        :return: The rebuilder of this Aircraft.  # noqa: E501
        :rtype: list[object]
        """
        return self._rebuilder

    @rebuilder.setter
    def rebuilder(self, rebuilder):
        """Sets the rebuilder of this Aircraft.

        Description not available  # noqa: E501

        :param rebuilder: The rebuilder of this Aircraft.  # noqa: E501
        :type: list[object]
        """

        self._rebuilder = rebuilder

    @property
    def _class(self):
        """Gets the _class of this Aircraft.  # noqa: E501

        Description not available  # noqa: E501

        :return: The _class of this Aircraft.  # noqa: E501
        :rtype: list[object]
        """
        return self.__class

    @_class.setter
    def _class(self, _class):
        """Sets the _class of this Aircraft.

        Description not available  # noqa: E501

        :param _class: The _class of this Aircraft.  # noqa: E501
        :type: list[object]
        """

        self.__class = _class

    @property
    def model_start_date(self):
        """Gets the model_start_date of this Aircraft.  # noqa: E501

        Description not available  # noqa: E501

        :return: The model_start_date of this Aircraft.  # noqa: E501
        :rtype: list[str]
        """
        return self._model_start_date

    @model_start_date.setter
    def model_start_date(self, model_start_date):
        """Sets the model_start_date of this Aircraft.

        Description not available  # noqa: E501

        :param model_start_date: The model_start_date of this Aircraft.  # noqa: E501
        :type: list[str]
        """

        self._model_start_date = model_start_date

    @property
    def height(self):
        """Gets the height of this Aircraft.  # noqa: E501

        Description not available  # noqa: E501

        :return: The height of this Aircraft.  # noqa: E501
        :rtype: list[object]
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this Aircraft.

        Description not available  # noqa: E501

        :param height: The height of this Aircraft.  # noqa: E501
        :type: list[object]
        """

        self._height = height

    @property
    def model_end_date(self):
        """Gets the model_end_date of this Aircraft.  # noqa: E501

        Description not available  # noqa: E501

        :return: The model_end_date of this Aircraft.  # noqa: E501
        :rtype: list[str]
        """
        return self._model_end_date

    @model_end_date.setter
    def model_end_date(self, model_end_date):
        """Sets the model_end_date of this Aircraft.

        Description not available  # noqa: E501

        :param model_end_date: The model_end_date of this Aircraft.  # noqa: E501
        :type: list[str]
        """

        self._model_end_date = model_end_date

    @property
    def number_of_launches(self):
        """Gets the number_of_launches of this Aircraft.  # noqa: E501

        Description not available  # noqa: E501

        :return: The number_of_launches of this Aircraft.  # noqa: E501
        :rtype: list[int]
        """
        return self._number_of_launches

    @number_of_launches.setter
    def number_of_launches(self, number_of_launches):
        """Sets the number_of_launches of this Aircraft.

        Description not available  # noqa: E501

        :param number_of_launches: The number_of_launches of this Aircraft.  # noqa: E501
        :type: list[int]
        """

        self._number_of_launches = number_of_launches

    @property
    def wing_area(self):
        """Gets the wing_area of this Aircraft.  # noqa: E501

        Description not available  # noqa: E501

        :return: The wing_area of this Aircraft.  # noqa: E501
        :rtype: list[float]
        """
        return self._wing_area

    @wing_area.setter
    def wing_area(self, wing_area):
        """Sets the wing_area of this Aircraft.

        Description not available  # noqa: E501

        :param wing_area: The wing_area of this Aircraft.  # noqa: E501
        :type: list[float]
        """

        self._wing_area = wing_area

    @property
    def wingspan(self):
        """Gets the wingspan of this Aircraft.  # noqa: E501

        Description not available  # noqa: E501

        :return: The wingspan of this Aircraft.  # noqa: E501
        :rtype: list[float]
        """
        return self._wingspan

    @wingspan.setter
    def wingspan(self, wingspan):
        """Sets the wingspan of this Aircraft.

        Description not available  # noqa: E501

        :param wingspan: The wingspan of this Aircraft.  # noqa: E501
        :type: list[float]
        """

        self._wingspan = wingspan

    @property
    def model_end_year(self):
        """Gets the model_end_year of this Aircraft.  # noqa: E501

        Description not available  # noqa: E501

        :return: The model_end_year of this Aircraft.  # noqa: E501
        :rtype: list[str]
        """
        return self._model_end_year

    @model_end_year.setter
    def model_end_year(self, model_end_year):
        """Sets the model_end_year of this Aircraft.

        Description not available  # noqa: E501

        :param model_end_year: The model_end_year of this Aircraft.  # noqa: E501
        :type: list[str]
        """

        self._model_end_year = model_end_year

    @property
    def aircraft_user(self):
        """Gets the aircraft_user of this Aircraft.  # noqa: E501

        Description not available  # noqa: E501

        :return: The aircraft_user of this Aircraft.  # noqa: E501
        :rtype: list[object]
        """
        return self._aircraft_user

    @aircraft_user.setter
    def aircraft_user(self, aircraft_user):
        """Sets the aircraft_user of this Aircraft.

        Description not available  # noqa: E501

        :param aircraft_user: The aircraft_user of this Aircraft.  # noqa: E501
        :type: list[object]
        """

        self._aircraft_user = aircraft_user

    @property
    def length(self):
        """Gets the length of this Aircraft.  # noqa: E501

        Description not available  # noqa: E501

        :return: The length of this Aircraft.  # noqa: E501
        :rtype: list[object]
        """
        return self._length

    @length.setter
    def length(self, length):
        """Sets the length of this Aircraft.

        Description not available  # noqa: E501

        :param length: The length of this Aircraft.  # noqa: E501
        :type: list[object]
        """

        self._length = length

    @property
    def weight(self):
        """Gets the weight of this Aircraft.  # noqa: E501

        Description not available  # noqa: E501

        :return: The weight of this Aircraft.  # noqa: E501
        :rtype: list[object]
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this Aircraft.

        Description not available  # noqa: E501

        :param weight: The weight of this Aircraft.  # noqa: E501
        :type: list[object]
        """

        self._weight = weight

    @property
    def label(self):
        """Gets the label of this Aircraft.  # noqa: E501

        short description of the resource  # noqa: E501

        :return: The label of this Aircraft.  # noqa: E501
        :rtype: list[str]
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this Aircraft.

        short description of the resource  # noqa: E501

        :param label: The label of this Aircraft.  # noqa: E501
        :type: list[str]
        """

        self._label = label

    @property
    def version(self):
        """Gets the version of this Aircraft.  # noqa: E501

        Description not available  # noqa: E501

        :return: The version of this Aircraft.  # noqa: E501
        :rtype: list[object]
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Aircraft.

        Description not available  # noqa: E501

        :param version: The version of this Aircraft.  # noqa: E501
        :type: list[object]
        """

        self._version = version

    @property
    def number_of_seats(self):
        """Gets the number_of_seats of this Aircraft.  # noqa: E501

        Description not available  # noqa: E501

        :return: The number_of_seats of this Aircraft.  # noqa: E501
        :rtype: list[int]
        """
        return self._number_of_seats

    @number_of_seats.setter
    def number_of_seats(self, number_of_seats):
        """Sets the number_of_seats of this Aircraft.

        Description not available  # noqa: E501

        :param number_of_seats: The number_of_seats of this Aircraft.  # noqa: E501
        :type: list[int]
        """

        self._number_of_seats = number_of_seats

    @property
    def mission(self):
        """Gets the mission of this Aircraft.  # noqa: E501

        Description not available  # noqa: E501

        :return: The mission of this Aircraft.  # noqa: E501
        :rtype: list[object]
        """
        return self._mission

    @mission.setter
    def mission(self, mission):
        """Sets the mission of this Aircraft.

        Description not available  # noqa: E501

        :param mission: The mission of this Aircraft.  # noqa: E501
        :type: list[object]
        """

        self._mission = mission

    @property
    def model_start_year(self):
        """Gets the model_start_year of this Aircraft.  # noqa: E501

        Description not available  # noqa: E501

        :return: The model_start_year of this Aircraft.  # noqa: E501
        :rtype: list[str]
        """
        return self._model_start_year

    @model_start_year.setter
    def model_start_year(self, model_start_year):
        """Sets the model_start_year of this Aircraft.

        Description not available  # noqa: E501

        :param model_start_year: The model_start_year of this Aircraft.  # noqa: E501
        :type: list[str]
        """

        self._model_start_year = model_start_year

    @property
    def unit_cost(self):
        """Gets the unit_cost of this Aircraft.  # noqa: E501

        Description not available  # noqa: E501

        :return: The unit_cost of this Aircraft.  # noqa: E501
        :rtype: list[float]
        """
        return self._unit_cost

    @unit_cost.setter
    def unit_cost(self, unit_cost):
        """Sets the unit_cost of this Aircraft.

        Description not available  # noqa: E501

        :param unit_cost: The unit_cost of this Aircraft.  # noqa: E501
        :type: list[float]
        """

        self._unit_cost = unit_cost

    @property
    def width(self):
        """Gets the width of this Aircraft.  # noqa: E501

        Description not available  # noqa: E501

        :return: The width of this Aircraft.  # noqa: E501
        :rtype: list[object]
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this Aircraft.

        Description not available  # noqa: E501

        :param width: The width of this Aircraft.  # noqa: E501
        :type: list[object]
        """

        self._width = width

    @property
    def discharge_average(self):
        """Gets the discharge_average of this Aircraft.  # noqa: E501

        Description not available  # noqa: E501

        :return: The discharge_average of this Aircraft.  # noqa: E501
        :rtype: list[float]
        """
        return self._discharge_average

    @discharge_average.setter
    def discharge_average(self, discharge_average):
        """Sets the discharge_average of this Aircraft.

        Description not available  # noqa: E501

        :param discharge_average: The discharge_average of this Aircraft.  # noqa: E501
        :type: list[float]
        """

        self._discharge_average = discharge_average

    @property
    def number_of_crew(self):
        """Gets the number_of_crew of this Aircraft.  # noqa: E501

        Description not available  # noqa: E501

        :return: The number_of_crew of this Aircraft.  # noqa: E501
        :rtype: list[int]
        """
        return self._number_of_crew

    @number_of_crew.setter
    def number_of_crew(self, number_of_crew):
        """Sets the number_of_crew of this Aircraft.

        Description not available  # noqa: E501

        :param number_of_crew: The number_of_crew of this Aircraft.  # noqa: E501
        :type: list[int]
        """

        self._number_of_crew = number_of_crew

    @property
    def number_of_rockets(self):
        """Gets the number_of_rockets of this Aircraft.  # noqa: E501

        Description not available  # noqa: E501

        :return: The number_of_rockets of this Aircraft.  # noqa: E501
        :rtype: list[int]
        """
        return self._number_of_rockets

    @number_of_rockets.setter
    def number_of_rockets(self, number_of_rockets):
        """Sets the number_of_rockets of this Aircraft.

        Description not available  # noqa: E501

        :param number_of_rockets: The number_of_rockets of this Aircraft.  # noqa: E501
        :type: list[int]
        """

        self._number_of_rockets = number_of_rockets

    @property
    def related_mean_of_transportation(self):
        """Gets the related_mean_of_transportation of this Aircraft.  # noqa: E501

        Description not available  # noqa: E501

        :return: The related_mean_of_transportation of this Aircraft.  # noqa: E501
        :rtype: list[object]
        """
        return self._related_mean_of_transportation

    @related_mean_of_transportation.setter
    def related_mean_of_transportation(self, related_mean_of_transportation):
        """Sets the related_mean_of_transportation of this Aircraft.

        Description not available  # noqa: E501

        :param related_mean_of_transportation: The related_mean_of_transportation of this Aircraft.  # noqa: E501
        :type: list[object]
        """

        self._related_mean_of_transportation = related_mean_of_transportation

    @property
    def power_type(self):
        """Gets the power_type of this Aircraft.  # noqa: E501

        Description not available  # noqa: E501

        :return: The power_type of this Aircraft.  # noqa: E501
        :rtype: list[object]
        """
        return self._power_type

    @power_type.setter
    def power_type(self, power_type):
        """Sets the power_type of this Aircraft.

        Description not available  # noqa: E501

        :param power_type: The power_type of this Aircraft.  # noqa: E501
        :type: list[object]
        """

        self._power_type = power_type

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
        if not isinstance(other, Aircraft):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Aircraft):
            return True

        return self.to_dict() != other.to_dict()