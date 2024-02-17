import sqlite3

# Connect to the database
conn = sqlite3.connect('workouts.db')
c = conn.cursor()

# Create tables
c.execute('''CREATE TABLE IF NOT EXISTS workouts (
                id INTEGER PRIMARY KEY,
                name TEXT,
                description TEXT
             )''')

c.execute('''CREATE TABLE IF NOT EXISTS exercises (
                id INTEGER PRIMARY KEY,
                workout_id INTEGER,
                exercise_name TEXT,
                FOREIGN KEY (workout_id) REFERENCES workouts(id)
             )''')

# Sample workout plans with exercises
workouts = [
    ("Beginner Full Body Workout", "A beginner full-body workout routine.", [
        "Squats",
        "Push-ups",
        "Lunges"
    ]),
    ("Beginner Upper Body Workout", "A beginner upper body workout routine.", [
        "Bench-Press",
        "Lat-pulldowns",
        "Shoulder-Press"
    ]),
    ("Chest and back", "Arnold split", [
        "Bench-Press",
        "Pull-ups",
        "Upperback-rows",
        "Incline-dumbbell-press",
        "Pec-flies"
    ]),
    ("Arms", "Arnold split", [
        "Dumbbell-shoulder-press",
        "Preacher-curls",
        "Skullcrushers",
        "Lateral-raises",
        "Tricep-pushdowns",
        "Rear-delt-flies"
    ]),
    ("Legs", "Intermediate Legs workout", [
        "Squats",
        "Deadlifts",
        "Leg-extensions",
        "Hamstring-curls",
        "Calf-raises"
    ]),
    ("Push", "PPL split", [
        "Bench-Press",
        "Chest-machine-press",
        "Shoulder-press",
        "Lateral-raises",
        "Tricep-pushdowns"
    ]),
    ("Pull", "PPL split", [
        "Lat-pulldowns",
        "Upper-back-rows",
        "Dumbbell-curls",
        "Barbell-rows",
        "Cable-curls"
    ]),
    # Add more workout plans
]


for workout in workouts:
    c.execute("INSERT INTO workouts (name, description) VALUES (?, ?)", (workout[0], workout[1]))
    workout_id = c.lastrowid
    for exercise in workout[2]:
        c.execute("INSERT INTO exercises (workout_id, exercise_name) VALUES (?, ?)", (workout_id, exercise))


conn.commit()
conn.close()

print("Workout plans and exercises have been successfully added to the database.")