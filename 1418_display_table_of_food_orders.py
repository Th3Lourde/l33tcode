'''
Given an array of orders
create a display table

Each order:
 = [Person, Table, Food]

 Display table:

 Each row has tables
 Each table shows the number of orders
 for each type of food

Have a dict where the table is the key.

this maps to a dict with the different meals as keys and the freq as values.

E.g. : ["David", "3", "Ceviche"]

table = {
    "3": {"Ceviche": 1},
}

["Corina", "10", "Beef Burrito"]

table = {
    "3": {"Ceviche": 1},
    "10": {"Beef Burrito": 1},
}

First check to see if the table ∃ ∈ table, add if need be
If food in table += 1 to entry, else create it.

(This should be easy enough to do in one pass)

When you see a food, check to see if it exists in the master
food set

Have tables be stored as ints

1) Create table object
    while creating it, create a master food set

So we have table obj and a set of food, cast to list, sort.

Then for each table, check the number of orders for each type of
food, add the number of times something was ordered



'''


class Solution:
    def displayTable(self, orders):
        table = {}
        food = set()

        for order in orders:
            tableNum = int(order[1])

            # Add in table
            if tableNum not in table:
                table[tableNum] = {}

            # Add food to master food set
            if order[2] not in food:
                food.add(order[2])

            # Add food to table order
            if order[2] not in table[tableNum]:
                table[tableNum][order[2]] = 1

            else:
                table[tableNum][order[2]] += 1

        header = ["Table"]

        foods = list(food)
        foods.sort()

        for f in foods:
            header.append(f)

        ans = [header]

        tables = list(table.keys())
        tables.sort()

        for t in tables:
            row = [str(t)]

            for f in foods:
                if f in table[t]:
                    row.append(str(table[t][f]))
                else:
                    row.append("0")

            ans.append(row)

        return ans

if __name__ == '__main__':
    s = Solution()

    print(s.displayTable([["David","3","Ceviche"],["Corina","10","Beef Burrito"],
        ["David","3","Fried Chicken"],["Carla","5","Water"],["Carla","5","Ceviche"],
        ["Rous","3","Ceviche"]]))
