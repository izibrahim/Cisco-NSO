from nsosdk import NSOSDK
#############################################################################################################################


nsosdk = NSOSDK('USERNAME','PWD','IP_ADDRESS','8080')
output = nsosdk.show_command('DEVICE-1','show run int loopback0')
print(output)
