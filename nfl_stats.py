import csv

# Open the CSV file and read the data
with open('nfl_offensive_stats.csv', mode='r') as file:
    csv_reader = csv.reader(file)
    # Read the header
    header = next(csv_reader)
    # Read the rest of the data
    data = [row for row in csv_reader]

# Print the header and first few rows of data
# print("Header:", header)
# Calculate the total passing yards for players whose position is "QB"
qb_passing_yards = {}

for row in data:
    position = row[2]
    player = row[3]
    passing_yards = int(row[7])  # Convert passing yards to integer

    if position == "QB":
        if player not in qb_passing_yards:
            qb_passing_yards[player] = 0
        qb_passing_yards[player] += passing_yards

# Print the total passing yards for each QB
# for player, yards in qb_passing_yards.items():
# print(f"{player}: {yards} yards")

# Sort the QBs by total passing yards in descending order and exclude Tom Brady
sorted_qb_passing_yards = sorted(
    ((player, yards) for player, yards in qb_passing_yards.items() if player != "Tom Brady"),
    key=lambda x: x[1],
    reverse=True
)

# Print the sorted passing yards
for player, yards in sorted_qb_passing_yards:
    print(f"{player}: {yards} yards")

    import matplotlib.pyplot as plt

    # Filter players with more than 4000 passing yards
    filtered_qb_passing_yards = [(player, yards) for player, yards in sorted_qb_passing_yards if yards > 4000]

    # Sort by passing yards in ascending order
    filtered_qb_passing_yards.sort(key=lambda x: x[1])

    # Extract player names and passing yards
    players = [player for player, yards in filtered_qb_passing_yards]
    passing_yards = [yards for player, yards in filtered_qb_passing_yards]

    # Plot the data
    plt.figure(figsize=(10, 6))
    plt.bar(players, passing_yards, color='skyblue')
    plt.xlabel('Players')
    plt.ylabel('Passing Yards')
    plt.title('Players with More Than 4000 Passing Yards')
    plt.tight_layout()
    plt.xticks(rotation=90)
    plt.show()