# header đầy đủ
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer e4b8e1f593dc4a731a153c5ec8cc9b8bbb583ae964ce650a741113091b4e2ac6",
}

# header thiếu token authorization
miss_headers = {
    "Content-Type": "application/json"
}

# header sai token authorization
wrong_headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer e4b8e1f593dc4a731a153c5ec8cc9b8bbb583ae964ce650a741113091b4e2a"
}
