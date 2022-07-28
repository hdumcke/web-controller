import json
import time


class Controller:

    def __init__(self, message_rate):
        self.message_rate = message_rate
        self.params = {}
        self.params['pupper'] = {}
        self.params['dance'] = {}
        self.params['walk'] = {}
        self.msg = {}
        self._setDefaults(self.params['dance'], self.msg)
        self._setDefaults(self.params['walk'], self.msg)

    def _setDefaults(self, params, msg):
        msg["ly"] = 0
        msg["lx"] = 0
        msg["rx"] = 0
        msg["ry"] = 0
        msg["L2"] = 0
        msg["R2"] = 0
        msg["R1"] = 0
        if "L1" not in msg.keys():
            msg["L1"] = 0
        msg["dpady"] = 0
        msg["dpadx"] = 0
        msg["x"] = 0
        msg["square"] = 0
        msg["circle"] = 0
        if "triangle" not in msg.keys():
            msg["triangle"] = 0
        msg["message_rate"] = self.message_rate
        params['yaw'] = 0.
        params['pitch'] = 0.
        params['roll'] = 0.
        params['height'] = 0.
        params['vel_x'] = 0
        params['vel_y'] = 0

    def setParams(self, gait, command, param):
        if command == 'status':
            return
        self.params[gait][command] = float(param)
        return

    def getParams(self, gait, command, param):
        if command == 'status':
            if param == 'start':
                if gait == 'walk':
                    self.msg["R1"] = 1
                    self.msg["R2"] = 1
                if gait == 'dance':
                    self.msg["circle"] = 1
                if gait == 'pupper':
                    self.msg["L1"] = 1
                    self.msg["triangle"] = 0
            else:
                if gait == 'pupper':
                    if param == 'stop':
                        # force Deactivating Robot
                        self.msg["L1"] = 0
                        self.msg["triangle"] = 0
                        time.sleep(2 / self.message_rate)
                        self.msg["L1"] = 1
                        time.sleep(2 / self.message_rate)
                        self.msg["L1"] = 0
                    if param == 'shutdown':
                        self.msg["triangle"] = 1
                if gait == 'dance':
                    self._setDefaults(self.params[gait], self.msg)
                    time.sleep(2 / self.message_rate)
                    self.msg["circle"] = 1
                    time.sleep(2 / self.message_rate)
                    self._setDefaults(self.params[gait], self.msg)
                if gait == 'walk':
                    self._setDefaults(self.params[gait], self.msg)
                    time.sleep(2 / self.message_rate)
                    self.msg["R1"] = 1
                    time.sleep(2 / self.message_rate)
                    self._setDefaults(self.params[gait], self.msg)
            return json.dumps(self.params[gait])
        else:
            # setParams is called async and this command has not been updated
            self.params[gait][command] = float(param)
            self.updateMsg(gait)
        return json.dumps(self.params[gait])

    def getMsg(self):
        return self.msg

    def updateMsg(self, gait):
        if gait == 'dance':
            self.msg["rx"] = self.params[gait]['yaw']/100
            self.msg["ry"] = self.params[gait]['pitch']/100
            self.msg["dpady"] = self.params[gait]['height']/100
            self.msg["dpadx"] = self.params[gait]['roll']/100
        else:
            self.msg["lx"] = self.params[gait]['vel_x']/100
            self.msg["ly"] = self.params[gait]['vel_y']/100

        return self.msg
