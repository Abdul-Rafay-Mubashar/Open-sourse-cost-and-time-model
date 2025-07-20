import math
import random 
import pandas as pd

from collections import defaultdict
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


all_paths: list = []
time_path: list = []
activity_info: list = []


CSV_PATH = "./data/synthetic_effort_dataset.csv"
names = ['Abdul', 'Ali', 'Iqbal', 'Uneeb']
model = LinearRegression()


def read_data_and_train_model(csv_path: str):
    df = pd.read_csv(csv_path)
    le = LabelEncoder()
    df["TaskCat_Label"] = le.fit_transform(df["Task Category"])

    X = df[["TaskCat_Label", "Complexity Value", "Experience"]]
    Y = df["Actual Time (hrs)"]
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
    model.fit(X_train, Y_train)

def build_activity_graph(data):
    graph = defaultdict(list)
    all_nodes = set()
    children = set()

    for item in data:
        act = item["activity"]
        pre_acts = item["pre_activity"] or []
        if not isinstance(pre_acts, list):
            pre_acts = [pre_acts]

        all_nodes.add(act)
        for pre in pre_acts:
            graph[pre].append(act)
            children.add(act)
            all_nodes.add(pre)

    roots = list(all_nodes - children)
    return graph, roots

def dfs_paths(graph, current, path, all_paths):
    if current not in graph or not graph[current]: 
        all_paths.append(path)
        return
    for neighbor in graph[current]:
        dfs_paths(graph, neighbor, path + [neighbor], all_paths)

def get_prediction(activity: str, experience: int, name: str, complexity_level: int, per_hour_rate: int, type: int,):
    data = [[type, complexity_level, experience]]
    prediction = model.predict(data)
    rounded_up = math.ceil(prediction.item())
    return name, activity, rounded_up

def get_predicton_of_each_activity(activites, names):
    for activity in activites:
        # name = input(f"Enter developer name for activity {activity['activity']}: ")
        # per_hour = int(input(f"Enter per hour rate for developer {name}: "))
        # experience = int(input(f"experence of developer : "))
        # name, activity, roundedup = get_prediction(activity["activity"], experience, name, activity["complexity-level"], per_hour, activity["type"])

        experience = random.randint(1, 15)
        complexity_level = random.randint(1, 4)
        per_hour_rate = random.choice(range(15, 51, 5))
        activity_type = random.randint(1, 4)
        name = random.choice(names)
        name, activity, roundedup = get_prediction(
            activity=activity["activity"],
            experience=experience,
            name=name,
            complexity_level=complexity_level,
            per_hour_rate=per_hour_rate,
            type=activity_type
        )
        activity_info.append({ "name":name, "activity": activity, "time": roundedup, "rate":per_hour_rate*roundedup})

def time_path_wise():
    for path in all_paths:
        path_time = 0
        for activity in path:
            for single_activity in activity_info:
                if activity == single_activity['activity']:
                    path_time = path_time + single_activity['time']
                    break
        time_path.append({"Path":path, 'time': path_time})
    return max(time_path, key=lambda x: x['time'])

def cost_complete_project():
    totel_cost = 0
    for activity in activity_info:
        totel_cost = totel_cost + activity['rate']
    return totel_cost

def show_activity_costs():
    cost = cost_complete_project()
    time = time_path_wise()

    print(f"Totel cost for project is {cost}$")
    print(f"Totel time for project is {time['time']}hrs")
    print("\n")


    print("------Activities Prices-------")
    print("\n")

    for activity in activity_info:
        print(f"Activity {activity['activity']} is done in {activity['time']}hrs in {activity['rate']}$ by {activity['name']}")
    
    print("\n")
    print("------Developer Prices------")
    print("\n")

    price_by_name = {}
    for item in activity_info:
        name = item["name"]
        price = item["rate"]

        if name in price_by_name:
            price_by_name[name] += price
        else:
            price_by_name[name] = price
    for developer,price in price_by_name.items():
        print(f"You need to pay {developer} price {price}$")
    print("\n")



def main(data, csv_path, names):
    read_data_and_train_model(csv_path)
    graph, roots = build_activity_graph(data)
    for root in roots:
        dfs_paths(graph, root, [root], all_paths)
    get_predicton_of_each_activity(data, names)
    show_activity_costs()

if __name__ == "__main__":
    data = [
        {"activity": "A", "pre_activity": [], "complexity-level": 1, "type": 1},
        {"activity": "B", "pre_activity": ["A"], "complexity-level": 2, "type": 4},
        {"activity": "C", "pre_activity": ["A"], "complexity-level": 1, "type": 3},
        {"activity": "D", "pre_activity": ["B"], "complexity-level": 2, "type": 2},
        {"activity": "E", "pre_activity": ["B"], "complexity-level": 3, "type": 1},
        {"activity": "F", "pre_activity": ["C"], "complexity-level": 1, "type": 2},
        {"activity": "G", "pre_activity": ["D", "E"], "complexity-level": 3, "type": 3},
        {"activity": "H", "pre_activity": ["E", "F"], "complexity-level": 3, "type": 2},  
        {"activity": "I", "pre_activity": ["F"], "complexity-level": 2, "type": 1}
    ]
    main(data, CSV_PATH, names)
    