import streamlit as st
import json
from agent_api import generate_agent_dialogue
from reward_model import train_reward_model
from rl_trainer import train_agent_with_rl

st.set_page_config(page_title="客服AI RLHF微调Demo", layout="wide")

st.title("客服AI RLHF微调Demo")

# 1. 选择/输入用户诉求
st.header("1. 输入用户诉求")
user_intent = st.text_input("请输入用户诉求", "我要查询订单到了吗？")

# 2. 选择黄金标准对话
st.header("2. 黄金标准对话")
with open("golden_cases.json", "r", encoding="utf-8") as f:
    golden_cases = json.load(f)
golden_dialogue = None
for case in golden_cases:
    if case["user_intent"] == user_intent:
        golden_dialogue = case["dialogue"]
        break
if golden_dialogue:
    for turn in golden_dialogue:
        st.chat_message(turn["role"]).write(turn["content"])
else:
    st.info("未找到匹配的黄金标准对话，请手动录入。")

# 3. Agent仿真对话
st.header("3. Agent仿真对话")
agent_dialogue = generate_agent_dialogue(user_intent)
for turn in agent_dialogue:
    st.chat_message(turn["role"]).write(turn["content"])

# 4. 偏好对数据生成
st.header("4. 偏好对数据")
if golden_dialogue:
    preference_data = {
        "context": [f'{golden_dialogue[0]["role"].capitalize()}: {golden_dialogue[0]["content"]}',
                    f'{golden_dialogue[1]["role"].capitalize()}: {golden_dialogue[1]["content"]}'],
        "chosen": [f'{golden_dialogue[2]["role"].capitalize()}: {golden_dialogue[2]["content"]}',
                   f'{golden_dialogue[3]["role"].capitalize()}: {golden_dialogue[3]["content"]}'],
        "rejected": [f'{agent_dialogue[2]["role"].capitalize()}: {agent_dialogue[2]["content"]}',
                     f'{agent_dialogue[3]["role"].capitalize()}: {agent_dialogue[3]["content"]}']
    }
    st.json(preference_data)
    st.download_button("导出偏好对数据", json.dumps(preference_data, ensure_ascii=False), file_name="preference_data.json")
else:
    st.warning("无黄金标准对话，无法生成偏好对。")

# 5. 奖励模型训练
st.header("5. 奖励模型训练")
if st.button("训练奖励模型"):
    model_name = train_reward_model([preference_data])
    st.success(f"奖励模型训练完成：{model_name}")

# 6. RL微调
st.header("6. RL微调")
if st.button("用奖励模型微调Agent"):
    agent_name = train_agent_with_rl("agent_model_v1", "reward_model_v1", [preference_data])
    st.success(f"Agent RL微调完成：{agent_name}") 