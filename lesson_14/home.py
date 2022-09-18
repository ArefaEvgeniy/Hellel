# Создайте свой произвольный класс и в нём помимо обычных методов и
# атрибутов создайте несколько статических методов и методов класса.
# Продемонстрируйте их работу.


class Tree:
    last_owner = None
    quan_of_owners = 0

    def __init__(self, quantity_of_a, owner, name="tree"):
        self.quantitu_of_a = quantity_of_a
        self.name = name
        self.owner = owner
        self.tree_doc = f"{quantity_of_a}, {name}, {owner}"
        Tree.last_owner = owner
        Tree.quan_of_owners += 1

    @staticmethod
    def tree_price():
        print(50 * "-", "tree priece is 300$", "apple price is 2$", "the resale price is set by the last owner",
              50 * "-", sep="\n")

    @classmethod
    def all_info(cls):
        print(f"last_owner: {cls.last_owner}\nquan_of_owners: {cls.quan_of_owners}")

    @classmethod
    def price_info(cls):
        if cls.last_owner == None:
            cls.tree_price()
        else:
            print(f"He/She {cls.last_owner} is the last owner")
