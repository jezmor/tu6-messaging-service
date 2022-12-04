# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base.version import Version
from twilio.rest.flex_api.v1.assessments import AssessmentsList
from twilio.rest.flex_api.v1.channel import ChannelList
from twilio.rest.flex_api.v1.configuration import ConfigurationList
from twilio.rest.flex_api.v1.flex_flow import FlexFlowList
from twilio.rest.flex_api.v1.good_data import GoodDataList
from twilio.rest.flex_api.v1.interaction import InteractionList
from twilio.rest.flex_api.v1.user_roles import UserRolesList
from twilio.rest.flex_api.v1.web_channel import WebChannelList


class V1(Version):

    def __init__(self, domain):
        """
        Initialize the V1 version of FlexApi

        :returns: V1 version of FlexApi
        :rtype: twilio.rest.flex_api.v1.V1.V1
        """
        super(V1, self).__init__(domain)
        self.version = 'v1'
        self._assessments = None
        self._channel = None
        self._configuration = None
        self._flex_flow = None
        self._good_data = None
        self._interaction = None
        self._user_roles = None
        self._web_channel = None

    @property
    def assessments(self):
        """
        :rtype: twilio.rest.flex_api.v1.assessments.AssessmentsList
        """
        if self._assessments is None:
            self._assessments = AssessmentsList(self)
        return self._assessments

    @property
    def channel(self):
        """
        :rtype: twilio.rest.flex_api.v1.channel.ChannelList
        """
        if self._channel is None:
            self._channel = ChannelList(self)
        return self._channel

    @property
    def configuration(self):
        """
        :rtype: twilio.rest.flex_api.v1.configuration.ConfigurationList
        """
        if self._configuration is None:
            self._configuration = ConfigurationList(self)
        return self._configuration

    @property
    def flex_flow(self):
        """
        :rtype: twilio.rest.flex_api.v1.flex_flow.FlexFlowList
        """
        if self._flex_flow is None:
            self._flex_flow = FlexFlowList(self)
        return self._flex_flow

    @property
    def good_data(self):
        """
        :rtype: twilio.rest.flex_api.v1.good_data.GoodDataList
        """
        if self._good_data is None:
            self._good_data = GoodDataList(self)
        return self._good_data

    @property
    def interaction(self):
        """
        :rtype: twilio.rest.flex_api.v1.interaction.InteractionList
        """
        if self._interaction is None:
            self._interaction = InteractionList(self)
        return self._interaction

    @property
    def user_roles(self):
        """
        :rtype: twilio.rest.flex_api.v1.user_roles.UserRolesList
        """
        if self._user_roles is None:
            self._user_roles = UserRolesList(self)
        return self._user_roles

    @property
    def web_channel(self):
        """
        :rtype: twilio.rest.flex_api.v1.web_channel.WebChannelList
        """
        if self._web_channel is None:
            self._web_channel = WebChannelList(self)
        return self._web_channel

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.FlexApi.V1>'