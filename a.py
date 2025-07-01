from google import genai

client = genai.Client(api_key="AIzaSyCjxfX0Z6BHjvkLIUN_O0VkgxWJgrjs-XA")


def generate_summary(text, length, format):
    prompt = f"""Tóm tắt nội dung văn bản dưới đây cho tôi
    Yêu cầu:
    1. Tóm tắt độ dài tối đa là {length} từ.
    2. Định dạng tóm tắt là {format}.
    3. Tóm tắt phải ngắn gọn, súc tích và dễ hiểu.

    Văn bản cần tóm tắt:
    {text}
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )
    
    return response.text

text = """
Trung Kiên tên thật là Trịnh Trần Trung Kiên, quê Hà Nội, là một ca sĩ, nhạc sĩ và nhà sản xuất âm nhạc nổi tiếng tại Việt Nam. Anh bắt đầu sự nghiệp âm nhạc từ năm 2010 và nhanh chóng trở thành một trong những nghệ sĩ được yêu thích nhất tại Việt Nam. Trung Kiên đã phát hành nhiều album và đĩa đơn thành công, với các ca khúc nổi bật như "Yêu em dài lâu", "Tình yêu màu nắng" và "Hạnh phúc mới". Anh cũng đã tham gia nhiều chương trình truyền hình và sự kiện âm nhạc lớn, góp phần làm phong phú thêm nền âm nhạc Việt Nam.
Trung Kiên được biết đến với giọng hát ấm áp, phong cách biểu diễn cuốn hút và khả năng sáng tác đa dạng. Anh đã giành được nhiều giải thưởng âm nhạc danh giá, bao gồm Giải thưởng Âm nhạc Cống hiến và Giải thưởng Làn Sóng Xanh. Ngoài ra, Trung Kiên còn là một nhà sản xuất âm nhạc tài năng, đã hợp tác với nhiều nghệ sĩ khác để tạo ra những sản phẩm âm nhạc chất lượng cao.
"""
summary = generate_summary(text, length=20, format="đoạn văn")

print(summary)