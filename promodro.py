import time


def study_session(study_minutes, break_minutes):
    print(f"Study time: {study_minutes} minutes")
    time.sleep(study_minutes * 60)  # Study session in seconds
    print(f"Break time: {break_minutes} minutes")
    time.sleep(break_minutes * 60)  # Break session in seconds


def main():
    study_minutes = 25
    break_minutes = 5
    cycles = 2  # Set to 2 cycles

    for i in range(cycles):
        print(f"Cycle {i + 1} starting...")
        study_session(study_minutes, break_minutes)

    print("Good job! You've completed 2 cycles!")


if __name__ == "__main__":
    main()
