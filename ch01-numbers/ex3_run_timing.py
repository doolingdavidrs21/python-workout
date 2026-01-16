def run_timing():
    """
    Asks how long it took you to run 10 km.
    The function continue to ask how long (in minutss)
    it took for additional runs, until the user presses Enter.
    At that point, the function exits - but only after
    calculating and displaying the average time that the
    10 km runs took.
    """
    run_times = []
    while True:
        run_time = input("Enter 10 km run time: ")
        if not run_time:
            break
        else:
            try:
                run_time = float(run_time)
            except ValueError as ve:
                print(f"Goddamnit it: {ve} Enter a number!")
                continue
        run_times.append(run_time)
        mean_run_time = sum(run_times)/len(run_times)
    print(f"Average of {mean_run_time:.2f}, over {len(run_times)} runs")




