import sys, jsons, datetime, time

def fmt(msg):
    # SAMPLE MSG:
    # {"currentRoundId": 99, "flag": "ENOBwAAAAAAAAAGAAAAYwAAAH9vgxIajeeNqdH1fmCy0Lk0NRFB", "function": "getflag", "message": "error getting profile from db: 'Could not find flag_7_r99_t6_i0 in <enochecker.nosqldict.NoSqlDict object at 0x7f040c2b1640>'", "method": "getflag", "module": "checker", "relatedRoundId": 99, "serviceName": "medicalappointment", "severity": "DEBUG", "severityLevel": 0, "taskChainId": "flag_7_r99_t6_i0", "taskId": 60236, "teamId": 6, "teamName": "NOP6", "timestamp": "2021-06-17T13:30:41.891248Z", "tool": "MedicalAppointmentChecker", "type": "infrastructure", "variantId": 0}
    ts_str = datetime.date.strftime(jmsg["timestamp"], "%T:%f")
    print(ts_str,":",jmsg["message"])

line = sys.stdin.readline()
while line:
    try:
        jmsg = jsons.loads(line)
    except:
        break
    fmt(jmsg)
    line = sys.stdin.readline()
