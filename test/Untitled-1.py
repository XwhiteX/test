#! /usr/bin/env python
# -*- coding: utf-8 -*-

from wayang_core.request_handler import RequestHandler
import json

# 服务器下发 - 执行SDK API命令 e.g. joinChannel
CMD_SDK = 1

# 服务器下发 - 上报指定数据 e.g. reportCPU
CMD_APP = 2

# 服务器下发 - 执行其他动作 (非SDK API) e.g. hideView
CMD_OTHER = 3

# App 上报 - SDK回调事件的数据  e.g. didJoinChannel
CMD_CALLBACK = 4

# MediaServerSdk response
CMD_RESPONSE = 5


class WayangRobotMediaServerSdk(object):

    def __init__(self):
        self.requester = RequestHandler()
        self.deviceQr = None
        self.server = None

    def closeConnection(self):
        self.requester.close_connection()

    def convertToBool(self, value):
        if str.lower(str(value)) == 'false':
            return False
        elif str.lower(str(value)) == 'true':
            return True
        else:
            return None

# ===================MediaServerSdk APIs======================

    def CreateMediaServer(self, appId):
        cmd = "CreateMediaServer"
        info_dict = {
            'appId': appId
        }
        return self.requester.send_request(
            self.deviceQr, self.server, cmd, info_dict)

    def StartService(self):
        cmd = "StartService"
        return self.requester.send_request(self.deviceQr, self.server, cmd)

    def StopService(self):
        cmd = "StopService"
        return self.requester.send_request(self.deviceQr, self.server, cmd)

    def Release(self):
        cmd = "Release"
        return self.requester.send_request(self.deviceQr, self.server, cmd)

    def JoinChannel(
            self,
            channel,
            uid,
            chanelKey=None,
            idleLimitSec=None,
            channelProfile=None,
            appliteDir=None,
            recordFileRootDir=None,
            cfgFilePath=None,
            isVideoOnly=None,
            isAudioOnly=None,
            isMixingEnabled=None,
            audioIndicationInterval=None,
            mixResolution=None,
            mixedVideoAudio=None,
            secret=None,
            decryptionMode=None,
            lowUdpPort=None,
            highUdpPort=None,
            captureInterval=None,
            getAudioFrame=None,
            getVideoFrame=None,
            streamType=None,
            withDownStream=None,
            lowComputation=None,
            triggerMode=None,
            upstreamResolution=None):
        cmd = "JoinChannel"
        meida_server_key = []
        config_key = []
        info_key = []
        info_dict = {
            "channelKey": chanelKey,
            "channel": channel,
            "uid": uid,
            "config": {
                "idleLimitSec": idleLimitSec,
                "channelProfile": channelProfile,
                "appliteDir": appliteDir,
                "recordFileRootDir": recordFileRootDir,
                "cfgFilePath": cfgFilePath,
                "isVideoOnly": isVideoOnly,
                "isAudioOnly": isAudioOnly,
                "isMixingEnabled": isMixingEnabled,
                "audioIndicationInterval": audioIndicationInterval,
                "mixResolution": mixResolution,
                "mixedVideoAudio": mixedVideoAudio,
                "secret": secret,
                "decryptionMode": decryptionMode,
                "lowUdpPort": lowUdpPort,
                "highUdpPort": highUdpPort,
                "captureInterval": captureInterval,
                "getAudioFrame": getAudioFrame,
                "getVideoFrame": getVideoFrame,
                "streamType": streamType,
                "withDownStream": withDownStream,
                "lowComputation": lowComputation,
                "triggerMode": triggerMode,
                "upstreamResolution": upstreamResolution
            }
        }
        # for key in info_dict["config"]:
        #     if info_dict["config"][key] is None:
        #         meida_server_key.append(key)
        # for key in info_dict["config"]:
        #     info_dict["config"].pop(key)

        for key in info_dict["config"]:
            if info_dict["config"][key] is None:
                config_key.append(key)
        for key in config_key:
            info_dict["config"].pop(key)
        if len(info_dict["config"]) == 0:
            info_dict.pop("config")
        for key in info_dict:
            if info_dict[key] is None:
                info_key.append(key)
        for key in info_key:
            info_dict.pop(key)

        return self.requester.send_request(
            self.deviceQr, self.server, cmd, info_dict)

    def LeaveChannel(self):
        cmd = "LeaveChannel"
        return self.requester.send_request(self.deviceQr, self.server, cmd)

    def SetVideoMixingLayout(
            self,
            canvasWidth,
            canvasHeight,
            backgroundColor,
            regionCount,
            regions,
            uid,
            x,
            y,
            width,
            height,
            alpha,
            renderMode,
            appData,
            appDataLength):
        cmd = "SetVideoMixingLayout"
        keys = []
        info_dict = {
            "canvasWidth": canvasWidth,
            "canvasHeight": canvasHeight,
            "backgroundColor": backgroundColor,
            "regionCount": regionCount,
            "regions": regions,
            "uid": uid,
            "x": x,
            "y": y,
            "width": width,
            "height": height,
            "alpha": alpha,
            "renderMode": renderMode,
            "appData": appData,
            "appDataLength": appDataLength
        }
        for key in info_dict:
            if info_dict[key] is None:
                keys.append(key)
        for key in keys:
            info_dict.pop(key)
        return self.requester.send_request(
            self.deviceQr, self.server, cmd, info_dict)

    def GetProperties(self):
        cmd = "GetProperties"
        return self.requester.send_request(self.deviceQr, self.server, cmd)

    def SetUserBackground(self, uid, imagePath):
        cmd = "SetUserBackground"
        info_dict = {
            "uid": uid,
            "imagePath": imagePath
        }
        return self.requester.send_request(
            self.deviceQr, self.server, cmd, info_dict)

    def SetLogLevel(self, loglevel):
        cmd = "SetLogLevel"
        info_dict = {
            "loglevel": loglevel
        }
        return self.requester.send_request(
            self.deviceQr, self.server, cmd, info_dict)

    def StoppedOnError(self):
        cmd = "StoppedOnError"
        return self.requester.send_request(self.deviceQr, self.server, cmd)

    def OpenStreamingUrl(self, path):
        cmd = "OpenStreamingUrl"
        info_dict = {
            "path": path
        }
        return self.requester.send_request(
            self.deviceQr, self.server, cmd, info_dict)

    def StartStreaming(self):
        cmd = "StartStreaming"
        return self.requester.send_request(self.deviceQr, self.server, cmd)

    def StopStreaming(self):
        cmd = "StopStreaming"
        return self.requester.send_request(self.deviceQr, self.server, cmd)

    def AppendStreamingUrl(self, path):
        cmd = "AppendStreamingUrl"
        info_dict = {
            "path": path
        }
        return self.requester.send_request(
            self.deviceQr, self.server, cmd, info_dict)

    def RemoveStreamUrl(self, path):
        cmd = "RemoveStreamUrl"
        info_dict = {
            "path": path
        }
        return self.requester.send_request(
            self.deviceQr, self.server, cmd, info_dict)

    def GetStreamingUrlLength(self):
        cmd = "GetStreamingUrlLength"
        return self.requester.send_request(self.deviceQr, self.server, cmd)

    def ResumeStreaming(self):
        cmd = "ResumeStreaming"
        return self.requester.send_request(self.deviceQr, self.server, cmd)

    def PauseStreaming(self):
        cmd = "PauseStreaming"
        return self.requester.send_request(self.deviceQr, self.server, cmd)

    def SeekStreamingPosition(self, toms):  # toms(milliseconds)
        cmd = "SeekStreamingPosition"
        info_dict = {
            "toms": toms
        }
        return self.requester.send_request(
            self.deviceQr, self.server, cmd, info_dict)

    def GetStreamingPosition(self):
        cmd = "GetStreamingPosition"
        return self.requester.send_request(self.deviceQr, self.server, cmd)

    def GetDuration(self):
        cmd = "GetDuration"
        return self.requester.send_request(self.deviceQr, self.server, cmd)

# TODO
#  api not implemented
# SetAudioEncoderConfigurationHandler
# SetVideoEncoderConfigurationHandler

    def EnableServerSEI(self, sei):  # sei(sei mode number)
        cmd = "EnableServerSEI"
        info_dict = {
            "sei": sei
        }
        return self.requester.send_request(
            self.deviceQr, self.server, cmd, info_dict)

# ========CallBack=============
# TODO
# audioFrameReceivedCallback
#     def audioFrameReceived(self):
#         cmd = "audioFrameReceived"
# return self.requester.send_request(self.deviceQr, self.server, cmd,
# CMD_CALLBACK)

    def OnError(self):
        cmd = "OnError"
        return self.requester.wait_for_response_extra(
            self.deviceQr, self.server, cmd, CMD_CALLBACK)

    def OnWarning(self):
        cmd = "OnWarning"
        return self.requester.wait_for_response_extra(
            self.deviceQr, self.server, cmd, CMD_CALLBACK)

    def OnJoinChannelSuccess(self):
        cmd = "OnJoinChannelSuccess"
        return self.requester.wait_for_response_extra(
            self.deviceQr, self.server, cmd, CMD_CALLBACK)

    def OnLeaveChannel(self):
        cmd = "OnLeaveChannel"
        return self.requester.wait_for_response_extra(
            self.deviceQr, self.server, cmd, CMD_CALLBACK)

    def OnUserJoined(self):
        cmd = "OnUserJoined"
        return self.requester.wait_for_response_extra(
            self.deviceQr, self.server, cmd, CMD_CALLBACK)

    def OnUserOffline(self):
        cmd = "OnUserOffline"
        return self.requester.wait_for_response_extra(
            self.deviceQr, self.server, cmd, CMD_CALLBACK)

    def videoFrameReceived(self):
        cmd = "videoFrameReceived"
        return self.requester.wait_for_response_extra(
            self.deviceQr, self.server, cmd, CMD_CALLBACK)

    def OnActiveSpeaker(self):
        cmd = "OnActiveSpeaker"
        return self.requester.wait_for_response_extra(
            self.deviceQr, self.server, cmd, CMD_CALLBACK)

    def OnAudioVolumeIndication(self):
        cmd = "OnAudioVolumeIndication"
        return self.requester.wait_for_response_extra(
            self.deviceQr, self.server, cmd, CMD_CALLBACK)

    def OnFirstRemoteVideoDecoded(self):
        cmd = "OnFirstRemoteVideoDecoded"
        return self.requester.wait_for_response_extra(
            self.deviceQr, self.server, cmd, CMD_CALLBACK)

    def OnFirstRemoteAudioFrame(self):
        cmd = "OnFirstRemoteAudioFrame"
        return self.requester.wait_for_response_extra(
            self.deviceQr, self.server, cmd, CMD_CALLBACK)

    def OnReceivingStreamStatusChanged(self):
        cmd = "OnReceivingStreamStatusChanged"
        return self.requester.wait_for_response_extra(
            self.deviceQr, self.server, cmd, CMD_CALLBACK)

    def OnConnectionLost(self):
        cmd = "OnConnectionLost"
        return self.requester.wait_for_response_extra(
            self.deviceQr, self.server, cmd, CMD_CALLBACK)

    def OnConnectionInterrupted(self):
        cmd = "OnConnectionInterrupted"
        return self.requester.wait_for_response_extra(
            self.deviceQr, self.server, cmd, CMD_CALLBACK)

    def OnMediaStreamingStateChanged(self):
        cmd = "OnMediaStreamingStateChanged"
        return self.requester.wait_for_response_extra(
            self.deviceQr, self.server, cmd, CMD_CALLBACK)

    def OnMediaStreamingMeta(self):
        cmd = "OnMediaStreamingMeta"
        return self.requester.wait_for_response_extra(
            self.deviceQr, self.server, cmd, CMD_CALLBACK)

    def OnMediaStreamingStats(self):
        cmd = "OnMediaStreamingStats"
        return self.requester.wait_for_response_extra(
            self.deviceQr, self.server, cmd, CMD_CALLBACK)
