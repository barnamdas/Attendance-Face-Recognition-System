import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
        'databaseURL':"https://faceattendencerealtime-68a49-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "aditya":
    {
        "name": "Aditya",
        "major": "cse",
        "starting_year":2022,
        "total_attendance":4,
        "standing":"G",
        "year":2,
        "last_attendance_time":"2026-12-11 00:54:34"
    },
        "barnam 2":
    {
        "name": "barnam",
        "major": "cse",
        "starting_year":2021,
        "total_attendance":12,
        "standing":"B",
        "year":3,
        "last_attendance_time":"2025-12-11 00:54:34"
    },
        "elon_musk":
    {
        "name": "elon_musk",
        "major": "cse",
        "starting_year":2020,
        "total_attendance":7,
        "standing":"G",
        "year":4,
        "last_attendance_time":"2024-12-11 00:54:34"
    },
        "sunitha":
    {
        "name": "sunitha",
        "major": "cse",
        "starting_year":2022,
        "total_attendance":4,
        "standing":"G2",
        "year":2,
        "last_attendance_time":"2026-12-11 00:54:34"
    },
     "vivek":
    {
        "name": "vivek",
        "major": "cse",
        "starting_year":2022,
        "total_attendance":4,
        "standing":"G2",
        "year":2,
        "last_attendance_time":"2026-12-11 00:54:34"
    }
}

for key,value in data.items():
    ref.child(key).set(value)