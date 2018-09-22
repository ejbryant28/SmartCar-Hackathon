import smartcar

access_token = '8569474c-e7c0-4d50-a794-bb4eb0cf180f'

response = smartcar.get_vehicle_ids(access_token)

vid = response['vehicles'][0]

vehicle = smartcar.Vehicle(vid, access_token)

location = vehicle.location()

print(location)