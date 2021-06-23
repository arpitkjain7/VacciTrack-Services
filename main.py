from client.integration.external_caller import APIInterface

request = {
    "to": "/topics/Vaccitrack",
    "collapse_key": "type_a",
    "data": {"body": "TriggerVaccineCheck", "title": "VacciTrack"},
}
response = APIInterface.post(route="https://fcm.googleapis.com/fcm/send", data=request)
print(response)
