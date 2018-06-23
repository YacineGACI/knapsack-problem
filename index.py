from flask import Flask, render_template, request, jsonify, Response
import time, json
import knapsack

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")




@app.route('/result', methods=["POST"])
def result():
    data = request.get_json()
    totalWeight = data["totalWeight"]
    weights = data["weights"]
    values = data["values"]
    itemIndexes = data["indexes"]
    time1 = time.time()
    sol = knapsack.Knapsack(totalWeight, weights, values, itemIndexes)
    res = sol.run()
    spenTime = time.time() - time1
    items = sol.showItems()
    items = " ".join("#"+str(i)+"," for i in items)
    items = items[:-1]
    res = {"res":int(res), "items": items, "time":spenTime}
    print(sol.matrix)
    return jsonify(res)




if __name__=="__main__":
    app.run(debug=True)