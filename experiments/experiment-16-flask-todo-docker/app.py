from flask import Flask,jsonify,request
from pathlib import Path
from contextlib import contextmanager
import os,sqlite3
app=Flask(__name__)
DB=Path(os.environ.get("TODO_DB",str(Path(__file__).with_name("todos.db"))))
@contextmanager
def db():
 c=sqlite3.connect(DB);c.row_factory=sqlite3.Row
 try:
  yield c
  c.commit()
 except Exception:
  c.rollback()
  raise
 finally:
  c.close()
def init():
 with db() as c:c.execute("CREATE TABLE IF NOT EXISTS todos(id INTEGER PRIMARY KEY,title TEXT NOT NULL,done INTEGER NOT NULL DEFAULT 0)")
@app.get("/health")
def health():return jsonify(status="ok")
@app.get("/api/todos")
def listing():
 init()
 with db() as c:return jsonify([dict(r) for r in c.execute("SELECT id,title,done FROM todos ORDER BY id")])
@app.post("/api/todos")
def create():
 init();title=str((request.get_json(silent=True) or {}).get("title","")).strip()
 if not title:return jsonify(error="title is required"),400
 with db() as c:
  cur=c.execute("INSERT INTO todos(title) VALUES (?)",(title,));return jsonify(id=cur.lastrowid,title=title,done=0),201
@app.patch("/api/todos/<int:todo_id>")
def done(todo_id):
 init()
 with db() as c:
  cur=c.execute("UPDATE todos SET done=1 WHERE id=?",(todo_id,))
  if not cur.rowcount:return jsonify(error="todo not found"),404
  return jsonify(id=todo_id,done=1)
if __name__=="__main__":init();app.run(host="0.0.0.0",port=5000)
