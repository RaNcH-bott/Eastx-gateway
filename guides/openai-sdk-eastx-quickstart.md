# 使用 OpenAI SDK 接入 EastX：首次调用与常见错误 | OpenAI SDK Quickstart

[官网原文 / Canonical guide](https://eastx.ai/zh/community/openai-sdk-eastx-quickstart)

![EastX 首次调用流程：密钥、模型 ID、SDK 请求与用量 / First request workflow](https://eastx.ai/api/v1/community-images/6439fe0b-f72f-4826-bb13-ed7fd47a6c45.png)



## 中文：使用 OpenAI SDK 接入 EastX

**服务地区：** EastX 对访问 IP 位于中国内地的用户关闭注册和充值。符合地区条件的用户可在账户充值页核对可用的充值方式和网络。



EastX 的 Chat Completions 接口可通过 OpenAI Python SDK 调用。本文从模型查询开始，完成一次非流式文本请求，再说明错误排查。兼容接口不代表每个模型都支持相同参数；请以所选模型及当前文档为准。


更新：2026-11-14。EastX 将多模型接入、API Key 管理和用量核对集中在同一平台，适合需要在项目与客户端之间复用接入方式的开发者。



### 1. 准备密钥、余额与模型


在 EastX 控制台创建 API Key，妥善保存。确认余额和密钥的模型权限、额度、来源 IP 限制。不要把密钥放进浏览器前端、公开仓库或截图。API 地址为 `https://api.eastx.ai/v1`。


先查阅[API 文档](https://eastx.ai/en/docs)和[价格页面](https://eastx.ai/en/pricing)。价格与模型可用性会变化；复制当前模型 ID，不要把展示名称当作 ID。



### 2. 安装 SDK 并设置环境变量



```bash
python -m pip install openai
```


在本机设置环境变量 `EASTX_API_KEY`。它保存你的 EastX 密钥，而不是其他平台的密钥。以下 Python 代码会读取该变量；缺失时应先配置环境，再运行。



### 3. 查询可调用模型



```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["EASTX_API_KEY"],
    base_url="https://api.eastx.ai/v1",
    timeout=60.0,
    max_retries=0,
)
for model in client.models.list().data:
    print(model.id)
```


选择其中支持文本 Chat Completions 的模型，将其准确 ID 设置为 `EASTX_MODEL`。模型列表用于发现目录，不能替代对接口能力与密钥权限的核对。首次排查时关闭 SDK 自动重试，便于看清每次请求。



### 4. 发出首次请求



```python
response = client.chat.completions.create(
    model=os.environ["EASTX_MODEL"],
    messages=[{"role": "user", "content": "Say hello in one sentence."}],
    max_tokens=128,
)
print(response.choices[0].message.content)
print(response.usage)
```


该片段接在上一个代码块之后运行。正常响应应包含生成结果；同时查看 usage 和控制台用量记录。若所选模型不接受 `max_tokens` 等参数，按该模型说明调整，不要反复发送同一失败请求。请求可能产生费用。



### 5. 按状态码排查



- **401**：检查密钥是否缺失、复制错误或已失效。

- **402**：查看具体错误类型；余额预检查与密钥额度都可能阻止请求。余额检查可能考虑输入和最大输出的预估费用。

- **403**：核对密钥状态、允许的模型及来源 IP。

- **404**：核对模型 ID、模型是否启用，以及请求路径是否重复添加 `/v1`。

- **429**：检查密钥或租户限流；有 Retry-After 时遵循它，降低并发并采用有上限的退避。

- **5xx 或超时**：保留时间、状态码和可用的请求标识，先判断是否已经完成或计费，再决定是否重试。不要把含密钥的完整请求发到公开论坛。



### 常见问题


**是否只改 base URL 就够了？** 对受支持的 Chat Completions 文本请求，还需使用 EastX 密钥、正确模型 ID 和允许的参数。Responses、工具调用、视觉输入等能力应逐项核对。


**能否用列表中的任意模型跑这段代码？** 不能。图像、视频或 embedding 模型可能需要其他接口；先确认模型用途。


**为什么实际费用不能只看回答字数？** 计费以模型规则及记录的用量为准，涉及输入、输出以及可能适用的缓存、阶梯或推理用量。发布前请复核价格页。



---



## English: Connect the OpenAI SDK to EastX

**Regional availability:** EastX registration and top-ups are unavailable from IP addresses in mainland China. Eligible users can check current funding options and networks on the account funding page.



EastX Chat Completions can be called with the OpenAI Python SDK. This tutorial starts with model discovery, sends a non-streaming text request, and explains troubleshooting. API compatibility does not mean every model accepts the same parameters; check the selected model and current documentation.


Updated: 2026-11-14. EastX brings multi-model access, API key management and usage review into one platform, helping developers reuse an integration across projects and clients.



### 1. Prepare a key, balance and model


Create an API key in the EastX console and store it securely. Check your balance, key model permissions, spending cap and source-IP restrictions. Never put the key in browser-side code, public repositories or screenshots. The API base URL is `https://api.eastx.ai/v1`.


Read the [API documentation](https://eastx.ai/en/docs) and [pricing page](https://eastx.ai/en/pricing). Prices and availability can change. Copy the current model ID rather than its display name.



### 2. Install the SDK and configure the environment



```bash
python -m pip install openai
```


Set the environment variable `EASTX_API_KEY` on your machine to your EastX key, not a key from another platform. The Python code below reads this variable. Configure it before running the example.



### 3. Discover models



```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["EASTX_API_KEY"],
    base_url="https://api.eastx.ai/v1",
    timeout=60.0,
    max_retries=0,
)
for model in client.models.list().data:
    print(model.id)
```


Choose a model supporting text Chat Completions and set its exact ID as `EASTX_MODEL`. The list helps discover the catalog; it does not replace checking endpoint capabilities and key permissions. Automatic SDK retries are disabled here to make each attempt clear during initial troubleshooting.



### 4. Send the first request



```python
response = client.chat.completions.create(
    model=os.environ["EASTX_MODEL"],
    messages=[{"role": "user", "content": "Say hello in one sentence."}],
    max_tokens=128,
)
print(response.choices[0].message.content)
print(response.usage)
```


Run this after the previous Python block. A successful response should contain generated output. Review usage and the console usage record. If the selected model rejects a parameter such as `max_tokens`, adjust it according to that model’s documentation instead of repeatedly sending the same failing request. Requests may incur charges.



### 5. Troubleshoot by status code



- **401**: Check for a missing, incorrectly copied or invalid key.

- **402**: Inspect the error type. Balance prechecks and key spending caps can block requests. The balance check may include input and estimated maximum output cost.

- **403**: Check key status, allowed models and source-IP restrictions.

- **404**: Check the model ID, availability and whether `/v1` was accidentally added twice.

- **429**: Check key or tenant limits. Follow Retry-After when present, reduce concurrency and use bounded backoff.

- **5xx or timeout**: Keep the timestamp, status and any available request identifier. Determine whether the request completed or was billed before retrying. Do not post requests containing secrets in public forums.



### Frequently asked questions


**Is changing the base URL enough?** For supported text Chat Completions, you also need an EastX key, correct model ID and supported parameters. Check Responses, tool calling and vision support separately.


**Can every listed model run this example?** No. Image, video and embedding models may require different endpoints. Check the model’s purpose first.


**Why can’t I estimate the bill from answer length alone?** Billing follows model rules and recorded usage, including input, output and applicable cache, tier or reasoning usage. Check the current pricing page before deployment.



### 继续阅读 / Related guides

- [EastX API 报错排查：429、402、403 与 5xx | API Error Troubleshooting](https://eastx.ai/zh/community/api-errors-429-402-5xx)
- [WorkBuddy 接入 EastX：自定义模型、API 地址与费用管理 | WorkBuddy Setup](https://eastx.ai/zh/community/workbuddy-eastx-custom-model)
- [ZCode 接入 EastX：桌面端与 CLI 配置、模型切换和预算 | ZCode Setup](https://eastx.ai/zh/community/zcode-eastx-setup)
