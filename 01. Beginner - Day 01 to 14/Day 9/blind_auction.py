from art import logo
print(logo)

# TODO-4: Compare bids in dictionary
def find_highest_bidder(bidding_dictionary):
    max_bid = 0
    max_bidder = ''
    for bid in bidding_dictionary:
        if bidding_dictionary[bid] > max_bid:
            max_bid = bidding_dictionary[bid]
            max_bidder = bid

    print(f"The winner is {max_bidder} with a bid of ${max_bid}.")


bids = {}
bidding = True

while bidding:
    # TODO-1: Ask the user for input
    name = input("What is your name ? ")
    price = int(input("What is your bid ? $"))

    # TODO-2: Save data into dictionary {name: price}
    bids[name] = price

    # TODO-3: Whether if new bids need to be added
    more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.").lower()
    print("\n" * 100)
    if more_bidders == 'no':
        bidding = False
        find_highest_bidder(bids)




