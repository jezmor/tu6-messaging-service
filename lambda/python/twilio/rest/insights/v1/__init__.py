# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base.version import Version
from twilio.rest.insights.v1.call import CallList
from twilio.rest.insights.v1.call_summaries import CallSummariesList
from twilio.rest.insights.v1.conference import ConferenceList
from twilio.rest.insights.v1.room import RoomList
from twilio.rest.insights.v1.setting import SettingList


class V1(Version):

    def __init__(self, domain):
        """
        Initialize the V1 version of Insights

        :returns: V1 version of Insights
        :rtype: twilio.rest.insights.v1.V1.V1
        """
        super(V1, self).__init__(domain)
        self.version = 'v1'
        self._settings = None
        self._calls = None
        self._call_summaries = None
        self._conferences = None
        self._rooms = None

    @property
    def settings(self):
        """
        :rtype: twilio.rest.insights.v1.setting.SettingList
        """
        if self._settings is None:
            self._settings = SettingList(self)
        return self._settings

    @property
    def calls(self):
        """
        :rtype: twilio.rest.insights.v1.call.CallList
        """
        if self._calls is None:
            self._calls = CallList(self)
        return self._calls

    @property
    def call_summaries(self):
        """
        :rtype: twilio.rest.insights.v1.call_summaries.CallSummariesList
        """
        if self._call_summaries is None:
            self._call_summaries = CallSummariesList(self)
        return self._call_summaries

    @property
    def conferences(self):
        """
        :rtype: twilio.rest.insights.v1.conference.ConferenceList
        """
        if self._conferences is None:
            self._conferences = ConferenceList(self)
        return self._conferences

    @property
    def rooms(self):
        """
        :rtype: twilio.rest.insights.v1.room.RoomList
        """
        if self._rooms is None:
            self._rooms = RoomList(self)
        return self._rooms

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Insights.V1>'