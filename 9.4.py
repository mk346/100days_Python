#
import os
logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)

bidding_finished = False
bids = {}

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def find_highest_bidder(bidding_record):
    max_bidder = 0
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > max_bidder:
            max_bidder = bid_amount
            print(f"The winner is {bidder} with a bid amount ${max_bidder}")
while not bidding_finished:
    name = input("Enter your name: ")
    price = int(input("Amount to bid: $"))
    bids[name] = price
    should_continue = input("Are there and more biders? Type 'yes' or 'no'): \n")
    if should_continue == 'no':
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == 'yes':
        clear()