from discordwebhook import Discord
import time

username = input("Please eneter your discord username: ")

while True:
    time.sleep(10) #time is in seconds
    discord = Discord(
    url="https://discordapp.com/api/webhooks/1002548075375624255/7d78qgrRLwMwo6RFPzB-QvppEWsV07tv_RMUorGqrlNQf6eBQ2mvparDnb4GYfes7smE"
    )
    discord.post(content =f"@{username}, how are you doing today?")