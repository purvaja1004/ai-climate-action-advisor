# agent.py
import os
from typing import Dict

from langgraph.graph import StateGraph, END
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage

# -------------------------
# API KEY CHECK
# -------------------------
assert os.getenv("GOOGLE_API_KEY"), "❌ GOOGLE_API_KEY not set"

# -------------------------
# GEMINI MODEL
# -------------------------
llm = ChatGoogleGenerativeAI(
    model="models/gemini-2.5-flash",
    temperature=0.2,
    max_output_tokens=200
)

# -------------------------
# CLASSIFIER NODE
# -------------------------
def classify_node(state: dict) -> dict:
    prompt = f"""
Classify the activity into ONLY one category:
transport, energy, food, waste, other

Activity: {state['activity']}

Respond with ONLY one word.
"""
    response = llm.invoke([HumanMessage(content=prompt)])
    state["category"] = response.content.strip().lower()
    return state


# -------------------------
# ANALYSIS NODE (NO JSON FROM LLM)
# -------------------------
def analysis_node(state: dict) -> dict:
    activity = state["activity"].lower()
    category = state["category"]

    # -------- TRANSPORT --------
    if category == "transport":
        if "bus" in activity or "public" in activity:
            impact = "Low"
            carbon = "1.5 kg CO2 approx"
            suggestions = [
                "Public transport reduces per-person emissions",
                "Continue using buses instead of private vehicles"
            ]
        else:
            impact = "Medium"
            carbon = "4 kg CO2 approx"
            suggestions = [
                "Consider public transport or carpooling",
                "Reduce unnecessary trips"
            ]

    # -------- ENERGY --------
    elif category == "energy":
        impact = "Medium"
        carbon = "3 kg CO2 approx"
        suggestions = [
            "Switch off devices when not in use",
            "Use energy-efficient appliances"
        ]

    # -------- FOOD --------
    elif category == "food":
        impact = "Medium"
        carbon = "2.5 kg CO2 approx"
        suggestions = [
            "Reduce food waste",
            "Prefer locally sourced food"
        ]

    # -------- WASTE --------
    elif category == "waste":
        impact = "Low"
        carbon = "1 kg CO2 approx"
        suggestions = [
            "Segregate waste properly",
            "Recycle whenever possible"
        ]

    else:
        impact = "Low"
        carbon = "Minimal"
        suggestions = ["Provide more details"]

    state["result"] = {
        "impact": impact,
        "carbon_footprint": carbon,
        "suggestions": suggestions,
        "confidence": "0.85"
    }
    return state


# -------------------------
# ROUTER
# -------------------------
def router(state: dict) -> str:
    if state["category"] in ["transport", "energy", "food", "waste"]:
        return "analysis"
    return "analysis"


# -------------------------
# GRAPH
# -------------------------
builder = StateGraph(dict)
builder.set_entry_point("classify")

builder.add_node("classify", classify_node)
builder.add_node("analysis", analysis_node)

builder.add_conditional_edges(
    "classify",
    router,
    {"analysis": "analysis"}
)

builder.add_edge("analysis", END)

graph = builder.compile()


# -------------------------
# PUBLIC FUNCTION
# -------------------------
def run_agent(activity: str) -> Dict:
    final = graph.invoke({"activity": activity})

    return {
        "category": final["category"],
        **final["result"]
    }
