const test = require("node:test");
const assert = require("node:assert/strict");
const { summarizeTasks } = require("../src/summarize-tasks");

test("summarizes counts, remaining work and rounded completion", () => {
  const tasks = [
    { id: "CC-1", status: "done" },
    { id: "CC-2", status: "in_progress" },
    { id: "CC-3", status: "todo" },
  ];
  assert.deepEqual(summarizeTasks(tasks), {
    total: 3,
    completed: 1,
    remaining: 2,
    completionPercent: 33,
    counts: { todo: 1, in_progress: 1, done: 1 },
  });
});

test("returns a zero percentage for an empty task list", () => {
  assert.deepEqual(summarizeTasks([]), {
    total: 0,
    completed: 0,
    remaining: 0,
    completionPercent: 0,
    counts: { todo: 0, in_progress: 0, done: 0 },
  });
});

test("does not mutate input task data", () => {
  const task = Object.freeze({ id: "CC-1", status: "done" });
  const tasks = Object.freeze([task]);
  summarizeTasks(tasks);
  assert.deepEqual(tasks, [task]);
});

test("rejects a non-array value", () => {
  assert.throws(() => summarizeTasks(null), { name: "TypeError" });
});

test("rejects malformed task entries", () => {
  assert.throws(() => summarizeTasks([null]), /each task must be an object/);
  assert.throws(() => summarizeTasks([{ status: "todo" }]), /non-empty string id/);
  assert.throws(() => summarizeTasks([{ id: "CC-1", status: "blocked" }]), /unsupported task status/);
});

test("rejects duplicate task ids", () => {
  assert.throws(
    () => summarizeTasks([{ id: "CC-1", status: "todo" }, { id: "CC-1", status: "done" }]),
    /duplicate task id/,
  );
});
