import requests
import re
import json

class NSOSDK:
    def __init__(self,username,password,ip_address,port):
        print("NSO SDK")
        self.username = username
        self.password = password
        self.ip_address = ip_address
        self.port = port

    def show_command(self,hostname,cmd):
        """ This method is use to get the show command from Cisco XR NED """
        show_search = re.search("^sh.+|^Sh.+|^SH.+",cmd)
        if show_search:
            baseurl = f'http://{self.username}:{self.password}@{self.ip_address}:{self.port}/api/operational/devices/device/{hostname}/live-status/cisco-ios-xr-stats:exec/_operations/any/'
            print(baseurl)
            payload=f"    <input>\r\n       <args>{cmd}</args>\r\n    </input>"
            print(payload)
            headers = {
                    'Content-Type': 'application/vnd.yang.data+xml'
                    }
            response = requests.request("POST", baseurl, headers=headers, data=payload)
            print(response)
            #response = re.search("^<.+|^</.+|&#13;",response.text)
            return response.text.replace("&#13;",'').replace("</output>",'').replace("<output>",'').replace("<result>",'').replace("/<result>",'')
            #return response.group(0)
        else:
            return "Command should start with Show"

    def sync_from(self,hostname):
        """This method is use to do the sync from the device"""
        baseurl = f'http://{self.username}:{self.password}@{self.ip_address}:{self.port}/api/operations/devices/device/{hostname}/sync-from'
        response = requests.request("POST", baseurl)
        print(response.text)
        return self
    def services(self):
        """list of services"""
        baseurl = f'http://{self.username}:{self.password}@{self.ip_address}:{self.port}/api/operational/services'
        response = requests.request("GET", baseurl)
        return response.text
    def device_group(self,j=None):
        """ This method is use to get the device group from the NSO to get the result in Json parse JSON inside the method"""
        if j is not None:
            headers = {
                'Content-Type': 'application/json',
                'Accept': 'application/vnd.yang.collection+json, application/vnd.yang.data+json',}
            baseurl = f'http://{self.username}:{self.password}@{self.ip_address}:{self.port}/api/operational/devices/device-group'
            response = requests.request("GET", baseurl,headers=headers)
            res = json.loads(response.text)
            return res
        else:
            baseurl = f'http://{self.username}:{self.password}@{self.ip_address}:{self.port}/api/operational/devices/device-group'
            response = requests.request("GET", baseurl)
            return response.text

    def device_platform(self,hostname):
        """This method use to get the Device detail including version,serial number,model"""
        baseurl = f'http://{self.username}:{self.password}@{self.ip_address}:{self.port}/api/operational/devices/device/{hostname}/platform'
        response = requests.request("GET", baseurl)
        return response.text
    def template(self):
        """This Method use to get the NSO templates"""
        baseurl = f'http://{self.username}:{self.password}@{self.ip_address}:{self.port}/api/config/devices/template'
        response = requests.request("GET", baseurl)
        return response.text
    def configpush(self,configparse,hostname):
        """This method is use the push the xml format to Cisco XR  """
        payload=f"{configparse}"
        print(payload)
        headers = {
             'Content-Type': 'application/vnd.yang.data+xml'
            }
        baseurl = f'http://{self.username}:{self.password}@{self.ip_address}:{self.port}/api/config/devices/device/{hostname}/config'
        response = requests.request("PATCH", baseurl, headers=headers, data=payload)
        return response.text
    def send_command(self,hostname,cmd):
        """ This method is use to push the plain SSH to using NSO to IOS XR devices
        cmd = '''
            conf t
            interface loopback77889
            description testing apis
            commit
            '''
            output1 = nsosdk.send_command('R1',cmd)
            print(output1) """
        baseurl = f'http://{self.username}:{self.password}@{self.ip_address}:{self.port}/api/operational/devices/device/{hostname}/live-status/cisco-ios-xr-stats:exec/_operations/any/'
        #print(baseurl)
        payload=f"    <input>\r\n       <args>{cmd}</args>\r\n    </input>"
        headers = {
                    'Content-Type': 'application/vnd.yang.data+xml'
                 }
        print(payload)
        response = requests.request("POST", baseurl, headers=headers, data=payload)
        #print(response)
        #print(response.text)
        return response.text
    def device_module(self):
        """Get the device model """
        baseurl = f'http://{self.username}:{self.password}@{self.ip_address}:{self.port}/api/operational/devices/device-module'
        response = requests.request("GET", baseurl)
        return response.text
    def add_device(self,hostname,ip,group,protocol,unlocked):
            payload=f"<device>\r\n <name>{hostname}</name>\r\n <address>{ip}</address>\r\n <authgroup>{group}</authgroup>\r\n <device-type>\r\n   <cli>\r\n     <ned-id>tailf-ned-cisco-ios-id:cisco-ios</ned-id>\r\n     <protocol>{protocol}</protocol>\r\n   </cli>\r\n </device-type>\r\n <state>\r\n   <admin-state>{unlocked}</admin-state>\r\n </state>\r\n</device>"
            print(payload)
            headers = {
                    'Content-Type': 'application/vnd.yang.data+xml'}
            baseurl = f'http://{self.username}:{self.password}@{self.ip_address}:{self.port}/api/config/devices'
            response = requests.request("POST", baseurl,headers=headers, data=payload)
            print(response.text)
            print(response)
    def config_validator(self,cmd):
            payload=f"<input><ned_id>cisco-ios-xr</ned_id><commands>{cmd}</commands></input>"
            print(payload)
            headers = {
                    'Content-Type': 'application/vnd.yang.data+xml'}
            baseurl = f'http://{self.username}:{self.password}@{self.ip_address}:{self.port}/api/running/commands/_operations/validateConfiguration'
            response = requests.request("POST", baseurl,headers=headers, data=payload)
            print(response.text)
            print(response)
