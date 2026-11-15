# 图像与视频 API 接入：端点、任务查询与重复提交排查 | Image and Video APIs

[官网原文 / Canonical guide](https://eastx.ai/zh/community/image-video-api-integration)

## 中文

### 先区分三种需求

让模型理解图片属于视觉输入；生成新图片使用图片生成接口；生成视频通常是异步任务。它们不能都塞进普通文本聊天请求。EastX 将这些能力放在同一 API 管理体系下，但调用前仍要选择正确模型和端点。

### 图片生成

图片生成入口为 `POST /v1/images/generations`。选择当前支持的图片模型，按其说明设置 prompt、数量与尺寸。响应可能给出生成图片 URL，业务应及时下载并保存所需成果，不把可能过期的返回链接当作永久素材库。不要从某个模型的尺寸选项推断所有图片模型都相同。

### 视频任务创建与查询

视频入口为 `POST /v1/contents/generations/tasks`。以下为文档中的请求结构，模型 ID 与可计费分辨率应先查模型详情：

```json
{
  "model": "YOUR_VIDEO_MODEL_ID",
  "content": [{"type": "text", "text": "A paper plane over a lake."}],
  "resolution": "720p",
  "duration": 4,
  "ratio": "16:9",
  "generate_audio": false
}
```

创建时使用稳定的 `Idempotency-Key`。保存返回任务 ID，再调用 `GET /v1/contents/generations/tasks/{task_id}` 查询。`queued` 与 `processing` 继续等待；`succeeded` 后读取 `content.video_url`；`failed` 是失败终态。文档建议约每 10 秒查询同一任务。

### 最容易造成重复费用的错误

页面没更新就重新创建任务，或者网络超时后换一个幂等键重发。相同创建动作重试应复用相同键和请求体。遇到 `pending_confirmation` 查询原任务并联系支持；`billing_pending` 则检查余额与原 Key 预算。不要把这些状态当成必须新建任务的信号。

### 素材与成本

参考图片、视频、音频按模型支持的 content 字段提交，使用可访问的 HTTPS URL 或已授权资产引用；本地文件路径不能直接交给远程 API。费用应结合模型、分辨率、时长和音频选项核对，不能套用文本 Token 的简单比较。

EastX 适合把文本脚本、图片和视频生成整合到同一项目管理中：统一 Key 与消费记录，异步任务保存独立 ID。生产系统应保存输入版本、任务状态和成果位置，方便恢复中断任务。

---

## English

### Separate three different needs

Understanding an image is vision input; creating an image uses generation; video generation is typically asynchronous. These are not all ordinary text-chat requests. EastX brings them into one API management system, while each still needs the correct model and endpoint.

### Image generation

Use `POST /v1/images/generations` with a currently supported image model. Configure prompt, count and dimensions according to that model. Responses may provide generated-image URLs; download and store required assets rather than treating a potentially expiring link as a permanent library. Dimensions supported by one model do not establish support for all models.

### Create and query video tasks

Use `POST /v1/contents/generations/tasks`. This follows the documented structure; check the model ID and priced resolutions in model details:

```json
{
  "model": "YOUR_VIDEO_MODEL_ID",
  "content": [{"type": "text", "text": "A paper plane over a lake."}],
  "resolution": "720p",
  "duration": 4,
  "ratio": "16:9",
  "generate_audio": false
}
```

Send a stable `Idempotency-Key` when creating the task. Save its ID and query `GET /v1/contents/generations/tasks/{task_id}`. Continue waiting for `queued` or `processing`; read `content.video_url` after `succeeded`; `failed` is terminal. Documentation suggests polling the same task about every 10 seconds.

### Avoid duplicate submissions

An unchanged screen or network timeout is not a reason to create another task with a new key. Retry the same creation with the same idempotency key and body. For `pending_confirmation`, query the original task and contact support. For `billing_pending`, inspect balance and the original key budget.

### Assets and cost

Submit image, video and audio references using supported content fields and accessible HTTPS URLs or authorized asset references. A local file path is not accessible to a remote API. Check model, resolution, duration and audio options when estimating cost; text-token comparisons are insufficient.

EastX helps combine script, image and video production under shared key and usage management. Keep a separate ID for every asynchronous task, and preserve input versions, status and output locations so interrupted production can resume.

### 资料与更新 / Sources and updates

更新 / Updated: 2026-11-14

- [EastX API 文档 / API documentation](https://eastx.ai/en/docs)
- [模型与定价 / Models and pricing](https://eastx.ai/en/pricing)

### 继续阅读 / Related guides

- [大模型 API 费用怎么算：输入、输出、缓存与阶梯计费 | Understanding API Costs](https://eastx.ai/zh/community/api-pricing-input-output-cache-tiers)
- [EastX 可靠性与数据处理 FAQ：Key、日志、上游与任务恢复 | Reliability FAQ](https://eastx.ai/zh/community/api-reliability-data-handling-faq)
