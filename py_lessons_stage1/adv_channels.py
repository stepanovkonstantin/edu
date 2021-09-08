stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}

max_sales_amount = 0
for channel, sales_amount in stats.items():
    if sales_amount > max_sales_amount:
        max_sales_amount = sales_amount
        channel_max_amount = channel
print(channel_max_amount)
