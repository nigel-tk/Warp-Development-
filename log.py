import json
class LogAnalyse():

    def __init__(self):
        pass
    
    # open log file and get all log information  
    # can be updated or ammended if log files are in different format. 
    def get_log(self):
        log_entries= []
        with open("sample_log.log", "r") as file:
         
         ## easier to handle log info as a list of dictionary elements file rather than pure string manipulating JSON is the inspiration for this. 
         for line in file:
             line = line.strip()
             #for this sample log timestamp will always be the 1st 23 characters 
             timestamp = line[:23]
             # the rest of the log line will be all characters after 23 characters 
             remaining = line[24:]
             #Get the level or event (INFO, ERROR, WARNING) and the log message 
             parts = remaining.split(maxsplit=1)  
            
             level, message = parts
             
             date, time = timestamp.split(" ")
             log_entries.append({
                "timestamp": timestamp,
                "date": date,
                "time": time,
                "level": level,
                "message": message
                })

        return log_entries

    #analyse all aspects of log. 
    #Criteria can be passed, if items of log match criteria, then those log lines will be printed.
    #You can analyse criteria by Event (Error, WARNING, INFO), Date, and message

    def analyse_log(self, criteria, criteria_value): 
        log_json = self.get_log() 

        for line in log_json: 
            #Print log line that meets criteria. 
            #Because log has timestamp all events printed are sequential
            if line[criteria].lower() == criteria_value.lower(): 
                print(f"AT TIME: {line['time'][:8]} ON DATE: {line['date']}  EVENT: {line['level']} occured with message:  {line['message']}")


LogAnalyse().analyse_log('level','info')
print('--------------------------------')
LogAnalyse().analyse_log('date','2025-04-10')
print('--------------------------------')
LogAnalyse().analyse_log('time','08:15:25.123')
print('--------------------------------')
LogAnalyse().analyse_log('message','System startup initiated')
