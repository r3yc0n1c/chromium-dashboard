from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from chromestatus_openapi.models.base_model import Model
from chromestatus_openapi import util


class SurveyAnswers(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, is_language_polyfill=None, is_api_polyfill=None, is_same_origin_css=None, launch_or_contact=None, explanation=None):  # noqa: E501
        """SurveyAnswers - a model defined in OpenAPI

        :param is_language_polyfill: The is_language_polyfill of this SurveyAnswers.  # noqa: E501
        :type is_language_polyfill: bool
        :param is_api_polyfill: The is_api_polyfill of this SurveyAnswers.  # noqa: E501
        :type is_api_polyfill: bool
        :param is_same_origin_css: The is_same_origin_css of this SurveyAnswers.  # noqa: E501
        :type is_same_origin_css: bool
        :param launch_or_contact: The launch_or_contact of this SurveyAnswers.  # noqa: E501
        :type launch_or_contact: str
        :param explanation: The explanation of this SurveyAnswers.  # noqa: E501
        :type explanation: str
        """
        self.openapi_types = {
            'is_language_polyfill': bool,
            'is_api_polyfill': bool,
            'is_same_origin_css': bool,
            'launch_or_contact': str,
            'explanation': str
        }

        self.attribute_map = {
            'is_language_polyfill': 'is_language_polyfill',
            'is_api_polyfill': 'is_api_polyfill',
            'is_same_origin_css': 'is_same_origin_css',
            'launch_or_contact': 'launch_or_contact',
            'explanation': 'explanation'
        }

        self._is_language_polyfill = is_language_polyfill
        self._is_api_polyfill = is_api_polyfill
        self._is_same_origin_css = is_same_origin_css
        self._launch_or_contact = launch_or_contact
        self._explanation = explanation

    @classmethod
    def from_dict(cls, dikt) -> 'SurveyAnswers':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SurveyAnswers of this SurveyAnswers.  # noqa: E501
        :rtype: SurveyAnswers
        """
        return util.deserialize_model(dikt, cls)

    @property
    def is_language_polyfill(self) -> bool:
        """Gets the is_language_polyfill of this SurveyAnswers.


        :return: The is_language_polyfill of this SurveyAnswers.
        :rtype: bool
        """
        return self._is_language_polyfill

    @is_language_polyfill.setter
    def is_language_polyfill(self, is_language_polyfill: bool):
        """Sets the is_language_polyfill of this SurveyAnswers.


        :param is_language_polyfill: The is_language_polyfill of this SurveyAnswers.
        :type is_language_polyfill: bool
        """

        self._is_language_polyfill = is_language_polyfill

    @property
    def is_api_polyfill(self) -> bool:
        """Gets the is_api_polyfill of this SurveyAnswers.


        :return: The is_api_polyfill of this SurveyAnswers.
        :rtype: bool
        """
        return self._is_api_polyfill

    @is_api_polyfill.setter
    def is_api_polyfill(self, is_api_polyfill: bool):
        """Sets the is_api_polyfill of this SurveyAnswers.


        :param is_api_polyfill: The is_api_polyfill of this SurveyAnswers.
        :type is_api_polyfill: bool
        """

        self._is_api_polyfill = is_api_polyfill

    @property
    def is_same_origin_css(self) -> bool:
        """Gets the is_same_origin_css of this SurveyAnswers.


        :return: The is_same_origin_css of this SurveyAnswers.
        :rtype: bool
        """
        return self._is_same_origin_css

    @is_same_origin_css.setter
    def is_same_origin_css(self, is_same_origin_css: bool):
        """Sets the is_same_origin_css of this SurveyAnswers.


        :param is_same_origin_css: The is_same_origin_css of this SurveyAnswers.
        :type is_same_origin_css: bool
        """

        self._is_same_origin_css = is_same_origin_css

    @property
    def launch_or_contact(self) -> str:
        """Gets the launch_or_contact of this SurveyAnswers.


        :return: The launch_or_contact of this SurveyAnswers.
        :rtype: str
        """
        return self._launch_or_contact

    @launch_or_contact.setter
    def launch_or_contact(self, launch_or_contact: str):
        """Sets the launch_or_contact of this SurveyAnswers.


        :param launch_or_contact: The launch_or_contact of this SurveyAnswers.
        :type launch_or_contact: str
        """

        self._launch_or_contact = launch_or_contact

    @property
    def explanation(self) -> str:
        """Gets the explanation of this SurveyAnswers.


        :return: The explanation of this SurveyAnswers.
        :rtype: str
        """
        return self._explanation

    @explanation.setter
    def explanation(self, explanation: str):
        """Sets the explanation of this SurveyAnswers.


        :param explanation: The explanation of this SurveyAnswers.
        :type explanation: str
        """

        self._explanation = explanation
