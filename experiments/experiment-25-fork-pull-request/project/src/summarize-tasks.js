const VALID_STATUSES = new Set(["todo", "in_progress", "done"]);

/**
 * Summarize a CampusConnect task list without mutating the input records.
 * Each task must have a non-empty string id and one supported status.
 */
function summarizeTasks(tasks) {
  if (!Array.isArray(tasks)) {
    throw new TypeError("tasks must be an array");
  }

  const counts = { todo: 0, in_progress: 0, done: 0 };
  const ids = new Set();

  for (const task of tasks) {
    if (!task || typeof task !== "object" || Array.isArray(task)) {
      throw new TypeError("each task must be an object");
    }
    if (typeof task.id !== "string" || task.id.trim() === "") {
      throw new TypeError("each task must have a non-empty string id");
    }
    if (ids.has(task.id)) {
      throw new TypeError(`duplicate task id: ${task.id}`);
    }
    if (!VALID_STATUSES.has(task.status)) {
      throw new TypeError(`unsupported task status: ${String(task.status)}`);
    }
    ids.add(task.id);
    counts[task.status] += 1;
  }

  const total = tasks.length;
  const completed = counts.done;
  return {
    total,
    completed,
    remaining: total - completed,
    completionPercent: total === 0 ? 0 : Math.round((completed / total) * 100),
    counts,
  };
}

module.exports = { summarizeTasks };
