# result = [{
#   id: 1,
#   name: "CEO",
#   children: [{
#     id: 2,
#     name: "CTO",
#     children: [{
#       id: 4,
#       name: "Engineering Manager 1",
#       children: [{
#         id: 7,
#         name: "Engineer",
#         children: [],
#       }]
#     }, {
#       id: 5,
#       name: "Engineering Manager 2",
#       children: []
#     }]
#   }, {
#     id: 3,
#     name: "CFO",
#     children: [{
#       id: 6,
#       name: "Financial Analyst 1",
#       children: []
#     }]
#   }]
# }]

import json


# variables hold references to values in dictionaries. That way, it's possible to change inner dictionaries and the variable referencing an outer dict will track the changes.
def build_hierarchy(workers):
    root = None
    workers_by_id = {worker["id"]: {
        "id": worker["id"], "name": worker["name"], "children": []} for worker in workers}

    for worker in workers:
        if worker["parent_id"] == None:
            root = workers_by_id[worker["id"]]
        else:
            workers_by_id[worker["parent_id"]]["children"].append(
                workers_by_id[worker["id"]])
    return root


workers = [
    {"id": 6, "name": "Financial Analyst 1", "parent_id": 3},
    {"id": 4, "name": "Engineering Manager 1", "parent_id": 2},
    {"id": 1, "name": "CEO", "parent_id": None},
    {"id": 2, "name": "CTO", "parent_id": 1},
    {"id": 3, "name": "CFO", "parent_id": 1},
    {"id": 5, "name": "Engineering Manager 2", "parent_id": 2},
    {"id": 7, "name": "Engineer", "parent_id": 4}
]

hierarchy = build_hierarchy(workers)
print(json.dumps(hierarchy, indent=2))
