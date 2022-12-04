# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import deserialize
from twilio.base import serialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page
from twilio.rest.studio.v2.flow.execution import ExecutionList
from twilio.rest.studio.v2.flow.flow_revision import FlowRevisionList
from twilio.rest.studio.v2.flow.test_user import FlowTestUserList


class FlowList(ListResource):

    def __init__(self, version):
        """
        Initialize the FlowList

        :param Version version: Version that contains the resource

        :returns: twilio.rest.studio.v2.flow.FlowList
        :rtype: twilio.rest.studio.v2.flow.FlowList
        """
        super(FlowList, self).__init__(version)

        # Path Solution
        self._solution = {}
        self._uri = '/Flows'.format(**self._solution)

    def create(self, friendly_name, status, definition,
               commit_message=values.unset):
        """
        Create the FlowInstance

        :param unicode friendly_name: The string that you assigned to describe the Flow
        :param FlowInstance.Status status: The status of the Flow
        :param dict definition: JSON representation of flow definition
        :param unicode commit_message: Description of change made in the revision

        :returns: The created FlowInstance
        :rtype: twilio.rest.studio.v2.flow.FlowInstance
        """
        data = values.of({
            'FriendlyName': friendly_name,
            'Status': status,
            'Definition': serialize.object(definition),
            'CommitMessage': commit_message,
        })

        payload = self._version.create(method='POST', uri=self._uri, data=data, )

        return FlowInstance(self._version, payload, )

    def stream(self, limit=None, page_size=None):
        """
        Streams FlowInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.studio.v2.flow.FlowInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(page_size=limits['page_size'], )

        return self._version.stream(page, limits['limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists FlowInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.studio.v2.flow.FlowInstance]
        """
        return list(self.stream(limit=limit, page_size=page_size, ))

    def page(self, page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of FlowInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of FlowInstance
        :rtype: twilio.rest.studio.v2.flow.FlowPage
        """
        data = values.of({'PageToken': page_token, 'Page': page_number, 'PageSize': page_size, })

        response = self._version.page(method='GET', uri=self._uri, params=data, )

        return FlowPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of FlowInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of FlowInstance
        :rtype: twilio.rest.studio.v2.flow.FlowPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return FlowPage(self._version, response, self._solution)

    def get(self, sid):
        """
        Constructs a FlowContext

        :param sid: The SID that identifies the resource to fetch

        :returns: twilio.rest.studio.v2.flow.FlowContext
        :rtype: twilio.rest.studio.v2.flow.FlowContext
        """
        return FlowContext(self._version, sid=sid, )

    def __call__(self, sid):
        """
        Constructs a FlowContext

        :param sid: The SID that identifies the resource to fetch

        :returns: twilio.rest.studio.v2.flow.FlowContext
        :rtype: twilio.rest.studio.v2.flow.FlowContext
        """
        return FlowContext(self._version, sid=sid, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Studio.V2.FlowList>'


class FlowPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the FlowPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.studio.v2.flow.FlowPage
        :rtype: twilio.rest.studio.v2.flow.FlowPage
        """
        super(FlowPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of FlowInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.studio.v2.flow.FlowInstance
        :rtype: twilio.rest.studio.v2.flow.FlowInstance
        """
        return FlowInstance(self._version, payload, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Studio.V2.FlowPage>'


class FlowContext(InstanceContext):

    def __init__(self, version, sid):
        """
        Initialize the FlowContext

        :param Version version: Version that contains the resource
        :param sid: The SID that identifies the resource to fetch

        :returns: twilio.rest.studio.v2.flow.FlowContext
        :rtype: twilio.rest.studio.v2.flow.FlowContext
        """
        super(FlowContext, self).__init__(version)

        # Path Solution
        self._solution = {'sid': sid, }
        self._uri = '/Flows/{sid}'.format(**self._solution)

        # Dependents
        self._revisions = None
        self._test_users = None
        self._executions = None

    def update(self, status, friendly_name=values.unset, definition=values.unset,
               commit_message=values.unset):
        """
        Update the FlowInstance

        :param FlowInstance.Status status: The status of the Flow
        :param unicode friendly_name: The string that you assigned to describe the Flow
        :param dict definition: JSON representation of flow definition
        :param unicode commit_message: Description of change made in the revision

        :returns: The updated FlowInstance
        :rtype: twilio.rest.studio.v2.flow.FlowInstance
        """
        data = values.of({
            'Status': status,
            'FriendlyName': friendly_name,
            'Definition': serialize.object(definition),
            'CommitMessage': commit_message,
        })

        payload = self._version.update(method='POST', uri=self._uri, data=data, )

        return FlowInstance(self._version, payload, sid=self._solution['sid'], )

    def fetch(self):
        """
        Fetch the FlowInstance

        :returns: The fetched FlowInstance
        :rtype: twilio.rest.studio.v2.flow.FlowInstance
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return FlowInstance(self._version, payload, sid=self._solution['sid'], )

    def delete(self):
        """
        Deletes the FlowInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri, )

    @property
    def revisions(self):
        """
        Access the revisions

        :returns: twilio.rest.studio.v2.flow.flow_revision.FlowRevisionList
        :rtype: twilio.rest.studio.v2.flow.flow_revision.FlowRevisionList
        """
        if self._revisions is None:
            self._revisions = FlowRevisionList(self._version, sid=self._solution['sid'], )
        return self._revisions

    @property
    def test_users(self):
        """
        Access the test_users

        :returns: twilio.rest.studio.v2.flow.test_user.FlowTestUserList
        :rtype: twilio.rest.studio.v2.flow.test_user.FlowTestUserList
        """
        if self._test_users is None:
            self._test_users = FlowTestUserList(self._version, sid=self._solution['sid'], )
        return self._test_users

    @property
    def executions(self):
        """
        Access the executions

        :returns: twilio.rest.studio.v2.flow.execution.ExecutionList
        :rtype: twilio.rest.studio.v2.flow.execution.ExecutionList
        """
        if self._executions is None:
            self._executions = ExecutionList(self._version, flow_sid=self._solution['sid'], )
        return self._executions

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Studio.V2.FlowContext {}>'.format(context)


class FlowInstance(InstanceResource):

    class Status(object):
        DRAFT = "draft"
        PUBLISHED = "published"

    def __init__(self, version, payload, sid=None):
        """
        Initialize the FlowInstance

        :returns: twilio.rest.studio.v2.flow.FlowInstance
        :rtype: twilio.rest.studio.v2.flow.FlowInstance
        """
        super(FlowInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'sid': payload.get('sid'),
            'account_sid': payload.get('account_sid'),
            'friendly_name': payload.get('friendly_name'),
            'definition': payload.get('definition'),
            'status': payload.get('status'),
            'revision': deserialize.integer(payload.get('revision')),
            'commit_message': payload.get('commit_message'),
            'valid': payload.get('valid'),
            'errors': payload.get('errors'),
            'warnings': payload.get('warnings'),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
            'webhook_url': payload.get('webhook_url'),
            'url': payload.get('url'),
            'links': payload.get('links'),
        }

        # Context
        self._context = None
        self._solution = {'sid': sid or self._properties['sid'], }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: FlowContext for this FlowInstance
        :rtype: twilio.rest.studio.v2.flow.FlowContext
        """
        if self._context is None:
            self._context = FlowContext(self._version, sid=self._solution['sid'], )
        return self._context

    @property
    def sid(self):
        """
        :returns: The unique string that identifies the resource
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def account_sid(self):
        """
        :returns: The SID of the Account that created the resource
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def friendly_name(self):
        """
        :returns: The string that you assigned to describe the Flow
        :rtype: unicode
        """
        return self._properties['friendly_name']

    @property
    def definition(self):
        """
        :returns: JSON representation of flow definition
        :rtype: dict
        """
        return self._properties['definition']

    @property
    def status(self):
        """
        :returns: The status of the Flow
        :rtype: FlowInstance.Status
        """
        return self._properties['status']

    @property
    def revision(self):
        """
        :returns: The latest revision number of the Flow's definition
        :rtype: unicode
        """
        return self._properties['revision']

    @property
    def commit_message(self):
        """
        :returns: Description of change made in the revision
        :rtype: unicode
        """
        return self._properties['commit_message']

    @property
    def valid(self):
        """
        :returns: Boolean if the flow definition is valid
        :rtype: bool
        """
        return self._properties['valid']

    @property
    def errors(self):
        """
        :returns: List of error in the flow definition
        :rtype: list[dict]
        """
        return self._properties['errors']

    @property
    def warnings(self):
        """
        :returns: List of warnings in the flow definition
        :rtype: list[dict]
        """
        return self._properties['warnings']

    @property
    def date_created(self):
        """
        :returns: The ISO 8601 date and time in GMT when the resource was created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The ISO 8601 date and time in GMT when the resource was last updated
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def webhook_url(self):
        """
        :returns: The webhook_url
        :rtype: unicode
        """
        return self._properties['webhook_url']

    @property
    def url(self):
        """
        :returns: The absolute URL of the resource
        :rtype: unicode
        """
        return self._properties['url']

    @property
    def links(self):
        """
        :returns: Nested resource URLs
        :rtype: unicode
        """
        return self._properties['links']

    def update(self, status, friendly_name=values.unset, definition=values.unset,
               commit_message=values.unset):
        """
        Update the FlowInstance

        :param FlowInstance.Status status: The status of the Flow
        :param unicode friendly_name: The string that you assigned to describe the Flow
        :param dict definition: JSON representation of flow definition
        :param unicode commit_message: Description of change made in the revision

        :returns: The updated FlowInstance
        :rtype: twilio.rest.studio.v2.flow.FlowInstance
        """
        return self._proxy.update(
            status,
            friendly_name=friendly_name,
            definition=definition,
            commit_message=commit_message,
        )

    def fetch(self):
        """
        Fetch the FlowInstance

        :returns: The fetched FlowInstance
        :rtype: twilio.rest.studio.v2.flow.FlowInstance
        """
        return self._proxy.fetch()

    def delete(self):
        """
        Deletes the FlowInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    @property
    def revisions(self):
        """
        Access the revisions

        :returns: twilio.rest.studio.v2.flow.flow_revision.FlowRevisionList
        :rtype: twilio.rest.studio.v2.flow.flow_revision.FlowRevisionList
        """
        return self._proxy.revisions

    @property
    def test_users(self):
        """
        Access the test_users

        :returns: twilio.rest.studio.v2.flow.test_user.FlowTestUserList
        :rtype: twilio.rest.studio.v2.flow.test_user.FlowTestUserList
        """
        return self._proxy.test_users

    @property
    def executions(self):
        """
        Access the executions

        :returns: twilio.rest.studio.v2.flow.execution.ExecutionList
        :rtype: twilio.rest.studio.v2.flow.execution.ExecutionList
        """
        return self._proxy.executions

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Studio.V2.FlowInstance {}>'.format(context)
