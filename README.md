# 客服AI RLHF微调Demo

本项目为一个端到端的强化学习微调（RLHF）原型Demo，支持：
- 黄金标准对话与Agent仿真对话生成
- 偏好对数据自动生成与导出
- 奖励模型训练与RL微调（伪代码）

## 产品功能
- 输入用户诉求，展示黄金标准与Agent仿真多轮对话
- 自动生成偏好对数据（chosen/rejected）
- 奖励模型训练与RL微调（伪代码流程）
- 支持偏好对数据导出

## 快速开始（本地运行）

1. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```
2. 启动前端：
   ```bash
   streamlit run app.py
   ```
3. 按照页面流程体验各功能

## 在线部署（推荐）

你可以一键将本项目部署到 [Streamlit Community Cloud](https://streamlit.io/cloud)：

1. 访问 https://streamlit.io/cloud 并用 GitHub 账号登录
2. 点击 "New app"，选择你的仓库 `henrythu2/rft`，分支 `main`，主文件 `app.py`
3. 点击 "Deploy"，几分钟后即可获得在线访问链接

详细官方指南见：[Streamlit Cloud 官方文档](https://docs.streamlit.io/streamlit-community-cloud/get-started/deploy-an-app)

## 目录结构
- `app.py`：主入口
- `golden_cases.json`：黄金标准对话样例
- `agent_api.py`：Agent仿真API
- `reward_model.py`：奖励模型训练
- `rl_trainer.py`：RL微调
- `requirements.txt`：依赖

## 参考
- [OpenAI RFT Guide](https://platform.openai.com/docs/guides/reinforcement-fine-tuning)
- [你的GitHub仓库](https://github.com/henrythu2/rft) 