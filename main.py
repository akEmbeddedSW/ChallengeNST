import pandas as pd

# Create a data frame with Raw, Binary, and SeatID columns.
data = pd.DataFrame(columns=['Raw', 'Binary', 'SeatID'])
# Read inout.txt from directory into Raw column.
inputFile = 'input.txt'
data['Raw'] = pd.read_csv(inputFile, header=None)
# Iterate over Raw column.
for index in data['Raw'].index:
    # Provide additional information in case of an exception.
    try:
        # Read each scanned sequence.
        instance = data.loc[index, 'Raw']
        # Replace F, B, R, and L with 0 and 1.
        binary = instance.replace('F', '0').replace('B', '1')\
                         .replace('L', '0').replace('R', '1')
        # Convert binary to decimal/seat IDs.
        data.loc[index, 'SeatID'] = int(binary, 2)
        # Previous step ran so the replacement is correct.
        data.loc[index, 'Binary'] = binary
    except Exception as e:
        # Print the exception and additional info but not to panic
        print('\n', e, '\n We have characters other than F, B, L, and R\n',
              'Check this instance in the input: {}\n'.format(instance),
              'It should be at line {} of {}\n'.format(index+1, inputFile))
        # Raise will through an error and stop the process.
        # raise
# Make sure that we detect duplicated instances.
duplicateRows = data[data.duplicated(subset=['SeatID'])]
# Printing duplicated values.
if not duplicateRows.empty:
    print(' Duplicated seat IDs were found.\n',
          'Only their first occurrence will be kept')
    for index in duplicateRows.index:
        scanned = data.loc[index, 'Raw']
        print(' Check this instance in the input: {}\n'.format(scanned),
              'It should be at line {} of {}\n'.format(index+1, inputFile))

# Remove all occurrences except the first one,
data.drop_duplicates(subset=['SeatID'], keep="first", inplace=True)
# Print a summary of the dataframe
print(data)
# Convert the whole dataframe as a string and display
# print(data.to_string())
# Find the maximum value in seat IDs
maxID = data['SeatID'].max()
# Find the minimum value in seat IDs
minID = data['SeatID'].min()
# Print lowest seat ID, row, and seat.
print('Lowest  seat ID: {:4} - row: {:4} - seat: {:4}'.
      format(minID, (minID >> 3), (minID & 7)))
# Print highest seat ID, row, and seat.
print('Highest seat ID: {:4} - row: {:4} - seat: {:4}'.
      format(maxID, (maxID >> 3), (maxID & 7)))
#///////////////////////////////////////////////////////////////////////
# Create a range from min to max representing all the available seats
allSeats = pd.DataFrame(range(minID,maxID+1), columns=['Range'])
# Compare scanned with all the available seats to find empty seats
emptySeats = allSeats[~allSeats['Range'].isin(data['SeatID'])]
# Iterate over all the empty seats
for index in emptySeats.index:
    # Extract seat ID
    seatID = allSeats.loc[index, 'Range']
    # Check if seats next to the empty seat are in the list
    if ((not data.loc[data['SeatID'] == seatID- 1].empty) and
        (not data.loc[data['SeatID'] == seatID+ 1].empty)):
        # If meet the condition, my seat can be as the following
        print("Potentially, my seat ID: {:4}, Row: {:4}, Seat: {:4}"
              .format(seatID, seatID >> 3, seatID & 7))
