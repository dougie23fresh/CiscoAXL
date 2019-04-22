__author__ = 'Melvin Douglas'
__version__ = '12'
__email__ = 'melvin.douglas@'
__status__ = 'Development' #'Prototype', 'Development', or 'Production'.

import os
from zeep import Client
from zeep.cache import SqliteCache
from zeep.transports import Transport
from zeep.plugins import HistoryPlugin
from requests import Session
from requests.auth import HTTPBasicAuth
import urllib3

# allow program to continue running without
# warnings about not verifying HTTPS certificates
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# Allow DH ciphers
urllib3.util.ssl_.DEFAULT_CIPHERS = 'HIGH:!DH:!aNULL' #= 'ALL'
#urllib3.util.ssl_.DEFAULT_CIPHERS = 'ALL'

class axl:
    def __init__(self, username, password, server_ip, server_ver=11.5, tls_verify=True, timeout=10):
        self.last_exception = None

        wsdl = 'file://' + os.path.join(os.getcwd(), f'CiscoAXL/schema/{server_ver}/AXLAPI.wsdl')
        address = f'https://{server_ip}:8443/axl/'
        binding = '{http://www.cisco.com/AXLAPIService/}AXLAPIBinding'

        session = Session()
        session.verify = tls_verify
        session.auth = HTTPBasicAuth(username, password)

        cache = SqliteCache()
        transport = Transport(cache=cache, session=session, timeout=timeout, operation_timeout=timeout)
        history = HistoryPlugin()
        self.client = Client(wsdl=wsdl, transport=transport, plugins=[history])

        self.service = self.client.create_service(binding, address)

    def _callSoap_func(self, func_name, data):
        try:
            result = getattr(self.service, func_name)(**data)
            #result = self.service.updateAppUser(**data)
        except Exception as fault:
            result = None
            self.last_exception = fault
        if result is not None: result = result['return']
        return result
        
    # region System
    ## LDAP/Enterprise Parameters/Service Parameters/Licensing
    # ProcessNode
    def ProcessNodeCreate(self, data):
        return self._callSoap_func('addProcessNode', data)
    def ProcessNodeGet(self, data):
        return self._callSoap_func('getProcessNode', data)
    def ProcessNodeGets(self, data):
        return self._callSoap_func('listProcessNode', data)
    def ProcessNodeUpdate(self, data):
        return self._callSoap_func('updateProcessNode', data)
    def ProcessNodeRemove(self, data):
        return self._callSoap_func('removeProcessNode', data)
    # CallManager
    def CallManagerGet(self, data):
        return self._callSoap_func('getCallManager', data)
    def CallManagerGets(self, data):
        return self._callSoap_func('listCallManager', data)
    def CallManagerUpdate(self, data):
        return self._callSoap_func('updateCallManager', data)
    # CallManagerGroup
    def CallManagerGroupCreate(self, data):
        return self._callSoap_func('addCallManagerGroup', data)
    def CallManagerGroupGet(self, data):
        return self._callSoap_func('getCallManagerGroup', data)
    def CallManagerGroupGets(self, data):
        return self._callSoap_func('listCallManagerGroup', data)
    def CallManagerGroupUpdate(self, data):
        return self._callSoap_func('updateCallManagerGroup', data)
    def CallManagerGroupRemove(self, data):
        return self._callSoap_func('removeCallManagerGroup', data)
    # PhoneNtp
    def PhoneNtpCreate(self, data):
        return self._callSoap_func('addPhoneNtp', data)
    def PhoneNtpGet(self, data):
        return self._callSoap_func('getPhoneNtp', data)
    def PhoneNtpGets(self, data):
        return self._callSoap_func('listPhoneNtp', data)
    def PhoneNtpUpdate(self, data):
        return self._callSoap_func('updatePhoneNtp', data)
    def PhoneNtpRemove(self, data):
        return self._callSoap_func('removePhoneNtp', data)
    # DateTimeGroup
    def DateTimeGroupCreate(self, data):
        return self._callSoap_func('addDateTimeGroup', data)
    def DateTimeGroupGet(self, data):
        return self._callSoap_func('getDateTimeGroup', data)
    def DateTimeGroupGets(self, data):
        return self._callSoap_func('listDateTimeGroup', data)
    def DateTimeGroupUpdate(self, data):
        return self._callSoap_func('updateDateTimeGroup', data)
    def DateTimeGroupRemove(self, data):
        return self._callSoap_func('removeDateTimeGroup', data)
    # PresenceGroup
    def PresenceGroupCreate(self, data):
        return self._callSoap_func('addPresenceGroup', data)
    def PresenceGroupGet(self, data):
        return self._callSoap_func('getPresenceGroup', data)
    def PresenceGroupGets(self, data):
        return self._callSoap_func('listPresenceGroup', data)
    def PresenceGroupUpdate(self, data):
        return self._callSoap_func('updatePresenceGroup', data)
    def PresenceGroupRemove(self, data):
        return self._callSoap_func('removePresenceGroup', data)
    # Region
    def RegionCreate(self, data):
        return self._callSoap_func('addRegion', data)
    def RegionGet(self, data):
        return self._callSoap_func('getRegion', data)
    def RegionGets(self, data):
        return self._callSoap_func('listRegion', data)
    def RegionUpdate(self, data):
        return self._callSoap_func('updateRegion', data)
    def RegionRemove(self, data):
        return self._callSoap_func('removeRegion', data)
    # DevicePool
    def DevicePoolCreate(self, data):
        return self._callSoap_func('addDevicePool', data)
    def DevicePoolGet(self, data):
        return self._callSoap_func('getDevicePool', data)
    def DevicePoolGets(self, data):
        return self._callSoap_func('listDevicePool', data)
    def DevicePoolUpdate(self, data):
        return self._callSoap_func('updateDevicePool', data)
    def DevicePoolRemove(self, data):
        return self._callSoap_func('removeDevicePool', data)
    # Location
    def LocationCreate(self, data):
        return self._callSoap_func('addLocation', data)
    def LocationGet(self, data):
        return self._callSoap_func('getLocation', data)
    def LocationGets(self, data):
        return self._callSoap_func('listLocation', data)
    def LocationUpdate(self, data):
        return self._callSoap_func('updateLocation', data)
    def LocationRemove(self, data):
        return self._callSoap_func('removeLocation', data)
    # PhysicalLocation
    def PhysicalLocationCreate(self, data):
        return self._callSoap_func('addPhysicalLocation', data)
    def PhysicalLocationGet(self, data):
        return self._callSoap_func('getPhysicalLocation', data)
    def PhysicalLocationGets(self, data):
        return self._callSoap_func('listPhysicalLocation', data)
    def PhysicalLocationUpdate(self, data):
        return self._callSoap_func('updatePhysicalLocation', data)
    def PhysicalLocationRemove(self, data):
        return self._callSoap_func('removePhysicalLocation', data)
    # Srst
    def SrstCreate(self, data):
        return self._callSoap_func('addSrst', data)
    def SrstGet(self, data):
        return self._callSoap_func('getSrst', data)
    def SrstGets(self, data):
        return self._callSoap_func('listSrst', data)
    def SrstUpdate(self, data):
        return self._callSoap_func('updateSrst', data)
    def SrstRemove(self, data):
        return self._callSoap_func('removeSrst', data)
    # Enterprise Parameter
    # ServiceParameter
    def ServiceParameterGet(self, data):
        return self._callSoap_func('getServiceParameter', data)
    def ServiceParameterGets(self, data):
        return self._callSoap_func('listServiceParameter', data)
    def ServiceParameterUpdate(self, data):
        return self._callSoap_func('updateServiceParameter', data)
    # GeoLocation
    def GeoLocationCreate(self, data):
        return self._callSoap_func('addGeoLocation', data)
    def GeoLocationGet(self, data):
        return self._callSoap_func('getGeoLocation', data)
    def GeoLocationGets(self, data):
        return self._callSoap_func('listGeoLocation', data)
    def GeoLocationUpdate(self, data):
        return self._callSoap_func('updateGeoLocation', data)
    def GeoLocationRemove(self, data):
        return self._callSoap_func('removeGeoLocation', data)
    # PhoneSecurityProfile
    def PhoneSecurityProfileCreate(self, data):
        return self._callSoap_func('addPhoneSecurityProfile', data)
    def PhoneSecurityProfileGet(self, data):
        return self._callSoap_func('getPhoneSecurityProfile', data)
    def PhoneSecurityProfileGets(self, data):
        return self._callSoap_func('listPhoneSecurityProfile', data)
    def PhoneSecurityProfileUpdate(self, data):
        return self._callSoap_func('updatePhoneSecurityProfile', data)
    def PhoneSecurityProfileRemove(self, data):
        return self._callSoap_func('removePhoneSecurityProfile', data)
    # SipTrunkSecurityProfile
    def SipTrunkSecurityProfileCreate(self, data):
        return self._callSoap_func('addSipTrunkSecurityProfile', data)
    def SipTrunkSecurityProfileGet(self, data):
        return self._callSoap_func('getSipTrunkSecurityProfile', data)
    def SipTrunkSecurityProfileGets(self, data):
        return self._callSoap_func('listSipTrunkSecurityProfile', data)
    def SipTrunkSecurityProfileUpdate(self, data):
        return self._callSoap_func('updateSipTrunkSecurityProfile', data)
    def SipTrunkSecurityProfileRemove(self, data):
        return self._callSoap_func('removeSipTrunkSecurityProfile', data)
    # endregion

    # region Call Routing
    #AARGroup/application dial rules/sip Dial Rules/Router Filter/access list/time period/time schedule/Intercom/Client matter Codes/forced authorization codes/call park/call pickup group/meet Me/route plan report/
    # RouteGroup
    def RouteGroupCreate(self, data):
        return self._callSoap_func('addRouteGroup', data)
    def RouteGroupGet(self, data):
        return self._callSoap_func('getRouteGroup', data)
    def RouteGroupGets(self, data):
        return self._callSoap_func('listRouteGroup', data)
    def RouteGroupUpdate(self, data):
        return self._callSoap_func('updateRouteGroup', data)
    def RouteGroupRemove(self, data):
        return self._callSoap_func('removeRouteGroup', data)
    # RouteList
    def RouteListCreate(self, data):
        return self._callSoap_func('addRouteList', data)
    def RouteListGet(self, data):
        return self._callSoap_func('getRouteList', data)
    def RouteListGets(self, data):
        return self._callSoap_func('listRouteList', data)
    def RouteListUpdate(self, data):
        return self._callSoap_func('updateRouteList', data)
    def RouteListRemove(self, data):
        return self._callSoap_func('removeRouteList', data)
    # RoutePattern
    def RoutePatternCreate(self, data):
        return self._callSoap_func('addRoutePattern', data)
    def RoutePatternGet(self, data):
        return self._callSoap_func('getRoutePattern', data)
    def RoutePatternGets(self, data):
        return self._callSoap_func('listRoutePattern', data)
    def RoutePatternUpdate(self, data):
        return self._callSoap_func('updateRoutePattern', data)
    def RoutePatternRemove(self, data):
        return self._callSoap_func('removeRoutePattern', data)
    # LineGroup
    def LineGroupCreate(self, data):
        return self._callSoap_func('addLineGroup', data)
    def LineGroupGet(self, data):
        return self._callSoap_func('getLineGroup', data)
    def LineGroupGets(self, data):
        return self._callSoap_func('listLineGroup', data)
    def LineGroupUpdate(self, data):
        return self._callSoap_func('updateLineGroup', data)
    def LineGroupRemove(self, data):
        return self._callSoap_func('removeLineGroup', data)
    # HuntList
    def HuntListCreate(self, data):
        return self._callSoap_func('addHuntList', data)
    def HuntListGet(self, data):
        return self._callSoap_func('getHuntList', data)
    def HuntListGets(self, data):
        return self._callSoap_func('listHuntList', data)
    def HuntListUpdate(self, data):
        return self._callSoap_func('updateHuntList', data)
    def HuntListRemove(self, data):
        return self._callSoap_func('removeHuntList', data)
    # HuntPilot
    def HuntPilotCreate(self, data):
        return self._callSoap_func('addHuntPilot', data)
    def HuntPilotGet(self, data):
        return self._callSoap_func('getHuntPilot', data)
    def HuntPilotGets(self, data):
        return self._callSoap_func('listHuntPilot', data)
    def HuntPilotUpdate(self, data):
        return self._callSoap_func('updateHuntPilot', data)
    def HuntPilotRemove(self, data):
        return self._callSoap_func('removeHuntPilot', data)
    # RoutePartition
    def RoutePartitionCreate(self, data):
        return self._callSoap_func('addRoutePartition', data)
    def RoutePartitionGet(self, data):
        return self._callSoap_func('getRoutePartition', data)
    def RoutePartitionGets(self, data):
        return self._callSoap_func('listRoutePartition', data)
    def RoutePartitionUpdate(self, data):
        return self._callSoap_func('updateRoutePartition', data)
    def RoutePartitionRemove(self, data):
        return self._callSoap_func('removeRoutePartition', data)
    # Css
    def CssCreate(self, data):
        return self._callSoap_func('addCss', data)
    def CssGet(self, data):
        return self._callSoap_func('getCss', data)
    def CssGets(self, data):
        return self._callSoap_func('listCss', data)
    def CssUpdate(self, data):
        return self._callSoap_func('updateCss', data)
    def CssRemove(self, data):
        return self._callSoap_func('removeCss', data)
    # CmcInfo
    def CmcInfoCreate(self, data):
        return self._callSoap_func('addCmcInfo', data)
    def CmcInfoGet(self, data):
        return self._callSoap_func('getCmcInfo', data)
    def CmcInfoGets(self, data):
        return self._callSoap_func('listCmcInfo', data)
    def CmcInfoUpdate(self, data):
        return self._callSoap_func('updateCmcInfo', data)
    def CmcInfoRemove(self, data):
        return self._callSoap_func('removeCmcInfo', data)
    # FacInfo
    def FacInfoCreate(self, data):
        return self._callSoap_func('addFacInfo', data)
    def FacInfoGet(self, data):
        return self._callSoap_func('getFacInfo', data)
    def FacInfoGets(self, data):
        return self._callSoap_func('listFacInfo', data)
    def FacInfoUpdate(self, data):
        return self._callSoap_func('updateFacInfo', data)
    def FacInfoRemove(self, data):
        return self._callSoap_func('removeFacInfo', data)
    # TransPattern
    def TransPatternCreate(self, data):
        return self._callSoap_func('addTransPattern', data)
    def TransPatternGet(self, data):
        return self._callSoap_func('getTransPattern', data)
    def TransPatternGets(self, data):
        return self._callSoap_func('listTransPattern', data)
    def TransPatternUpdate(self, data):
        return self._callSoap_func('updateTransPattern', data)
    def TransPatternRemove(self, data):
        return self._callSoap_func('removeTransPattern', data)
    # CallPark
    def CallParkCreate(self, data):
        return self._callSoap_func('addCallPark', data)
    def CallParkGet(self, data):
        return self._callSoap_func('getCallPark', data)
    def CallParkGets(self, data):
        return self._callSoap_func('listCallPark', data)
    def CallParkUpdate(self, data):
        return self._callSoap_func('updateCallPark', data)
    def CallParkRemove(self, data):
        return self._callSoap_func('removeCallPark', data)
    # CallPickupGroup
    def CallPickupGroupCreate(self, data):
        return self._callSoap_func('addCallPickupGroup', data)
    def CallPickupGroupGet(self, data):
        return self._callSoap_func('getCallPickupGroup', data)
    def CallPickupGroupGets(self, data):
        return self._callSoap_func('listCallPickupGroup', data)
    def CallPickupGroupUpdate(self, data):
        return self._callSoap_func('updateCallPickupGroup', data)
    def CallPickupGroupRemove(self, data):
        return self._callSoap_func('removeCallPickupGroup', data)
    # Line
    def LineCreate(self, data):
        return self._callSoap_func('addLine', data)
    def LineGet(self, data):
        return self._callSoap_func('getLine', data)
    def LineGets(self, data):
        return self._callSoap_func('listLine', data)
    def LineUpdate(self, data):
        return self._callSoap_func('updateLine', data)
    def LineRemove(self, data):
        return self._callSoap_func('removeLine', data)
    # MeetMe
    def MeetMeCreate(self, data):
        return self._callSoap_func('addMeetMe', data)
    def MeetMeGet(self, data):
        return self._callSoap_func('getMeetMe', data)
    def MeetMeGets(self, data):
        return self._callSoap_func('listMeetMe', data)
    def MeetMeUpdate(self, data):
        return self._callSoap_func('updateMeetMe', data)
    def MeetMeRemove(self, data):
        return self._callSoap_func('removeMeetMe', data)
    # RoutePlan
    def RoutePlanGet(self, data):
        return self._callSoap_func('getRoutePlan', data)
    def RoutePlanGets(self, data):
        return self._callSoap_func('listRoutePlan', data)
    def RoutePlanUpdate(self, data):
        return self._callSoap_func('updateRoutePlan', data)
    # endregion

    # region Media Resources
    # Annunciator
    def AnnunciatorGet(self, data):
        return self._callSoap_func('getAnnunciator', data)
    def AnnunciatorGets(self, data):
        return self._callSoap_func('listAnnunciator', data)
    def AnnunciatorUpdate(self, data):
        return self._callSoap_func('updateAnnunciator', data)
    # ConferenceBridge
    def ConferenceBridgeCreate(self, data):
        return self._callSoap_func('addConferenceBridge', data)
    def ConferenceBridgeGet(self, data):
        return self._callSoap_func('getConferenceBridge', data)
    def ConferenceBridgeGets(self, data):
        return self._callSoap_func('listConferenceBridge', data)
    def ConferenceBridgeUpdate(self, data):
        return self._callSoap_func('updateConferenceBridge', data)
    def ConferenceBridgeRemove(self, data):
        return self._callSoap_func('removeConferenceBridge', data)
    # Mtp
    def MtpCreate(self, data):
        return self._callSoap_func('addMtp', data)
    def MtpGet(self, data):
        return self._callSoap_func('getMtp', data)
    def MtpGets(self, data):
        return self._callSoap_func('listMtp', data)
    def MtpUpdate(self, data):
        return self._callSoap_func('updateMtp', data)
    def MtpRemove(self, data):
        return self._callSoap_func('removeMtp', data)
    # MohAudioSource
    def MohAudioSourceCreate(self, data):
        return self._callSoap_func('addMohAudioSource', data)
    def MohAudioSourceGet(self, data):
        return self._callSoap_func('getMohAudioSource', data)
    def MohAudioSourceGets(self, data):
        return self._callSoap_func('listMohAudioSource', data)
    def MohAudioSourceUpdate(self, data):
        return self._callSoap_func('updateMohAudioSource', data)
    def MohAudioSourceRemove(self, data):
        return self._callSoap_func('removeMohAudioSource', data)
    # MohServer
    def MohServerGet(self, data):
        return self._callSoap_func('getMohServer', data)
    def MohServerGets(self, data):
        return self._callSoap_func('listMohServer', data)
    def MohServerUpdate(self, data):
        return self._callSoap_func('updateMohServer', data)
    # Transcoder
    def TranscoderCreate(self, data):
        return self._callSoap_func('addTranscoder', data)
    def TranscoderGet(self, data):
        return self._callSoap_func('getTranscoder', data)
    def TranscoderGets(self, data):
        return self._callSoap_func('listTranscoder', data)
    def TranscoderUpdate(self, data):
        return self._callSoap_func('updateTranscoder', data)
    def TranscoderRemove(self, data):
        return self._callSoap_func('removeTranscoder', data)
    # MediaResourceGroup
    def MediaResourceGroupCreate(self, data):
        return self._callSoap_func('addMediaResourceGroup', data)
    def MediaResourceGroupGet(self, data):
        return self._callSoap_func('getMediaResourceGroup', data)
    def MediaResourceGroupGets(self, data):
        return self._callSoap_func('listMediaResourceGroup', data)
    def MediaResourceGroupUpdate(self, data):
        return self._callSoap_func('updateMediaResourceGroup', data)
    def MediaResourceGroupRemove(self, data):
        return self._callSoap_func('removeMediaResourceGroup', data)
    # MediaResourceList
    def MediaResourceListCreate(self, data):
        return self._callSoap_func('addMediaResourceList', data)
    def MediaResourceListGet(self, data):
        return self._callSoap_func('getMediaResourceList', data)
    def MediaResourceListGets(self, data):
        return self._callSoap_func('listMediaResourceList', data)
    def MediaResourceListUpdate(self, data):
        return self._callSoap_func('updateMediaResourceList', data)
    def MediaResourceListRemove(self, data):
        return self._callSoap_func('removeMediaResourceList', data)
    # endregion

    # region Advanced Features
    # VoiceMailPort
    def VoiceMailPortCreate(self, data):
        return self._callSoap_func('addVoiceMailPort', data)
    def VoiceMailPortGet(self, data):
        return self._callSoap_func('getVoiceMailPort', data)
    def VoiceMailPortGets(self, data):
        return self._callSoap_func('listVoiceMailPort', data)
    def VoiceMailPortUpdate(self, data):
        return self._callSoap_func('updateVoiceMailPort', data)
    def VoiceMailPortRemove(self, data):
        return self._callSoap_func('removeVoiceMailPort', data)
    # MessageWaiting
    def MessageWaitingCreate(self, data):
        return self._callSoap_func('addMessageWaiting', data)
    def MessageWaitingGet(self, data):
        return self._callSoap_func('getMessageWaiting', data)
    def MessageWaitingGets(self, data):
        return self._callSoap_func('listMessageWaiting', data)
    def MessageWaitingUpdate(self, data):
        return self._callSoap_func('updateMessageWaiting', data)
    def MessageWaitingRemove(self, data):
        return self._callSoap_func('removeMessageWaiting', data)
    # VoiceMailPilot
    def VoiceMailPilotCreate(self, data):
        return self._callSoap_func('addVoiceMailPilot', data)
    def VoiceMailPilotGet(self, data):
        return self._callSoap_func('getVoiceMailPilot', data)
    def VoiceMailPilotGets(self, data):
        return self._callSoap_func('listVoiceMailPilot', data)
    def VoiceMailPilotUpdate(self, data):
        return self._callSoap_func('updateVoiceMailPilot', data)
    def VoiceMailPilotRemove(self, data):
        return self._callSoap_func('removeVoiceMailPilot', data)
    # VoiceMailProfile
    def VoiceMailProfileCreate(self, data):
        return self._callSoap_func('addVoiceMailProfile', data)
    def VoiceMailProfileGet(self, data):
        return self._callSoap_func('getVoiceMailProfile', data)
    def VoiceMailProfileGets(self, data):
        return self._callSoap_func('listVoiceMailProfile', data)
    def VoiceMailProfileUpdate(self, data):
        return self._callSoap_func('updateVoiceMailProfile', data)
    def VoiceMailProfileRemove(self, data):
        return self._callSoap_func('removeVoiceMailProfile', data)
    # endregion

    # region Device
    # CtiRoutePoint
    def CtiRoutePointCreate(self, data):
        return self._callSoap_func('addCtiRoutePoint', data)
    def CtiRoutePointGet(self, data):
        return self._callSoap_func('getCtiRoutePoint', data)
    def CtiRoutePointGets(self, data):
        return self._callSoap_func('listCtiRoutePoint', data)
    def CtiRoutePointUpdate(self, data):
        return self._callSoap_func('updateCtiRoutePoint', data)
    def CtiRoutePointRemove(self, data):
        return self._callSoap_func('removeCtiRoutePoint', data)
    # Phone
    def PhoneCreate(self, data):
        return self._callSoap_func('addPhone', data)
    def PhoneGet(self, data):
        return self._callSoap_func('getPhone', data)
    def PhoneGets(self, data):
        return self._callSoap_func('listPhone', data)
    def PhoneUpdate(self, data):
        return self._callSoap_func('updatePhone', data)
    def PhoneRemove(self, data):
        return self._callSoap_func('removePhone', data)
    # SipTrunk
    def SipTrunkCreate(self, data):
        return self._callSoap_func('addSipTrunk', data)
    def SipTrunkGet(self, data):
        return self._callSoap_func('getSipTrunk', data)
    def SipTrunkGets(self, data):
        return self._callSoap_func('listSipTrunk', data)
    def SipTrunkUpdate(self, data):
        return self._callSoap_func('updateSipTrunk', data)
    def SipTrunkRemove(self, data):
        return self._callSoap_func('removeSipTrunk', data)
    # RemoteDestination
    def RemoteDestinationCreate(self, data):
        return self._callSoap_func('addRemoteDestination', data)
    def RemoteDestinationGet(self, data):
        return self._callSoap_func('getRemoteDestination', data)
    def RemoteDestinationGets(self, data):
        return self._callSoap_func('listRemoteDestination', data)
    def RemoteDestinationUpdate(self, data):
        return self._callSoap_func('updateRemoteDestination', data)
    def RemoteDestinationRemove(self, data):
        return self._callSoap_func('removeRemoteDestination', data)
    # DefaultDeviceProfile
    def DefaultDeviceProfileCreate(self, data):
        return self._callSoap_func('addDefaultDeviceProfile', data)
    def DefaultDeviceProfileGet(self, data):
        return self._callSoap_func('getDefaultDeviceProfile', data)
    def DefaultDeviceProfileGets(self, data):
        return self._callSoap_func('listDefaultDeviceProfile', data)
    def DefaultDeviceProfileUpdate(self, data):
        return self._callSoap_func('updateDefaultDeviceProfile', data)
    def DefaultDeviceProfileRemove(self, data):
        return self._callSoap_func('removeDefaultDeviceProfile', data)
    # DeviceProfile
    def DeviceProfileCreate(self, data):
        return self._callSoap_func('addDeviceProfile', data)
    def DeviceProfileGet(self, data):
        return self._callSoap_func('getDeviceProfile', data)
    def DeviceProfileGets(self, data):
        return self._callSoap_func('listDeviceProfile', data)
    def DeviceProfileUpdate(self, data):
        return self._callSoap_func('updateDeviceProfile', data)
    def DeviceProfileRemove(self, data):
        return self._callSoap_func('removeDeviceProfile', data)
    # PhoneButtonTemplate
    def PhoneButtonTemplateCreate(self, data):
        return self._callSoap_func('addPhoneButtonTemplate', data)
    def PhoneButtonTemplateGet(self, data):
        return self._callSoap_func('getPhoneButtonTemplate', data)
    def PhoneButtonTemplateGets(self, data):
        return self._callSoap_func('listPhoneButtonTemplate', data)
    def PhoneButtonTemplateUpdate(self, data):
        return self._callSoap_func('updatePhoneButtonTemplate', data)
    def PhoneButtonTemplateRemove(self, data):
        return self._callSoap_func('removePhoneButtonTemplate', data)
    # SoftKeyTemplate
    def SoftKeyTemplateCreate(self, data):
        return self._callSoap_func('addSoftKeyTemplate', data)
    def SoftKeyTemplateGet(self, data):
        return self._callSoap_func('getSoftKeyTemplate', data)
    def SoftKeyTemplateGets(self, data):
        return self._callSoap_func('listSoftKeyTemplate', data)
    def SoftKeyTemplateUpdate(self, data):
        return self._callSoap_func('updateSoftKeyTemplate', data)
    def SoftKeyTemplateRemove(self, data):
        return self._callSoap_func('removeSoftKeyTemplate', data)
    # IpPhoneServices
    def IpPhoneServicesCreate(self, data):
        return self._callSoap_func('addIpPhoneServices', data)
    def IpPhoneServicesGet(self, data):
        return self._callSoap_func('getIpPhoneServices', data)
    def IpPhoneServicesGets(self, data):
        return self._callSoap_func('listIpPhoneServices', data)
    def IpPhoneServicesUpdate(self, data):
        return self._callSoap_func('updateIpPhoneServices', data)
    def IpPhoneServicesRemove(self, data):
        return self._callSoap_func('removeIpPhoneServices', data)
    # SipProfile
    def SipProfileCreate(self, data):
        return self._callSoap_func('addSipProfile', data)
    def SipProfileGet(self, data):
        return self._callSoap_func('getSipProfile', data)
    def SipProfileGets(self, data):
        return self._callSoap_func('listSipProfile', data)
    def SipProfileUpdate(self, data):
        return self._callSoap_func('updateSipProfile', data)
    def SipProfileRemove(self, data):
        return self._callSoap_func('removeSipProfile', data)
    # CommonDeviceConfig
    def CommonDeviceConfigCreate(self, data):
        return self._callSoap_func('addCommonDeviceConfig', data)
    def CommonDeviceConfigGet(self, data):
        return self._callSoap_func('getCommonDeviceConfig', data)
    def CommonDeviceConfigGets(self, data):
        return self._callSoap_func('listCommonDeviceConfig', data)
    def CommonDeviceConfigUpdate(self, data):
        return self._callSoap_func('updateCommonDeviceConfig', data)
    def CommonDeviceConfigRemove(self, data):
        return self._callSoap_func('removeCommonDeviceConfig', data)
    # CommonPhoneConfig
    def CommonPhoneConfigCreate(self, data):
        return self._callSoap_func('addCommonPhoneConfig', data)
    def CommonPhoneConfigGet(self, data):
        return self._callSoap_func('getCommonPhoneConfig', data)
    def CommonPhoneConfigGets(self, data):
        return self._callSoap_func('listCommonPhoneConfig', data)
    def CommonPhoneConfigUpdate(self, data):
        return self._callSoap_func('updateCommonPhoneConfig', data)
    def CommonPhoneConfigRemove(self, data):
        return self._callSoap_func('removeCommonPhoneConfig', data)
    # RemoteDestinationProfile
    def RemoteDestinationProfileCreate(self, data):
        return self._callSoap_func('addRemoteDestinationProfile', data)
    def RemoteDestinationProfileGet(self, data):
        return self._callSoap_func('getRemoteDestinationProfile', data)
    def RemoteDestinationProfileGets(self, data):
        return self._callSoap_func('listRemoteDestinationProfile', data)
    def RemoteDestinationProfileUpdate(self, data):
        return self._callSoap_func('updateRemoteDestinationProfile', data)
    def RemoteDestinationProfileRemove(self, data):
        return self._callSoap_func('removeRemoteDestinationProfile', data)
    # endregion

    # region User Management
    # AppUser
    def AppUserCreate(self, data):
        return self._callSoap_func('addAppUser', data)
    def AppUserGet(self, data):
        return self._callSoap_func('getAppUser', data)
    def AppUserGets(self, data):
        return self._callSoap_func('listAppUser', data)
    def AppUserUpdate(self, data):
        return self._callSoap_func('updateAppUser', data)
    def AppUserRemove(self, data):
        return self._callSoap_func('removeAppUser', data)
    # User
    def UserCreate(self, data):
        return self._callSoap_func('addUser', data)
    def UserGet(self, data):
        return self._callSoap_func('getUser', data)
    def UserGets(self, data):
        return self._callSoap_func('listUser', data)
    def UserUpdate(self, data):
        return self._callSoap_func('updateUser', data)
    def UserRemove(self, data):
        return self._callSoap_func('removeUser', data)
    # UserGroup
    def UserGroupCreate(self, data):
        return self._callSoap_func('addUserGroup', data)
    def UserGroupGet(self, data):
        return self._callSoap_func('getUserGroup', data)
    def UserGroupGets(self, data):
        return self._callSoap_func('listUserGroup', data)
    def UserGroupUpdate(self, data):
        return self._callSoap_func('updateUserGroup', data)
    def UserGroupRemove(self, data):
        return self._callSoap_func('removeUserGroup', data)
    # UserPhoneAssociation
    def UserPhoneAssociationCreate(self, data):
        return self._callSoap_func('addUserPhoneAssociation', data)
    # UcService
    def UcServiceCreate(self, data):
        return self._callSoap_func('addUcService', data)
    def UcServiceGet(self, data):
        return self._callSoap_func('getUcService', data)
    def UcServiceGets(self, data):
        return self._callSoap_func('listUcService', data)
    def UcServiceUpdate(self, data):
        return self._callSoap_func('updateUcService', data)
    def UcServiceRemove(self, data):
        return self._callSoap_func('removeUcService', data)
    # ServiceProfile
    def ServiceProfileCreate(self, data):
        return self._callSoap_func('addServiceProfile', data)
    def ServiceProfileGet(self, data):
        return self._callSoap_func('getServiceProfile', data)
    def ServiceProfileGets(self, data):
        return self._callSoap_func('listServiceProfile', data)
    def ServiceProfileUpdate(self, data):
        return self._callSoap_func('updateServiceProfile', data)
    def ServiceProfileRemove(self, data):
        return self._callSoap_func('removeServiceProfile', data)
    # endregion

    # region Thin AXL (SQL Queries / Updates)
    # endregion
