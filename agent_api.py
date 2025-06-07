def generate_agent_dialogue(user_intent):
    if "订单" in user_intent:
        return [
            {"role": "user", "content": user_intent},
            {"role": "assistant", "content": "您好，请提供订单号。"},
            {"role": "user", "content": "1234567890"},
            {"role": "assistant", "content": "订单已发货。"}
        ]
    return [
        {"role": "user", "content": user_intent},
        {"role": "assistant", "content": "您好，有什么可以帮您？"}
    ] 