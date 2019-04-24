from twisted.python import log
import rg_lib
import api_req_limit
import api_auth
import api_rxg
import api_zb_device


async def ListModule(req_handler, arg):
    """
    :param req_handler: http request
    :param arg: {"status_only": boolean, "token"}
    :return: {"devices": [zb device,...]}
    """
    try:
        await api_req_limit.CheckHTTP(req_handler)
        await api_auth.CheckRight(arg['token'])
        return await api_zb_device.Module.List(arg)
    except Exception:
        rg_lib.Cyclone.HandleErrInException()


async def ProbeDevice(req_handler, para):
    """
    :param req_handler:
    :param para: {"deviceids", "working_seconds": 0, "token"}
    :return:
    """
    try:
        await api_req_limit.CheckHTTP(req_handler)
        await api_auth.CheckRight(para['token'])
        return await api_zb_device.Module.ProbeDevice(para['moduleid'])
    except Exception:
        rg_lib.Cyclone.HandleErrInException()


async def ResetModule(req_handler, para):
    try:
        await api_req_limit.CheckHTTP(req_handler)
        await api_auth.CheckRight(para['token'])
        await api_rxg.XY.ClearModule(para['moduleid'])
        return await api_rxg.XY.RebootModule(para['moduleid'])
    except Exception:
        rg_lib.Cyclone.HandleErrInException()


async def BackupModule(req_handler, para):
    """
    :param req_handler:
    :param sessionid:
    :param para: {"schedule": schedule tbl}
    :return: {deviceids, data_tbl: deviceid->[schedule id,...]}
    """
    try:
        await api_req_limit.CheckHTTP(req_handler)
        await api_auth.CheckRight(para['token'])
        return await api_zb_device.Module.Backup(para['moduleid'])
    except Exception:
        rg_lib.Cyclone.HandleErrInException()


async def RestoreModule(req_handler, para):
    """
    :param req_handler:
    :param sessionid:
    :param para: {"scheduleids": [id,...]}
    :return:
    """
    try:
        await api_req_limit.CheckHTTP(req_handler)
        await api_auth.CheckRight(para['token'])
        return await api_zb_device.Module.Restore(para['src_moduleid'],
                                                  para['target_moduleid'])
    except Exception:
        rg_lib.Cyclone.HandleErrInException()


async def RebootModule(req_handler, para):
    """
    :param req_handler:
    :param sessionid:
    :param para: {"search_no": all, valid invalid}
    :return: [schedule obj,...]
    """
    try:
        await api_req_limit.CheckHTTP(req_handler)
        await api_auth.CheckRight(para['token'])
        return await api_rxg.XY.RebootModule(para['moduleid'])
    except Exception:
        rg_lib.Cyclone.HandleErrInException()


async def RebootAll(req_handler, para):
    """
    :param req_handler:
    :param para: {}
    :return: {groupids: [groupid,...], data_tbl: {groupid->[sensor data]}}
    """
    try:
        await api_req_limit.CheckHTTP(req_handler)
        await api_auth.CheckRight(para['token'])
        return await api_rxg.XY.RebootAll()
    except Exception:
        rg_lib.Cyclone.HandleErrInException()

