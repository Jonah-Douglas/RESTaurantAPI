from flask import Flask, request
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

# order_put_args = reqparse.RequestParser()
# order_put_args.add_argument("orderID", type=int, help="Name of the video is required", required=True)
# order_put_args.add_argument("meal", type=str, help="Name of the meal is required", required=True)
# order_put_args.add_argument("main", type=int, help="Name of the main entree is required", required=True)
# order_put_args.add_argument("side", type=int, help="Name of the side entree is required", required=True)
# order_put_args.add_argument("drink", type=int, help="Name of the drink is allowed")
# order_put_args.add_argument("dessert", type=int, help="Name of the dessert is required")

orders = {}

class Order(Resource):
    def put(self, order_id):
        order = parseOrder(request.form['order'])
        validateOrder(order)
        if order != 0:
            prepResponse(order)
            # print(request.form['order'])
            # args = order_put_args.parse_args(order_id)
            # orders[order_id] = args
            return {}# orders[order_id], 201
        else:
            return {"usage": "Example input- Breakfast 1, 2"}, 400

api.add_resource(Order, "/order/<int:order_id>")

# --------------------------------------------------------------------------------------------------------
# parse the user request into an object we can then validate with our given ruleset
def parseOrder(unedited_order):
    meal = []                                                   # store which meal type (b, l, d)
    options = []                                                # store customer options with their counts indexed by option
    edited_order = []                                           # object to store modified user request

    unedited_order = unedited_order.replace(',', ' ')           # remove commas and \n from user request
    unedited_order = unedited_order.replace('\n', '')           

    # build string for meal name
    for i in range(len(unedited_order)):
        if unedited_order[i] != ' ':
            if  unedited_order[i].isalpha():
                meal.append(unedited_order[i])
            else:
                return 0
        else:
            break
    
    # retrieve customer options (assumes input now is: name option option...)
    for i in range(len(unedited_order)):
        if unedited_order[i] != ' ' and unedited_order[i].isnumeric():
            if 1 <= int(unedited_order[i]) <= 4:
                options.append(int(unedited_order[i]))
            else:
                return 0

    mealname = ''.join(meal)
    options.sort()

    # throw mealname and sorted options into edited_order object for return
    edited_order.append(mealname)
    for i in range(len(options)):
        edited_order.append(options[i])

    return edited_order

# --------------------------------------------------------------------------------------------------------
def validateOrder(order):
    valid_order = True
    print(order)

    if len(order) < 3 or order[1] != 1 or order[2] != 2:
        print("HERE1")
        return 0
    if order[0] == "Breakfast":
        if (len(order) > 3 and order[3] != 3) or '4' in order:
            print("HERE2")
            return 0

        order[3] = len(order) - 3                       # order[3] is coffee option, so place tally here
        #print(order)
    elif order[0] == "Lunch":
        return True
    elif order[0] == "Dinner":
        return True
    else:
        valid_order = False
    
    return order

# --------------------------------------------------------------------------------------------------------
def prepResponse(order):
    return True

if __name__ == '__main__':
    app.run(debug=True)