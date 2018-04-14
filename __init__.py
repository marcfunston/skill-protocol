# Copyright 2017, Mycroft AI Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


# author Marc Funston
# date 4/13/2018

from os.path import dirname, join
import subprocess

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from random import choice


class ProtocolSkill(MycroftSkill):
    def __init__(self):
        super(ProtocolSkill, self).__init__(name="ProtocolSkill")

    @intent_handler(IntentBuilder("AlphaIntent").require("Protocol").require("Alpha"))
    def handle_alpha_intent(self, message):
        self.speak_dialog("protocol.alpha")
        try:
            subprocess.call("/home/m/Desktop/mycroft-core/start-mycroft.sh\ all", shell=True)
        finally:
            self.speak_dialog("protocol.error")

        
    @intent_handler(IntentBuilder("GammaIntent").require("Protocol").require("Gamma"))
    def handle_gamma_intent(self, message):
        self.speak_dialog("protocol.gamma")
        try:
            subprocess.call("/home/m/Desktop/mycroft-core/start-mycroft.sh\ debug\ &", shell=True)
        finally:
            self.speak_dialog("protocol.error")


    @intent_handler(IntentBuilder("OmegaIntent").require("Protocol").require("Omega"))
    def handle_omega_intent(self, message):
        self.speak_dialog("protocol.omega")
        try:
            subprocess.call("/home/m/Desktop/mycroft-core/stop-mycroft.sh", shell=True)
        finally:
            self.speak_dialog("protocol.error")

         

    def stop(self):
        pass

def create_skill():
    return ProtocolSkill()
