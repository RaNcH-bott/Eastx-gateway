# EastX Gateway Examples

[16 篇双语教程 / 16 bilingual guides](guides/README.md)

## 中文

EastX 是面向海外开发者的多模型 AI API 网关。SDK 和兼容客户端可共用 API 入口，按项目分别管理 Key、额度和用量。**中国内地 IP 无法注册和充值。** 符合地区条件的用户可在账户充值页查看当前支持的渠道和 USDT 网络。

1. 在 EastX 创建 API Key，从模型目录复制支持 Chat Completions 的准确模型 ID。
2. 安装依赖 `python -m pip install -r requirements.txt`。在本地环境设置 `EASTX_API_KEY` 和 `EASTX_MODEL`。
3. 运行 `python examples/quickstart.py`。核对输出、usage 和账户用量，再选择是否进一步测试流式输出和工具调用。

Base URL 为 `https://api.eastx.ai/v1`。报 404 先核对地址是否重复拼接 `/v1` 以及模型 ID。报 402 同时检查账户余额和 Key 额度。

[API 文档](https://eastx.ai/en/docs) · [定价](https://eastx.ai/en/pricing) · [隐私政策](https://eastx.ai/en/privacy) · [客户端接入](docs/clients.md)

## English

EastX is a multi-model AI API gateway for international developers. SDK projects and compatible clients can share an API entry point while managing keys, spending caps, and usage by project. **Registration and top-ups are unavailable from IP addresses in mainland China.** Eligible users can check current payment options and USDT networks in the account funding page.

1. Create an EastX API key and copy the exact ID of a model that supports Chat Completions.
2. Install the SDK with `python -m pip install -r requirements.txt`. Set `EASTX_API_KEY` and `EASTX_MODEL` in your local environment.
3. Run `python examples/quickstart.py`. Check the output, usage, and console records before moving on to streaming and tool calls.

Use `https://api.eastx.ai/v1` as the base URL. For a 404, check for a duplicate `/v1` and verify the model ID. For a 402, check both the account balance and the key spending cap. Live requests may incur usage charges.

[API docs](https://eastx.ai/en/docs) · [Pricing](https://eastx.ai/en/pricing) · [Privacy policy](https://eastx.ai/en/privacy) · [Client setup](docs/clients.md)
