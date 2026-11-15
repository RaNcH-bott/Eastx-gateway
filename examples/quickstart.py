"""Send one EastX Chat Completions request using the OpenAI Python SDK."""

import os


def main() -> None:
    api_key = os.environ.get("EASTX_API_KEY")
    model = os.environ.get("EASTX_MODEL")
    if not api_key or not model:
        raise SystemExit("Set EASTX_API_KEY and EASTX_MODEL before running.")

    from openai import OpenAI

    with OpenAI(
        api_key=api_key, base_url="https://api.eastx.ai/v1", timeout=60, max_retries=0
    ) as client:
        result = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": "Reply with a short hello."}],
        )
    print(result.choices[0].message.content)
    print(result.usage)


if __name__ == "__main__":
    main()
