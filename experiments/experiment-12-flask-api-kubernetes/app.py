from flask import Flask, jsonify, request
app=Flask(__name__)
TASKS=[{"id":1,"title":"Read the lab brief","done":False}]
@app.get("/health")
def health(): return jsonify(status="ok",service="campus-tasks-api")
@app.get("/api/tasks")
def list_tasks(): return jsonify(TASKS)
@app.post("/api/tasks")
def create_task():
 title=str((request.get_json(silent=True) or {}).get("title","")).strip()
 if not title: return jsonify(error="title is required"),400
 item={"id":max((t["id"] for t in TASKS),default=0)+1,"title":title,"done":False}
 TASKS.append(item);return jsonify(item),201
if __name__=="__main__": app.run(host="0.0.0.0",port=5000)
