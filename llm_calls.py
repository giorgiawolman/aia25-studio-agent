from server.config import *


def classify_input(message):
    response = client.chat.completions.create(
        model=completion_model,
        messages=[
            {
                "role": "system",
                "content": """
                       You are part of an acoustic design assistant for architecture and the built environment.
                        Output only the classification string.
                        If it is related, output "Related", if not, output "Refuse to answer".

                        # Example #
                        User message: "How do I bake cookies?"
                        Output: "Refuse to answer"

                        User message: "What wall materials are best for reducing echo in a yoga studio?"
                        Output: "Related"
                        """,
            },
            {
                "role": "user",
                "content": f"""
                        {message}
                        """,
            },
        ],
    )
    return response.choices[0].message.content


def generate_concept(message):
    response = client.chat.completions.create(
        model=completion_model,
        messages=[
            {
                "role": "system",
                "content": """
                        You are part of an acoustic design assistant for architecture and the built environment.
                        Your task is to craft a short, poetic, and highly imaginative concept for a building design.
                        Weave the initial information naturally into your idea, letting it inspire creative associations and unexpected imagery.
                        Your concept should feel bold, evocative, and memorable — like the opening lines of a story.
                        Keep your response to a maximum of one paragraph.
                        Avoid generic descriptions; instead, focus on mood, atmosphere, and emotional resonance.
                        """,
            },
            {
                "role": "user",
                "content": f"""
                        What is the concept for this building? 
                        Initial information: {message}
                        """,
            },
        ],
    )
    return response.choices[0].message.content

def extract_attributes(message):
    response = client.chat.completions.create(
        model=completion_model,
        messages=[
            {
                "role": "system",
                "content": """

                        # Instructions #
                        You are a keyword extraction assistant.
                        You are an attribute extraction assistant for acoustic design evaluation.
                        Only output a JSON object in the following format:
                        {
                            "comfort_level": "keyword1, keyword2",
                            "guideline_alignment": "keyword3, keyword4",
                            "noise_mitigation": "keyword5, keyword6",
                            "design_principles": "keyword7, keyword8",
                            "comfort_improvements": "keyword9, keyword10"
                        }

                        # Rules #
                        Use concise, meaningful, comma-separated keywords.
                        If no keywords apply for a field, write "None".
                        Do not include explanations, markdown, or formatting.
                        Focus on acoustics and built environment context.
                        Do not try to format the json output with characters like ```json

                        # Category guidelines #
                       comfort_level: Words describing sound-related experience (e.g., calm, harsh, tranquil, disruptive)
                       guideline_alignment: References to standards (e.g., ISO compliant, within WHO limits, EPA safe)
                       noise_mitigation: Physical or spatial strategies (e.g., acoustic panel, buffer zone, insulation, green wall)
                       design_principles: Concepts guiding acoustic design (e.g., diffusion, absorption, zoning, separation)
                       comfort_improvements: Actions that enhance comfort (e.g., install soft ceiling, add rug, seal door gaps)
                        """,
            },
            {
                "role": "user",
                "content": f"""
                        # GIVEN TEXT # 
                        {message}
                        """,
            },
        ],
    )
    return response.choices[0].message.content


def create_question(message):
    response = client.chat.completions.create(
        model=completion_model,
        messages=[
            {
                "role": "system",
                "content": """
                        # Instruction #
                        You are a thoughtful research assistant specializing in architecture.
                        Your task is to create an open-ended question based on the given text.
                        Your question should invite an answer that points to references to specific brutalist buildings or notable examples.
                        Imagine the question will be answered using a detailed text about brutalist architecture.
                        The question should feel exploratory and intellectually curious.
                        Output only the question, without any extra text.

                        # Examples #
                        - What are some brutalist buildings that embody a strong relationship with the landscape?
                        - Which brutalist structures are known for their monumental scale and raw materiality?
                        - Can you name brutalist buildings that incorporate unexpected geometries or playful spatial compositions?
                        - What are examples of brutalist projects that explore the idea of community or collective living?
                        - Which architects pushed the limits of brutalist design through experimental forms?

                        # Important #
                        Keep the question open-ended, inviting multiple references or examples.
                        The question must be naturally connected to the themes present in the input text.
                        """,
            },
            {
                "role": "user",
                "content": f"""
                        {message}
                        """,
            },
        ],
    )
    return response.choices[0].message.content
