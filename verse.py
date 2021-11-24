import scriptures
book = ["Genesis", "Exodus", "Leviticus", "Numbers", "Deuteronomy",
"Joshua", "Judges", "Ruth", "1Samuel", "2Samuel", "1Kings",
"2Kings", "1Chronicles", "2Chronicles", "Ezra", "Nehemiah",
"Esther", "Job", "Psalms", "Proverbs", "Ecclesiastes",
"Song of Solomon", "Isaiah", "Jeremiah", "Lamentations", "Ezekiel",
"Daniel", "Hosea", "Joel", "Amos", "Obadiah", "Jonah",
"Micah", "Nahum", "Habakkuk", "Zephaniah", "Haggai", "Zechariah",
"Malachi", "Matthew", "Mark", "Luke", "John", "Acts", "Romans",
"1Corinthians", "2Corinthians", "Galatians", "Ephesians",
"Philippians", "Colossians", "1Thessalonians", "2Thessalonians",
"1Timothy", "2Timothy", "Titus", "Philemon", "Hebrews", "James",
"1Peter", "2Peter", "1John", "2John", "3John", "Jude", "Revelation" ]
abrevBook = ["gen", "exo", "lev", "num", "deu", "jos", "jdg",
"rut", "1sa", "2sa", "1ki", "2ki", "1ch", "2ch",
"ezr", "neh", "est", "job", "psa", "pro", "ecc",
"son", "isa", "jer", "lam", "eze", "dan", "hos",
"joe", "amo", "oba", "jon", "mic", "nah", "hab",
"zep", "hag", "zec", "mal", "mat", "mar", "luk",
"joh", "act", "rom", "1co", "2co", "gal", "eph",
"phi", "col", "1th", "2th", "1ti", "2ti", "tit",
"phl", "heb", "jam", "1pe", "2pe", "1jo", "2jo",
"3jo", "jud", "rev"]
# from guibible.net import Bible
# sample=Bible("Psalms",2,1,6)
# sample.read()
for i in book:
    print(scriptures.normalize_reference(f'{i}',chapter=1))
