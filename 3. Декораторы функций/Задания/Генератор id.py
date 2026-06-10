def make_id_generator(prefix):

    def wrapper():
        wrapper.count += 1
        return f'{prefix}-{str(wrapper.count).zfill(3)}'
    wrapper.count = 0

    return wrapper

user_id = make_id_generator('USR')
order_id = make_id_generator('ORD')

print(user_id())
print(user_id())
print(user_id())
print(order_id())
print(order_id())
print(order_id())
print(user_id())