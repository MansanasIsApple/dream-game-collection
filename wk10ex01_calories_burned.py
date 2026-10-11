# wk10ex01_calories_burned.py
# Gaming Session Tracker

def compute_session_points(hours, points_per_hour):
    return hours * points_per_hour


def main():
    sessions = int(input("How many gaming sessions? "))

    session_points_list = []
    total_points = 0

    for i in range(sessions):
        game = input("Enter game name: ")
        hours = float(input("Enter hours played: "))
        points_per_hour = float(input("Enter points earned per hour: "))

        session_points = compute_session_points(hours, points_per_hour)

        session_points_list.append(session_points)
        total_points += session_points

    print("Points per session:", session_points_list)
    print("Total points earned:", total_points)


if __name__ == "__main__":
    main()
