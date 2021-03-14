from FreeTAKServer.model.FTSModel.fts_protocol_object import FTSProtocolObject
#######################################################
#
# detail.py
# Python implementation of the Class detail
# Generated by Enterprise Architect
# Created on(FTSProtocolObject): 11-Feb-2020 11:08:07 AM
# Original author: Corvo
#
#######################################################
from FreeTAKServer.model.FTSModel.Takv import Takv
from FreeTAKServer.model.FTSModel.Uid import Uid
from FreeTAKServer.model.FTSModel.Precisionlocation import Precisionlocation
from FreeTAKServer.model.FTSModel._Group import _Group
from FreeTAKServer.model.FTSModel.Status import Status
from FreeTAKServer.model.FTSModel.Track import Track
from FreeTAKServer.model.FTSModel.Marti import Marti
from FreeTAKServer.model.FTSModel.Link import Link
from .Contact import Contact
from .Emergency import Emergency
from FreeTAKServer.model.FTSModel.Chat import Chat
from FreeTAKServer.model.FTSModel.Remarks import Remarks
from FreeTAKServer.model.FTSModel.Serverdestination import _Serverdestination as Serverdestination
from .Color import Color
from FreeTAKServer.model.FTSModel.Usericon import Usericon
from .Archive import Archive
from FreeTAKServer.model.FTSModel.Summary import Summary
from FreeTAKServer.model.FTSModel.Mission import Mission

class Detail(FTSProtocolObject):
    """An optional element used to hold CoT sub-schema. empty element
    """
    def __init__(self):
        pass

    @staticmethod
    def Connection():
        detail = Detail()
        detail.takv = Takv.connection()
        detail.contact = Contact.connection()
        detail.uid = Uid.connection()
        detail.precisionlocation = Precisionlocation.connection()
        detail._group = _Group.connection()
        detail.status = Status.connection()
        detail.track = Track.connection()
        detail.remarks = Remarks.connection()
        return detail

    @staticmethod
    def GeoChat():
        detail = Detail()
        detail._chat = Chat.geochat()
        detail.link = Link.geochat()
        detail.remarks = Remarks.geochat()
        detail._serverdestination = Serverdestination.geochat()
        detail.marti = Marti.drop_point()
        return detail

    @staticmethod
    def Ping():
        detail = Detail()
        detail.setuid(None)
        return detail

    @staticmethod
    def FederatedCoT():
        detail = Detail()
        detail.remarks = Remarks.FederatedCoT()
        detail.status = Status.FederatedCoT()
        return detail

    @staticmethod
    def Other():
        detail = Detail()
        detail.marti = Marti.other()
        return detail

    @staticmethod
    def emergencyOn():
        detail = Detail()
        detail.link = Link.emergency_on()
        detail.contact = Contact.emergency_on()
        detail.emergency = Emergency.emergency_on()
        return detail

    @staticmethod
    def emergencyOff():
        detail = Detail()
        detail.emergency = Emergency.emergency_off()
        return detail

    @staticmethod
    def dropPoint():
        detail = Detail()
        detail.archive = Archive.drop_point()
        detail.status = Status.drop_point()
        detail.usericon = Usericon.drop_point()
        detail.link = Link.drop_point()
        detail.color = Color.drop_point()
        detail.precisionlocation = Precisionlocation.drop_point()
        detail.contact = Contact.drop_point()
        detail.remarks = Remarks.drop_point()
        detail.marti = Marti.drop_point()
        detail.summary = Summary.drop_point()
        return detail

    @staticmethod
    def disconnect():
        detail = Detail()
        detail.link = Link.disconnect()
        return detail

    @staticmethod
    def UserUpdate():
        detail = Detail()
        detail._group = _Group.UserUpdate()
        detail.status = Status.UserUpdate()
        detail.takv = Takv.UserUpdate()
        detail.track = Track.UserUpdate()
        detail.contact = Contact.UserUpdate()
        detail.uid = Uid.UserUpdate()
        detail.precisionlocation = Precisionlocation.UserUpdate()
        return detail

    @staticmethod
    def SimpleCoT():
        detail = Detail()
        detail.contact = Contact.SimpleCoT()
        return detail

    @staticmethod
    def Presence():
        detail = Detail()
        detail.contact = Contact.Presence()
        detail._group = _Group.Presence()
        return detail

    @staticmethod
    def ExcheckUpdate():
        detail = Detail()
        detail.mission = Mission.ExcheckUpdate()
        return detail

    def setarchive(self, archive):
        self.archive = archive

    def getarchive(self):
        return self.archive

    def setsummary(self, summary):
        self.summary = summary

    def getsummary(self):
        return self.summary

    def setremarks(self, remarks):
        self.remarks = remarks

    def getremarks(self):
        return self.remarks

    def setlink(self, link):
        self.link = link

    def getlink(self):
        return self.link

    def setstatus(self, status):
        self.status = status

    def getstatus(self):
        return self.status

    def setusericon(self, usericon):
        self.usericon = usericon

    def getusericon(self):
        return self.usericon

    def setcolor(self, color):
        self.color = color

    def getcolor(self):
        return self.color

    def setcontact(self, contact):
        self.contact = contact

    def getcontact(self):
        return self.contact

    def sethierarchy(self, hierarchy):
        self.hierarchy = hierarchy

    def gethierarchy(self):
        return self.hierarchy

    def setuid(self, uid):
        self.uid = uid

    def getuid(self):
        return self.uid

    def settakv(self, takv):
        self.takv = takv

    def gettakv(self):
        return self.takv

    def set__group(self, group):
        self._group = group

    def get__group(self):
        return self._group

    def set_group(self, group):
        self._group = group

    def get_group(self):
        return self._group

    def setprecisionlocation(self, Precisionlocation):
        self.precisionlocation = Precisionlocation

    def getprecisionlocation(self):
        return self.precisionlocation

    def settrack(self, track):
        self.track = track

    def gettrack(self):
        return self.track

    def setmarti(self, marti):
        self.marti = marti

    def getmarti(self):
        return self.marti

    def setemergency(self, emergency):
        self.emergency = emergency

    def getemergency(self):
        return self.emergency

    def set_chat(self, chat):
        self._chat = chat

    def get_chat(self):
        return self._chat

    def set__chat(self, chat):
        self._chat = chat

    def get__chat(self):
        return self._chat

    def set_serverdestination(self, serverdestination):
        self._serverdestination = serverdestination

    def get_serverdestination(self):
        return self._serverdestination

    def set__serverdestination(self, serverdestination):
        self._serverdestination = serverdestination

    def get__serverdestination(self):
        return self._serverdestination



