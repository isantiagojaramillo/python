"""System module."""

def get_product(**data):
    """System module."""
    print(data["id"], data["name"])

get_product(id="1",
            name="iPhone",
            description="This is an iphone")
