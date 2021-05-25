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
        if validateOrder(order):
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
            meal.append(unedited_order[i])
        else:
            break
    
    # retrieve customer options (assumes input now is: name option option...)
    for i in range(len(unedited_order)):
        if unedited_order[i] != ' ' and unedited_order[i].isnumeric():
            options.append(int(unedited_order[i]))

    mealname = ''.join(meal)
    options.sort()

    # throw mealname and sorted options into edited_order object for return
    edited_order.append(mealname)
    for i in range(len(options)):
        edited_order.append(options[i])

    # #collects tally of each options appearance and throws tally into the options index within edited_order
    # current_option = 1
    # tally = 0
    # duplicates = 0                                                  # track duplicates so edited_order can be popped down
    # for i in range(len(edited_order)):
    #     if i != 0:
    #         if current_option == edited_order[i]:
    #             tally+=1
    #             if tally > 1:
    #                 duplicates+=1
    #         else:
    #             edited_order[current_option] = tally
    #             tally = 1
    #             current_option = edited_order[i]

    # # update final tally
    # if (len(edited_order)) > 1:
    #     edited_order[current_option] = tally

    #removes extra length of edited_order that previously contained duplicates for options
    # j = 0
    # while j < duplicates:
    #     edited_order.pop()
    #     j+=1

    return edited_order

# --------------------------------------------------------------------------------------------------------
def validateOrder(order):
    valid_order = True
    print(order)

    if order[1] != 1 or order[2] != 2:
        valid_order =False
    if order[0] == "Breakfast":
        if len(order) > 3 and order[3] != 3:
            valid_order =False

        order[3] = len(order) - 3                       # order[3] is coffee option, so place tally here
    elif order[0] == "Lunch":
        return True
    elif order[0] == "Dinner":
        return True
    else:
        valid_order = False
    
    return valid_order

if __name__ == '__main__':
    app.run(debug=True)