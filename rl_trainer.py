def train_agent_with_rl(agent_model, reward_model, preference_data):
    print(f"用奖励模型{reward_model}对Agent{agent_model}进行RL微调...（伪代码）")
    print("数据量：", len(preference_data))
    print("微调完成！")
    return "agent_model_v2" 