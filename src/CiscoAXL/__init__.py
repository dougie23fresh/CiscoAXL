import json
import xmltodict
from soap import SOAP


class AXL(SOAP):
    """
    The CUCM AXL class

    https://developer.cisco.com/docs/axl/

    :param host: The Hostname / IP Address of the server
    :type host: String
    :returns: return an AXL object
    :rtype: AXL
    """

    def __init__(self, host, username, password, version=11.5, tls_verify=True, timeout=30):
        # Setup Variables
        self.host = host
        self.version = version
        self.timeout = timeout
        self.attempts = 0
        self.max_retries = 3
        self.backoff_times = [1, 5, 10]
        self.logging = False
        self.url = f'https://{self.host}:8443/axl/'
        super().__init__(self.url, username, password, tls_verify=tls_verify, timeout=timeout)

    def _soapRequest(self, soap_action, data):
        soaprequest = {
            'soap-env:Envelope': {
                '@xmlns:soap-env': 'http://schemas.xmlsoap.org/soap/envelope/',
                'soap-env:Body': {f'ns0:{soap_action}': {'@xmlns:ns0': f'http://www.cisco.com/AXL/API/{self.version}'}},
            }
        }
        soaprequest.get('soap-env:Envelope').get('soap-env:Body').get(f'ns0:{soap_action}').update(data)
        return soaprequest

    def _soapResponse(self, response, soap_action):
        if response['success']:
            result = xmltodict.parse(response['response'].content, xml_attribs=False)
            result = json.loads(json.dumps(result))
            if result.get('soapenv:Envelope').get('soapenv:Body').get('soapenv:Fault'):
                last_exception = result.get('soapenv:Envelope').get('soapenv:Body').get('soapenv:Fault')
                return {'success': False, 'response': last_exception}
            result = result.get('soapenv:Envelope').get('soapenv:Body').get(f'ns:{soap_action}Response')
            result = result.get('return', {}) if result.get('return', {}) is not None else {}
            return {'success': True, 'response': result}
        else:
            return response

    def request(self, soap_action, data):
        data = self._soapRequest(soap_action, data)
        payload = xmltodict.unparse(data)
        headers = {
            'Content_type': 'text/xml; charset=utf-8',
            'SOAPAction': f'"CUCM:DB ver={self.version} {soap_action}"',
        }
        response = self._send_request(self.url, headers=headers, payload=payload, http_method='POST')
        response_data = self._soapResponse(response, soap_action)
        return response_data

    # region Phones

    def add_phone(self, phone_data=None):
        axl_result = self.request('addPhone', phone_data)
        return axl_result

    def get_phone(self, name=None):
        data = {'name': name}
        axl_result = self.request('getPhone', data)
        return axl_result

    def delete_phone(self, name=None):
        data = {'name': name}
        axl_result = self.request('removePhone', data)
        return axl_result

    def apply_phone(self, name=None):
        data = {'name': name}
        axl_result = self.request('applyPhone', data)
        return axl_result

    def list_phone(self, search_criteria_data=None, returned_tags=None):
        returned_tags = {
            'AllowPresentationSharingUsingBfcp': '',
            'aarNeighborhoodName': '',
            'allowCtiControlFlag': '',
            'allowMraMode': '',
            'allowiXApplicableMedia': '',
            'alwaysUsePrimeLine': '',
            'alwaysUsePrimeLineForVoiceMessage': '',
            'authenticationMode': '',
            'authenticationString': '',
            'authenticationUrl': '',
            'automatedAlternateRoutingCssName': '',
            'blockIncomingCallsWhenRoaming': '',
            'builtInBridgeStatus': '',
            'callInfoPrivacyStatus': '',
            'callingSearchSpaceName': '',
            'certificateOperation': '',
            'certificateStatus': '',
            'cgpnTransformationCssName': '',
            'class': '',
            'commonDeviceConfigName': '',
            'commonPhoneConfigName': '',
            'confidentialAccess': '',
            'currentConfig': '',
            'currentProfileName': '',
            'defaultProfileName': '',
            'description': '',
            'deviceMobilityMode': '',
            'devicePoolName': '',
            'deviceTrustMode': '',
            'dialRulesName': '',
            'digestUser': '',
            'directoryUrl': '',
            'dndOption': '',
            'dndRingSetting': '',
            'dndStatus': '',
            'earlyOfferSupportForVoiceCall': '',
            'ecKeySize': '',
            'enableActivationID': '',
            'enableCallRoutingToRdWhenNoneIsActive': '',
            'enableExtensionMobility': '',
            'featureControlPolicy': '',
            'geoLocationFilterName': '',
            'geoLocationName': '',
            'hlogStatus': '',
            'homeNetworkId': '',
            'hotlineDevice': '',
            'idleTimeout': '',
            'idleUrl': '',
            'ignorePresentationIndicators': '',
            'informationUrl': '',
            'isActive': '',
            'isDualMode': '',
            'isProtected': '',
            'joinAcrossLines': '',
            'keyOrder': '',
            'keySize': '',
            'loadInformation': '',
            'locationName': '',
            'loginDuration': '',
            'loginTime': '',
            'loginUserId': '',
            'mediaResourceListName': '',
            'messagesUrl': '',
            'mlppIndicationStatus': '',
            'mobilityUserIdName': '',
            'model': '',
            'mraServiceDomain': '',
            'mtpPreferedCodec': '',
            'mtpRequired': '',
            'name': '',
            'networkHoldMohAudioSourceId': '',
            'networkLocale': '',
            'networkLocation': '',
            'numberOfButtons': '',
            'outboundCallRollover': '',
            'ownerUserName': '',
            'packetCaptureDuration': '',
            'packetCaptureMode': '',
            'phoneServiceDisplay': '',
            'phoneSuite': '',
            'phoneTemplateName': '',
            'preemption': '',
            'presenceGroupName': '',
            'primaryPhoneName': '',
            'product': '',
            'protocol': '',
            'protocolSide': '',
            'proxyServerUrl': '',
            'remoteDevice': '',
            'requireDtmfReception': '',
            'requireOffPremiseLocation': '',
            'requireThirdPartyRegistration': '',
            'rerouteCallingSearchSpaceName': '',
            'retryVideoCallAsAudio': '',
            'rfc2833Disabled': '',
            'ringSettingBusyBlfAudibleAlert': '',
            'ringSettingIdleBlfAudibleAlert': '',
            'roamingDevicePoolName': '',
            'secureAuthenticationUrl': '',
            'secureDirectoryUrl': '',
            'secureIdleUrl': '',
            'secureInformationUrl': '',
            'secureMessageUrl': '',
            'secureServicesUrl': '',
            'securityProfileName': '',
            'sendGeoLocation': '',
            'servicesUrl': '',
            'singleButtonBarge': '',
            'sipProfileName': '',
            'softkeyTemplateName': '',
            'sshUserId': '',
            'subscribeCallingSearchSpaceName': '',
            'traceFlag': '',
            'unattendedPort': '',
            'upgradeFinishTime': '',
            'useDevicePoolCgpnTransformCss': '',
            'useTrustedRelayPoint': '',
            'userHoldMohAudioSourceId': '',
            'userLocale': '',
        }
        data = {'searchCriteria': search_criteria_data, 'returnedTags': returned_tags}
        axl_result = self.request('listPhone', data)
        return axl_result

    def update_phone(self, phone_data=None):
        axl_result = self.request('updatePhone', phone_data)
        return axl_result

    # endregion

    # region CallManagerGroup

    def get_ucm_group(self, name):
        data = {'name': name}
        axl_result = self.request('getCallManagerGroup', data)
        return axl_result

    def update_ucm_group_members(self, name, members):
        data = {'name': name, 'members': members}
        axl_result = self.request('updateCallManagerGroup', data)
        return axl_result

    def add_ucm_group(self, name, members):
        data = {'name': name, 'members': members}
        axl_result = self.request('addCallManagerGroup', data)
        return axl_result

    def remove_ucm_group(self, name):
        data = {'name': name}
        axl_result = self.request('removeCallManagerGroup', data)
        return axl_result

    # endregion

    # region Users

    def get_user(self, userid):
        data = {'userid': userid}
        axl_result = self.request('getUser', data)
        return axl_result

    def list_user(self, search_criteria_data, returned_tags=None):
        returned_tags = {
            "firstName": "",
            "middleName": "",
            "lastName": "",
            "emMaxLoginTime": "",
            "userid": "",
            "mailid": "",
            "department": "",
            "manager": "",
            "userLocale": "",
            "primaryExtension": "",
            "associatedPc": "",
            "enableCti": "",
            "subscribeCallingSearchSpaceName": "",
            "enableMobility": "",
            "enableMobileVoiceAccess": "",
            "maxDeskPickupWaitTime": "",
            "remoteDestinationLimit": "",
            "status": "",
            "enableEmcc": "",
            "patternPrecedence": "",
            "numericUserId": "",
            "mlppPassword": "",
            "homeCluster": "",
            "imAndPresenceEnable": "",
            "serviceProfile": "",
            "directoryUri": "",
            "telephoneNumber": "",
            "title": "",
            "mobileNumber": "",
            "homeNumber": "",
            "pagerNumber": "",
            "calendarPresence": "",
            "userIdentity": "",
        }
        data = {'searchCriteria': search_criteria_data, 'returnedTags': returned_tags}
        axl_result = self.request('listUser', data)
        return axl_result

    def update_user(self, user_data):
        axl_result = self.request('updateUser', user_data)
        return axl_result

    # endregion

    # region SQL

    def sql_get_device_pkid(self, device):
        sql_query = f"select pkid from device where name = '{device}'"
        axl_result = self.request('executeSQLQuery', {'sql': sql_query})
        return axl_result

    def sql_get_user_group_pkid(self, group_name):
        sql_query = f"select pkid from dirgroup where name = '{group_name}'"
        axl_result = self.request('executeSQLQuery', {'sql': sql_query})
        return axl_result

    def sql_get_enduser_pkid(self, userid):
        sql_query = f"select pkid from enduser where userid = '{userid}'"
        axl_result = self.request('executeSQLQuery', {'sql': sql_query})
        return axl_result

    def sql_associate_user_to_group(self, userid, group_name):
        user_group_pkid = self.sql_get_user_group_pkid(group_name)
        enduser_pkid = self.sql_get_enduser_pkid(userid)
        axl_result = {'success': False, 'message': '', 'response': ''}
        if user_group_pkid is not None and enduser_pkid is not None:
            sql_query = (
                "insert into enduserdirgroupmap (fkenduser, fkdirgroup)"
                f"values " "('{enduser_pkid}', '{user_group_pkid}')"
            )
            axl_result = self.request('executeSQLQuery', {'sql': sql_query})
        return axl_result

    def sql_remove_user_from_group(self, userid, group_name):
        pass

    def sql_query(self, sql_query):
        axl_result = self.request('executeSQLQuery', {'sql': sql_query})
        return axl_result

    # region Lines

    def get_line(self, dn, partition):
        # getLine
        data = {'dn': dn, 'partition': partition}
        axl_result = self.request('getLine', data)
        return axl_result

    def add_line(self, line_data):
        # addLine
        axl_result = self.request('addLine', line_data)
        return axl_result

    def update_line(self, line_data):
        # updateLine
        axl_result = self.request('updateLine', line_data)
        return axl_result

    def apply_line(self, dn, partition=None):
        # applyLine
        data = {'dn': dn, 'partition': partition}
        axl_result = self.request('applyLine', data)
        return axl_result

    # endregion

    # region Partitions

    def add_partition(self, name, description):
        # addRoutePartition
        pass

    def get_partition(self, name, returned_tags=None):
        # getRoutePartition
        pass

    def remove_partition(self, name):
        # removeRoutePartition
        pass

    # endregion

    # region Calling Search Space

    def add_css(self, name, description, partition_list):
        # addCss
        pass

    def get_css(self, name):
        pass

    def remove_css(self, name):
        pass

    def update_css(self, css_name, description, partition_list):
        pass

    # endregion

    # region Route Group

    def add_route_group(self, name, distribution_algorithm, device_list):
        # addRouteGroup
        pass

    def get_route_group(self, name):
        pass

    def remove_route_group(self, name):
        pass

    def update_route_group(self, name):
        pass

    # endregion

    # region Route List

    def add_route_list(self, name, description, cm_group, enabled, roan, members, ddi=None):
        # addRouteList
        pass

    def get_route_list(self, name):
        pass

    def remove_route_list(self, name):
        pass

    # endregion

    # region Route Pattern

    def add_route_pattern(self, pattern, partition, route_list, network_location, outside_dialtone):
        # addRoutePattern
        pass

    def get_route_pattern(self, pattern, partition):
        pass

    def remove_route_pattern(self, pattern, partition):
        pass

    def update_route_pattern(self, name):
        pass

    # endregion

    # region Translation Pattern

    def add_translation_pattern(self, pattern, partition, route_list, network_location, outside_dialtone):
        # addRoutePattern
        pass

    def get_translation_pattern(self, pattern, partition):
        pass

    def remove_translation_pattern(self, pattern, partition):
        pass

    def update_translation_pattern(self, name):
        pass

    # endregion

    # region Device Pool

    def get_device_pool(self, name):
        # getDevicePool
        pass

    # endregion

    # region Device Security Profile

    def get_phone_security_profile(self, name):
        pass

    # endregion

    # region SIP Trunk Security Profile

    def get_sip_trunk_security_profile(self, name):
        pass

    # endregion

    # region Reset / Restart Devices

    def do_reset_restart_device(self, device, is_hard_reset, is_mgcp):
        reset_data = {'deviceName': device, 'isHardReset': is_hard_reset, 'isMGCP': is_mgcp}
        axl_result = self.request('doDeviceReset', reset_data)
        return axl_result

    def reset_device(self, device):
        result = self.do_reset_restart_device(device, True, False)
        return result

    def restart_device(self, device):
        result = self.do_reset_restart_device(device, False, False)
        return result

    def reset_mgcp(self, device):
        result = self.do_reset_restart_device(device, True, True)
        return result

    def restart_mgcp(self, device):
        result = self.do_reset_restart_device(device, False, True)
        return result

    # endregion

    # region Service Parameters

    def sql_update_service_parameter(self, name, value):
        pass
        # query = "update processconfig set paramvalue = '{0}' where paramname = '{1}'".format(value, name)
        # axl_result = self.request('executeSQLQuery', {'sql': sql_query})
        # return axl_result

    def sql_get_service_parameter(self, name):
        sql_query = f"select * from processconfig where paramname = '{name}'"
        axl_result = self.request('executeSQLQuery', {'sql': sql_query})
        return axl_result

    # endregion

    #  region Device Association
    def sql_associate_device_to_user(self, device, userid, association_type='1'):
        device_pkid = self.sql_get_device_pkid(device)
        enduser_pkid = self.sql_get_enduser_pkid(userid)
        axl_result = {'success': False, 'message': '', 'response': ''}
        if device_pkid is not None and enduser_pkid is not None:
            sql_query = (
                f"insert into enduserdevicemap (fkenduser, fkdevice, defaultprofile, tkuserassociation) "
                f"values ('{enduser_pkid}','{device_pkid}','f','{association_type}')"
            )
            axl_result = self.request('executeSQLQuery', {'sql': sql_query})
        return axl_result

    # endregion
