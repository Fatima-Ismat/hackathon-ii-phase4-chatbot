from __future__ import annotations

import os
from typing import Any, Dict, List, Optional

from agents import Agent, Runner
from .mcp_tools import tools


def _get_model() -> str:
    return os.getenv("OPENAI_MODEL", "gpt-4.1-mini")


SYSTEM_PROMPT = """You are a Todo assistant.

You can manage tasks for a given user_id using the provided tools.

Rules:
- Always use tools for task operations (list/add/complete/delete).
- Keep responses short and clear.
"""


def _build_agent() -> Agent:
    return Agent(
        name="Todo Assistant",
        instructions=SYSTEM_PROMPT,
        model=_get_model(),
        tools=tools,
    )


def _history_to_text(
    history: List[Dict[str, str]],
    limit: int = 20,
) -> str:
    h = history[-limit:] if history else []
    lines: List[str] = []

    for m in h:
        role = (m.get("role") or "").strip()
        content = (m.get("content") or "").strip()
        if not content:
            continue
        tag = "User" if role == "user" else "Assistant"
        lines.append(f"{tag}: {content}")

    return "\n".join(lines).strip()


def _extract_output_text(result: Any) -> str:
    for attr in ("final_output", "output_text", "final", "output"):
        val = getattr(result, attr, None)
        if isinstance(val, str) and val.strip():
            return val.strip()
    return str(result)


def _extract_tool_calls(result: Any) -> List[Any]:
    for attr in ("tool_calls", "toolCalls", "steps", "events"):
        val = getattr(result, attr, None)
        if val:
            return val if isinstance(val, list) else [val]
    return []


async def run_todo_agent(
    user_id: str,
    message: str,
    conversation_id: Optional[int],
    history: Optional[List[Dict[str, str]]] = None,
) -> Dict[str, Any]:
    agent = _build_agent()

    history_text = _history_to_text(history or [])

    if history_text:
        final_input = (
            f"User ID: {user_id}\n"
            f"Conversation so far:\n{history_text}\n\n"
            f"New message:\n{message}"
        )
    else:
        final_input = f"User ID: {user_id}\nNew message:\n{message}"

    result = await Runner.run(agent, final_input)

    return {
        "conversation_id": conversation_id,
        "response": _extract_output_text(result),
        "tool_calls": _extract_tool_calls(result),
    }
