import asyncio
import edge_tts
import os

TEXT = """
Hello, Good morning Sir.
Welcome back. I hope you are having a wonderful day.
"""

VOICE = "en-US-ChristopherNeural"
OUTPUT_FILE = "\\audio\\input.mp3"


async def generate_audio():
    communicate = edge_tts.Communicate(
        TEXT,
        VOICE,
        rate="-5%",
        volume="+0%",
        pitch="-2Hz"
    )
    # Lưu file âm thanh vào thư mục audio
    await communicate.save(OUTPUT_FILE)
    print(f"Đã tạo file: {OUTPUT_FILE}")


if __name__ == "__main__":
    asyncio.run(generate_audio())
    print("File được lưu tại:", os.path.abspath(OUTPUT_FILE))