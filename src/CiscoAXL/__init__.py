__author__ = 'Melvin Douglas'
__version__ = '14'
__email__ = 'melvin.douglas@hotmail.com'
__status__ = 'Production'

import os
from zeep import Client
from zeep.cache import SqliteCache
from zeep.transports import Transport
from zeep.plugins import HistoryPlugin
from zeep.exceptions import Fault
from zeep.helpers import serialize_object
from requests import Session
from requests.auth import HTTPBasicAuth
import urllib3
from dataclasses import dataclass

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
urllib3.util.ssl_.DEFAULT_CIPHERS = 'HIGH:!DH:!aNULL' #= 'ALL'

class axl:
    def __init__(self, username, password, server_ip, server_ver=11.5, tls_verify=True, timeout=10):
        self.last_exception = None

        wsdl = 'file://' + os.path.join(os.getcwd(), f'schema/{server_ver}/AXLAPI.wsdl')
        address = f'https://{server_ip}:8443/axl/'
        binding = '{http://www.cisco.com/AXLAPIService/}AXLAPIBinding'

        session = Session()
        session.verify = tls_verify
        session.auth = HTTPBasicAuth(username, password)

        cache = SqliteCache()
        transport = Transport(cache=cache, session=session, timeout=timeout, operation_timeout=timeout)
        self.history = HistoryPlugin()
        self.client = Client(wsdl=wsdl, transport=transport, plugins=[self.history])

        self.service = self.client.create_service(binding, address)

        # region System
        ## LDAP/Enterprise Parameters/Service Parameters/Licensing
        # ProcessNode
        class _ProcessNode: pass
        self.ProcessNode = _ProcessNode
        self.ProcessNode.Create = lambda data, serialize=False: self._callSoap_func('addProcessNode', data, serialize)
        self.ProcessNode.Get = lambda data, serialize=False: self._callSoap_func('getProcessNode', data, serialize)
        self.ProcessNode.List = lambda data, serialize=False: self._callSoap_func('listProcessNode', data, serialize)
        self.ProcessNode.Update = lambda data, serialize=False: self._callSoap_func('updateProcessNode', data, serialize)
        self.ProcessNode.Remove = lambda data, serialize=False: self._callSoap_func('removeProcessNode', data, serialize)
        # CallManager
        class _CallManager: pass
        self.CallManager = _CallManager
        self.CallManager.Get = lambda data, serialize=False: self._callSoap_func('getCallManager', data, serialize)
        self.CallManager.List = lambda data, serialize=False: self._callSoap_func('listCallManager', data, serialize)
        self.CallManager.Update = lambda data, serialize=False: self._callSoap_func('updateCallManager', data, serialize)
        # CallManagerGroup
        class _CallManagerGroup: pass
        self.CallManagerGroup = _CallManagerGroup
        self.CallManagerGroup.Create = lambda data, serialize=False: self._callSoap_func('addCallManagerGroup', data, serialize)
        self.CallManagerGroup.Get = lambda data, serialize=False: self._callSoap_func('getCallManagerGroup', data, serialize)
        self.CallManagerGroup.List = lambda data, serialize=False: self._callSoap_func('listCallManagerGroup', data, serialize)
        self.CallManagerGroup.Update = lambda data, serialize=False: self._callSoap_func('updateCallManagerGroup', data, serialize)
        self.CallManagerGroup.Remove = lambda data, serialize=False: self._callSoap_func('removeCallManagerGroup', data, serialize)
        # PhoneNtp
        class _PhoneNtp: pass
        self.PhoneNtp = _PhoneNtp
        self.PhoneNtp.Create = lambda data, serialize=False: self._callSoap_func('addPhoneNtp', data, serialize)
        self.PhoneNtp.Get = lambda data, serialize=False: self._callSoap_func('getPhoneNtp', data, serialize)
        self.PhoneNtp.List = lambda data, serialize=False: self._callSoap_func('listPhoneNtp', data, serialize)
        self.PhoneNtp.Update = lambda data, serialize=False: self._callSoap_func('updatePhoneNtp', data, serialize)
        self.PhoneNtp.Remove = lambda data, serialize=False: self._callSoap_func('removePhoneNtp', data, serialize)

        # DateTimeGroup

        # PresenceGroup

        # Region
        class _Region: pass
        self.Region = _Region
        self.Region.Create = lambda data, serialize=False: self._callSoap_func('addRegion', data, serialize)
        self.Region.Get = lambda data, serialize=False: self._callSoap_func('getRegion', data, serialize)
        self.Region.List = lambda data, serialize=False: self._callSoap_func('listRegion', data, serialize)
        self.Region.Update = lambda data, serialize=False: self._callSoap_func('updateRegion', data, serialize)
        self.Region.Remove = lambda data, serialize=False: self._callSoap_func('removeRegion', data, serialize)

        # DevicePool
        class _DevicePool: pass
        self.DevicePool = _DevicePool
        self.DevicePool.Create = lambda data, serialize=False: self._callSoap_func('addDevicePool', data, serialize)
        self.DevicePool.Get = lambda data, serialize=False: self._callSoap_func('getDevicePool', data, serialize)
        self.DevicePool.List = lambda data, serialize=False: self._callSoap_func('listDevicePool', data, serialize)
        self.DevicePool.Update = lambda data, serialize=False: self._callSoap_func('updateDevicePool', data, serialize)
        self.DevicePool.Remove = lambda data, serialize=False: self._callSoap_func('removeDevicePool', data, serialize)
        # Location
        class _Location: pass
        self.Location = _Location
        self.Location.Create = lambda data, serialize=False: self._callSoap_func('addLocation', data, serialize)
        self.Location.Get = lambda data, serialize=False: self._callSoap_func('getLocation', data, serialize)
        self.Location.List = lambda data, serialize=False: self._callSoap_func('listLocation', data, serialize)
        self.Location.Update = lambda data, serialize=False: self._callSoap_func('updateLocation', data, serialize)
        self.Location.Remove = lambda data, serialize=False: self._callSoap_func('removeLocation', data, serialize)

        # PhysicalLocation

        # Srst

        # Enterprise Parameter
        # ServiceParameter

        # GeoLocation

        # PhoneSecurityProfile

        # SipTrunkSecurityProfile

        # endregion

        # region Call Routing
        #AARGroup/application dial rules/sip Dial Rules/Router Filter/access list/time period/time schedule/Intercom/Client matter Codes/forced authorization codes/call park/call pickup group/meet Me/route plan report/
        # RouteGroup

        # RouteList

        # RoutePattern

        # LineGroup

        # HuntList

        # HuntPilot

        # RoutePartition
        class _RoutePartition: pass
        self.RoutePartition = _RoutePartition
        self.RoutePartition.Create = lambda data, serialize=False: self._callSoap_func('addRoutePartition', data, serialize)
        self.RoutePartition.Get = lambda data, serialize=False: self._callSoap_func('getRoutePartition', data, serialize)
        self.RoutePartition.List = lambda data, serialize=False: self._callSoap_func('listRoutePartition', data, serialize)
        self.RoutePartition.Update = lambda data, serialize=False: self._callSoap_func('updateRoutePartition', data, serialize)
        self.RoutePartition.Remove = lambda data, serialize=False: self._callSoap_func('removeRoutePartition', data, serialize)
        # Css
        class _Css: pass
        self.Css = _Css
        self.Css.Create = lambda data, serialize=False: self._callSoap_func('addCss', data, serialize)
        self.Css.Get = lambda data, serialize=False: self._callSoap_func('getCss', data, serialize)
        self.Css.List = lambda data, serialize=False: self._callSoap_func('listCss', data, serialize)
        self.Css.Update = lambda data, serialize=False: self._callSoap_func('updateCss', data, serialize)
        self.Css.Remove = lambda data, serialize=False: self._callSoap_func('removeCss', data, serialize)
        # CmcInfo

        # FacInfo

        # TransPattern

        # CallPark

        # CallPickupGroup

        # Line
        class _Line: pass
        self.Line = _Line
        self.Line.Create = lambda data, serialize=False: self._callSoap_func('addLine', data, serialize)
        self.Line.Get = lambda data, serialize=False: self._callSoap_func('getLine', data, serialize)
        self.Line.List = lambda data, serialize=False: self._callSoap_func('listLine', data, serialize)
        self.Line.Update = lambda data, serialize=False: self._callSoap_func('updateLine', data, serialize)
        self.Line.Remove = lambda data, serialize=False: self._callSoap_func('removeLine', data, serialize)
        # MeetMe

        # RoutePlan
        class _RoutePlan: pass
        self.RoutePlan = _RoutePlan
        self.RoutePlan.Get = lambda data, serialize=False: self._callSoap_func('getRoutePlan', data, serialize)
        self.RoutePlan.List = lambda data, serialize=False: self._callSoap_func('listRoutePlan', data, serialize)
        self.RoutePlan.Update = lambda data, serialize=False: self._callSoap_func('updateRoutePlan', data, serialize)

        # endregion

        # region Media Resources
        # Annunciator

        # ConferenceBridge

        # Mtp

        # MohAudioSource

        # MohServer

        # Transcoder

        # MediaResourceGroup

        # MediaResourceList

        # endregion

        # region Advanced Features
        # VoiceMailPort

        # MessageWaiting

        # VoiceMailPilot

        # VoiceMailProfile

        # endregion

        # region Device
        # CtiRoutePoint
        class _CtiRoutePoint: pass
        self.CtiRoutePoint = _CtiRoutePoint
        self.CtiRoutePoint.Create = lambda data, serialize=False: self._callSoap_func('addCtiRoutePoint', data, serialize)
        self.CtiRoutePoint.Get = lambda data, serialize=False: self._callSoap_func('getCtiRoutePoint', data, serialize)
        self.CtiRoutePoint.List = lambda data, serialize=False: self._callSoap_func('listCtiRoutePoint', data, serialize)
        self.CtiRoutePoint.Update = lambda data, serialize=False: self._callSoap_func('updateCtiRoutePoint', data, serialize)
        self.CtiRoutePoint.Remove = lambda data, serialize=False: self._callSoap_func('removeCtiRoutePoint', data, serialize)
        # Phone
        class _Phone: pass
        self.Phone = _Phone
        self.Phone.Create = lambda data, serialize=False: self._callSoap_func('addPhone', data, serialize)
        self.Phone.Get = lambda data, serialize=False: self._callSoap_func('getPhone', data, serialize)
        self.Phone.List = lambda data, serialize=False: self._callSoap_func('listPhone', data, serialize)
        self.Phone.Update = lambda data, serialize=False: self._callSoap_func('updatePhone', data, serialize)
        self.Phone.Remove = lambda data, serialize=False: self._callSoap_func('removePhone', data, serialize)
        # SipTrunk

        # RemoteDestination

        # DefaultDeviceProfile

        # DeviceProfile
        class _DeviceProfile: pass
        self.DeviceProfile = _DeviceProfile
        self.DeviceProfile.Create = lambda data, serialize=False: self._callSoap_func('addDeviceProfile', data, serialize)
        self.DeviceProfile.Get = lambda data, serialize=False: self._callSoap_func('getDeviceProfile', data, serialize)
        self.DeviceProfile.List = lambda data, serialize=False: self._callSoap_func('listDeviceProfile', data, serialize)
        self.DeviceProfile.Update = lambda data, serialize=False: self._callSoap_func('updateDeviceProfile', data, serialize)
        self.DeviceProfile.Remove = lambda data, serialize=False: self._callSoap_func('removeDeviceProfile', data, serialize)
        # PhoneButtonTemplate

        # SoftKeyTemplate

        # IpPhoneServices

        # SipProfile

        # CommonDeviceConfig

        # CommonPhoneConfig

        # RemoteDestinationProfile

        # endregion

        # region User Management
        # AppUser

        # User
        class _User: pass
        self.User = _User
        self.User.Create = lambda data, serialize=False: self._callSoap_func('addUser', data, serialize)
        self.User.Get = lambda data, serialize=False: self._callSoap_func('getUser', data, serialize)
        self.User.List = lambda data, serialize=False: self._callSoap_func('listUser', data, serialize)
        self.User.Update = lambda data, serialize=False: self._callSoap_func('updateUser', data, serialize)
        self.User.Remove = lambda data, serialize=False: self._callSoap_func('removeUser', data, serialize)
        # UserGroup
        class _UserGroup: pass
        self.UserGroup = _UserGroup
        self.UserGroup.Create = lambda data, serialize=False: self._callSoap_func('addUserGroup', data, serialize)
        self.UserGroup.Get = lambda data, serialize=False: self._callSoap_func('getUserGroup', data, serialize)
        self.UserGroup.List = lambda data, serialize=False: self._callSoap_func('listUserGroup', data, serialize)
        self.UserGroup.Update = lambda data, serialize=False: self._callSoap_func('updateUserGroup', data, serialize)
        self.UserGroup.Remove = lambda data, serialize=False: self._callSoap_func('removeUserGroup', data, serialize)
        # UserPhoneAssociation
        class _UserPhoneAssociation: pass
        self.UserPhoneAssociation = _UserPhoneAssociation
        self.UserPhoneAssociation.Create = lambda data, serialize=False: self._callSoap_func('addUserPhoneAssociation', data, serialize)
        # UcService

        # ServiceProfile

        # endregion

        # region Thin AXL (SQL Queries / Updates)
        class _Sql: pass
        self.Sql = _Sql
        self.Sql.Query = lambda data, serialize=False: self._callSoap_func('executeSQLQuery', data, serialize)
        # endregion
    def _callSoap_func(self, func_name, data, serialize=False):
        try:
            result = getattr(self.service, func_name)(**data)
            #result = self.service.updateAppUser(**data)
        except Exception as fault:
            result = None
            self.last_exception = fault
        if result is not None: result = result['return']
        if serialize is True:
            return serialize_object(result)
        return result

