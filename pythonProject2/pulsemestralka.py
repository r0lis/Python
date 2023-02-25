ZACATEK_DNE = 8
KONEC_DNE = 18


def selection_sort(activities):
    sorted_activities = []
    while activities:
        max_time = float("-inf")
        max_time_idx = []
        # Get index of activity that ends the latest
        for i, activity_time in enumerate(activities):
            if activity_time[1] > max_time:
                max_time = activity_time[1]
                max_time_idx = i

        # Pop activity that ends the latest and append it to a new list
        sorted_activities.append(activities.pop(max_time_idx))
    return sorted_activities

def get_correct_activities(activities):
    correct_tasks = []
    for activity in activities:
        if all(ZACATEK_DNE <= hodina <= KONEC_DNE for hodina in activity):
            correct_tasks.append(activity)
    return correct_tasks

def scheduler(activities):
    last_end = -1
    ans = 0
    daily_plan = []
    remains = []
    while activities:
        if activities[-1][0] >= last_end:
            activity = activities.pop()
            daily_plan.append(activity)
            last_end = activity[1]
        else:
            remains.append(activities.pop())
    return daily_plan, remains

def main(activities, flag=True):
    if not activities:
        print("Není zde žádná aktivita. Program je ukončen.")
        return

    correct_activities = get_correct_activities(activities)
    sorted_activities = selection_sort(correct_activities)
    print(sorted_activities)
    daily_plan, remains = scheduler(sorted_activities)

    print(daily_plan)

    if flag:
        return len(daily_plan)


if __name__ == "__main__":
    my_activities = [[10, 11], [14, 18], [6, 10], [15, 17], [7, 10], [8, 9]]
    main(my_activities)