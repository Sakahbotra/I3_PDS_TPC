total_seconds = 9875
hour = total_seconds // 3600
minute = (total_seconds % 3600) // 60
remainding_seconds = total_seconds % 60

print(f"{total_seconds} seconds = {hour} h {minute} min {remainding_seconds} s")

rebuild_total = (hour * 3600) + (minute * 60) + remainding_seconds
is_correct = rebuild_total == total_seconds

print(f"Check: {is_correct}")
