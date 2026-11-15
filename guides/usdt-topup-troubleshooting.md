# EastX USDT 充值教程：网络、金额、TxID 与到账排查 | USDT Top-up Guide

[官网原文 / Canonical guide](https://eastx.ai/zh/community/usdt-topup-troubleshooting)

## 中文

**服务地区：** EastX 对访问 IP 位于中国内地的用户关闭注册和充值。符合地区条件的用户可在账户充值页核对可用的充值方式和网络。


### 用 USDT 为多个模型与客户端统一准备余额

EastX 的 USDT 充值适合希望通过链上资金支付 API 用量的用户。充值后的余额用于平台内实际调用，无需为每个接入的客户端重复建立一套充值流程。WorkBuddy、ZCode 与其他兼容工具可分别使用专用 Key，消费在同一账户中核对。

### 充值前准备三项信息

打开账户充值页，选择可用的 USDT 入口。核对平台当前提供的网络、你的钱包或交易所支持的提币网络，以及订单显示的代币信息。同名 USDT 不代表不同网络可以混用；发送网络、接收网络与资产必须一致。

### 按当前订单操作

1. 输入计划充值金额，在页面允许范围内创建订单。
2. 阅读订单的收款地址、付款期限与实际应付金额。实际金额可能带小数，不要自行四舍五入。
3. 在钱包或交易所核对网络、地址、金额，以及手续费是否会从到账金额中扣除。
4. 完成转账后保存完整 TxID。若订单提供交易哈希验证入口，提交该笔转账的完整哈希。
5. 检查订单状态和 EastX 余额；链上提交、链上确认与平台入账是三个不同阶段。

每次都以自己的当前订单为付款依据，不复用教程截图、聊天里转发的地址或过期订单。

### 已转账但没有到账怎么查？

先在对应网络的区块浏览器检查交易是否成功、接收地址与金额是否一致。然后核对 EastX 订单状态与 TxID 是否填写完整。若网络、资产或金额不一致，保存订单号、TxID、网络和时间，联系支持处理，不要为了“补一下”而盲目再转一笔。

订单过期后不要继续付款；已经在期限内付款但未完成核验时，按订单提供的入口或支持流程处理。到账速度同时受链上确认、交易所提币与核验流程影响，排查时先确定卡在哪一段。

### 充值后仍提示 402？

确认余额已增加，再检查当前 API Key 的消费上限及请求的最大输出设置。余额预检查和 Key 额度是不同限制。使用[API 排错指南](https://eastx.ai/zh/community/api-errors-429-402-5xx)继续定位。

**USDT 余额能直接充进客户端订阅吗？** 这里充值的是 EastX API 余额；在客户端选用 EastX 自定义模型后，相关 API 请求才使用该余额。

---

## English

**Regional availability:** EastX registration and top-ups are unavailable from IP addresses in mainland China. Eligible users can check current funding options and networks on the account funding page.


### Fund multiple models and clients through one API balance

EastX USDT funding suits users paying for API usage with on-chain funds. The balance supports calls on the platform, avoiding a separate funding workflow for each connected client. WorkBuddy, ZCode and other compatible tools can use dedicated keys while spending is reviewed in one account.

### Check three things first

Open account funding and choose an available USDT option. Match the network offered by EastX, the withdrawal network supported by your wallet or exchange, and the asset shown on the order. Tokens sharing the USDT name are not interchangeable across networks.

### Follow the current order

1. Enter a planned amount within the page's allowed range and create the order.
2. Read the address, deadline and exact amount due. Preserve decimal places rather than rounding.
3. Check network, address, amount and whether withdrawal fees reduce the received amount.
4. Save the full transaction hash after sending. If the order offers hash verification, submit that transaction's complete TxID.
5. Check the order and EastX balance. Submission, blockchain confirmation and account credit are separate stages.

Use your own current order, never a tutorial screenshot, forwarded address or expired order.

### Sent but not credited?

Check the transaction on the correct network explorer: success, recipient and amount. Then inspect order status and the submitted TxID. For network, asset or amount mismatches, keep the order number, hash, network and time, and contact support. Do not blindly send another transfer.

Do not pay an expired order. If payment was made before expiry but verification remains incomplete, use the order's verification or support flow. Arrival depends on blockchain confirmation, exchange withdrawal and verification; identify which stage is pending.

### Still receiving 402 after funding?

Confirm the balance increased, then check the key cap and maximum output setting. Balance prechecks and key caps are different restrictions. Continue with the [API error guide](https://eastx.ai/zh/community/api-errors-429-402-5xx).

**Does this fund a client's subscription?** No. It funds EastX API usage. Select the EastX custom model in the client so those API requests use this balance.

### 资料与更新 / Sources and updates

更新 / Updated: 2026-11-14

- [账户充值 / Account funding](https://eastx.ai/en/recharge)
- [EastX API 文档 / API documentation](https://eastx.ai/en/docs)

### 继续阅读 / Related guides

- [大模型 API 费用怎么算：输入、输出、缓存与阶梯计费 | Understanding API Costs](https://eastx.ai/zh/community/api-pricing-input-output-cache-tiers)
- [EastX API 报错排查：429、402、403 与 5xx | API Error Troubleshooting](https://eastx.ai/zh/community/api-errors-429-402-5xx)
