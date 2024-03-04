"""Write a Python function called calculate_discounted_price that takes the 
original price of an item and a discount percentage as input. The function 
should return the discounted price after applying the discount. Ensure that 
the function handles the case where the discount percentage is negative 
and raises a custom exception called InvalidDiscountError with an 
appropriate error message."""


class InvalidDiscountError(Exception):
    """Exception raised for invalid discount values.

    Attributes:
        discount -- the invalid discount value
        message -- explanation of the error
    """

    def __init__(self, discount, message="Invalid discount value"):
        self.discount = discount
        self.message = message
        super().__init__(self.message)

class DiscountedPrice:
    def __init__(self, original_price, discount_percentage):
        self.original_price = original_price
        self.discount_percentage = discount_percentage

    def calculate_discount(self):
        if self.discount_percentage < 0 or self.discount_percentage > 100:
            raise InvalidDiscountError(self.discount_percentage, "Discount must be between 0 and 100 percent")

        discounted_price = self.original_price - (self.original_price * self.discount_percentage / 100)
        return discounted_price

try:
    price_input = float(input("Enter original price: "))
    percentage_input = float(input("Enter discount percentage: "))

    discount_obj = DiscountedPrice(original_price=price_input, discount_percentage=percentage_input)
    discounted_price = discount_obj.calculate_discount()

    print(f"The discounted price is: {discounted_price}")

except InvalidDiscountError as e:
    print(f"Error: {e}")
except ValueError:
    print("Invalid input. Please enter valid numbers for original price and discount percentage.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")



