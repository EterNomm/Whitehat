import subprocess
import re
import platform

from .errors import *

class Wifi:
    r"""A class that implements Wifi function
    -----------
    Classmethod :
    - get_all_saved_pw()
    """

    @classmethod
    def get_all_saved_pw(self):
        r"""
        Get all saved passwords on your computer (Only work in Windows OS)
        """

        if platform.uname()[0] == "Windows":
            command_output = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output = True).stdout.decode()
            profile_names = (re.findall("All User Profile     : (.*)\r", command_output))
            wifi_list = []
            
            if len(profile_names) != 0:
                for name in profile_names:
                    wifi_profile = {}
                    profile_info = subprocess.run(["netsh", "wlan", "show", "profile", name], capture_output = True).stdout.decode()
                    if re.search("Security key           : Absent", profile_info):
                        continue
                    else:
                        wifi_profile["ssid"] = name
                        profile_info_pass = subprocess.run(["netsh", "wlan", "show", "profile", name, "key=clear"], capture_output = True).stdout.decode()
                        #    group after the : (which is the password).
                        password = re.search("Key Content            : (.*)\r", profile_info_pass)
                        if password == None:
                            wifi_profile["password"] = None
                        else:
                            wifi_profile["password"] = password[1]
                        wifi_list.append(wifi_profile) 
            
            
            return wifi_list

        else:
            raise UnsupportedOS(supported_os="Windows")
