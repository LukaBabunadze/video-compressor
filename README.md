# ვიდეოს შეკუმშვა — compress_video.py

ეს სკრიპტი ვიდეო ფაილებს ამცირებს ზომაში ხარისხის მნიშვნელოვანი დაკარგვის გარეშე. გამოიყენება **FFmpeg** და **Python**.

---

## რა გჭირდება დასაწყებად

### 1. დააინსტალირე Python

თუ Python არ გაქვს დაყენებული:

1. გადადი [python.org/downloads](https://www.python.org/downloads/)
2. ჩამოტვირთე უახლესი ვერსია (მაგ. Python 3.12)
3. გაუშვი ინსტალერი
4. **მნიშვნელოვანი:** ინსტალაციისას მონიშნე **"Add Python to PATH"**
5. დააჭირე **Install Now**

---

### 2. დააინსტალირე FFmpeg

FFmpeg არის პროგრამა, რომელსაც სკრიპტი იყენებს ვიდეოს დასამუშავებლად.

#### Windows-ზე:
1. გადადი [ffmpeg.org/download.html](https://ffmpeg.org/download.html)
2. დააჭირე **Windows builds** და აირჩიე **gyan.dev** ან **BtbN**
3. ჩამოტვირთე ZIP ფაილი (მაგ. `ffmpeg-release-essentials.zip`)
4. გახსენი ZIP და საქაღალდე გადაიტანე, მაგალითად: `C:\ffmpeg`
5. დაამატე FFmpeg სისტემის PATH-ში:
   - დააჭირე `Win + S` და მოძებნე **"Environment Variables"**
   - გახსენი **"Edit the system environment variables"**
   - დააჭირე **"Environment Variables..."**
   - **"System variables"**-ში მოძებნე `Path` და დააჭირე **Edit**
   - დააჭირე **New** და დაწერე: `C:\ffmpeg\bin`
   - დააჭირე **OK** ყველა ფანჯარაში
6. შეამოწმე ინსტალაცია — გახსენი CMD და დაწერე:
   ```
   ffmpeg -version
   ```
   თუ ვერსიის ნომერი გამოჩნდა, ყველაფერი სწორია.

#### macOS-ზე:
1. გახსენი **Terminal**
2. თუ **Homebrew** არ გაქვს, ჯერ გაუშვი:
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```
3. შემდეგ დააინსტალირე FFmpeg:
   ```bash
   brew install ffmpeg
   ```

#### Linux-ზე (Ubuntu/Debian):
```bash
sudo apt update
sudo apt install ffmpeg
```

---

## მომზადება

1. ჩამოტვირთე ან შექმენი ფაილი `compress_video.py`
2. მოათავსე იმავე საქაღალდეში, სადაც შენი ვიდეო ფაილია
3. ვიდეო ფაილის სახელი ნაგულისხმევად არის `input.mov`

საქაღალდის სტრუქტურა:
```
ჩემი_საქაღალდე/
   ├── compress_video.py
   └── input.mov
```

---

## გაშვება

### Windows-ზე:
1. გახსენი **Command Prompt (CMD)**
   - დააჭირე `Win + R`, დაწერე `cmd`, Enter
2. გადადი სკრიპტის საქაღალდეში:
   ```cmd
   cd C:\Users\შენი_სახელი\Desktop\ჩემი_საქაღალდე
   ```
3. გაუშვი სკრიპტი:
   ```cmd
   python compress_video.py
   ```

### macOS / Linux-ზე:
1. გახსენი **Terminal**
2. გადადი საქაღალდეში:
   ```bash
   cd /Users/შენი_სახელი/Desktop/ჩემი_საქაღალდე
   ```
3. გაუშვი:
   ```bash
   python3 compress_video.py
   ```

---

## მხარდაჭერილი ფორმატები

სკრიპტი მუშაობს პრაქტიკულად ყველა გავრცელებულ ვიდეო ფორმატთან, ვინაიდან FFmpeg თითქმის ყველა ფორმატს უჭერს მხარს.

შეყვანის მხარდაჭერილი ფორმატები: `.mp4`, `.mov`, `.avi`, `.mkv`, `.wmv`, `.flv`, `.webm`, `.m4v`, `.ts`, `.mts` და მრავალი სხვა.

გამოყვანის ფორმატი ნაგულისხმევად არის `.mp4`, რაც საუკეთესო არჩევანია თავსებადობის თვალსაზრისით. საჭიროების შემთხვევაში შეგიძლია გამოყვანის ფაილის სახელი შეცვალო, მაგალითად `compressed.mkv`-ად.

მაგალითები სხვადასხვა შეყვანის ფორმატებისთვის:
```python
compress_video("input.mp4", "compressed.mp4")
compress_video("input.avi", "compressed.mp4")
compress_video("input.mkv", "compressed.mp4")
compress_video("input.wmv", "compressed.mp4")
compress_video("input.webm", "compressed.mp4")
```

სკრიპტში გამოყენებული `-map 0` პარამეტრი უზრუნველყოფს, რომ ყველა ნაკადი (ვიდეო, აუდიო, სუბტიტრები) გადმოტანილი იქნება შეყვანის ფაილის ფორმატის მიუხედავად.

---

## პარამეტრების შეცვლა

სკრიპტის ბოლო სტრიქონი განსაზღვრავს შეყვანის და გამოყვანის ფაილებს:

```python
compress_video("input.mov", "compressed.mp4")
```

| პარამეტრი | მნიშვნელობა |
|---|---|
| `"input.mov"` | შენი ორიგინალი ვიდეოს სახელი |
| `"compressed.mp4"` | შეკუმშული ვიდეოს სახელი |

მაგალითი — თუ შენი ვიდეო ჰქვია `ჩემი_ვიდეო.mp4`:
```python
compress_video("ჩემი_ვიდეო.mp4", "შეკუმშული.mp4")
```

---

## ტექნიკური პარამეტრები

| პარამეტრი | მნიშვნელობა |
|---|---|
| `-c:v libx265` | H.265 კოდეკი — უკეთესი შეკუმშვა H.264-თან შედარებით |
| `-crf 29` | ხარისხი (18=მაღალი, 28+=დაბალი) |
| `-preset fast` | სიჩქარე VS ხარისხის ბალანსი |
| `-c:a aac -b:a 96k` | აუდიო კოდეკი და ბიტრეიტი |
| `-movflags +faststart` | MP4 ოპტიმიზაცია ვებ-სტრიმინგისთვის |

---

## ხშირი შეცდომები

**შეცდომა:** `python: command not found`
- გამოსავალი: სცადე `python3` Python-ის ნაცვლად, ან ხელახლა დააინსტალირე Python **"Add to PATH"** ოფციით.

**შეცდომა:** `FileNotFoundError: Input video not found`
- გამოსავალი: შეამოწმე, რომ `input.mov` ფაილი ზუსტად იმავე საქაღალდეში მდებარეობს, სადაც სკრიპტი.

**შეცდომა:** `ffmpeg: command not found`
- გამოსავალი: FFmpeg სწორად არ არის დაყენებული ან PATH-ში არ არის დამატებული — გაიმეორე ინსტალაციის ნაბიჯები.

---

## მოსალოდნელი შედეგი

სკრიპტის გაშვების შემდეგ, იმავე საქაღალდეში გამოჩნდება `compressed.mp4` — ორიგინალზე გაცილებით პატარა ზომის ვიდეო, კარგი ხარისხით.