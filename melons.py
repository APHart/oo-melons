"""Classes for melon orders."""

import random


class AbstractMelonOrder(object):
    """Any melon order from anywhere"""

    def __init__(self, species, qty, tax, order_type):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False
        self.tax = tax
        self.order_type = order_type

    def get_base_price(self):
        """Splurge pricing, returns base_price per order."""

        base_price = random.randint(5, 9)

        print base_price
        return base_price

    def get_total(self):
        """Calculate price, including tax."""

        base_price = self.get_base_price()

        if self.species.lower() == "christmas melon":
            base_price = 1.5 * base_price

        total = (1 + self.tax) * self.qty * base_price

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        super(DomesticMelonOrder, self).__init__(species, qty, 0.08, "domestic")


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes with country code"""

        super(InternationalMelonOrder, self).__init__(species, qty, 0.17,
                                                      "international")
        self.country_code = country_code

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

    def get_total(self):
        """Adds $3 to orders with a qty less than 10."""

        int_total = super(InternationalMelonOrder, self).get_total()

        if self.qty < 10:
            int_total += 3

        return int_total


class GovernmentMelonOrder(AbstractMelonOrder):
    """Melon order for government"""

    passed_inspection = False

    def __init__(self, species, qty):
        """Initialize melon order for gov"""
        super(GovernmentMelonOrder, self).__init__(species, qty,
                                                   0.0, "government")

        # self.passed = False  #talk about in code review

    def mark_inspection(self, passed):
        """Record fact that inspection has been passed"""
        #making sure that passed is a bool
        if isinstance(passed, bool):
            self.passed_inspection = passed
        else:
            print "That is not a valid input"
