"""Brand standards enforcement — colors, fonts, naming."""
BRAND_COLORS = {
    "pink": "#FF1D6C",
    "amber": "#F5A623",
    "blue": "#2979FF",
    "violet": "#9C27B0",
    "gradient_start": "#FF6B2B",
    "gradient_end": "#00D4FF",
    "bg_dark": "#0a0a0a",
    "text_light": "#f5f5f5",
}

BRAND_FONTS = {
    "heading": "Space Grotesk",
    "body": "Inter",
    "code": "JetBrains Mono",
}

NAMING_RULES = [
    "Products use 'Road' prefix: RoadCode, RoadCoin, RoadChain",
    "Infrastructure uses road metaphors: TollBooth, PitStop, OneWay",
    "AI products use 'Lucidia' or 'BlackRoad AI' prefix",
    "Never use 'BlackRoad' as two words in code (always BlackRoad)",
]

def validate_color(hex_code: str) -> bool:
    return hex_code.startswith("#") and len(hex_code) == 7
