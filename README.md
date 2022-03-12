# Cisco-NSO
Cisco NSOSDK have multiple RESTAPIs that we can use to perform certain action using Cisco NSO.
- show_command: method is used to get the show command from the router.
- config_validator: method is used to validate the configuration this is the best feature in NSO to check the configuration before sending to the router. 
- add_device: method is used to add the device in NSO.
- send_command:  method is used to push the configuration on the router.
- sync_from: method used to sync the network devices with NSO.
- device_platform: This method use to get the Device detail including version,serial number,model.

- Examples: 
- from nsosdk import NSOSDK

- nsosdk = NSOSDK('USERNAME','PWD','IP_ADDRESS','8080')
- output = nsosdk.show_command('DEVICE-1','show run int loopback0')
- print(output)

- cmd = '''
- router ospf 234
- network point-to-point
- exit
- '''
- config_val = nsosdk.config_validator(cmd)
- print(config_val)

- add_device = nsosdk.add_device("APIDevice","1.0.1.2","MYDEVICE","telnet","unlocked")
- print(add_device)
