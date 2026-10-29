total_seconds = 9875
hour = total_seconds // 3600
minute = (total_seconds % 3600) // 60
remainding_seconds = total_seconds % 60

print(f"{total_seconds} seconds = {hour} h {minute} min {remainding_seconds} s")
