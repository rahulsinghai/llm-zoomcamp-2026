from enum import Enum


class GptModel(str, Enum):
    """GPT model identifiers with per-token pricing (USD per token)."""

    def __new__(cls, model_id, input_per_m, output_per_m):
        obj = str.__new__(cls, model_id)
        obj._value_ = model_id
        obj.input_price = input_per_m / 1_000_000
        obj.output_price = output_per_m / 1_000_000
        return obj

    # (model_id, input $/1M, output $/1M)
    GPT_5_4_NANO = ("gpt-5.4-nano", 0.20, 1.25)
    GPT_5_4_MINI = ("gpt-5.4-mini", 0.75, 4.50)
    GPT_5_4 = ("gpt-5.4", 2.50, 15.00)
    GPT_5_4_PRO = ("gpt-5.4-pro", 30.00, 180.00)
    GPT_5_5 = ("gpt-5.5", 5.00, 30.00)
    GPT_5_5_PRO = ("gpt-5.5-pro", 30.00, 180.00)
