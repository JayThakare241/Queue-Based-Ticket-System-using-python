from flask import Flask, request, redirect
from queue_ds import PriorityQueueSystem
from storage import save_enqueue, save_dequeue
from utils import estimated_wait_minutes

app = Flask(__name__)
qs = PriorityQueueSystem()

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Ticket Counter</title>
</head>
<body>
    <h1>Queue Based Ticket System</h1>

    <form method="post" action="/add">
        Name: <input type="text" name="name" required>
        VIP: <input type="checkbox" name="vip">
        <button type="submit">Add Customer</button>
    </form>

    <form method="post" action="/serve" style="margin-top:10px;">
        <button type="submit">Serve Customer</button>
    </form>

    <h2>Current Queue</h2>
    <ol>
        {queue_items}
    </ol>
</body>
</html>
"""


@app.route("/")
def index():
    items = ""

    for i, customer in enumerate(qs.queue_list()):
        wait = estimated_wait_minutes(i)
        items += f"<li>{customer} - Estimated wait: {wait} min</li>"

    return HTML_TEMPLATE.format(queue_items=items)


@app.route("/add", methods=["POST"])
def add_customer():
    name = request.form.get("name")
    is_vip = "vip" in request.form

    if name:
        customer = qs.issue_ticket(name, is_vip)
        save_enqueue(customer)

    return redirect("/")


@app.route("/serve", methods=["POST"])
def serve_customer():
    customer = qs.serve_customer()

    if customer:
        save_dequeue(customer)

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
