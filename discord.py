from discordwebhook import Discord
import time

username = input("Please enter your discord username: ")

while True:
    time.sleep(86400) #time is in seconds so for 24 hours it would be 86400 seconds
    discord = Discord(
    url="https://discordapp.com/api/webhooks/1002548075375624255/7d78qgrRLwMwo6RFPzB-QvppEWsV07tv_RMUorGqrlNQf6eBQ2mvparDnb4GYfes7smE"
    )
    discord.post(content =f"@{username}")
