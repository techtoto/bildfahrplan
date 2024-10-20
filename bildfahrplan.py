import matplotlib.pyplot as plt
import json

json_file = "./routes/Alzey-Mainz.json"

with open(json_file, encoding="UTF-8") as f:
    data = json.load(f)

data["route"].sort(key=lambda r: r["km"])

def search_by_ril100(ril100):
    for entry in data["route"]:
        if entry["ril100"] == ril100:
            return entry
    return {}

fig, ax = plt.subplots(figsize=(9, 6))

ax.set_xlim(data["route"][0]["km"], data["route"][-1]["km"])
ax.set_xticks([route_entry["km"] for route_entry in data["route"]])
ax.set_xticklabels([route_entry["ril100"] for route_entry in data["route"]])
ax.xaxis.tick_top()

ax.set_ylim(120, 0)

for journey in data["journeys"]:
    x_axis = []
    y_axis = []

    for stop in journey["stops"]:
        route_entry = search_by_ril100(stop["ril100"])
        if stop["arrival"] != None:
            x_axis.append(route_entry["km"])
            y_axis.append(stop["arrival"])
        if stop["departure"] != None:
            x_axis.append(route_entry["km"])
            y_axis.append(stop["departure"])

    ax.plot(x_axis, y_axis, label=journey["line"])

ax.grid()
ax.legend(loc="lower center", bbox_to_anchor=(0.5, -0.1), ncol=4)

plt.show()
