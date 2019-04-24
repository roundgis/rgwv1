from twisted.python import log
import rg_lib
import api_req_limit
import api_auth
import api_core
import api_zb_device


async def Remove(req_handler, arg):
    """
    :param req_handler: http request
    :param arg: {"deviceids", "token"}
    :return: ok
    """
    try:
        await api_req_limit.CheckHTTP(req_handler)
        await api_auth.CheckRight(arg['token'])
        return await api_zb_device.Remove(arg['deviceids'])
    except Exception:
        rg_lib.Cyclone.HandleErrInException()


async def Reset(req_handler, para):
    """
    :param req_handler:
    :param para: {"deviceids", "working_seconds": 0, "token"}
    :return:
    """
    try:
        await api_req_limit.CheckHTTP(req_handler)
        await api_auth.CheckRight(para['token'])
        return await api_zb_device.Reset(para['deviceids'])
    except Exception:
        rg_lib.Cyclone.HandleErrInException()


async def Add(req_handler, para):
    try:
        await api_req_limit.CheckHTTP(req_handler)
        await api_auth.CheckRight(para['token'])
        return await api_zb_device.Add(para['device'])
    except Exception:
        rg_lib.Cyclone.HandleErrInException()


async def Set(req_handler, para):
    """
    :param req_handler:
    :param sessionid:
    :param para: {"schedule": schedule tbl}
    :return: {deviceids, data_tbl: deviceid->[schedule id,...]}
    """
    try:
        await api_req_limit.CheckHTTP(req_handler)
        await api_auth.CheckRight(para['token'])
        return await api_zb_device.Set(para['device'])
    except Exception:
        rg_lib.Cyclone.HandleErrInException()


async def Get(req_handler, para):
    """
    :param req_handler:
    :param sessionid:
    :param para: {"scheduleids": [id,...]}
    :return:
    """
    try:
        await api_req_limit.CheckHTTP(req_handler)
        await api_auth.CheckRight(para['token'])
        return await api_zb_device.Get(para['deviceid'])
    except Exception:
        rg_lib.Cyclone.HandleErrInException()


async def Search(req_handler, para):
    """
    :param req_handler:
    :param sessionid:
    :param para: {"search_no": all, valid invalid}
    :return: [schedule obj,...]
    """
    try:
        await api_req_limit.CheckHTTP(req_handler)
        await api_auth.CheckRight(para['token'])
        return await api_zb_device.Search(para['arg'])
    except Exception:
        rg_lib.Cyclone.HandleErrInException()


async def GetOpLog(req_handler, para):
    """
    :param req_handler:
    :param para: {}
    :return: {groupids: [groupid,...], data_tbl: {groupid->[sensor data]}}
    """
    try:
        await api_req_limit.CheckHTTP(req_handler)
        await api_auth.CheckRight(para['token'])
        return await api_core.DeviceLog.Get(para['start_ts'], para['stop_ts'], para['deviceid'])
    except Exception:
        rg_lib.Cyclone.HandleErrInException()


async def GetOpErrorCount(req_handler, para):
    """
    :param req_handler:
    :param para: {}
    :return: {groupids: [groupid,...], data_tbl: {groupid->[sensor data]}}
    """
    try:
        await api_req_limit.CheckHTTP(req_handler)
        await api_auth.CheckRight(para['token'])
        devs = await api_core.BizDB.Query(["select id, name, device_no from rgw_zb_device", []])
        devids = [i['id'] for i in devs]
        devs_tbl = {i['id']: i for i in devs}
        recs = await api_core.DeviceLog.GetErrorCount(para['start_ts'], para['stop_ts'], devids)
        for rec in recs:
            rec['device_no'] = devs_tbl[rec['deviceid']]['device_no']
            rec['device_name'] = devs_tbl[rec['deviceid']]['name']
        return recs
    except Exception:
        rg_lib.Cyclone.HandleErrInException()


async def GetNId(req_handler, para):
    """
    :param req_handler:
    :param para: {}
    :return: {groupids: [groupid,...], data_tbl: {groupid->[sensor data]}}
    """
    try:
        await api_req_limit.CheckHTTP(req_handler)
        await api_auth.CheckRight(para['token'])
        return await api_zb_device.TryGetNId(para['moduleid'], para['deviceid'])
    except Exception:
        rg_lib.Cyclone.HandleErrInException()


async def Reboot(req_handler, para):
    """
    :param req_handler:
    :param para: {}
    :return: {groupids: [groupid,...], data_tbl: {groupid->[sensor data]}}
    """
    try:
        await api_req_limit.CheckHTTP(req_handler)
        await api_auth.CheckRight(para['token'])
        return await api_zb_device.Reboot(para['deviceids'])
    except Exception:
        rg_lib.Cyclone.HandleErrInException()
