from scapy.all import *
from modules._module import Module
from utils.custom_print import print_info
from utils.check_root import is_root
from utils.monitor import Sniffing
from utildata.dataset_options import Option


class HomeModule(Module):

    def __init__(self):
        information = {"Name": "Wifi Sniffing",
                       "Description": "Discover Access Points",
                       "privileges": "root",
                       "Author": "@josueencinar"}

        # -----------name-----default_value--description--required?
        options = {"iface": Option.create(name="iface", required=True),
                   "channel": Option.create(name="channel")}

        self.ap_dict = {}
        self.station_dict = {}
        self.F_bssids = []
        # Constructor of the parent class
        super(HomeModule, self).__init__(information, options)

    # This module must be always implemented, it is called by the run option
    def run(self):
        if not  is_root:
            return
        print_info("Use CTRL^C to end this task")
        sn = Sniffing(iface=self.args["iface"], channel=self.args["channel"], show_stations=False)
        sn.start_sniffing()