import json
from twisted.internet import error, defer
import treq
import rg_lib
import api_core


async def Req(rpc_no, method, params, timeout):
    tbl = {'id': 1,
           'method': method,
           'params': params}
    try:
        url = await api_core.SysCfg.GetGwApiUrl(rpc_no)
        if url:
            resp_defer = await treq.post(url, data=json.dumps(tbl).encode('utf-8'), timeout=timeout)
            res = await resp_defer.json()
            if res['error']:
                raise rg_lib.RGError(res['error'])
            else:
                return res['result']
        else:
            raise ValueError('Invalid Url')
    except error.TimeoutError:
        raise rg_lib.RGError(rg_lib.ErrorType.Timeout())
    except defer.CancelledError:
        raise rg_lib.RGError(rg_lib.ErrorType.Timeout())


class XY:
    @classmethod
    async def Req(cls, method, params, timeout):
        return await Req('api/xy', method, params, timeout)

    @classmethod
    async def GetModules(cls):
        return await cls.Req('GetModules',
                             [{}], 10)

    @classmethod
    async def GetModule(cls, moduleid):
        return await cls.Req('GetModule',
                             [{'moduleid': moduleid}], 10)

    @classmethod
    async def ProbeDevice(cls, moduleid):
        return await cls.Req('ProbeDevice',
                             [{
                                 "moduleid": moduleid,
                             }], 600)

    @classmethod
    async def GetSwitchStatus(cls, moduleid, nid):
        return await cls.Req('GetSwitchStatus',
                             [{
                                 "moduleid": moduleid,
                                 "nid": nid
                               }], 10)

    @classmethod
    async def SetSwitchStatus(cls, moduleid, nid, on_off):
        return await cls.Req('SetSwitchStatus',
                             [{
                                 "moduleid": moduleid,
                                 "nid": nid,
                                 "on_off": on_off
                             }], 10)

    @classmethod
    async def RemoveDevice(cls, moduleid, nid, deviceid):
        return await cls.Req('RemoveDevice',
                             [{
                                 "moduleid": moduleid,
                                 "nid": nid,
                                 "deviceid": deviceid
                             }
                              ], 100)

    @classmethod
    async def GetDeviceNId(cls, moduleid, deviceid):
        return await cls.Req('GetDeviceNId',
                             [
                                 {
                                     'moduleid': moduleid,
                                     'deviceid': deviceid
                                  }], 10)

    @classmethod
    async def GetTemperatureHumidity(cls, moduleid, nid):
        return await cls.Req('GetTemperatureHumidity',
                             [{
                                 'moduleid': moduleid,
                                 'nid': nid
                             }], 10)

    @classmethod
    async def GetLiquidLevel(cls, moduleid, nid):
        return await cls.Req('GetLiquidLevel',
                             [{
                                 'moduleid': moduleid,
                                 'nid': nid
                             }], 10)

    @classmethod
    async def GetSoil3IN1(cls, moduleid, nid):
        return await cls.Req('GetSoil3IN1',
                             [{
                                 'moduleid': moduleid,
                                 'nid': nid
                             }], 10)

    @classmethod
    async def GetAnalog(cls, moduleid, nid):
        return await cls.Req('GetAnalog',
                             [{
                                 'moduleid': moduleid,
                                 'nid': nid
                             }], 10)

    @classmethod
    async def RebootDevice(cls, moduleid, nid):
        return await cls.Req('RebootDevice',
                             [{
                                 'moduleid': moduleid,
                                 'nid': nid
                             }], 10)

    @classmethod
    async def RebootModule(cls, moduleid):
        return await cls.Req('RebootModule',
                             [{'moduleid': moduleid}], 20)

    @classmethod
    async def RebootAll(cls):
        return await cls.Req('RebootAll', [{}], 10)

    @classmethod
    async def ClearModule(cls, moduleid):
        return await cls.Req('ClearModule',
                             [{'moduleid': moduleid}], 20)

    @classmethod
    async def BackupModule(cls, moduleid):
        return await cls.Req('BackupModule',
                             [{'moduleid': moduleid}], 20)

    @classmethod
    async def RestoreModule(cls, moduleid, backup):
        return await cls.Req('RestoreModule',
                             [{'moduleid': moduleid,
                               'backup': backup}], 30)
