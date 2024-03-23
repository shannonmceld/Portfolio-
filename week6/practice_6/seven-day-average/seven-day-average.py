import csv
import requests


def main():
    # Read NYTimes Covid Database
    download = requests.get(
        "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv"
    )
    decoded_content = download.content.decode("utf-8")
    file = decoded_content.splitlines()
    reader = csv.DictReader(file)

    # Construct 14 day lists of new cases for each states
    new_cases = calculate(reader)

    # Create a list to store selected states
    states = []
    print("Choose one or more states to view average COVID cases.")
    print("Press enter when done.\n")

    while True:
        state = input("State: ")
        if state in new_cases:
            states.append(state)
        if len(state) == 0:
            break

    print(f"\nSeven-Day Averages")

    # Print out 7-day averages for this week vs last week
    comparative_averages(new_cases, states)


# TODO: Create a dictionary to store 14 most recent days of new cases by state
def calculate(reader):
    #create a dictionary
    new_cases = dict()
    previous_cases = dict()

    #get the key and values
    for i in reader:
        state = i["state"]
        date = i["date"]
        case = int (i["cases"])

        #since the data is cumulative make sure to update
        if state not in previous_cases:
            previous_cases[state] = case
            new_cases[state] = []
        else:
            newcase = case - previous_cases[state]
            previous_cases[state] = case

            if state not in new_cases:
                new_cases[state] = []

            if len(new_cases[state]) > 14:
                    new_cases[state].pop(0)
            new_cases[state].append(newcase)

    return new_cases

# TODO: Calculate and print out seven day average for given state
def comparative_averages(new_cases, states):
    for state in states:
        recent = new_cases[state][7:]
        previous = new_cases[state][0:7]
        avg_recent = round(sum(recent) / 7)
        avg_previous = round(sum(previous) / 7)

        difference = avg_recent - avg_previous

        if difference > 0:
            msg = "an increase"
        else:
            msg = "a decrease"

        try:
            d = difference / avg_previous
            p = round(d * 100)
        except ZeroDivisionError:
            raise ZeroDivisionError

        print(f"{state} had a 7-day average of {avg_recent} and {msg} of {p}%.")



main()
