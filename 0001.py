#题目：做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？
import uuid

# Generate 200 unique codes
codes = [str(uuid.uuid4()) for _ in range(5)]

# Print the codes
print(codes)


