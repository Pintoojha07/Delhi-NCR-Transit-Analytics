import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

print("Dataset generate ho raha hai, thoda wait karo...")

# Locations aur transport modes
origins = ['Sector-52 Noida', 'Sector 135 Noida', 'Botanical Garden', 'Kalkaji Mandir']
destinations = ['NHPC Chowk', 'Sector 27 Faridabad', 'Badarpur Border', 'Bata Chowk']
transport_modes = ['Delhi Metro', 'Uber Shuttle', 'City Bus']

data = []
start_date = datetime(2026, 9, 1)

# 5000 rows ka data generate kar rahe hain
for i in range(1, 5001):
    trip_id = f"TRP{10000 + i}"
    random_days = random.randint(0, 30)
    
    # Time logic (Office aane-jaane ka time)
    hour = random.choices([7, 8, 9, 10, 14, 15, 17, 18, 19, 20], 
                          weights=[1, 3, 4, 2, 1, 1, 2, 4, 3, 1])[0]
    minute = random.randint(0, 59)
    trip_datetime = start_date + timedelta(days=random_days, hours=hour, minutes=minute)
    
    origin = random.choice(origins)
    destination = random.choice(destinations)
    mode = random.choice(transport_modes)
    
    # Travel Time Logic
    if mode == 'Delhi Metro':
        base_time = random.randint(35, 45)
    elif mode == 'Uber Shuttle':
        base_time = random.randint(40, 60)
    else: 
        base_time = random.randint(50, 75)
        
    # Peak hours mein delay zyada dikhane ke liye
    is_peak_hour = hour in [8, 9, 18, 19]
    if is_peak_hour:
        delay_minutes = np.random.normal(loc=15, scale=5)
    else:
        delay_minutes = np.random.normal(loc=3, scale=2)
        
    actual_time = int(base_time + max(0, delay_minutes))
    
    data.append([
        trip_id, 
        trip_datetime.strftime('%Y-%m-%d'), 
        trip_datetime.strftime('%H:%M:%S'), 
        trip_datetime.strftime('%A'), 
        origin, 
        destination, 
        mode, 
        base_time, 
        actual_time,
        actual_time - base_time
    ])

# CSV file mein save karna
columns = ['Trip_ID', 'Date', 'Time', 'Day_of_Week', 'Origin', 'Destination', 'Transport_Mode', 'Expected_Time_Mins', 'Actual_Time_Mins', 'Delay_Mins']
df = pd.DataFrame(data, columns=columns)
df.to_csv('ncr_transit_data.csv', index=False)

print("Congratulations! 'ncr_transit_data.csv' file successfully ready  .")