import os
from lib.action import LogAction
from lib.column import (
    Status,
    Talk,
    Vote,
    Divine,
    Execute
)


def analyze_log(agentRoleRate:dict, roleSet:set, analyzeLogPath:str) -> None:
    currentGameRole = dict()    # key: agent name value: role

    with open(analyzeLogPath, "r", encoding="utf-8") as f:
        for line in f:
            line = line.rstrip("\n")
            splitted_line = line.split(",")
            day = splitted_line[0]
            action = splitted_line[1]

            if(LogAction.is_status(action=action)):
                agentRole = Status.get_role(splitted_line=splitted_line)
                agentName = Status.get_aget_name(splitted_line=splitted_line)
                print(agentName + ":" + agentRole)
            elif(LogAction.is_talk(action=action)):
                pass

if __name__ == "__main__":
    agentRoleRate = dict()      # key: agent name value: (key: role value: win num)
    roleSet = set()             # keep role

    
    print(Status.column)
    print("----------")
    print(Divine.column)
    print("----------")
    print(Execute.column)

    # for log in os.listdir(logPath):
    #     currentLog = logPath + log
    #     analyze_log(agentRoleRate=agentRoleRate, roleSet=roleSet, analyzeLogPath=currentLog)