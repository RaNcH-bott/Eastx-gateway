# Qwen、Kimi、GLM 怎么选：办公、编程与长文档任务 | Model Selection

[官网原文 / Canonical guide](https://eastx.ai/zh/community/qwen-kimi-glm-model-selection)

## 中文

### 按任务选具体模型，不给整个系列贴标签

Qwen、Kimi、GLM 都包含不同版本与能力配置。选择时先明确任务需要文本、图片、工具调用还是长上下文，再看当前具体模型的能力和价格。一个系列里的模型不能互相代替。

### 三类任务的比较方法

**办公与资料整理**：给同一份资料，要求输出结论、依据与待办。检查是否遗漏金额、日期和负责人，记录需要人工修改的地方。

**编程与 Agent**：用同一小型仓库与测试，让模型定位问题、修改文件并解释变更。检查工具是否实际执行、测试是否通过、是否误改无关文件。只比较聊天答案看不出 Agent 的真实完成能力。

**长文档与检索**：让模型回答文档中不同位置的问题，并要求给出原文依据。输入长度接近档位边界时，核对价格是否变化；不要只用“能放进去”判断上下文质量。

### 在 EastX 上建立可复用比较

从目录复制三个候选模型的精确 ID，使用同一 OpenAI 兼容入口和相同输入。保留各自参数、任务成功率、总耗时、输入输出用量与总费用。在支持自定义模型的客户端中建立清楚的模型名称，避免误选 Auto 或旧配置。

EastX 的价值在于把模型切换和用量比较放到统一入口下：你可以为 WorkBuddy、ZCode 等分别配置 Key，再按任务选择模型，而不必每次重新维护一套供应商凭据与消费记录。

### 一个实用的默认分工

先让一款满足工具要求的模型承担复杂任务；再从候选中选择完成摘要、分类等简单任务成本更低的配置。这个分工由自己的样本决定，不把某个品牌固定写成“最强”或“最便宜”。对高价值输出保留人工复核。

**怎么开始？** 用[SDK 接入教程](https://eastx.ai/zh/community/openai-sdk-eastx-quickstart)跑通一个模型，再复用代码更换 ID。模型切换前核对工具、图片输入和输出长度设置。

---

## English

### Choose a specific model for a specific job

Qwen, Kimi and GLM each contain different versions and capability profiles. Decide whether you need text, vision, tools or long context, then inspect the exact model and its current price. Models within one family are not interchangeable.

### Compare three workload types

**Office and document work:** provide the same source and request conclusions, evidence and action items. Check amounts, dates, owners and required corrections.

**Coding and agents:** use the same small repository and tests. Ask the model to diagnose, edit and explain. Verify real tool execution, passing tests and the absence of unrelated edits. Chat responses alone do not measure agent completion.

**Long documents and retrieval:** ask questions whose evidence appears in different parts of the document. Require supporting passages. Check pricing around input-tier boundaries; fitting text into a context window does not establish retrieval quality.

### Make the comparison reusable on EastX

Copy exact IDs for three candidates and use the same compatible entry point and inputs. Record parameters, task success, total time, token usage and total cost. Give custom models clear client labels so Auto or old configurations are not selected accidentally.

EastX brings model switching and usage comparison into one integration. Separate keys for WorkBuddy, ZCode and other clients let you choose models by task without repeatedly managing separate provider credentials and spending records.

### A practical starting split

Use a model that meets your tool requirements for complex jobs, then select a cheaper successful configuration for summaries and classification. Let your samples determine the split instead of assigning permanent “best” or “cheapest” labels to a brand. Review high-value outputs.

**Getting started:** run one model with the [SDK tutorial](https://eastx.ai/zh/community/openai-sdk-eastx-quickstart), then reuse the code with another ID. Recheck tools, vision and output limits when switching.

### 资料与更新 / Sources and updates

更新 / Updated: 2026-11-14

- [EastX API 文档 / API documentation](https://eastx.ai/en/docs)
- [模型与定价 / Models and pricing](https://eastx.ai/en/pricing)

### 继续阅读 / Related guides

- [DeepSeek API 接入与选型：客户端、成本和推理任务 | DeepSeek on EastX](https://eastx.ai/zh/community/deepseek-api-integration-selection)
- [多模型 API 网关怎么选：从客户端接入到真实任务成本 | Choosing an AI API Gateway](https://eastx.ai/zh/community/choose-multi-model-api-gateway)
