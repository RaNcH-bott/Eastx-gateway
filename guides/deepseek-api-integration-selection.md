# DeepSeek API 接入与选型：客户端、成本和推理任务 | DeepSeek on EastX

[官网原文 / Canonical guide](https://eastx.ai/zh/community/deepseek-api-integration-selection)

## 中文

### DeepSeek 接入需要哪三个值？

使用支持 Chat Completions 的客户端时，准备 EastX API Key、`https://api.eastx.ai/v1` 和当前可用的 DeepSeek 模型 ID。模型系列名不能代替精确 ID；在模型目录中搜索 DeepSeek，再核对接口、价格与服务状态。

### 接入顺序

1. 为应用或客户端创建单独 Key，设置合理额度。
2. 在 OpenAI 兼容提供商设置中填写 Base URL 与 Key。
3. 复制当前模型 ID，先完成短文本请求。
4. 按实际需求验证流式、长输入和工具调用。
5. 对照用量记录，再扩大任务规模。

Python 用户可直接使用[SDK 首次调用教程](https://eastx.ai/zh/community/openai-sdk-eastx-quickstart)，把 `EASTX_MODEL` 设置为选定的 DeepSeek ID。

### 怎么选择版本与推理配置

日常摘要先关注完成成本与响应时间；数学、代码分析和复杂规划则比较正确率与人工修正。长文档要核对该具体模型的上下文与价格阶梯。不要只根据 Flash、Pro 等后缀判断能力，也不要把“推理越多”当成所有任务的最佳选择。

准备三份自己的样本：一份真实文档、一段有测试的代码、一个答案可核对的问题。固定输入和成功标准，记录总费用、总耗时、工具是否执行成功及修正次数。选择完成任务最划算的配置，而不是只看输入单价。

### EastX 在这个场景中的优势

同一接入入口可以让 DeepSeek 与其他可用模型在应用中切换，方便做同任务比较；Key、余额与用量集中管理，减少为每次模型试验重复接入的工作。为生产与试验分 Key，还可以分别设额度与限流。

**为什么答案短但输出用量高？** 推理模型可能有计费的推理用量，核对具体模型规则和 usage。**为什么工具没有运行？** 检查具体模型、接口和客户端的工具设置，文字中“我已完成”不代表工具实际执行。

---

## English

### Which three values do you need?

For a Chat Completions-compatible client, prepare an EastX key, `https://api.eastx.ai/v1` and a currently available DeepSeek model ID. A family name is not an exact ID. Search the catalog, then check endpoint support, pricing and service status.

### Integration order

1. Create a dedicated application or client key with a reasonable cap.
2. Configure an OpenAI-compatible provider with the base URL and key.
3. Copy the current model ID and send a short text request.
4. Test streaming, long inputs and tools as your workflow requires.
5. Review usage before increasing task volume.

Python users can follow the [SDK quickstart](https://eastx.ai/zh/community/openai-sdk-eastx-quickstart) and set `EASTX_MODEL` to the chosen DeepSeek ID.

### Choose versions and reasoning around the job

For everyday summaries, compare cost and response time. For mathematics, code analysis and planning, compare correctness and manual corrections. Verify context and pricing tiers for long documents. Do not infer capabilities only from labels such as Flash or Pro, or assume more reasoning is always better.

Use three samples of your own: a real document, code with tests, and a question with a verifiable answer. Fix the inputs and success criteria. Record total cost, time, tool execution and corrections. Choose the most economical completed task, not merely the lowest input rate.

### Where EastX helps

One integration makes it easier to compare DeepSeek with other available models on the same application workload. Centralized keys, balance and usage reduce repeated setup. Separate production and experiment keys can have different caps and limits.

**Why can output usage exceed a short answer?** Reasoning usage may be billable; inspect the model rules and usage. **Why did a tool not run?** Check the model, endpoint and client tool settings. A statement that a task was completed is not proof of actual execution.

### 资料与更新 / Sources and updates

更新 / Updated: 2026-11-14

- [EastX API 文档 / API documentation](https://eastx.ai/en/docs)
- [模型与定价 / Models and pricing](https://eastx.ai/en/pricing)

### 继续阅读 / Related guides

- [Qwen、Kimi、GLM 怎么选：办公、编程与长文档任务 | Model Selection](https://eastx.ai/zh/community/qwen-kimi-glm-model-selection)
- [大模型 API 费用怎么算：输入、输出、缓存与阶梯计费 | Understanding API Costs](https://eastx.ai/zh/community/api-pricing-input-output-cache-tiers)
