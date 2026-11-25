#!/usr/bin/env python3
"""Houseplant Out-of-Office entry: writes one auto-reply to /output/entry.txt."""

import os

# 93 characters
REPLY = "I am currently out of the office, photosynthesizing. Your email has been composted for later."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(REPLY)

print("bytes:", len(REPLY.encode("utf-8")))
