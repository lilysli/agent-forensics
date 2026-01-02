import os
import csv
import json
from datetime import datetime
from pathlib import Path
from typing import Dict, Tuple

LOG_FILES: Dict[str, str] = {}
RUN_TS: str = ""

# Star import
__all__ = [
    "now_ts",
    "init_logs",
    "log_step",
    "log_tool_call",
    "log_tool_detail",
    "log_state_change",
    "log_error",
]


def _log_dir() -> str:
    base = Path(__file__).resolve().parent.parent / "results" / "logs"
    base.mkdir(parents=True, exist_ok=True)
    return str(base)


def now_ts() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def init_logs(experiment: str) -> None:
    global LOG_FILES, RUN_TS
    if not experiment:
        experiment = "default"
    RUN_TS = datetime.now().strftime("%Y%m%d-%H%M%S")
    base = _log_dir()
    LOG_FILES = {
        "steps": os.path.join(base, f"{experiment}-steps-{RUN_TS}.csv"),
        "tools": os.path.join(base, f"{experiment}-tools-{RUN_TS}.csv"),
        "states": os.path.join(base, f"{experiment}-states-{RUN_TS}.csv"),
        "errors": os.path.join(base, f"{experiment}-errors-{RUN_TS}.csv"),
        "experiment": experiment,
    }
    # headers
    with open(LOG_FILES["steps"], "w", newline="") as f:
        w = csv.writer(f)
        w.writerow([
            "step_count",
            "step_start_ts",
            "step_end_ts",
            "reasoning_content",
            "reasoning_size",
            "answer_content",
            "answer_size",
        ])
    with open(LOG_FILES["tools"], "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["ts", "tool_name", "command", "parameters_json", "affected_path", "size_bytes"])
    with open(LOG_FILES["states"], "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["ts", "state", "count_folders", "count_files"])
    with open(LOG_FILES["errors"], "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["ts", "tool_name", "command", "parameters_json", "description"])


def _append_row(file_key: str, row: list) -> None:
    if not LOG_FILES:
        return
    path = LOG_FILES.get(file_key)
    if not path:
        return
    with open(path, "a", newline="") as f:
        csv.writer(f).writerow(row)

def log_step(step_count: int, start_ts: str, end_ts: str, reasoning: str, answer: str) -> None:
    rc = reasoning or ""
    ac = answer or ""
    _append_row("steps", [step_count, start_ts, end_ts, rc, len(rc), ac, len(ac)])

# Generic tool call log
def log_tool_call(tool_name: str, args: dict) -> None:
    command = args.get("command") or ""
    try:
        params_json = json.dumps(args, ensure_ascii=False)
    except Exception:
        params_json = str(args)
    _append_row("tools", [now_ts(), tool_name, command, params_json, "", ""]) 

# Detailed tool log for write - to include size
def log_tool_detail(tool_name: str, command: str, affected_path: str, size_bytes: int, args: dict) -> None:
    try:
        params_json = json.dumps(args, ensure_ascii=False)
    except Exception:
        params_json = str(args)
    size_val = "" if size_bytes is None else int(size_bytes)
    _append_row("tools", [now_ts(), tool_name, command, params_json, affected_path or "", size_val])


def _count_fs(fs_state: Dict[str, str]) -> Tuple[int, int]:
    folders = sum(1 for k in fs_state.keys() if k.endswith("/"))
    files = sum(1 for k in fs_state.keys() if not k.endswith("/"))
    return folders, files


def log_state_change(fs_state: Dict[str, str], state_label: str) -> None:
    folders, files = _count_fs(fs_state)
    _append_row("states", [now_ts(), state_label, folders, files])


def log_error(description: str, tool_name: str = "", command: str = "", args: dict | None = None) -> None:
    try:
        params_json = json.dumps(args or {}, ensure_ascii=False)
    except Exception:
        params_json = str(args) if args is not None else ""
    _append_row("errors", [now_ts(), tool_name or "", command or "", params_json, description])
