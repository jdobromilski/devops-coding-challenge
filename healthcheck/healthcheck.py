import requests
import datetime
import os

time_format = '%H:%M:%S'
remote_url = 'http://jarek-myapp.com/now'

def lambda_handler(event, context):
    if requests.get(remote_url).status_code == 200:
        remote_time = requests.get(remote_url).text

        remote_time = datetime.datetime.strptime(remote_time, time_format)
        #print(f'jarek-myapp.com time: {remote_time}')

        # Getting current time to match the remote time format
        local_time = datetime.datetime.now().strftime(time_format)
        # Convert time back to datetime
        local_time = datetime.datetime.strptime(local_time, time_format)
        #print(f'Local time: {local_time}')

        time_difference = remote_time - local_time
        time_difference_in_seconds = time_difference.seconds

        if time_difference_in_seconds > 1:
            return "Failed"
        else:
            return "OK"
    else:
        return "Failed"
