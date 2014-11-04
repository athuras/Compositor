# vim: set fileencoding=utf-8 :
# Palettes for ASCII art.
from __future__ import unicode_literals

alphabet = "abcdefghijklmnopqrstuvwxyz"
numeric = "1234567890"
symbols = """!@#$%^&*()_+-=[]{}\|;:'"/?.>,<`~"""
shenanigans1 = """¡™£¢∞§¶•ªº–≠œ∑®†øπ“‘«åß∂ƒ©˙∆˚¬…æΩ≈ç√∫˜˜µ≤≥÷"""
shenanigans2 = """⁄€‹›ﬁﬂ‡°·‚—±Œ„‰ˇÁ¨ˆØ∏”’»ÅÍÎÏ˝ÓÔÒÚÆ¸˛Ç◊ı˜Â¯˘¿"""
alpha_numeric = alphabet + alphabet.upper() + numeric + symbols + u' '

cacophony = alpha_numeric + shenanigans1 + shenanigans2
