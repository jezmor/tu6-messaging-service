# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base.version import Version
from twilio.rest.conversations.v1.address_configuration import AddressConfigurationList
from twilio.rest.conversations.v1.configuration import ConfigurationList
from twilio.rest.conversations.v1.conversation import ConversationList
from twilio.rest.conversations.v1.credential import CredentialList
from twilio.rest.conversations.v1.participant_conversation import ParticipantConversationList
from twilio.rest.conversations.v1.role import RoleList
from twilio.rest.conversations.v1.service import ServiceList
from twilio.rest.conversations.v1.user import UserList


class V1(Version):

    def __init__(self, domain):
        """
        Initialize the V1 version of Conversations

        :returns: V1 version of Conversations
        :rtype: twilio.rest.conversations.v1.V1.V1
        """
        super(V1, self).__init__(domain)
        self.version = 'v1'
        self._configuration = None
        self._address_configurations = None
        self._conversations = None
        self._credentials = None
        self._participant_conversations = None
        self._roles = None
        self._services = None
        self._users = None

    @property
    def configuration(self):
        """
        :rtype: twilio.rest.conversations.v1.configuration.ConfigurationList
        """
        if self._configuration is None:
            self._configuration = ConfigurationList(self)
        return self._configuration

    @property
    def address_configurations(self):
        """
        :rtype: twilio.rest.conversations.v1.address_configuration.AddressConfigurationList
        """
        if self._address_configurations is None:
            self._address_configurations = AddressConfigurationList(self)
        return self._address_configurations

    @property
    def conversations(self):
        """
        :rtype: twilio.rest.conversations.v1.conversation.ConversationList
        """
        if self._conversations is None:
            self._conversations = ConversationList(self)
        return self._conversations

    @property
    def credentials(self):
        """
        :rtype: twilio.rest.conversations.v1.credential.CredentialList
        """
        if self._credentials is None:
            self._credentials = CredentialList(self)
        return self._credentials

    @property
    def participant_conversations(self):
        """
        :rtype: twilio.rest.conversations.v1.participant_conversation.ParticipantConversationList
        """
        if self._participant_conversations is None:
            self._participant_conversations = ParticipantConversationList(self)
        return self._participant_conversations

    @property
    def roles(self):
        """
        :rtype: twilio.rest.conversations.v1.role.RoleList
        """
        if self._roles is None:
            self._roles = RoleList(self)
        return self._roles

    @property
    def services(self):
        """
        :rtype: twilio.rest.conversations.v1.service.ServiceList
        """
        if self._services is None:
            self._services = ServiceList(self)
        return self._services

    @property
    def users(self):
        """
        :rtype: twilio.rest.conversations.v1.user.UserList
        """
        if self._users is None:
            self._users = UserList(self)
        return self._users

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Conversations.V1>'
