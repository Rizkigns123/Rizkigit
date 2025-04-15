def tentukan_nilai(score):
    if 90 <= score <= 100:
        return "A", "Dengan Pujian"
    elif 80 <= score <= 89:
        return "B", "Sangat Memuaskan"
    elif 70 <= score <= 79:
        return "C", "Memuaskan"
    elif 60 <= score <= 69:
        return "D", "Tidak Memuaskan"
    elif 0 <= score <= 59:
        return "E", "Tidak LULUS"
    else:
        return None, "Skor tidak valid (harus antara 0-100)"

def main():
    try:
        score_input = input("_
