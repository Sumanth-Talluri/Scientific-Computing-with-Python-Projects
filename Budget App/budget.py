class Category:
    # class variables
    category = None
    ledger = []

    # constructor
    def __init__(self, cat):
        self.category = cat
        self.ledger = []

    # to deposit amount
    def deposit(self, amt, desc=""):
        self.ledger.append({"amount": amt, "description": desc})

    # to withdraw amount
    def withdraw(self, amt, desc=""):
        if self.check_funds(amt):
            self.ledger.append({"amount": -(amt), "description": desc})
            return True
        else:
            return False

    # to check balance
    def get_balance(self):
        bal = 0
        for transaction in self.ledger:
            bal += transaction["amount"]
        return bal

    # to transfer amount to other category
    def transfer(self, amt, cat):
        if self.check_funds(amt):
            self.ledger.append(
                {"amount": -(amt), "description": f"Transfer to {cat.category}"})
            cat.deposit(amt, f"Transfer from {self.category}")
            return True
        else:
            return False

    # check if certain amount is present
    def check_funds(self, amt):
        if self.get_balance() < amt:
            return False
        else:
            return True

    # this will execute when the object is printed
    def __str__(self):
        res = f"*************{self.category}*************\n"
        total = 0
        for transaction in self.ledger:
            # if description is not given
            try:
                desc = transaction["description"][:23].ljust(23)
            except:
                desc = "".ljust(23)
            amt = transaction["amount"]
            amt = round(amt, 2)
            total += amt
            res += f"{desc}"
            res += str("{:.2f}".format(amt)).rjust(7) + "\n"
        res += f"Total: {round(total,2)}"
        return res


# displaying the bar chart
def create_spend_chart(categories):
    res = "Percentage spent by category\n"
    total_amt_spent = 0
    amts = {}

    for categ in categories:
        amt_spent = 0
        for transaction in categ.ledger:
            if transaction["amount"] < 0:
                amt_spent += -(transaction["amount"])
        amts[categ] = amt_spent
        total_amt_spent += amt_spent

    percent = {}
    for categ in categories:
        per = (amts[categ]/total_amt_spent)*100
        per = int(per)
        # rem = per % 10
        # if rem < 5:
        #     per = int(per/10)*10
        # else:
        #     per = int((per+10)/10)*10
        percent[categ] = per

    # starting at 100 and stopping at 0 by dec 10 each time
    for x in range(100, -10, -10):
        res += str(x).rjust(3) + "| "
        for categ in categories:
            if percent[categ] >= x:
                res += "o  "
            else:
                res += "   "
        res += "\n"

    dashes = len(categories)*3 + 1
    dash = "-"
    res += f"    {dash*dashes}\n"

    maxx = len(categories[0].category)
    for categ in categories:
        if len(categ.category) > maxx:
            maxx = len(categ.category)
    i = 0
    for x in range(maxx):
        res += "     "
        for categ in categories:
            try:
                if categ.category[i]:
                    res += categ.category[i] + "  "
                else:
                    res += " "
            except:
                res += "   "
        if x != maxx-1:
            res += "\n"
        i += 1
    return res
