import pywhatkit
from datetime import datetime, timedelta

# Get the current time
current_time = datetime.now()

# Calculate the time after 2 minutes
scheduled_time = current_time + timedelta(minutes=2)

# Extract hour and minute from the scheduled time
hour = scheduled_time.hour
minute = scheduled_time.minute

# Send the message using pywhatkit
pywhatkit.sendwhatmsg('+918329828303', 'happy birthday', hour, minute, wait_time=5)
