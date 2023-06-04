print("Name: Charchika Priya")
print("Reg no. 22MCA1124")
def race_time(participants):
    for participant in participants:
        name, start_time, finish_time = participant
        race_time = finish_time - start_time
        print(f"{name} finished the race in {race_time} seconds.")

participants = [("Charchika", 0, 35), ("Priya", 3, 40), ("Ruchi", 5, 45)]
race_time(participants)
