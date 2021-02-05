def loading_bar(percentage):
    bar_items = percentage // 10
    bar_list = ""
    for item in range(0, percentage // bar_items):
        if item < bar_items:
            bar_list += "%"
        else:
            bar_list += "."

    if bar_items < 10:
        print(f"{percentage}% [{bar_list}]")
        print("Still loading...")
    else:
        print("100% Complete!")
        print(f"[{bar_list}]")


loading_progress = int(input())
loading_bar(loading_progress)
