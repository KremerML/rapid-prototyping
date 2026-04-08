from models import Paper

PAPERS = [
    Paper(
        link="https://arxiv.org/abs/2303.08774",
        title="GPT-4 Technical Report",
        summary=(
            "OpenAI introduces GPT-4, a large multimodal model that accepts image and text inputs "
            "and produces text outputs. GPT-4 exhibits human-level performance on various professional "
            "and academic benchmarks, including passing a simulated bar exam in the top 10% of test takers."
        ),
        channel="#ml-research",
        shared_by="@alice",
    ),
    Paper(
        link="https://arxiv.org/abs/2302.13971",
        title="LLaMA: Open and Efficient Foundation Language Models",
        summary=(
            "Meta AI presents LLaMA, a collection of foundation language models ranging from 7B to 65B "
            "parameters trained on publicly available data. LLaMA-13B outperforms GPT-3 on most benchmarks "
            "while being 10x smaller, enabling research on large language models with limited compute."
        ),
        channel="#ml-research",
        shared_by="@bob",
    ),
    Paper(
        link="https://arxiv.org/abs/2305.10403",
        title="Voyager: An Open-Ended Embodied Agent with Large Language Models",
        summary=(
            "Voyager is the first LLM-powered embodied lifelong learning agent in Minecraft. It uses GPT-4 "
            "to continuously explore the world, acquire diverse skills, and make novel discoveries without "
            "human intervention, outperforming prior agents in tech tree progression and world exploration."
        ),
        channel="#ai-agents",
        shared_by="@carol",
    ),
    Paper(
        link="https://arxiv.org/abs/2307.09288",
        title="Llama 2: Open Foundation and Fine-Tuned Chat Models",
        summary=(
            "Meta releases Llama 2, a family of pretrained and fine-tuned LLMs scaled from 7B to 70B "
            "parameters. Llama 2-Chat models are optimized for dialogue and outperform open-source chat "
            "models on most benchmarks. The paper includes a detailed safety evaluation and red-teaming methodology."
        ),
        channel="#ml-research",
        shared_by="@alice",
    ),
    Paper(
        link="https://arxiv.org/abs/2310.06825",
        title="Ring Attention with Blockwise Transformers for Near-Infinite Context",
        summary=(
            "This work introduces Ring Attention, a technique that distributes the self-attention computation "
            "across multiple devices in a ring topology, enabling training and inference on sequences of "
            "near-infinite length without memory bottlenecks, overcoming a key limitation of standard transformers."
        ),
        channel="#systems",
        shared_by="@dave",
    ),
    Paper(
        link="https://arxiv.org/abs/2312.11805",
        title="Gemini: A Family of Highly Capable Multimodal Models",
        summary=(
            "Google DeepMind presents Gemini, a family of multimodal models built to handle text, images, "
            "audio, and video. Gemini Ultra achieves state-of-the-art performance on 30 of 32 academic "
            "benchmarks examined, and is the first model to surpass human expert performance on MMLU."
        ),
        channel="#ml-research",
        shared_by="@bob",
    ),
]
